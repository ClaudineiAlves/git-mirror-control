# Pokémon Ruby e Sapphire · pokeruby (GBA)

Repositório: https://github.com/pret/pokeruby · Espelho: https://github.com/alves-r/mirror-pret-pokeruby

Desmontagem completa do Pokémon Ruby e Sapphire. Ela monta as ROMs só com o código e os recursos do repositório. Para jogar, a ROM roda num emulador de GBA.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `pokeruby.gba` e `pokesapphire.gba`, além das revisões 1.1 e 1.2 e das versões alemãs) |
| Precisa de emulador | Sim: mGBA no Linux (oficial `mgba-qt`) e no Windows (sugestão) |
| Você precisa fornecer | Nada além das ferramentas: o build não pede ROM base. Você indicou que não consegue dumpar GBA, mas aqui isso não faz falta. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Ativo. `make (alvo) COMPARE=1` confere se a ROM bate com a original. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O INSTALL.md pede as ferramentas de build, o `git`, a `libpng` e o devkitARM (pacote `gba-dev` do pacman do devkitPro).

1. Instale o básico: `sudo pacman -S --needed base-devel git libpng`
2. Configure o pacman do devkitPro (https://devkitpro.org/wiki/devkitPro_pacman) e instale o `gba-dev`.
3. Defina as variáveis do devkitARM:
   ```bash
   export DEVKITPRO=/opt/devkitpro
   echo "export DEVKITPRO=$DEVKITPRO" >> ~/.bashrc
   export DEVKITARM=$DEVKITPRO/devkitARM
   echo "export DEVKITARM=$DEVKITARM" >> ~/.bashrc
   ```
4. Clone o projeto e o compilador `agbcc`, e instale o agbcc no projeto:
   ```bash
   git clone https://github.com/pret/pokeruby
   git clone https://github.com/pret/agbcc
   cd agbcc && ./build.sh && ./install.sh ../pokeruby
   cd ../pokeruby
   ```
5. Compile:
   - `make ruby -j$(nproc)` gera o Ruby;
   - `make sapphire` gera o Sapphire;
   - para as revisões, use alvos como `make ruby_rev2` (Ruby 1.2);
   - para as versões alemãs, rode antes `make clean && sh de_before.sh` e depois `make ruby_de` ou `make sapphire_de`. Para voltar ao inglês, rode `make clean && sh de_after.sh`. Esse passo é obrigatório.
6. Abra a ROM num emulador (sugestão: `sudo pacman -S mgba-qt`).

O INSTALL.md também aceita outro toolchain ARM: `make TOOLCHAIN="/caminho/do/toolchain"`, com uma subpasta `bin`.

## Windows

O INSTALL.md indica o WSL 2 no Windows 10 (build 18917 ou mais novo):

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu: `sudo apt update && sudo apt install build-essential git libpng-dev`
3. Instale o devkitARM (https://devkitpro.org/wiki/Getting_Started) e defina `DEVKITPRO` e `DEVKITARM` como no passo 3 da seção Arch Linux.
4. Siga os passos 4 e 5 da seção Arch Linux.
5. Abra a ROM gerada no mGBA para Windows (sugestão).

Em versões antigas do Windows, sem o subsistema Linux, o INSTALL.md usa o MSYS2 com o instalador gráfico do devkitPro.

## Fontes

- [README](https://github.com/pret/pokeruby#readme)
- [INSTALL.md](https://github.com/pret/pokeruby/blob/master/INSTALL.md)

<!-- verificado: 2026-10-15 -->
