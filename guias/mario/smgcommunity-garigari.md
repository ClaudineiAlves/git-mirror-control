# Super Mario Galaxy 2 · Garigari (Wii)

Repositório: https://github.com/SMGCommunity/Garigari · Espelho: https://github.com/alves-r/mirror-smgcommunity-garigari

Decompilação em andamento do Super Mario Galaxy 2. Não gera nada jogável, e o README avisa que não é um port para PC.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | O jogo extraído pelo Dolphin para `orig/SB4E01/` (EUA). Basta o `sys/main.dol`. O README ainda mostra o marcador `GAMEID`; o ID real é o da pasta `config/` do repositório. ⚠️ Você indicou que não consegue dumpar Wii. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o Super Mario Galaxy 2 original roda no Dolphin com a sua cópia (sugestão).

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed git python ninja dolphin-emu`
2. Clone: `git clone https://github.com/SMGCommunity/Garigari.git && cd Garigari`
3. No Dolphin, extraia a partição de dados do jogo (**Data Partition → Extract Entire Partition**) para `orig/SB4E01/`. Basta manter `sys/main.dol`.
4. Configure com `python configure.py` e compile com `ninja`.

## Windows

1. Instale o Python (python.org, marcando **Add python.exe to PATH**), o ninja (`pip install ninja`), o Git for Windows e o Dolphin.
2. Clone o repositório.
3. Extraia o jogo pelo Dolphin para `orig\SB4E01\`.
4. Rode `python configure.py` e depois `ninja`.

## Fontes

- [README › Dependencies e Building](https://github.com/SMGCommunity/Garigari#readme)
- [Pasta config/ do repositório](https://github.com/SMGCommunity/Garigari/tree/main/config)

<!-- verificado: 2026-10-15 -->
