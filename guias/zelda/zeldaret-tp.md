# The Legend of Zelda: Twilight Princess · tp (GameCube/Wii)

Repositório: https://github.com/zeldaret/tp · Espelho: https://github.com/alves-r/mirror-zeldaret-tp

Decompilação do Twilight Princess. O código das versões de GameCube já bate por completo. O README deixa claro que o projeto **não é e não será** um port: ele recompila um binário idêntico ao original.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | A imagem de disco em `orig/<ID>/`. Versões de GameCube: `GZ2E01` (EUA, padrão), `GZ2P01` (Europa) e `GZ2J01` (Japão). Também há versões de Wii e do Nvidia Shield chinês. ⚠️ Você indicou que não consegue dumpar GameCube nem Wii. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | O código das versões de GameCube bate por completo, mas nem todas as unidades estão ligadas. As versões de Debug e Wii seguem em andamento. |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o Twilight Princess original roda no Dolphin com a sua cópia (sugestão). Há também um port nativo para PC de outro projeto, o Dusk (duskport.com), que usa a sua ISO. Ele é citado no README do gow2-recomp.

## Arch Linux

1. Instale as ferramentas. O `clang-format` é opcional: `sudo pacman -S --needed git python ninja`
2. Clone: `git clone https://github.com/zeldaret/tp.git && cd tp`
3. Copie a imagem do disco para `orig/GZ2E01/`. Depois do primeiro build, ela pode ser apagada.
4. Configure: `python configure.py`. Para outra versão, use `--version`.
5. Compile: `ninja`

## Windows

O README recomenda as ferramentas nativas do Windows, sem WSL nem MSYS2.

1. Instale o Python (python.org, marcando **Add python.exe to PATH**), o ninja (`pip install ninja`) e o Git for Windows.
2. Clone o repositório e copie a imagem para `orig\GZ2E01\`.
3. Rode `python configure.py` e depois `ninja`.

## Fontes

- [README › Dependencies e Building](https://github.com/zeldaret/tp#readme)
- [README do gow2-recomp, citando o Dusk](https://github.com/andrebrumdev/gow2-recomp#state-of-the-art-in-game-recompilation)

<!-- verificado: 2026-10-15 -->
