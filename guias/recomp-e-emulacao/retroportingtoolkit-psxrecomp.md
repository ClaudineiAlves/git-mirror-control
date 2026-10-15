# PlayStation · PSXRecomp (PS1)

Repositório: https://github.com/RetroPortingToolKit/psxrecomp · Espelho: https://github.com/alves-r/mirror-retroportingtoolkit-psxrecomp

Ecossistema de recompilação estática de jogos de PS1. Traduz o código MIPS do jogo para C e o liga a um runtime que modela o hardware do console. Os ports prontos ficam em repositórios próprios.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim, só Windows: a CLI (pré-release v0.3.3-alpha, de 03/09/2026: `psxrecomp-cli-windows-x86_64.zip`). Há também pacotes noturnos do código-fonte. |
| Precisa de emulador | Não |
| Você precisa fornecer | O disco do jogo (`.cue`/`.bin`, `.iso` ou `.chd`). A BIOS é opcional, porque o OpenBIOS livre vem embutido; uma BIOS original `SCPH1001.BIN` também é aceita. ⚠️ Você indicou que não consegue dumpar PS1. |
| Arch Linux | Nativo (pelo código-fonte) |
| Windows | Nativo |
| Estado | Alpha. Ports publicados: Tomba! e Tomba! 2, Ape Escape, Mega Man X4, X5 e X6, entre outros, e o [Resident Evil 3](../resident-evil/alexbeavs-ps1-ports-resident-evil-3-recomp.md). |
| Dificuldade | Difícil (toolchain manual) |

O projeto gerado ainda precisa de trabalho específico do jogo para virar um port jogável.

## Arch Linux

O README pede Git, Python 3, CMake 3.20+, Ninja e um compilador C/C++. O SDL3 é baixado sozinho se não houver no sistema.

1. Instale (sugestão, a partir da lista do Debian): `sudo pacman -S --needed git base-devel cmake ninja python`
2. Clone o branch `master` com submódulos, numa pasta separada dos seus projetos de jogo:
   ```bash
   git clone --recursive https://github.com/RetroPortingToolKit/psxrecomp.git
   ```
3. Gere o projeto de um jogo:
   ```bash
   sh psxrecomp/tools/new_project_layout/setup_project.sh --disc ~/dumps/jogo.cue --bios ~/bios/SCPH1001.BIN --dir ~/src
   ```
   Para jogos de vários discos, depois registre os outros com `tools/new_project_layout/update_disc_set.py`.
4. Compile com o `build.sh` do projeto gerado.

O README também oferece um pacote de toolchain pronto: `tools/fetch_toolchain.sh --artifact linux-x64`.

## Windows

1. Instale o Git e o Python: `winget install Git.Git Python.Python.3.12`
2. Escolha o compilador:
   - **toolchain pronto (recomendado):**
     1. Baixe o `cmake-clang-v1-windows-x64.zip` em https://github.com/RetroPortingToolKit/RetroPorting-Toolchains/releases e extraia, ex.: em `C:\retcomm-toolchain`.
     2. No PowerShell, rode `$env:PSXRECOMP_TOOLCHAIN_DIR = "C:\retcomm-toolchain"` e `$env:Path = "C:\retcomm-toolchain\bin;$env:Path"`.
   - **ou o Visual Studio:**
     1. Instale o Build Tools 2022 com **Desktop development with C++**.
     2. Instale o CMake e o Ninja: `winget install Kitware.CMake Ninja-build.Ninja`.
     3. Use o "Developer PowerShell for VS 2022".
3. Clone o repositório como no passo 2 da seção Arch Linux e gere o projeto:
   ```powershell
   powershell -File tools\new_project_layout\setup_project.ps1 -Disc C:\dumps\jogo.cue -Bios C:\BIOS\SCPH1001.BIN -Dir C:\src
   ```
4. Compile com o `build.ps1` do projeto gerado.

## Controles e configurações

- **BIOS:** o OpenBIOS roda por padrão. Para usar a BIOS original, escolha o seu `SCPH1001.BIN` nas configurações. Ela precisa ser exatamente a imagem esperada pelo build.
- **Saves:** os cartões de memória funcionam com as duas BIOS. Os save states não: os de uma BIOS não carregam na outra.
- **Mods:** são pacotes `.psxmod` versionados, não discos modificados.

## Fontes

- [README › Games, What It Is, Build requirements, Getting Started e Which PlayStation BIOS does it use?](https://github.com/RetroPortingToolKit/psxrecomp#readme)
- [docs/BUILDING.md](https://github.com/RetroPortingToolKit/psxrecomp/blob/master/docs/BUILDING.md)
- [docs/GAME_PROJECT_SETUP.md](https://github.com/RetroPortingToolKit/psxrecomp/blob/master/docs/GAME_PROJECT_SETUP.md)

<!-- verificado: 2026-10-15 -->
