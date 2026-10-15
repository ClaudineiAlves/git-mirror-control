# Super Mario 64 · sm64 (N64)

Repositório: https://github.com/n64decomp/sm64 · Espelho: https://github.com/alves-r/mirror-n64decomp-sm64

Decompilação completa do Super Mario 64 que reconstrói a ROM original (versões Japão, EUA, Europa, Shindou e iQue). Para jogar, a ROM gerada roda num emulador de N64.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera a ROM `.z64` na pasta `build/`) |
| Precisa de emulador | Sim. No Linux: RMG (AUR `rmg`) ou mupen64plus (oficial). No Windows: RMG ou simple64. (Sugestão.) |
| Você precisa fornecer | Uma ROM do Super Mario 64 com o nome `baserom.<versão>.z64` na pasta do projeto, onde a versão é `jp`, `us`, `eu`, `sh` ou `cn`. Ela serve para extrair os assets. ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Decompilação completa; a nomeação e a documentação do código seguem em andamento. Último push em 04/02/2024. |
| Dificuldade | Média (compilar com script) |

As ROMs geradas batem com estes SHA-1: `jp` `8a20a5c83d6ceb0f0506cfc9fa20d8f438cafe51`, `us` `9bef1128717f958171a4afac3ed78ee2bb4e86ce`, `eu` `4ac5721683d0e0b6bbb561b58a71740845dceea9`, `sh` `3f319ae697533a255a1003d09202379d78d5a2e0` e `cn` `2e1db2780985a1f068077dc0444b685f39cd90ec`.

## Arch Linux

O README tem uma seção própria para o Arch.

1. Instale as dependências: `sudo pacman -S --needed base-devel python git`
2. Instale o binutils de MIPS do AUR: `yay -S mips64-elf-binutils`
3. Clone: `git clone https://github.com/n64decomp/sm64.git && cd sm64`. O caminho completo do repositório não pode passar de 255 caracteres.
4. Copie a sua ROM para a pasta do projeto, com o nome certo (ex.: `baserom.us.z64`).
5. Compile: `make VERSION=us -j4`. Sem `VERSION`, o padrão é `us`. A ROM fica na pasta `build/`.
6. Instale um emulador de N64 (sugestão): `yay -S rmg`, ou `sudo pacman -S mupen64plus`
7. Abra no emulador o arquivo `.z64` gerado em `build/`.

Opções úteis do `make`:
- `COMPARE=0`: não confere o hash da ROM.
- `NON_MATCHING=1`: usa versões em C equivalentes nos trechos que ainda não batem.

## Windows

O README manda usar o WSL, de preferência com Debian ou Ubuntu.

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, instale as dependências: `sudo apt install -y binutils-mips-linux-gnu build-essential git pkgconf python3`
3. Clone dentro do Linux: `git clone https://github.com/n64decomp/sm64.git && cd sm64`
4. Copie a ROM para a pasta. O Explorador de Arquivos acessa o Linux em `\\wsl$\Ubuntu\home\<usuário>\sm64`.
5. Compile: `make VERSION=us -j4`
6. Abra o `.z64` gerado em `build/` num emulador de N64 do Windows, como RMG ou simple64 (sugestão).

## Fontes

- [README › Quick Start, Linux (Arch Linux), Windows e Step 3: Build the ROM](https://github.com/n64decomp/sm64#readme)

<!-- verificado: 2026-10-15 -->
