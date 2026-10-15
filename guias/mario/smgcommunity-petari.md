# Super Mario Galaxy · Petari (Wii)

Repositório: https://github.com/SMGCommunity/Petari · Espelho: https://github.com/alves-r/mirror-smgcommunity-petari

Decompilação em andamento do Super Mario Galaxy. Não gera nada jogável: o build recria o executável do jogo para conferir se bate com o original, e o README avisa que não é um port para PC.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | O jogo extraído pelo Dolphin para `orig/RMGX01/`, onde X é a região (`RMGJ01`, `RMGE01`, `RMGP01` ou `RMGK01`). Basta o `sys/main.dol`. ⚠️ Você indicou que não consegue dumpar Wii. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento; o progresso por região aparece no decomp.dev. A equipe cita um port para PC separado, o "AstroCore". |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o Super Mario Galaxy original roda no Dolphin com a sua cópia (sugestão: `sudo pacman -S dolphin-emu` no Arch).

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed git python ninja dolphin-emu`. No Linux, o `wibo` é baixado sozinho.
2. Clone: `git clone https://github.com/SMGCommunity/Petari.git && cd Petari`
3. No Dolphin, clique com o botão direito no jogo e escolha **Data Partition → Extract Entire Partition**, com destino `orig/RMGX01/` (X é a região). Basta manter `sys/main.dol`.
4. Configure: `python configure.py`. Sem opção, a versão usada é a `RMGK01` (Coreia); para outra, use `--version RMGE01`, por exemplo.
5. Compile: `ninja`

## Windows

O README recomenda as ferramentas nativas do Windows, sem WSL nem MSYS2.

1. Instale o Python (python.org) e marque **Add python.exe to PATH**.
2. Instale o ninja: `pip install ninja`
3. Instale o Git for Windows e o Dolphin.
4. Clone: `git clone https://github.com/SMGCommunity/Petari.git` e entre na pasta.
5. Extraia o jogo pelo Dolphin para `orig\RMGX01\`, como no passo 3 da seção Arch Linux.
6. Rode `python configure.py` (ou com `--version`) e depois `ninja`.

## Fontes

- [README › Dependencies e Building](https://github.com/SMGCommunity/Petari#readme)

<!-- verificado: 2026-10-15 -->
