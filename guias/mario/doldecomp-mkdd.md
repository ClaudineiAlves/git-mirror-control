# Mario Kart: Double Dash!! · mkdd (GameCube)

Repositório: https://github.com/doldecomp/mkdd · Espelho: https://github.com/alves-r/mirror-doldecomp-mkdd

Decompilação 1:1 em andamento do Mario Kart: Double Dash!!. Por enquanto só a versão de debug é suportada, e o build não gera nada jogável.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | A imagem de disco da versão de debug em `orig/MarioClub_us/`. Formatos aceitos: ISO (GCM), RVZ, WIA, WBFS, CISO, NFS, GCZ e TGC. ⚠️ Você indicou que não consegue dumpar GameCube. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento; só a versão de debug é suportada. |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o Mario Kart: Double Dash!! original roda no Dolphin com a sua cópia (sugestão).

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed git python ninja`
2. Clone com os submódulos: `git clone --recursive https://github.com/doldecomp/mkdd.git && cd mkdd`
3. Copie a imagem do disco para `orig/MarioClub_us/`.
4. Configure com `python configure.py` e compile com `ninja`.

## Windows

1. Instale o Python (python.org, marcando **Add python.exe to PATH**), o ninja (`pip install ninja`) e o Git for Windows.
2. Clone com `git clone --recursive https://github.com/doldecomp/mkdd.git` e copie a imagem para `orig\MarioClub_us\`.
3. Rode `python configure.py` e depois `ninja`.

## Fontes

- [README › Dependencies e Building](https://github.com/doldecomp/mkdd#readme)

<!-- verificado: 2026-10-15 -->
