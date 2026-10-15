# Resident Evil 4 · re4 (GameCube, protótipo de debug)

Repositório: https://github.com/adonis-singh/re4 · Espelho: https://github.com/alves-r/mirror-adonis-singh-re4

Decompilação completa do build de debug `G4BE08` do Resident Evil 4 de GameCube, um protótipo de 25/11/2004 em dois discos. O build devolve os arquivos originais idênticos, byte a byte.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado são os mesmos arquivos do disco original) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | As imagens dos dois discos do protótipo de debug `G4BE08` (`re4_debug_disc1.iso` e `re4_debug_disc2.gcm`) e o código-fonte GPL do compilador SN GCC (`NGC_GNU_SRC`). ⚠️ Você indicou que não consegue dumpar GameCube. |
| Arch Linux | Nativo |
| Windows | Via WSL2 (não documentado: o README pede Linux) |
| Estado | Completo: `main.dol` e as 114 RELs saem idênticos aos originais. |
| Dificuldade | Difícil (toolchain manual) |

Serve para estudar e preservar o código, não para jogar. **Como jogar o jogo, como alternativa:** o RE4 de GameCube roda no Dolphin com a sua cópia (sugestão). A versão "UHD" de PC, da Steam, tem o mod [re4_tweaks](nipkownix-re4_tweaks.md).

## Arch Linux

O README pede Linux, Python 3 e ninja. Na primeira configuração, o projeto baixa sozinho o decomp-toolkit, o objdiff, o wibo e os compiladores CodeWarrior.

1. Instale: `sudo pacman -S --needed git python ninja`
2. Clone: `git clone https://github.com/adonis-singh/re4 && cd re4`
3. Compile o SN GCC uma vez, a partir do código-fonte GPL da SN Systems: `SN_GCC_SRC=/caminho/para/NGC_GNU_SRC/NGC tools/sn-gcc/build.sh`
4. Copie as imagens dos discos: `cp re4_debug_disc1.iso re4_debug_disc2.gcm orig/G4BE08/`
5. Compile: `python3 configure.py && ninja`. O relatório final deve mostrar 100% igual e ligado.
6. Confira: `build/tools/dtk shasum -c config/G4BE08/build.sha1` deve mostrar 115 linhas `OK`.

## Windows

Não documentado no repositório: o README pede Linux. O caminho natural é o WSL2 (sugestão):

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu: `sudo apt update && sudo apt install git python3 ninja-build`
3. Siga os passos 2 a 6 da seção Arch Linux.

## Fontes

- [README › Building e How close is the match](https://github.com/adonis-singh/re4#readme)

<!-- verificado: 2026-10-15 -->
