# Paper Mario: A Porta Milenar · ttyd (GameCube)

Repositório: https://github.com/doldecomp/ttyd · Espelho: https://github.com/alves-r/mirror-doldecomp-ttyd

Decompilação em andamento do Paper Mario: The Thousand-Year Door. Não gera nada jogável: o build recria o executável do jogo para conferir se bate com o original.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | A imagem de disco da versão `G8MJ01` em `orig/G8MJ01/`. Formatos aceitos: ISO (GCM), RVZ, WIA, WBFS, CISO, NFS, GCZ e TGC. ⚠️ Você indicou que não consegue dumpar GameCube. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o jogo original roda no Dolphin com a sua cópia (sugestão).

O README ainda manda clonar o endereço antigo do projeto (`NWPlayer123/G8MJ01-dtk`). Os passos abaixo usam o repositório atual.

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed git python ninja`
2. Clone: `git clone https://github.com/doldecomp/ttyd.git && cd ttyd`
3. Copie a imagem do disco para `orig/G8MJ01/`. Depois do primeiro build, ela pode ser apagada.
4. Configure com `python configure.py` e compile com `ninja`.

## Windows

1. Instale o Python (python.org, marcando **Add python.exe to PATH**), o ninja (`pip install ninja`) e o Git for Windows.
2. Clone o repositório e copie a imagem para `orig\G8MJ01\`.
3. Rode `python configure.py` e depois `ninja`.

## Fontes

- [README › Dependencies e Building](https://github.com/doldecomp/ttyd#readme)

<!-- verificado: 2026-10-15 -->
