# N64: Recompiled · N64Recomp (N64)

Repositório: https://github.com/N64Recomp/N64Recomp · Espelho: https://github.com/alves-r/mirror-n64recomp-n64recomp

Ferramenta que recompila estaticamente binários de N64 em código C, que depois pode ser compilado para qualquer plataforma. É a base de ports como o [Zelda 64: Recompiled](../zelda/zelda64recomp-zelda64recomp.md).

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Não para o recompilador, que precisa ser compilado. Só a ferramenta de mods tem binário (`RecompModTool` e `RecompModTool.exe`, de 04/05/2025). |
| Precisa de emulador | Não |
| Você precisa fornecer | O ELF do jogo, que hoje só se obtém montando uma desmontagem ou decompilação dele, além da ROM de N64. ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo (compilando) |
| Windows | Nativo (compilando) |
| Estado | Usado em vários ports. Ainda não recompila overlays de RSP. |
| Dificuldade | Difícil (toolchain manual) |

É uma ferramenta para quem cria ports, não para jogar direto. Para jogar, use um port pronto feito com ela, como o Zelda 64: Recompiled.

## Arch Linux

O README pede CMake 3.20+ e um compilador com C++20.

1. Instale o básico (sugestão): `sudo pacman -S --needed git cmake base-devel`
2. Clone com submódulos e compile:
   ```bash
   git clone --recurse-submodules https://github.com/N64Recomp/N64Recomp.git && cd N64Recomp
   cmake -S . -B build
   cmake --build build
   ```
3. Use: `./N64Recomp <config.toml>`. O TOML define:
   - os caminhos de entrada (o ELF) e de saída;
   - as funções a substituir por stubs ou a pular;
   - patches de instruções isoladas.

O modo "single file output" gera todas as funções num arquivo só, útil para patches. O RSPRecomp, no mesmo repositório, recompila microcódigo de RSP.

## Windows

1. Instale o Visual Studio com C++ e CMake, ou o CMake com outro compilador C++20.
2. Siga os passos 2 e 3 da seção Arch Linux.

## Fontes

- [README › How it Works, How to Use, Single File Output Mode, RSP Microcode Support e Building](https://github.com/N64Recomp/N64Recomp#readme)
- [Releases (mod-tool-release)](https://github.com/N64Recomp/N64Recomp/releases)

<!-- verificado: 2026-10-15 -->
