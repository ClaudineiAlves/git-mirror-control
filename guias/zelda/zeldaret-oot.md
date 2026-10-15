# The Legend of Zelda: Ocarina of Time · oot (N64)

Repositório: https://github.com/zeldaret/oot · Espelho: https://github.com/alves-r/mirror-zeldaret-oot

Decompilação do Ocarina of Time que reconstrói a ROM original de várias versões (N64, GameCube e iQue). Para jogar, a ROM gerada roda num emulador de N64.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `build/<versão>/oot-<versão>.z64`) |
| Precisa de emulador | Sim. No Linux: RMG (AUR `rmg`) ou mupen64plus (oficial). No Windows: RMG ou simple64. (Sugestão.) |
| Você precisa fornecer | A ROM de uma versão suportada, em `baseroms/<versão>/baserom.z64` (ou `.n64`/`.v64`). Exemplos (MD5): `ntsc-1.0` `9f04c8e68534b870f707c247fa4b50fc`, `ntsc-1.2` `2258052847bdd056c8406a9ef6427f13` e `pal-1.0` `e040de91a74b61e3201db0e2323f768a`. Há também versões de GameCube e iQue; a tabela completa está no README. ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Ativo. Sem `VERSION`, o build usa a `gc-eu-mq-dbg`. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O README pede Python 3.10+, ferramentas de build, libxml2 e um binutils de MIPS (qualquer um entre `mips64-elf-`, `mips-linux-gnu-` e `mips64-linux-gnu-`, detectado sozinho).

1. Instale as dependências (conversão sugerida dos nomes do Ubuntu): `sudo pacman -S --needed git base-devel curl python python-pip libxml2`
2. Instale um binutils de MIPS do AUR: `yay -S mips64-elf-binutils`
3. Clone: `git clone https://github.com/zeldaret/oot.git && cd oot`
4. Copie a sua ROM para a pasta da versão, ex.: `baseroms/ntsc-1.0/baserom.z64`.
5. Prepare e extraia os assets: `make setup VERSION=ntsc-1.0`. Isso cria `baseroms/ntsc-1.0/baserom-decompressed.z64`.
6. Compile: `make VERSION=ntsc-1.0 -j$(nproc)`. A mensagem `build/ntsc-1.0/oot-ntsc-1.0.z64: OK` indica que a ROM bate com a original. O caminho do projeto não pode ser longo demais.
7. Abra `build/ntsc-1.0/oot-ntsc-1.0.z64` num emulador de N64 (sugestão: `yay -S rmg`).

O repositório também traz instruções com Docker (`docs/BUILDING_DOCKER.md`).

## Windows

O README recomenda o WSL com Ubuntu:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, instale as dependências:
   ```bash
   sudo apt-get update
   sudo apt-get install git build-essential curl python3 python3-pip python3-venv libxml2-dev binutils-mips-linux-gnu
   ```
3. Siga os passos 3 a 6 da seção Arch Linux. Para abrir a pasta atual no Explorador do Windows, use `explorer.exe .`.
4. Abra a ROM gerada num emulador de N64 do Windows, como RMG ou simple64 (sugestão).

## Fontes

- [README › Installation, Linux (passos 1 a 5) e Changing build options](https://github.com/zeldaret/oot#readme)
- [docs/BUILDING_DOCKER.md](https://github.com/zeldaret/oot/blob/main/docs/BUILDING_DOCKER.md)

<!-- verificado: 2026-10-15 -->
