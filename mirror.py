#!/usr/bin/env python3
"""Espelha repositórios do GitHub como repositórios privados na sua conta.

Para cada entrada do repos.txt: cria o espelho privado se ele faltar, copia
branches e tags quando a origem muda e organiza o espelho na GitHub List da
categoria (mais topics). Guia completo no README.md.
"""

from __future__ import annotations

import argparse
import base64
import contextlib
import hashlib
import http.client
import json
import logging
import os
import random
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.request
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

API_URL = "https://api.github.com"
API_VERSION = "2026-03-10"
GIT_BASE_URL = "https://github.com"
REPOS_FILE = Path(__file__).resolve().with_name("repos.txt")

ACCOUNT = "alves-r"  # conta que recebe os espelhos: o token precisa ser dela ("" aceita qualquer uma)
LISTS_PRIVATE = True
LIST_PREFIX = "Mirrors – "  # descrição das listas criadas: "Mirrors – <categoria>"
MIRROR_TOPIC = "mirror"

HTTP_TIMEOUT = 30
MAX_RETRIES = 4
MAX_RETRY_WAIT = 180  # s; se o rate limit só libera depois disso, a chamada falha em vez de esperar
GIT_TIMEOUT = 120
GIT_TRANSFER_TIMEOUT = 20 * 60
TIME_BUDGET = 20 * 60  # s; passado isso não começa outro repo (o job tem 30 min): o resto fica para a próxima
PUSH_BATCH = 500  # refspecs por push: repos com milhares de tags vão em lotes

log = logging.getLogger("mirror")


# --------------------------------------------------------------------- repos.txt

HEADER_RE = re.compile(r"\[(?P<name>[^\]]*)\](?:\s+#.*)?")
URL_RE = re.compile(
    r"https://(?:www\.)?github\.com/"
    r"(?P<owner>[a-z0-9][a-z0-9_-]{0,38})/"
    r"(?P<repo>[a-z0-9._-]{1,100}?)(?:\.git)?/?",
    re.IGNORECASE,
)
NAME_RE = re.compile(r"[A-Za-z0-9._-]{1,100}")
INLINE_COMMENT_RE = re.compile(r"\s+#.*$")


@dataclass
class Entry:
    line: int
    url: str
    category: str | None
    owner: str = ""
    repo: str = ""
    mirror: str = ""
    error: str = ""

    @property
    def origin(self) -> str:
        return f"{self.owner}/{self.repo}" if self.owner else self.url

    @property
    def canonical_url(self) -> str:
        return f"https://github.com/{self.owner}/{self.repo}"


class RepoFileError(Exception):
    def __init__(self, errors: list[str]):
        super().__init__("\n".join(errors))
        self.errors = errors


def mirror_name_for(owner: str, repo: str) -> str:
    name = f"mirror-{owner}-{repo}".lower()
    if len(name) > 100:  # limite do GitHub; o hash mantém o nome determinístico e único
        digest = hashlib.sha1(f"{owner}/{repo}".lower().encode()).hexdigest()[:8]
        name = f"{name[:91]}-{digest}"
    return name


def parse_repos_file(path: Path) -> tuple[list[Entry], list[str]]:
    """Lê o repos.txt. Erros de estrutura abortam tudo; URL inválida só invalida a entrada."""
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as err:
        raise RepoFileError([f"não foi possível ler {path}: {err.strerror or err}"]) from None

    entries: list[Entry] = []
    errors: list[str] = []
    headers: list[list] = []  # [nome, linha, nº de entradas]
    category: str | None = None
    seen_urls: dict[str, int] = {}
    seen_names: dict[str, int] = {}

    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("["):
            match = HEADER_RE.fullmatch(line)
            if not match:
                errors.append(f"linha {lineno}: cabeçalho malformado {line!r}; use [Nome da Categoria]")
                continue
            category = " ".join(match["name"].split())
            if not category:
                errors.append(f"linha {lineno}: cabeçalho vazio; dê um nome à categoria, ex.: [Ferramentas]")
            headers.append([category, lineno, 0])
            continue

        parts = INLINE_COMMENT_RE.sub("", line).split()
        entry = Entry(line=lineno, url=parts[0], category=category)
        entries.append(entry)
        if headers:
            headers[-1][2] += 1

        if len(parts) > 2:
            entry.error = f"linha {lineno}: itens demais; o formato é: URL [nome-do-espelho]"
            continue
        match = URL_RE.fullmatch(parts[0])
        if not match or match["repo"] in (".", ".."):
            entry.error = f"linha {lineno}: URL inválida {parts[0]!r}; use https://github.com/<owner>/<repo>"
            continue
        entry.owner, entry.repo = match["owner"], match["repo"]

        if len(parts) == 2:
            custom = parts[1]
            if not NAME_RE.fullmatch(custom) or custom in (".", "..") or custom.lower().endswith(".git"):
                entry.error = (
                    f"linha {lineno}: nome de espelho inválido {custom!r}; "
                    "use até 100 letras, números, '.', '-' ou '_'"
                )
                continue
            entry.mirror = custom
        else:
            entry.mirror = mirror_name_for(entry.owner, entry.repo)

        url_key = entry.origin.lower()
        if url_key in seen_urls:
            errors.append(f"linha {lineno}: URL duplicada; {entry.origin} já aparece na linha {seen_urls[url_key]}")
        else:
            seen_urls[url_key] = lineno
        # o nome não entra na mensagem: com --hide-names os logs não podem exibi-lo
        name_key = entry.mirror.lower()
        if name_key in seen_names:
            errors.append(f"linha {lineno}: nome de espelho repetido; já usado na linha {seen_names[name_key]}")
        else:
            seen_names[name_key] = lineno

    if errors:
        raise RepoFileError(errors)
    notes = [
        f"categoria [{name}] (linha {lineno}) está sem repositórios ativos"
        for name, lineno, count in headers
        if count == 0
    ]
    return entries, notes


