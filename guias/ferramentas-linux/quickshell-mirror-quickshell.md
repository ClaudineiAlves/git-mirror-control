# Quickshell · quickshell (Linux)

Repositório: https://github.com/quickshell-mirror/quickshell · Espelho: https://github.com/alves-r/mirror-quickshell-mirror-quickshell

Kit para criar shells de desktop com QtQuick, para Wayland e X11. É a base do [Caelestia Shell](caelestia-dots-shell.md). O repositório no GitHub é um espelho; o principal fica em https://git.outfoxxed.me/quickshell/quickshell.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim, pelos repositórios oficiais do Arch (`quickshell`) ou pelo AUR (`quickshell-git`). As tags do GitHub (v0.3.2, de 08/10/2026) não têm arquivos. |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Não suportado (é um kit para shells de desktop Linux) |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

O README remete ao site (https://quickshell.outfoxxed.me) para a instalação. O `BUILD.md` traz as instruções de compilação.

## Arch Linux

1. Instale (sugestão): `sudo pacman -S quickshell`, ou, pelo AUR, `yay -S quickshell-git`. O Caelestia Shell exige a versão git.
2. O `BUILD.md` avisa: o Quickshell usa APIs privadas do Qt e **precisa ser recompilado a cada versão nova do Qt**, ou vai fechar por incompatibilidade de ABI. Depois de atualizar o `qt6-base`, recompile o `quickshell-git`.

**Compilar a partir do código** (`BUILD.md`):
1. Dependências básicas: `cmake`, `qt6-base`, `qt6-declarative`, `libdrm` e `cli11`, mais `qt6-shadertools`, `spirv-tools` e `pkgconf` para compilar. Os recursos opcionais, como Wayland, X11, PipeWire e bandeja do sistema, têm dependências próprias, listadas no documento.
2. Compile com CMake e Ninja, como o documento descreve.

## Windows

Não suportado: o Quickshell cria shells de desktop para Wayland e X11 no Linux. O WSL2 (`wsl --install -d Ubuntu`) não serve para isso.

## Fontes

- [README](https://github.com/quickshell-mirror/quickshell#readme)
- [BUILD.md](https://github.com/quickshell-mirror/quickshell/blob/master/BUILD.md)

<!-- verificado: 2026-10-15 -->
