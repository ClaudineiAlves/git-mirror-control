# Pokémon FireRed e LeafGreen · pokefirered (GBA)

Repositório: https://github.com/pret/pokefirered · Espelho: https://github.com/alves-r/mirror-pret-pokefirered

Decompilação completa do Pokémon FireRed e LeafGreen em inglês. Ela monta as ROMs só com o código e os recursos do repositório. Para jogar, a ROM roda num emulador de GBA.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `pokefirered.gba`, `pokeleafgreen.gba` e as revisões 1.1) |
| Precisa de emulador | Sim: mGBA no Linux (oficial `mgba-qt`) e no Windows (sugestão) |
| Você precisa fornecer | Nada além das ferramentas: o build não pede ROM base. Você indicou que não consegue dumpar GBA, mas aqui isso não faz falta. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Ativo. `make compare` confere se a ROM bate com a original. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O INSTALL.md não tem seção própria para o Arch. Para "outras distribuições", ele manda instalar `gcc`, `g++`, `make`, `git` e `libpng` e depois o pacote `gba-dev` do pacman do devkitPro (https://devkitpro.org/wiki/devkitPro_pacman).

Um caminho mais curto (sugestão): usar os mesmos pacotes que o pokeemerald, do mesmo grupo, indica para o Arch. No Debian, o próprio INSTALL.md do FireRed também dispensa o devkitARM.

1. Instale: `sudo pacman -S --needed base-devel arm-none-eabi-binutils arm-none-eabi-newlib git libpng`
2. Clone o projeto e o compilador `agbcc`, e instale o agbcc no projeto:
   ```bash
   git clone https://github.com/pret/pokefirered
   git clone https://github.com/pret/agbcc
   cd agbcc && ./build.sh && ./install.sh ../pokefirered
   cd ../pokefirered
   ```
3. Compile:
   - `make -j$(nproc)` gera o `pokefirered.gba`;
   - `make leafgreen` gera o LeafGreen;
   - `make firered_rev1` e `make leafgreen_rev1` geram as versões 1.1.
4. Abra a ROM num emulador (sugestão: `sudo pacman -S mgba-qt`).

## Windows

O INSTALL.md recomenda o WSL1. O MSYS2 e o Cygwin também são documentados, mas são mais lentos.

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu --enable-wsl1` e reinicie.
2. De novo como administrador, rode `wsl --set-version Ubuntu 1`.
3. Abra o **Ubuntu**, crie o usuário e instale os pacotes:
   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install build-essential binutils-arm-none-eabi git libpng-dev
   ```
4. Trabalhe numa pasta do Windows que já exista, ex.: `cd /mnt/c/Users/<usuário>/Desktop/decomps`
5. Siga os passos 2 e 3 da seção Arch Linux.
6. Abra a ROM gerada no mGBA para Windows (sugestão).

## Problemas conhecidos

- **Trocou de terminal (ex.: do MSYS2 para o WSL1):** rode `make clean-tools` uma vez antes do próximo `make`.
- **Erro ao compilar o agbcc:** apague a pasta `agbcc` e instale de novo.

## Fontes

- [README](https://github.com/pret/pokefirered#readme)
- [INSTALL.md](https://github.com/pret/pokefirered/blob/master/INSTALL.md)
- [INSTALL.md do pokeemerald, seção Arch Linux](https://github.com/pret/pokeemerald/blob/master/INSTALL.md)

<!-- verificado: 2026-10-15 -->