def select_entries(entries: list[Entry], only: str) -> list[Entry]:
    key = re.sub(r"^https?://(www\.)?github\.com/", "", only.strip(), flags=re.IGNORECASE)
    key = key.removesuffix("/").removesuffix(".git").lower()
    return [e for e in entries if key in {e.mirror.lower(), e.origin.lower(), e.url.lower()}]


def topic_slug(name: str) -> str:
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")[:50].rstrip("-")


# ---------------------------------------------------------------------- API REST/GraphQL


class ApiError(Exception):
    def __init__(self, status: int | None, message: str):
        super().__init__(message)
        self.status = status


def _error_message(raw: bytes) -> str:
    try:
        payload = json.loads(raw)
    except ValueError:
        return raw[:200].decode("utf-8", "replace").strip()
    if not isinstance(payload, dict):
        return ""
    details = [
        item.get("message") or item.get("code") or ""
        for item in payload.get("errors") or []
        if isinstance(item, dict)
    ]
    details = [d for d in details if d]
    message = payload.get("message") or ""
    return f"{message} ({'; '.join(details)})" if details else message


def _backoff(attempt: int) -> float:
    return 2**attempt + random.random()


def _retry_wait(status: int, headers, message: str, attempt: int) -> float | None:
    """Quanto esperar antes de repetir a chamada, ou None se o erro não é temporário."""
    retry_after = headers.get("Retry-After") or ""
    remaining = headers.get("X-RateLimit-Remaining")
    reset = headers.get("X-RateLimit-Reset") or ""
    limited = status == 429 or (
        status == 403 and (retry_after or remaining == "0" or "rate limit" in message.lower())
    )
    if limited:
        if retry_after.isdigit():
            wait = int(retry_after)
        elif remaining == "0" and reset.isdigit():
            wait = int(reset) - int(time.time()) + 1
        else:
            wait = 60 * 2**attempt  # limite secundário sem dica: o GitHub pede ao menos 1 min
        return max(wait, 1) if wait <= MAX_RETRY_WAIT else None
    if status in (500, 502, 503, 504):
        return _backoff(attempt)
    return None


class GitHub:
    def __init__(self, token: str):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "git-mirror-control",
        }

    def request(self, method: str, path: str, body: dict | None = None):
        """Chama a API REST com retry/backoff. Retorna (json, headers)."""
        data = json.dumps(body).encode() if body is not None else None
        if data is None and method in ("PUT", "POST", "PATCH"):
            data = b""  # o GitHub exige Content-Length: 0 (ex.: dar estrela)
        where = f"{method} {path}"
        for attempt in range(MAX_RETRIES + 1):
            req = urllib.request.Request(API_URL + path, data=data, method=method, headers=self.headers)
            if body is not None:
                req.add_header("Content-Type", "application/json")
            try:
                with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                    raw = resp.read()
                    try:
                        return (json.loads(raw) if raw else None), resp.headers
                    except ValueError:
                        raise ApiError(resp.status, f"{where} → resposta inválida (não é JSON)") from None
            except urllib.error.HTTPError as err:
                message = _error_message(err.read()) or str(err.reason)
                wait = _retry_wait(err.code, err.headers, message, attempt)
                if wait is None or attempt == MAX_RETRIES:
                    raise ApiError(err.code, f"{where} → HTTP {err.code}: {message}") from None
                log.info("  %s → HTTP %s (%s); nova tentativa em %.0fs", where, err.code, message, wait)
            except (OSError, http.client.HTTPException) as err:
                if attempt == MAX_RETRIES:
                    raise ApiError(None, f"{where} → sem resposta: {getattr(err, 'reason', err)}") from None
                wait = _backoff(attempt)
                log.info("  %s → sem resposta (%s); nova tentativa em %.0fs", where, err, wait)
            time.sleep(wait)
        raise AssertionError("inalcançável")

    def graphql(self, query: str, **variables) -> dict:
        for attempt in range(MAX_RETRIES + 1):
            payload, headers = self.request("POST", "/graphql", {"query": query, "variables": variables})
            errors = (payload or {}).get("errors") or []
            if attempt < MAX_RETRIES and any(e.get("type") == "RATE_LIMITED" for e in errors):
                reset = headers.get("X-RateLimit-Reset") or ""
                wait = int(reset) - int(time.time()) + 1 if reset.isdigit() else 60 * 2**attempt
                if wait <= MAX_RETRY_WAIT:
                    log.info("  GraphQL → rate limit; nova tentativa em %ds", max(wait, 1))
                    time.sleep(max(wait, 1))
                    continue
            if errors:
                detail = "; ".join(e.get("message") or str(e) for e in errors)
                raise ApiError(None, f"GraphQL: {detail}")
            if not isinstance(payload, dict) or payload.get("data") is None:
                raise ApiError(None, "GraphQL: resposta sem dados")
            return payload["data"]
        raise AssertionError("inalcançável")


# ----------------------------------------------------------------------------- git


class GitError(Exception):
    pass


GIT_HINTS = (
    ("`workflow` scope", "o token precisa do escopo `workflow` (classic) ou de Workflows: write (fine-grained)"),
    ("exceeds", "o GitHub limita cada push a 2 GB e cada arquivo a 100 MB"),
    ("Repository not found", "o token não tem acesso a este repositório"),
    ("denied", "o token não tem permissão de escrita"),
    ("error: 403", "o token não tem permissão de escrita"),
)


