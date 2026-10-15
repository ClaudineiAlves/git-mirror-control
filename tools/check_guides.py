#!/usr/bin/env python3
"""Confere os guias de instalação (guias/) contra o repos.txt e o GitHub.

Lista:
- repos do repos.txt sem guia;
- guias de repos que saíram da lista;
- guias desatualizados: o último push do repo é posterior à data da linha
  `<!-- verificado: AAAA-MM-DD -->` no fim do guia;
- links do índice guias/README.md que apontam para arquivos inexistentes.

Uso: python tools/check_guides.py [--offline]
O token vem de GITHUB_TOKEN, GH_TOKEN ou `gh auth token`; sem token a API limita a 60 consultas/hora.
Sai com código 1 quando há algo a fazer.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from mirror import REPOS_FILE, RepoFileError, parse_repos_file, topic_slug  # noqa: E402 — mesmo parser do sync

GUIDES = ROOT / "guias"
VERIFIED_RE = re.compile(r"<!--\s*verificado:\s*(\d{4}-\d{2}-\d{2})\s*-->")
LINK_RE = re.compile(r"\]\((?!https?://)([^)#\s]+\.md)(?:#[^)]*)?\)")


def guide_path(entry) -> Path:
    folder = topic_slug(entry.category or "") or "sem-categoria"
    return GUIDES / folder / f"{entry.owner}-{entry.repo}.md".lower()


def token() -> str:
    for name in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(name, "").strip():
            return os.environ[name].strip()
    try:
        proc = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10, check=False)
        return proc.stdout.strip() if proc.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def pushed_at(full_name: str, auth: str) -> str:
    """Data (AAAA-MM-DD) do último push, ou 'indisponível (HTTP …)'."""
    req = urllib.request.Request(f"https://api.github.com/repos/{full_name}", headers={
        "Accept": "application/vnd.github+json", "User-Agent": "git-mirror-control-guides",
        **({"Authorization": f"Bearer {auth}"} if auth else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return (json.load(resp).get("pushed_at") or "")[:10]
    except urllib.error.HTTPError as err:
        return f"indisponível (HTTP {err.code})"
    except (urllib.error.URLError, TimeoutError) as err:
        return f"indisponível ({getattr(err, 'reason', err)})"


def broken_index_links() -> list[str]:
    index = GUIDES / "README.md"
    if not index.exists():
        return ["guias/README.md não existe"]
    text = index.read_text(encoding="utf-8")
    return [link for link in LINK_RE.findall(text) if not (GUIDES / link).resolve().is_file()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Confere os guias contra o repos.txt e o GitHub.")
    parser.add_argument("--offline", action="store_true", help="não consulta o GitHub (pula a checagem de datas)")
    args = parser.parse_args(argv)

    try:
        entries, _ = parse_repos_file(REPOS_FILE)
    except RepoFileError as err:
        print("repos.txt inválido:\n  " + "\n  ".join(err.errors))
        return 2
    entries = [e for e in entries if not e.error]
    expected = {guide_path(e): e for e in entries}
    existing = {p for p in GUIDES.rglob("*.md") if p.name != "README.md"} if GUIDES.exists() else set()

    missing = [(p, e) for p, e in expected.items() if p not in existing]
    orphans = sorted(existing - expected.keys())
    undated, outdated, unavailable = [], [], []

    present = [(p, e) for p, e in expected.items() if p in existing]
    dates = {}
    for path, entry in present:
        found = VERIFIED_RE.search(path.read_text(encoding="utf-8"))
        if found:
            dates[path] = found.group(1)
        else:
            undated.append(path)
    if not args.offline:
        auth = token()
        with ThreadPoolExecutor(max_workers=8) as pool:
            pushes = dict(zip(dates, pool.map(lambda p: pushed_at(expected[p].origin, auth), dates)))
        for path, pushed in pushes.items():
            if pushed.startswith("indisponível"):
                unavailable.append((path, pushed))
            elif pushed > dates[path]:
                outdated.append((path, dates[path], pushed))
    broken = broken_index_links()

    def rel(path: Path) -> str:
        return str(path.relative_to(ROOT))

    sections = [
        ("Repos sem guia", [f"{rel(p)}  ({e.canonical_url})" for p, e in missing]),
        ("Guias de repos que saíram do repos.txt", [rel(p) for p in orphans]),
        ("Guias desatualizados (refazer)", [f"{rel(p)}  verificado {d}, último push {u}" for p, d, u in outdated]),
        ("Guias sem a linha <!-- verificado: AAAA-MM-DD -->", [rel(p) for p in undated]),
        ("Repos indisponíveis no GitHub", [f"{rel(p)}  {why}" for p, why in unavailable]),
        ("Links quebrados no guias/README.md", broken),
    ]
    pending = False
    for title, items in sections:
        if items:
            pending = True
            print(f"{title} ({len(items)}):")
            print("\n".join(f"  - {item}" for item in items))
    if not pending:
        offline = " (datas não conferidas: --offline)" if args.offline else ""
        print(f"Tudo em dia: {len(present)} guias para {len(expected)} repos{offline}.")
    return 1 if pending else 0


if __name__ == "__main__":
    sys.exit(main())
