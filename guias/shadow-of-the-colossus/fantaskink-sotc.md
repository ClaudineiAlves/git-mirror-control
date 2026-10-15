# Shadow of the Colossus (preview) · SOTC (PS2)

Repositório: https://github.com/Fantaskink/SOTC · Espelho: https://github.com/alves-r/mirror-fantaskink-sotc

Decompilação em andamento da versão **preview** de Shadow of the Colossus para PS2. Não dá para jogar com ela: o build só recompila os executáveis para conferir se batem com o original.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: PCSX2 no Linux e no Windows ([guia](../recomp-e-emulacao/pcsx2-pcsx2.md)) |
| Você precisa fornecer | A ISO da versão preview, da qual saem `SCPS_150.97` (SHA-1 `c4d5576d1cae3721c411a746c7845f5c6f026dbb`) e `KERNEL.XFF`. ⚠️ Você indicou que não consegue dumpar PS2. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Em andamento. O progresso dos módulos `SCPS_150.97` e `KERNEL.XFF` aparece nos selos do README. |
| Dificuldade | Difícil (toolchain manual) |

**Como jogar o jogo, como alternativa:** o Shadow of the Colossus original de PS2 roda no PCSX2 ([guia](../recomp-e-emulacao/pcsx2-pcsx2.md)), e o remake de PS4 tem port nativo para Windows ([guia](ajncsystem-shadowofthecolossus-pc.md)). Os dois exigem a sua cópia.

## Arch Linux

O README só documenta Linux ou WSL2, com nomes de pacote do Ubuntu. A conversão abaixo é sugestão; o compilador cruzado MIPS só existe no AUR.

1. Instale as ferramentas:
   ```bash
   sudo pacman -S --needed git ninja python make
   yay -S mipsel-linux-gnu-gcc mips-linux-gnu-binutils
   ```
2. Clone: `git clone --recursive https://github.com/Fantaskink/SOTC.git && cd SOTC`
3. Crie o ambiente Python e instale as dependências:
   ```bash
   python3 -m venv ./.python3
   source .python3/bin/activate
   python3 -m pip install -U -r requirements.txt
   ```
4. Prepare o compilador: `scripts/setup_compiler.sh`
5. Crie a pasta `iso` na raiz do repositório e coloque nela `SCPS_150.97` e `KERNEL.XFF`, extraídos da sua ISO.
6. Compile: `make` (ou `make loader`, `make kernel` para um módulo só, e `make clean` para limpar).

Se a compilação der problema, o README sugere instalar o `gcc-multilib` (nome do Ubuntu). No Arch, o equivalente é habilitar o repositório multilib e instalar `lib32-gcc-libs` (sugestão).

## Windows

O projeto exige Linux ou WSL2. No Windows, use o WSL2:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, siga o README à risca:
   ```bash
   sudo apt install gcc-mipsel-linux-gnu binutils-mips-linux-gnu ninja-build
   sudo apt install python3-pip python3-venv
   git clone --recursive https://github.com/Fantaskink/SOTC.git && cd SOTC
   python3 -m venv ./.python3
   source .python3/bin/activate
   python3 -m pip install -U -r requirements.txt
   scripts/setup_compiler.sh
   ```
3. Crie a pasta `iso`, coloque `SCPS_150.97` e `KERNEL.XFF` nela e rode `make`.

## Fontes

- [README › Requirements e Setup](https://github.com/Fantaskink/SOTC#readme)

<!-- verificado: 2026-10-15 -->
