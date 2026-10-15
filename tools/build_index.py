#!/usr/bin/env python3
"""Gera guias/README.md (o índice) a partir da tabela de cada guia.

Uso: python tools/build_index.py
Cada guia precisa ter o título `# Nome (Console)` e a tabela Item/Detalhe do modelo.
Um guia com "⚠️ Suspeito" ou "Indisponível" no topo entra na lista de alertas.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from mirror import REPOS_FILE, parse_repos_file, topic_slug  # noqa: E402 — mesmo parser do sync

GUIDES = ROOT / "guias"
ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$", re.M)
ARCH = (("Nativo", "✅"), ("Via", "🟡"), ("Não documentado", "❔"), ("Não", "❌"))
WINDOWS = (("Nativo", "✅"), ("Via", "🟡"), ("Não documentado", "❔"), ("Não", "❌"))


def icon(value: str, table) -> str:
    return next((mark for prefix, mark in table if value.startswith(prefix)), "❔")


def read_guide(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), path.stem)
    rows = {key: value for key, value in ROW_RE.findall(text) if key not in ("Item", "---")}
    head = text[:600]
    flags = [label for key, label in (("⚠️ Suspeito", "⚠️ suspeito"), ("Indisponível", "indisponível")) if key in head]
    return {"title": title, "rows": rows, "alert": " e ".join(flags)}


def main() -> int:
    entries, _ = parse_repos_file(REPOS_FILE)
    order: dict[str, list] = {}
    for e in entries:
        if not e.error:
            order.setdefault(e.category or "Sem categoria", []).append(e)

    play_now, alerts, sections = [], [], []
    total = 0
    for category, items in order.items():
        slug = topic_slug(category) or "sem-categoria"
        lines = [f"## {category}", "", "| Jogo | Tipo | Arch Linux | Windows | Dificuldade | Guia |", "|---|---|:-:|:-:|---|---|"]
        for e in items:
            rel = f"{slug}/{e.owner}-{e.repo}.md".lower()
            path = GUIDES / rel
            if not path.exists():
                lines.append(f"| {e.origin} | — | — | — | — | sem guia |")
                continue
            total += 1
            g = read_guide(path)
            r = g["rows"]
            arch, win = icon(r.get("Arch Linux", ""), ARCH), icon(r.get("Windows", ""), WINDOWS)
            difficulty = r.get("Dificuldade", "—").split(" (")[0]
            lines.append(f"| {g['title']} | {r.get('Tipo', '—')} | {arch} | {win} | {difficulty} | [guia]({rel}) |")
            if g["alert"]:
                alerts.append(f"- {g['alert']}: [{g['title']}]({rel}) — {e.canonical_url}")
            elif r.get("Executável pronto", "").startswith("Sim"):
                play_now.append(f"| {g['title']} | {arch} | {win} | [guia]({rel}) |")
        sections.append("\n".join(lines))

    out = [
        "# Guias de instalação",
        "",
        "Como instalar cada repositório do [`repos.txt`](../repos.txt), do zero até jogar (ou usar), "
        "no Arch Linux e no Windows. Gerado por `tools/build_index.py`; confira pendências com "
        "`python tools/check_guides.py`.",
        "",
        "**Legenda:** ✅ nativo · 🟡 via Proton/Wine/WSL · ❌ não suportado · ❔ não documentado",
        "",
        "> Nenhum guia indica onde baixar ROMs, ISOs, BIOS ou jogos: o arquivo pedido em cada guia "
        "tem de vir da sua própria cópia.",
        "",
        "## Jogue agora (executável pronto)",
        "",
        "| Jogo | Arch Linux | Windows | Guia |",
        "|---|:-:|:-:|---|",
        *(play_now or ["| — | | | |"]),
        "",
        "## Indisponíveis ou suspeitos",
        "",
        *(alerts or ["Nenhum."]),
        "",
        *[s + "\n" for s in sections],
    ]
    (GUIDES / "README.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"guias/README.md: {total} guias, {len(play_now)} prontos para jogar, {len(alerts)} alertas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
