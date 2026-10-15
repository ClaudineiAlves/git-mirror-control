# The Legend of Zelda: The Wind Waker · tww (GameCube)

Repositório: https://github.com/zeldaret/tww · Espelho: https://github.com/alves-r/mirror-zeldaret-tww

Decompilação em andamento do The Wind Waker de GameCube. Não gera nada jogável: o build recria o executável do jogo para conferir se bate com o original.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | A imagem de disco em `orig/<ID>/`. Versões: `GZLE01` (EUA Rev 0 e Coreia Rev 48), `GZLP01` (PAL), `GZLJ01` (Japão) e `D44J01` (demo de quiosque japonesa). Formatos: ISO (GCM), RVZ, WIA, WBFS, CISO, NFS, GCZ e TGC. ⚠️ Você indicou que não consegue dumpar GameCube. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento; todas as versões de GameCube são suportadas. |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o Wind Waker original roda no Dolphin com a sua cópia (sugestão).

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed git python ninja`
2. Clone: `git clone https://github.com/zeldaret/tww.git && cd tww`
3. Copie a imagem do disco para `orig/GZLE01/`. Depois do primeiro build, ela pode ser apagada.
4. Configure: `python configure.py`. Para outra versão, use `--version GZLJ01` (Japão) ou `--version GZLP01` (PAL).
5. Compile: `ninja`

## Windows

O README recomenda as ferramentas nativas do Windows, sem WSL nem MSYS2.

1. Instale o Python (python.org, marcando **Add python.exe to PATH**), o ninja (`pip install ninja`) e o Git for Windows.
2. Clone o repositório e copie a imagem para `orig\GZLE01\`.
3. Rode `python configure.py` e depois `ninja`.

## Fontes

- [README › Dependencies e Building](https://github.com/zeldaret/tww#readme)

<!-- verificado: 2026-10-15 -->
