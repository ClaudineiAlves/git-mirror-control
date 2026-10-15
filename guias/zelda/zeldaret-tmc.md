# The Legend of Zelda: The Minish Cap · tmc (GBA)

Repositório: https://github.com/zeldaret/tmc · Espelho: https://github.com/alves-r/mirror-zeldaret-tmc

Decompilação em andamento do The Minish Cap, que gera a ROM de GBA a partir da sua cópia. Para jogar, a ROM roda num emulador de GBA.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `tmc.gba`) |
| Precisa de emulador | Sim: mGBA no Linux (oficial `mgba-qt`) e no Windows (sugestão) |
| Você precisa fornecer | A ROM original na raiz do repositório: `baserom.gba` (EUA, padrão, SHA-1 `b4bd50e4131b027c334547b4524e2dbbd4227130`), `baserom_eu.gba` (`cff199b36ff173fb6faf152653d1bccf87c26fb7`) ou `baserom_jp.gba` (`6c5404a1effb17f481f352181d0f1c61a2765c5d`). Também há duas demos. ⚠️ Você indicou que não consegue dumpar GBA. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Em andamento. O README avisa que o código ainda muda muito e que partes da ROM podem não ser "deslocáveis" para mods. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. Instale as dependências (conversão sugerida dos nomes do Ubuntu): `sudo pacman -S --needed git base-devel python python-pip python-pycparser cmake libpng arm-none-eabi-gcc arm-none-eabi-binutils arm-none-eabi-newlib`
2. Clone o projeto e o compilador `agbcc`, e instale as ferramentas:
   ```bash
   git clone https://github.com/zeldaret/tmc
   git clone https://github.com/pret/agbcc
   cd agbcc && sh build.sh && sh install.sh ../tmc
   cd ../tmc && make tools
   ```
3. Coloque a sua ROM na raiz do `tmc`, com o nome da tabela (ex.: `baserom.gba`).
4. Compile: `make -j$(nproc)`. Para outra versão: `make GAME_VERSION=EU`.
5. Abra o `tmc.gba` gerado num emulador de GBA (sugestão: `sudo pacman -S mgba-qt`).

## Windows

O INSTALL.md indica o WSL 2 no Windows 10 (build 18917 ou mais novo):

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, instale os pacotes que o INSTALL.md cita e o pycparser:
   ```bash
   sudo apt install build-essential git python3 python3-pip cmake libpng-dev gcc-arm-none-eabi
   pip3 install pycparser
   ```
   O pacote `gcc-arm-none-eabi` é o nome do Ubuntu para o `arm-none-eabi-gcc` (sugestão). O devkitPro, com o pacote `gba-dev`, também é suportado.
3. Siga os passos 2 a 4 da seção Arch Linux.
4. Abra a ROM no mGBA do Windows (sugestão).

## Fontes

- [README](https://github.com/zeldaret/tmc#readme)
- [INSTALL.md](https://github.com/zeldaret/tmc/blob/master/INSTALL.md)

<!-- verificado: 2026-10-15 -->
