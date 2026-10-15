# The Legend of Zelda: Majora's Mask · mm (N64)

Repositório: https://github.com/zeldaret/mm · Espelho: https://github.com/alves-r/mirror-zeldaret-mm

Decompilação do Majora's Mask (EUA 1.0) que reconstrói a ROM original. Para jogar, a ROM gerada roda num emulador de N64.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `build/n64-us/mm-n64-us.z64` e uma versão comprimida) |
| Precisa de emulador | Sim. No Linux: RMG (AUR `rmg`) ou mupen64plus (oficial). No Windows: RMG ou simple64. (Sugestão.) |
| Você precisa fornecer | A ROM dos EUA em `baseroms/n64-us/`, com o nome `baserom.z64` (ou `.n64`/`.v64`). ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Ativo; só a versão EUA 1.0 é suportada. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. Instale as dependências (conversão sugerida dos nomes do Ubuntu): `sudo pacman -S --needed git base-devel curl python python-pip libpng libxml2`
2. Instale o binutils de MIPS, que o README pede como `binutils-mips-linux-gnu`: `yay -S mips-linux-gnu-binutils`
3. Clone: `git clone https://github.com/zeldaret/mm.git && cd mm`
4. Copie a ROM dos EUA para `baseroms/n64-us/baserom.z64`.
5. Na primeira vez, rode `make init -j$(nproc)`. Ele cria o ambiente Python, extrai e desmonta a ROM e compila tudo. Depois disso, basta `make -j$(nproc)`.
6. As mensagens `build/n64-us/mm-n64-us.z64: OK` e `build/n64-us/mm-n64-us-compressed.z64: OK` indicam sucesso.
7. Abra a ROM gerada num emulador de N64 (sugestão: `yay -S rmg`).

## Windows

O README manda usar o WSL, com Debian ou Ubuntu:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu:
   ```bash
   sudo apt update
   sudo apt install git build-essential binutils-mips-linux-gnu curl python3 python3-pip python3-venv libpng-dev libxml2-dev
   ```
3. Siga os passos 3 a 6 da seção Arch Linux.
4. Abra a ROM gerada num emulador de N64 do Windows, como RMG ou simple64 (sugestão).

O repositório também documenta build com Docker (`docs/BUILDING_DOCKER.md`).

## Fontes

- [README › Installation, Linux (passos 1 a 4)](https://github.com/zeldaret/mm#readme)
- [docs/BUILDING_DOCKER.md](https://github.com/zeldaret/mm/blob/main/docs/BUILDING_DOCKER.md)

<!-- verificado: 2026-10-15 -->
