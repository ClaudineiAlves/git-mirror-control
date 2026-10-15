# Pokémon Platinum · pokeplatinum (DS)

Repositório: https://github.com/pret/pokeplatinum · Espelho: https://github.com/alves-r/mirror-pret-pokeplatinum

Decompilação em andamento do Pokémon Platinum dos EUA, que monta a ROM a partir do repositório. Para jogar, a ROM roda num emulador de DS.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `build/pokeplatinum.us.nds`) |
| Precisa de emulador | Sim. No Linux: melonDS (AUR `melonds`) ou DeSmuME (oficial `desmume`). No Windows: melonDS. (Sugestão.) |
| Você precisa fornecer | Nada além das ferramentas: o INSTALL.md não pede ROM base. Você indicou que não consegue dumpar DS, mas aqui isso não faz falta. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Em andamento. Gera a revisão 1 por padrão e a revisão 0, a primeira tiragem americana, com `ROM_REVISION=0`. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. O INSTALL.md manda habilitar o repositório multilib, que está desligado na sua máquina, por causa do `lib32-glibc`. Hoje esse pacote vem do repositório `core`, então o passo pode ser dispensável.
2. Instale as dependências: `sudo pacman -S arm-none-eabi-gcc bison flex gcc git make ninja python wget xz lib32-glibc libpng`
3. Clone: `git clone https://github.com/pret/pokeplatinum && cd pokeplatinum`
4. Compile: `make`. Sai o `build/pokeplatinum.us.nds` (revisão 1).
   - `make rom` pula a conferência de checksum, útil se você for alterar o código.
   - `ROM_REVISION=0 make` gera a revisão 0, que tem um erro na tela do GTS.
5. Abra a ROM num emulador de DS (sugestão: `yay -S melonds`).

## Windows

O INSTALL.md recomenda o WSL2:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. Confira com `wsl -l -v`. Se o Ubuntu não estiver na versão 2, rode `wsl --set-version Ubuntu 2`.
3. Entre com `wsl -d Ubuntu` e vá para a pasta pessoal do Linux: `cd ~`
4. Instale as dependências:
   ```bash
   sudo dpkg --add-architecture i386 && sudo apt update
   sudo apt install bison flex g++ gcc-arm-none-eabi git make ninja-build pkg-config wget python3 xz-utils nasm libc6:i386 libpng-dev
   ```
5. Siga os passos 3 e 4 da seção Arch Linux.
6. Abra a ROM gerada no melonDS (sugestão). O Explorador do Windows acessa os arquivos do Ubuntu pelo caminho `\\wsl$` (sugestão).

O INSTALL.md também documenta o WSL1, o MSYS2 e o macOS.

## Problemas conhecidos

- **O build falha depois de atualizar com o branch principal:** a seção "Troubleshooting FAQ" do INSTALL.md trata desse caso.

## Fontes

- [README](https://github.com/pret/pokeplatinum#readme)
- [INSTALL.md](https://github.com/pret/pokeplatinum/blob/main/INSTALL.md)

<!-- verificado: 2026-10-15 -->
