# Pokémon Emerald · pokeemerald (GBA)

Repositório: https://github.com/pret/pokeemerald · Espelho: https://github.com/alves-r/mirror-pret-pokeemerald

Decompilação completa do Pokémon Emerald. Ela monta a ROM só com o código e os recursos do repositório. Para jogar, a ROM roda num emulador de GBA.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `pokeemerald.gba`) |
| Precisa de emulador | Sim: mGBA no Linux (oficial `mgba-qt`) e no Windows (sugestão) |
| Você precisa fornecer | Nada além das ferramentas: o build não pede ROM base. Você indicou que não consegue dumpar GBA, mas aqui isso não faz falta. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Ativo. `make compare` confere se a ROM bate com a original. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. Instale os pacotes que o INSTALL.md indica para o Arch: `sudo pacman -S base-devel arm-none-eabi-binutils arm-none-eabi-newlib git libpng`
2. Numa pasta de trabalho, clone o projeto e o compilador `agbcc`, e instale o agbcc no projeto:
   ```bash
   git clone https://github.com/pret/pokeemerald
   git clone https://github.com/pret/agbcc
   cd agbcc && ./build.sh && ./install.sh ../pokeemerald
   cd ../pokeemerald
   ```
3. Compile: `make -j$(nproc)`. Sai o `pokeemerald.gba`.
4. Opcional: `make compare` mostra `pokeemerald.gba: OK` se a ROM for idêntica à original.
5. Abra a ROM num emulador (sugestão: `sudo pacman -S mgba-qt`).

## Windows

O INSTALL.md recomenda o WSL1, o caminho mais rápido. O MSYS2 e o Cygwin também são documentados, mas são mais lentos.

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu --enable-wsl1` e reinicie.
2. De novo como administrador, rode `wsl --set-version Ubuntu 1`.
3. Abra o **Ubuntu**, crie o usuário e instale os pacotes:
   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install build-essential binutils-arm-none-eabi git libpng-dev
   ```
4. Trabalhe numa pasta do Windows que já exista, ex.: `cd /mnt/c/Users/<usuário>/Desktop/decomps`
5. Siga os passos 2 a 4 da seção Arch Linux.
6. Abra a ROM gerada no mGBA para Windows (sugestão).

Para o build ficar mais rápido, o INSTALL.md sugere uma exceção no Microsoft Defender para a pasta do projeto.

## Problemas conhecidos

- **`fatal: could not set 'core.filemode' to 'false'` no clone (WSL):** rode `sudo umount /mnt/c` e `sudo mount -t drvfs C: /mnt/c -o metadata,noatime`. Depois volte à pasta e clone de novo.
- **Trocou de terminal (ex.: do MSYS2 para o WSL1):** rode `make clean-tools` uma vez antes do próximo `make`.
- **Erro ao compilar o agbcc:** apague a pasta `agbcc` e instale de novo.

## Fontes

- [README](https://github.com/pret/pokeemerald#readme)
- [INSTALL.md](https://github.com/pret/pokeemerald/blob/master/INSTALL.md)

<!-- verificado: 2026-10-15 -->
