# Silent Hill · silent-hill-decomp (PS1)

Repositório: https://github.com/shdecompilations/silent-hill-decomp · Espelho: https://github.com/alves-r/mirror-shdecompilations-silent-hill-decomp

Decompilação em andamento do Silent Hill de PS1 (versão americana 1.1). O build recria o executável e os overlays do jogo idênticos aos originais. O README deixa claro que o projeto **não é e não será** um port.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: DuckStation no Linux (AUR `duckstation`) e no Windows (sugestão) |
| Você precisa fornecer | O dump da versão NTSC-U 1.1 em `.bin` (SHA-1 `34278D31D9B9B12B3B5DB5E45BCBE548991ECBC7`, 616.494.480 bytes), salvo em `rom/image/SLUS-00707.bin`. ⚠️ Você indicou que não consegue dumpar PS1. |
| Arch Linux | Via distrobox com Ubuntu (o toolchain MIPS não está completo no Arch) |
| Windows | Via WSL2 (só para compilar) |
| Estado | Em andamento. O build ainda não é "deslocável", e trocar arquivos não está implementado. O build nativo no Windows compila, mas não bate com o original. |
| Dificuldade | Média (compilar com script) |

Serve para estudar o código, não para jogar. **Como jogar o jogo, como alternativa:** o Silent Hill original roda no DuckStation com a sua cópia (sugestão), e o [Silent Hill PC Port](slickamogus-silent-hill-decomp.md), feito a partir deste decomp, roda nativo.

## Arch Linux

A wiki do projeto pede os pacotes do Debian `binutils-mips-linux-gnu` e `cpp-mips-linux-gnu`. O primeiro existe no AUR (`mips-linux-gnu-binutils`), mas o segundo não tem equivalente no Arch nem no AUR. Sugestão: rodar o caminho do Ubuntu num container com distrobox.

1. Instale o distrobox (sugestão): `sudo pacman -S --needed distrobox podman`
2. Crie e entre num Ubuntu: `distrobox create --name shdecomp --image ubuntu:24.04 && distrobox enter shdecomp`
3. Dentro do container, instale o que a wiki pede:
   ```bash
   sudo apt update && sudo apt install git build-essential binutils-mips-linux-gnu cpp-mips-linux-gnu python3 python3-venv bchunk p7zip-full
   ```
4. Clone com submódulos: `git clone --recursive https://github.com/shdecompilations/silent-hill-decomp.git && cd silent-hill-decomp`
5. Copie o seu dump para `rom/image/SLUS-00707.bin`.
6. Crie o ambiente Python:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   python3 -m pip install -r requirements.txt
   ```
7. Extraia o necessário do disco com `make setup` e compile com `make`. No fim, a pasta `build` aparece e o checksum é conferido.

Para outras versões (PAL e japonesas), use `GAME_VERSION`, ex.: `make GAME_VERSION=EUR`. O foco do projeto é a versão americana 1.1.

## Windows

A wiki recomenda o Makefile no WSL2 com Debian ou Ubuntu:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, siga os passos 3 a 7 da seção Arch Linux.

Também há um caminho nativo com Ninja, que só precisa do Python e do Git. Ele é menos mantido e, no Windows, ainda não gera um binário idêntico ao original:

1. Rode `python -m ensurepip` e depois crie e ative o ambiente:
   ```bat
   python -m venv .venv
   .venv\Scripts\activate.bat
   python -m pip install -r requirements.txt
   ```
2. Rode `python ninja_config.py -iso_e`, depois `python ninja_config.py` e por fim `ninja`.
3. Se houver erro de leitura de texto, use `python -X utf8 ninja_config.py`.

## Fontes

- [README › Progress e avisos](https://github.com/shdecompilations/silent-hill-decomp#readme)
- [Wiki › Setup](https://github.com/shdecompilations/silent-hill-decomp/wiki/Setup)

<!-- verificado: 2026-10-15 -->
