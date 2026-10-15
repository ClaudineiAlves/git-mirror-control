# Super Mario Sunshine · sms (GameCube)

Repositório: https://github.com/doldecomp/sms · Espelho: https://github.com/alves-r/mirror-doldecomp-sms

Decompilação em andamento do Super Mario Sunshine. Não gera nada jogável: o build recria o executável do jogo para conferir se bate com o original.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | A imagem de disco de uma versão suportada, `GMSJ01` (Japão, Rev 0) ou `GMSP01` (PAL, Rev 0), em `orig/<ID>/`. Formatos aceitos: ISO (GCM), RVZ, WIA, WBFS, CISO, NFS, GCZ e TGC. ⚠️ Você indicou que não consegue dumpar GameCube. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o Super Mario Sunshine original roda no Dolphin com a sua cópia (sugestão).

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed git python ninja`. No Linux, o `wibo` é baixado sozinho.
2. Clone: `git clone https://github.com/doldecomp/sms.git && cd sms`
3. Copie a imagem do disco para `orig/GMSJ01/` (ou `orig/GMSP01/`). Depois do primeiro build, a imagem pode ser apagada.
4. Configure: `python configure.py`. Para a versão PAL, use `python configure.py --version GMSP01`.
5. Compile: `ninja`

## Windows

O README recomenda as ferramentas nativas do Windows, sem WSL nem MSYS2.

1. Instale o Python (python.org) e marque **Add python.exe to PATH**.
2. Instale o ninja: `pip install ninja`
3. Instale o Git for Windows.
4. Clone o repositório e copie a imagem do disco para `orig\GMSJ01\`.
5. Rode `python configure.py` e depois `ninja`.

## Fontes

- [README › Supported versions, Dependencies e Building](https://github.com/doldecomp/sms#readme)

<!-- verificado: 2026-10-15 -->
