# Pokémon Diamond e Pearl · pokediamond (DS)

Repositório: https://github.com/pret/pokediamond · Espelho: https://github.com/alves-r/mirror-pret-pokediamond

Decompilação em andamento do Pokémon Diamond e Pearl, que monta as ROMs dos EUA. Para jogar, a ROM roda num emulador de DS. O build depende de um compilador e de um SDK proprietários, que o projeto não distribui.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `build/diamond.us/pokediamond.us.nds` e `build/pearl.us/pokepearl.us.nds`) |
| Precisa de emulador | Sim. No Linux: melonDS (AUR `melonds`) ou DeSmuME (oficial `desmume`). No Windows: melonDS. (Sugestão.) |
| Você precisa fornecer | Os compiladores Metrowerks (MWCC 2.0/sp1 e 1.2/sp2p3) e o Nitro SDK 3.2, que são proprietários. O projeto não os distribui, e o INSTALL.md explica onde a comunidade os disponibiliza. O INSTALL.md não pede ROM base; você indicou que não consegue dumpar DS, mas aqui isso não faz falta. |
| Arch Linux | Nativo (com Wine para rodar o compilador) |
| Windows | Via MSYS2, Cygwin ou WSL1 (só para compilar) |
| Estado | Em andamento. No futuro haverá uma opção com GCC, sem o MWCC, mas ela não vai gerar uma ROM idêntica. |
| Dificuldade | Difícil (toolchain manual) |

## Arch Linux

1. Instale as dependências. O INSTALL.md diz que no Arch basta o `base-devel` no lugar de `build-essential`, `make` e `git`, mais o Wine. Os nomes dos demais pacotes no Arch são sugestão:
   `sudo pacman -S --needed base-devel git arm-none-eabi-binutils wine python libpng pkgconf pugixml`
2. Clone: `git clone https://github.com/pret/pokediamond && cd pokediamond`
3. Coloque os compiladores MWCC conforme o INSTALL.md. Depois copie o conteúdo de `tools/bin` do Nitro SDK para `tools/bin` do projeto.
4. Compile: `make` gera o Diamond, e `make pearl` gera o Pearl. Não é preciso limpar entre um e outro.
5. Abra a ROM num emulador de DS (sugestão: `yay -S melonds`).

Se o build falhar, o INSTALL.md oferece um script com Docker: `make clean` e depois `./contrib/docker/build_docker.sh` (ou `./contrib/docker/build_docker.sh pearl`).

## Windows

1. Instale o devkitARM e defina as variáveis no `~/.bashrc`. No MSYS2:
   ```bash
   export DEVKITPRO=C:/devkitPro
   export DEVKITARM=${DEVKITPRO}/devkitARM
   ```
   No Cygwin, use `DEVKITPRO=/cygdrive/c/devkitPro`.
2. Instale `make`, `git`, `build-essentials`, `libpng-devel`, `pkg-config` e `pugixml` pelo gerenciador do Cygwin ou pelo `pacman` do MSYS2. No MSYS2, a `libpng` precisa ser compilada a partir do código-fonte.
3. Siga os passos 2 a 4 da seção Arch Linux.
4. Abra a ROM gerada no melonDS (sugestão).

O WSL2 tem um problema com o `mwldarm`, que não acha o próprio executável. Se for usar o WSL, use o WSL1.

## Problemas conhecidos

- **Erro ao salvar as configurações ao indicar o arquivo de licença (Windows):** crie a variável de ambiente de sistema `LM_LICENSE_FILE` apontando para o `license.dat`.

## Fontes

- [README](https://github.com/pret/pokediamond#readme)
- [INSTALL.md](https://github.com/pret/pokediamond/blob/master/INSTALL.md)

<!-- verificado: 2026-10-15 -->