def _git_hint(message: str) -> str | None:
    return next((hint for needle, hint in GIT_HINTS if needle in message), None)


GIT_NOISE = ("hint:", "To ", "error: failed to push some refs")


def _git_errors(stderr: str, lines: int = 6) -> str:
    """Últimas linhas úteis do stderr do git (sem dicas e sem o genérico 'failed to push')."""
    useful = [line.strip() for line in stderr.splitlines() if line.strip() and not line.strip().startswith(GIT_NOISE)]
    return "\n".join(useful[-lines:])


def _first_line(text: str) -> str:
    return text.strip().splitlines()[0] if text.strip() else ""


class Git:
    """Executa git sem prompts e sem a config global; o token vai num header HTTP
    passado por variáveis de ambiente, nunca em URLs ou argumentos."""

    def __init__(self, token: str):
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k != "SSH_ASKPASS"}
        env.update(
            GIT_TERMINAL_PROMPT="0",
            GIT_CONFIG_GLOBAL=os.devnull,  # isola de ~/.gitconfig (insteadOf, helpers, hooks)
            GIT_CONFIG_COUNT="1",
            GIT_CONFIG_KEY_0="credential.helper",
            GIT_CONFIG_VALUE_0="",  # valor vazio zera os credential helpers
        )
        basic = base64.b64encode(f"x-access-token:{token}".encode()).decode()
        self.env_anon = env
        self.env_auth = {
            **env,
            "GIT_CONFIG_COUNT": "2",
            "GIT_CONFIG_KEY_1": f"http.{GIT_BASE_URL}/.extraHeader",
            "GIT_CONFIG_VALUE_1": f"Authorization: Basic {basic}",
        }

    def run(self, *args: str, auth: bool = True, timeout: int = GIT_TIMEOUT) -> str:
        try:
            proc = subprocess.run(
                ["git", *args],
                check=False,
                cwd=tempfile.gettempdir(),  # fora de qualquer repo: nenhuma config local interfere
                env=self.env_auth if auth else self.env_anon,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            raise GitError(f"git {_subcommand(args)}: tempo esgotado ({timeout}s)") from None
        if proc.returncode != 0:
            raise GitError(f"git {_subcommand(args)}: {_git_errors(proc.stderr) or f'código {proc.returncode}'}")
        return proc.stdout

    def ls_remote(self, url: str, *, auth: bool = True) -> dict[str, str]:
        return _parse_refs(self.run("ls-remote", "--heads", "--tags", url, auth=auth), peeled=True)

    def fetch(self, url: str, repo_dir: str, *, auth: bool = True) -> dict[str, str]:
        """Baixa só branches e tags (sem refs/pull/*) para um repo bare temporário."""
        self.run("init", "--bare", "--quiet", repo_dir, auth=False)
        self.run(
            f"--git-dir={repo_dir}", "fetch", "--quiet", url,
            "+refs/heads/*:refs/heads/*", "+refs/tags/*:refs/tags/*",
            auth=auth, timeout=GIT_TRANSFER_TIMEOUT,
        )
        out = self.run(
            f"--git-dir={repo_dir}", "for-each-ref", "--format=%(objectname)\t%(refname)",
            "refs/heads", "refs/tags", auth=False,
        )
        return _parse_refs(out)

    def push(self, repo_dir: str, url: str, refspecs: list[str]) -> None:
        for start in range(0, len(refspecs), PUSH_BATCH):
            batch = refspecs[start:start + PUSH_BATCH]
            for attempt in range(3):
                try:
                    self.run(f"--git-dir={repo_dir}", "push", "--quiet", url, *batch, timeout=GIT_TRANSFER_TIMEOUT)
                    break
                except GitError as err:
                    hint = _git_hint(str(err))
                    if hint:
                        raise GitError(f"{err}\n→ {hint}") from None
                    if attempt == 2:
                        raise
                    log.info("  push falhou (%s); nova tentativa", str(err).splitlines()[-1])
                    time.sleep(5 * (attempt + 1))


def _subcommand(args: tuple[str, ...]) -> str:
    return next((a for a in args if not a.startswith("-")), "")


def _parse_refs(out: str, *, peeled: bool = False) -> dict[str, str]:
    refs = {}
    for line in out.splitlines():
        sha, _, ref = line.partition("\t")
        if ref and not (peeled and ref.endswith("^{}")):
            refs[ref] = sha
    return refs


def git_url(full_name: str) -> str:
    return f"{GIT_BASE_URL}/{full_name}.git"


# ------------------------------------------------------------------- GitHub Lists

LISTS_QUERY = """
query($cursor: String) {
  viewer {
    lists(first: 100, after: $cursor) {
      pageInfo { hasNextPage endCursor }
      nodes {
        id name description
        items(first: 100) {
          pageInfo { hasNextPage endCursor }
          nodes { ... on Repository { nameWithOwner } }
        }
      }
    }
  }
}"""

LIST_ITEMS_QUERY = """
query($id: ID!, $cursor: String) {
  node(id: $id) {
    ... on UserList {
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes { ... on Repository { nameWithOwner } }
      }
    }
  }
}"""

CREATE_LIST_MUTATION = """
mutation($name: String!, $description: String, $isPrivate: Boolean) {
  createUserList(input: {name: $name, description: $description, isPrivate: $isPrivate}) {
    list { id name }
  }
}"""

SET_ITEM_LISTS_MUTATION = """
mutation($itemId: ID!, $listIds: [ID!]!) {
  updateUserListsForItem(input: {itemId: $itemId, listIds: $listIds}) {
    lists { id }
  }
}"""


@dataclass
class UserList:
    id: str | None
    name: str
    description: str
    items: set[str] = field(default_factory=set)  # nameWithOwner em minúsculas


def _item_names(items: dict) -> set[str]:
    return {n["nameWithOwner"].lower() for n in items["nodes"] if n and n.get("nameWithOwner")}


class Lists:
    """Cache das GitHub Lists da conta, carregado uma vez por execução.

    Uma lista é "gerenciada" se tem o nome de uma categoria do repos.txt ou a
    descrição "Mirrors – ...". Só essas são alteradas; as listas pessoais em que
    um espelho também esteja são preservadas.
    """

    def __init__(self, gh: GitHub, categories: set[str], *, dry_run: bool):
        self.gh = gh
        self.dry_run = dry_run
        self.categories = {c.casefold() for c in categories}
        self.lists: dict[str, UserList] = {}  # id → lista
        self.by_name: dict[str, str] = {}  # nome (casefold) → id
        self.broken: set[str] = set()
        self.emptied: set[str] = set()

    def load(self) -> None:
        cursor = None
        while True:
            page = self.gh.graphql(LISTS_QUERY, cursor=cursor)["viewer"]["lists"]
            for node in page["nodes"]:
                user_list = UserList(node["id"], node["name"], node.get("description") or "")
                items = node["items"]
                user_list.items |= _item_names(items)
                while items["pageInfo"]["hasNextPage"]:
                    items = self.gh.graphql(
                        LIST_ITEMS_QUERY, id=user_list.id, cursor=items["pageInfo"]["endCursor"]
                    )["node"]["items"]
                    user_list.items |= _item_names(items)
                self._add(user_list)
            if not page["pageInfo"]["hasNextPage"]:
                break
            cursor = page["pageInfo"]["endCursor"]

    def _add(self, user_list: UserList) -> None:
        self.lists[user_list.id] = user_list
        self.by_name.setdefault(user_list.name.casefold(), user_list.id)

    def _managed(self, user_list: UserList) -> bool:
        return user_list.name.casefold() in self.categories or user_list.description.startswith(LIST_PREFIX)

    def _list_for(self, category: str) -> str | None:
        """Id da lista da categoria, criada se faltar; None se não deu para criar."""
        key = category.casefold()
        if key in self.by_name:
            return self.by_name[key]
        if key in self.broken:
            return None
        description = LIST_PREFIX + category
        visibility = "privada" if LISTS_PRIVATE else "pública"
        if self.dry_run:
            log.info("  [dry-run] criaria a lista %s '%s'", visibility, category)
            self._add(UserList(f"dry-run:{category}", category, description))
            return self.by_name[key]
        try:
            data = self.gh.graphql(
                CREATE_LIST_MUTATION, name=category, description=description, isPrivate=LISTS_PRIVATE
            )
            created = (data.get("createUserList") or {}).get("list")
            if not created:
                raise ApiError(None, "GraphQL: createUserList não retornou a lista")
        except ApiError as err:
            self.broken.add(key)
            log.warning("não foi possível criar a lista '%s': %s", category, err)
            return None
        self._add(UserList(created["id"], created["name"], description))
        log.info("  lista %s '%s' criada", visibility, category)
        return created["id"]

    def assign(self, full_name: str, node_id: str | None, category: str | None) -> bool:
        """Deixa o espelho só na lista da sua categoria. Retorna True se algo mudou."""
        repo = full_name.lower()
        current = {list_id for list_id, user_list in self.lists.items() if repo in user_list.items}
        wanted = {list_id for list_id in current if not self._managed(self.lists[list_id])}
        if category:
            list_id = self._list_for(category)
            if list_id is None:
                return False
            wanted.add(list_id)
        if wanted == current:
            return False

        if not self.dry_run:
            if wanted - current:  # Lists só agrupam repos com estrela
                self.gh.request("PUT", f"/user/starred/{full_name}")
            self.gh.graphql(SET_ITEM_LISTS_MUTATION, itemId=node_id, listIds=sorted(wanted))
        for list_id in current - wanted:
            self.lists[list_id].items.discard(repo)
            self.emptied.add(list_id)
        for list_id in wanted - current:
            self.lists[list_id].items.add(repo)
        moves = sorted(f"saiu de '{self.lists[i].name}'" for i in current - wanted)
        moves += sorted(f"entrou em '{self.lists[i].name}'" for i in wanted - current)
        log.info("  %slista: %s", "[dry-run] " if self.dry_run else "", ", ".join(moves))
        return True

    def warn_emptied(self) -> None:
        for name in sorted(self.lists[i].name for i in self.emptied if not self.lists[i].items):
            log.warning("a lista '%s' ficou vazia; ela não é apagada automaticamente", name)


# --------------------------------------------------------------------- espelhamento


class SyncError(Exception):
    pass


@dataclass
class Origin:
    ok: bool
    reason: str = ""
    url: str = ""
    default_branch: str = ""
    refs: dict[str, str] = field(default_factory=dict)
    auth: bool = True


@dataclass
class Result:
    entry: Entry
    status: str = "failed"
    detail: str = ""
    recategorized: bool = False


class Mirrorer:
    def __init__(self, gh: GitHub, git: Git, login: str, *, dry_run: bool = False,
                 prune: bool = False, lists: Lists | None = None):
        self.gh = gh
        self.git = git
        self.login = login
        self.dry_run = dry_run
        self.prune = prune
        self.lists = lists
        self.tag = "[dry-run] " if dry_run else ""

    def probe_origin(self, e: Entry) -> Origin:
        try:
            info, _ = self.gh.request("GET", f"/repos/{e.owner}/{e.repo}")
        except ApiError as err:
            if err.status in (401, 429) or (err.status == 403 and "rate limit" in str(err).lower()):
                raise  # problema do token/cota, não da origem: vira falha, não proteção
            reason = {
                404: "HTTP 404: removida, renomeada sem redirect ou sem acesso",
                451: "HTTP 451: bloqueada por motivo legal, ex.: DMCA",
            }.get(err.status, str(err))
            return Origin(False, reason)
        if info.get("disabled"):
            return Origin(False, "repositório desativado pelo GitHub")
        if info["full_name"].lower() != e.origin.lower():
            log.info("  a origem agora é %s (renomeada ou transferida)", info["full_name"])

        origin = Origin(True, url=git_url(info["full_name"]), default_branch=info.get("default_branch") or "")
        try:
            origin.refs = self.git.ls_remote(origin.url)
        except GitError as err:
            if info.get("private"):
                return Origin(False, str(err))
            try:  # política de organização pode barrar tokens até em repo público
                origin.refs = self.git.ls_remote(origin.url, auth=False)
                origin.auth = False
            except GitError:
                return Origin(False, str(err))
        if not any(ref.startswith("refs/heads/") for ref in origin.refs):
            return Origin(False, "a origem não tem nenhum branch (foi esvaziada?)")
        return origin

    def find_mirror(self, e: Entry) -> dict | None:
        try:
            info, _ = self.gh.request("GET", f"/repos/{self.login}/{e.mirror}")
        except ApiError as err:
            if err.status == 404:
                return None
            raise
        expected = f"Mirror of {e.canonical_url}"
        if (info.get("description") or "").strip().casefold() != expected.casefold():
            raise SyncError(
                "já existe um repositório com o nome deste espelho, mas a descrição dele não é "
                f"'{expected}'; por segurança ele não será tocado. Use outro nome no repos.txt "
                "ou, se ele for mesmo o espelho, ajuste a descrição."
            )
        return info

    def sync(self, e: Entry) -> Result:
        result = Result(e)
        origin = self.probe_origin(e)
        mirror = self.find_mirror(e)
        if mirror and not mirror.get("private"):
            log.warning("%s: o espelho está PÚBLICO; torne-o privado em Settings › General", e.origin)

        if mirror and mirror.get("archived"):
            result.status, result.detail = "frozen", "espelho arquivado: nada muda até desarquivar"
            log.info("  %s", result.detail)
            return result
        if not origin.ok:
            if not mirror:
                raise SyncError(f"origem inacessível ({origin.reason}) e ainda não existe espelho; confira a URL")
            result.status, result.detail = "protected", f"origem inacessível ({origin.reason}); espelho mantido intacto"
            log.warning("%s: %s", e.origin, result.detail)
        elif not mirror:
            mirror, result.detail = self.create(e, origin)
            result.status = "created"
        else:
            result.status, result.detail = self.update(origin, mirror)

        if mirror is None:  # espelho novo numa simulação
            mirror = {"full_name": f"{self.login}/{e.mirror}", "node_id": None, "topics": []}
        result.recategorized = self.categorize(e, mirror) and result.status != "created"
        return result

    def create(self, e: Entry, origin: Origin) -> tuple[dict | None, str]:
        detail = f"cópia inicial: {len(origin.refs)} ref(s)"
        if self.dry_run:
            log.info("  [dry-run] criaria o espelho privado; %s", detail)
            return None, detail
        mirror, _ = self.gh.request("POST", "/user/repos", {
            "name": e.mirror,
            "description": f"Mirror of {e.canonical_url}",
            "private": True,
            "has_issues": False,
            "has_projects": False,
            "has_wiki": False,
        })
        log.info("  espelho privado criado")
        self.disable_actions(mirror, check=False)
        self.copy(origin, mirror, mirror_refs={})
        return mirror, detail

    def update(self, origin: Origin, mirror: dict) -> tuple[str, str]:
        mirror_refs = self.git.ls_remote(git_url(mirror["full_name"]))
        stale = [ref for ref, sha in origin.refs.items() if mirror_refs.get(ref) != sha]
        extra = [ref for ref in mirror_refs if ref not in origin.refs]
        kept = f"{len(extra)} ref(s) só no espelho, mantidos (--prune apaga)" if extra and not self.prune else ""

        if not stale and not (self.prune and extra):
            self.sync_default_branch(mirror, origin, mirror_refs)
            log.info("  em dia%s", f"; {kept}" if kept else "")
            return "uptodate", kept
        if self.dry_run:
            parts = [f"{len(stale)} ref(s) a atualizar"]
            if self.prune and extra:
                parts.append(f"{len(extra)} a remover (--prune)")
            log.info("  [dry-run] %s", ", ".join(parts))
            return "updated", ", ".join(parts)
        self.disable_actions(mirror, check=True)
        detail = self.copy(origin, mirror, mirror_refs)
        return "updated", "; ".join(filter(None, [detail, kept]))

    def copy(self, origin: Origin, mirror: dict, mirror_refs: dict[str, str]) -> str:
        """Busca branches/tags da origem e faz push forçado só do que mudou."""
        url = git_url(mirror["full_name"])
        with tempfile.TemporaryDirectory(prefix="mirror-") as tmp:
            repo_dir = os.path.join(tmp, "repo.git")
            local = self.git.fetch(origin.url, repo_dir, auth=origin.auth)
            changed = sorted(ref for ref, sha in local.items() if mirror_refs.get(ref) != sha)
            self.git.push(repo_dir, url, [f"+{ref}:{ref}" for ref in changed])
            # antes do --prune: o GitHub recusa apagar o branch padrão
            self.sync_default_branch(mirror, origin, local)
            removed = sorted(ref for ref in mirror_refs if ref not in local) if self.prune else []
            if removed:
                self.git.push(repo_dir, url, [f":{ref}" for ref in removed])
        detail = f"{len(changed)} ref(s) enviados" + (f", {len(removed)} removidos (--prune)" if removed else "")
        log.info("  %s", detail)
        return detail

    def sync_default_branch(self, mirror: dict, origin: Origin, refs: dict[str, str]) -> None:
        wanted = origin.default_branch
        if not wanted or mirror.get("default_branch") == wanted or f"refs/heads/{wanted}" not in refs:
            return
        if not self.dry_run:
            self.gh.request("PATCH", f"/repos/{mirror['full_name']}", {"default_branch": wanted})
        mirror["default_branch"] = wanted
        log.info("  %sbranch padrão do espelho → %s", self.tag, wanted)

    def disable_actions(self, mirror: dict, *, check: bool) -> None:
        """Desliga o Actions do espelho: workflows copiados da origem não rodam nem gastam minutos."""
        path = f"/repos/{mirror['full_name']}/actions/permissions"
        try:
            if check:
                permissions, _ = self.gh.request("GET", path)
                if not permissions.get("enabled"):
                    return
            self.gh.request("PUT", path, {"enabled": False})
        except ApiError as err:
            log.warning("não foi possível desativar o Actions do espelho: %s", err)

    def categorize(self, e: Entry, mirror: dict) -> bool:
        """Aplica topics e a GitHub List da categoria.

        Qualquer falha aqui vira aviso: categorizar nunca invalida o espelhamento.
        """
        changed = False
        slug = topic_slug(e.category or "")
        topics = [MIRROR_TOPIC] + ([slug] if slug and slug != MIRROR_TOPIC else [])
        if sorted(mirror.get("topics") or []) != sorted(topics):
            try:
                if not self.dry_run:
                    self.gh.request("PUT", f"/repos/{mirror['full_name']}/topics", {"names": topics})
                log.info("  %stopics → %s", self.tag, ", ".join(topics))
                changed = True
            except Exception as err:
                log.warning("%s: não foi possível aplicar os topics: %s", e.origin, err)
        if self.lists:
            try:
                changed |= self.lists.assign(mirror["full_name"], mirror.get("node_id"), e.category)
            except Exception as err:
                log.warning("%s: a categorização em Lists falhou: %s", e.origin, err)
        return changed

    def status_of(self, e: Entry) -> str:
        """Status para o comando list, sem alterar nada."""
        if e.error:
            return f"inválida: {e.error}"
        try:
            origin = self.probe_origin(e)
            mirror = self.find_mirror(e)
            if not mirror:
                return "a criar" if origin.ok else f"a criar, mas a origem está inacessível ({origin.reason})"
            if mirror.get("archived"):
                return "existe (arquivado: congelado)"
            if not origin.ok:
                return f"existe; origem inacessível ({origin.reason})"
            mirror_refs = self.git.ls_remote(git_url(mirror["full_name"]))
        except SyncError:
            return "conflito: o nome já é de um repositório que não é este espelho"
        except (ApiError, GitError) as err:
            return f"erro: {err}"
        stale = sum(1 for ref, sha in origin.refs.items() if mirror_refs.get(ref) != sha)
        return f"desatualizado ({stale} ref(s))" if stale else "em dia"


# ------------------------------------------------------------------ logs e resumo

STATUS_TEXT = {
    # status: (ícone, rótulo, rótulo na simulação)
    "created": ("✨", "criado", "a criar"),
    "updated": ("🔄", "atualizado", "a atualizar"),
    "uptodate": ("✅", "em dia", "em dia"),
    "protected": ("🛡️", "protegido", "protegido"),
    "frozen": ("🧊", "congelado", "congelado"),
    "deferred": ("⏭️", "adiado", "adiado"),
    "failed": ("❌", "falha", "falha"),
}
SUMMARY_COLUMNS = (
    ("created", "Criados", "A criar"),
    ("updated", "Atualizados", "A atualizar"),
    ("uptodate", "Em dia", "Em dia"),
    ("protected", "Protegidos", "Protegidos"),
    ("frozen", "Congelados", "Congelados"),
    ("deferred", "Adiados", "Adiados"),
    ("recategorized", "Recategorizados", "A recategorizar"),
    ("failed", "Falhas", "Falhas"),
)


def summary_columns(counts: Counter, dry_run: bool) -> list[tuple[str, str]]:
    """Colunas do resumo; congelados e adiados só aparecem quando existem."""
    return [(key, dry if dry_run else label) for key, label, dry in SUMMARY_COLUMNS
            if key not in ("frozen", "deferred") or counts[key]]


def _keep(text: str) -> str:
    return text


def make_scrubber(login: str, names: list[str]):
    """Troca '<login>/<espelho>' (em URLs e caminhos da API) por '<login>/(oculto)'."""
    if not names:
        return _keep
    alternatives = "|".join(re.escape(n) for n in sorted(set(names), key=len, reverse=True))
    pattern = re.compile(
        rf"(?<![\w.-]){re.escape(login)}/(?:{alternatives})(?=(?:\.git)?(?![\w.-]))", re.IGNORECASE
    )
    return lambda text: pattern.sub(f"{login}/(oculto)", text)


class LogFormatter(logging.Formatter):
    def __init__(self, ci: bool):
        super().__init__("%(message)s" if ci else "%(asctime)s %(levelname)-5s %(message)s", "%H:%M:%S")
        self.ci = ci
        self.scrub = _keep

    def format(self, record: logging.LogRecord) -> str:
        text = self.scrub(super().format(record))
        if self.ci and record.levelno >= logging.WARNING:
            # vira anotação do Actions; escapar quebras também impede injetar comandos
            kind = "error" if record.levelno >= logging.ERROR else "warning"
            return f"::{kind}::" + text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        return text.replace("\n", "\n      ")


class WarningCollector(logging.Handler):
    """Guarda os avisos para o resumo da execução."""

    def __init__(self):
        super().__init__(logging.WARNING)
        self.scrub = _keep
        self.messages: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        if record.levelno == logging.WARNING:
            self.messages.append(self.scrub(record.getMessage()))


def setup_logging(ci: bool) -> tuple[LogFormatter, WarningCollector]:
    logging.addLevelName(logging.WARNING, "AVISO")
    logging.addLevelName(logging.ERROR, "ERRO")
    formatter = LogFormatter(ci)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    collector = WarningCollector()
    log.handlers[:] = [handler, collector]
    log.setLevel(logging.INFO)
    log.propagate = False
    return formatter, collector


@contextlib.contextmanager
def log_group(ci: bool, title: str):
    if ci:
        print(f"::group::{title}", flush=True)
    try:
        yield
    finally:
        if ci:
            print("::endgroup::", flush=True)


def _md(text: str) -> str:
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("<", "&lt;").replace("\n", " ")


def render_summary(results: list[Result], counts: Counter, *, dry_run: bool, hide_names: bool,
                   login: str, warnings: list[str]) -> str:
    out = ["## 🪞 Espelhamento de repositórios", ""]
    if dry_run:
        out += ["> **Simulação** (`--dry-run`): nada foi alterado.", ""]
    if not results:
        out.append("Nenhum repositório ativo no `repos.txt`.")
    columns = summary_columns(counts, dry_run)
    if results:
        out.append("| " + " | ".join(label for _, label in columns) + " |")
        out.append("|" + ":-:|" * len(columns))
        out.append("| " + " | ".join(str(counts[key]) for key, _ in columns) + " |")

    groups: dict[str, list[Result]] = {}
    for result in results:
        groups.setdefault(result.entry.category or "Sem categoria", []).append(result)
    for category, rows in groups.items():
        header = ["Origem"] + ([] if hide_names else ["Espelho"]) + ["Status", "Detalhes"]
        out += ["", f"### {_md(category)}", "", "| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
        for result in rows:
            e = result.entry
            icon, label, dry_label = STATUS_TEXT[result.status]
            status = f"{icon} {dry_label if dry_run else label}"
            if result.recategorized:
                status += " · 🏷️ recategorizado"
            cells = [f"[{e.origin}]({e.canonical_url})" if e.owner else f"`{_md(e.url)}`"]
            if not hide_names:
                cells.append(f"[{e.mirror}](https://github.com/{login}/{e.mirror})" if e.mirror else "—")
            cells += [status, _md(result.detail)]
            out.append("| " + " | ".join(cells) + " |")

    if warnings:
        out += ["", f"<details><summary>⚠️ Avisos ({len(warnings)})</summary>", ""]
        out += [f"- {_md(w)}" for w in warnings]
        out += ["", "</details>"]
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------------ comandos


def whoami(gh: GitHub) -> tuple[str, str | None]:
    me, headers = gh.request("GET", "/user")
    return me["login"], headers.get("X-OAuth-Scopes")  # o header só existe em token classic


def check_scopes(scopes: str | None, *, lists: bool) -> None:
    if scopes is None:
        return
    granted = {s.strip() for s in scopes.split(",")}
    missing = [s for s in ("repo", "workflow") + (("user",) if lists else ()) if s not in granted]
    if missing:
        log.warning(
            "o token (classic) não tem o(s) escopo(s) %s; veja a seção do token no README",
            ", ".join(f"`{s}`" for s in missing),
        )


@dataclass
class Session:
    gh: GitHub
    git: Git
    login: str
    scopes: str | None
    ci: bool
    collector: WarningCollector
    scrub: Callable[[str], str]
    started: float


def cmd_sync(args, session: Session, all_entries: list[Entry], entries: list[Entry]) -> int:
    check_scopes(session.scopes, lists=not args.skip_lists)
    lists = None
    if not args.skip_lists and entries:
        lists = Lists(session.gh, {e.category for e in all_entries if e.category}, dry_run=args.dry_run)
        try:
            lists.load()
        except Exception as err:  # sem Lists o espelhamento segue normalmente
            log.warning("não foi possível ler suas Lists (%s); "
                        "a categorização em Lists fica de fora desta execução", err)
            lists = None
    mirrorer = Mirrorer(session.gh, session.git, session.login,
                        dry_run=args.dry_run, prune=args.prune, lists=lists)

    if args.dry_run:
        log.info("SIMULAÇÃO (--dry-run): nada será alterado")
    if not entries:
        log.info("nenhum repositório ativo no repos.txt; nada a fazer")

    results: list[Result] = []
    for index, e in enumerate(entries):
        # o 1º repo sempre roda: assim toda execução avança, mesmo se o anterior demorar
        if index and time.monotonic() - session.started > TIME_BUDGET:
            left = entries[index:]
            log.warning("tempo da execução esgotado (%d min): %d entrada(s) ficam para a próxima execução",
                        TIME_BUDGET // 60, len(left))
            results += [Result(rest, "deferred", "tempo da execução esgotado; fica para a próxima") for rest in left]
            break
        with log_group(session.ci, e.origin):
            target = "" if args.hide_names or not e.mirror else f" → {e.mirror}"
            log.info("▶ %s%s  [%s]", e.origin, target, e.category or "sem categoria")
            try:
                if e.error:
                    raise SyncError(e.error)
                result = mirrorer.sync(e)
            except (SyncError, ApiError, GitError) as err:
                result = Result(e, "failed", str(err))
                log.error("%s: %s", e.origin, err)
            except Exception as err:  # bug inesperado: registra e segue para o próximo repo
                result = Result(e, "failed", f"erro inesperado: {err!r}")
                log.exception("%s: erro inesperado", e.origin)
        results.append(result)

    if lists:
        lists.warn_emptied()

    counts = Counter(r.status for r in results)
    counts["recategorized"] = sum(r.recategorized for r in results)
    columns = summary_columns(counts, args.dry_run)
    log.info("Resumo: %s", " · ".join(f"{label.lower()}: {counts[key]}" for key, label in columns))
    for result in results:
        if result.status == "failed":
            log.info("  ❌ %s: %s", result.entry.origin, _first_line(result.detail))
    log.info("Concluído em %.0fs", time.monotonic() - session.started)

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        markdown = render_summary(results, counts, dry_run=args.dry_run, hide_names=args.hide_names,
                                  login=session.login, warnings=session.collector.messages)
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write(session.scrub(markdown))
    return 1 if counts["failed"] else 0


def cmd_list(args, session: Session, entries: list[Entry]) -> int:
    if not entries:
        print("Nenhum repositório ativo no repos.txt.")
        return 0
    mirrorer = Mirrorer(session.gh, session.git, session.login, dry_run=True)
    header = ["CATEGORIA", "ORIGEM"] + ([] if args.hide_names else ["ESPELHO"]) + ["STATUS"]
    rows = []
    for e in entries:
        row = [e.category or "—", e.origin] + ([] if args.hide_names else [e.mirror or "—"])
        rows.append(row + [session.scrub(mirrorer.status_of(e).replace("\n", " "))])
    widths = [max(len(row[i]) for row in [header, *rows]) for i in range(len(header) - 1)]
    for row in [header, *rows]:
        # a última coluna (status) não é alinhada, por isso zip mais curto que row
        print("  ".join([cell.ljust(width) for cell, width in zip(row, widths, strict=False)] + [row[-1]]))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mirror.py",
        description="Espelha repositórios do GitHub como repositórios privados na sua conta, "
                    "organizados em GitHub Lists conforme as categorias do repos.txt.",
        epilog="O token é lido da variável GITHUB_TOKEN. Guia completo no README.md.",
        add_help=False,
    )
    parser.add_argument("-h", "--help", action="help", help="mostra esta ajuda e sai")
    commands = parser.add_subparsers(dest="command", required=True, metavar="comando")

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("-h", "--help", action="help", help="mostra esta ajuda e sai")
    common.add_argument("--hide-names", action="store_true",
                        help="oculta os nomes dos espelhos nos logs e no resumo (para logs públicos)")

    sync = commands.add_parser(
        "sync", parents=[common], add_help=False, help="cria e atualiza os espelhos do repos.txt",
        description="Cria os espelhos que faltam, atualiza os desatualizados e aplica Lists e topics.",
    )
    sync.add_argument("--only", metavar="NOME",
                      help="processa só esta entrada (nome do espelho, owner/repo ou URL)")
    sync.add_argument("--dry-run", action="store_true", help="mostra o que seria feito, sem alterar nada")
    sync.add_argument("--prune", action="store_true",
                      help="apaga do espelho os branches e tags que não existem mais na origem")
    sync.add_argument("--skip-lists", action="store_true",
                      help="não mexe em estrelas nem em GitHub Lists (os topics continuam)")

    commands.add_parser(
        "list", parents=[common], add_help=False, help="mostra categoria, espelho e status de cada entrada",
        description="Mostra cada entrada com categoria, nome do espelho e status "
                    "(a criar / em dia / desatualizado / existe), sem alterar nada.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    started = time.monotonic()
    ci = os.environ.get("GITHUB_ACTIONS") == "true"
    formatter, collector = setup_logging(ci)

    try:
        all_entries, notes = parse_repos_file(REPOS_FILE)
    except RepoFileError as err:
        for message in err.errors:
            log.error("repos.txt, %s", message)
        log.error("nada foi feito: corrija o repos.txt")
        return 2
    for note in notes:
        log.info(note)

    entries = all_entries
    if getattr(args, "only", None):
        entries = select_entries(all_entries, args.only)
        if not entries:
            log.error("--only %s: nenhuma entrada do repos.txt corresponde", args.only)
            return 2

    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        log.error(
            "a variável GITHUB_TOKEN não está definida. No GitHub Actions, cadastre o secret "
            "MIRROR_TOKEN; localmente, rode: export GITHUB_TOKEN=<seu token> (veja o README)"
        )
        return 2

    gh = GitHub(token)
    try:
        login, scopes = whoami(gh)
    except ApiError as err:
        if err.status == 401:
            log.error("o token foi recusado (HTTP 401): está expirado ou foi revogado; "
                      "gere outro e atualize o secret MIRROR_TOKEN (veja o README)")
        else:
            log.error("não foi possível validar o token: %s", err)
        return 2
    if ACCOUNT and login.casefold() != ACCOUNT.casefold():
        log.error("o token é da conta %s, mas os espelhos devem ficar em %s: gere o token logado como %s "
                  "(ou ajuste ACCOUNT no mirror.py)", login, ACCOUNT, ACCOUNT)
        return 2

    scrub = _keep
    if args.hide_names:
        scrub = make_scrubber(login, [e.mirror for e in all_entries if e.mirror])
        formatter.scrub = collector.scrub = scrub
    session = Session(gh, Git(token), login, scopes, ci, collector, scrub, started)

    if args.command == "list":
        return cmd_list(args, session, entries)
    return cmd_sync(args, session, all_entries, entries)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
