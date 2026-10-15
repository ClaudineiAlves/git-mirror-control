# Paper Mario · PaperBoat (N64)

Repositório: https://github.com/HarbourMasters/PaperBoat · Espelho: https://github.com/alves-r/mirror-harbourmasters-paperboat

Port de PC do Paper Mario de N64 feito pela HarbourMasters, baseado na decompilação Paper Mario DX, com binário pronto para Windows, Linux e macOS.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (1.0.3, de 11/10/2026: `Paperboat-Mulberry-Delta-Win64.zip`, `Paperboat-Mulberry-Delta-Linux.zip` e Mac) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Paper Mario dos EUA (SHA-1 `3837f44cda784b466c9a2d99df70d77c322b97a0`). ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo; versão 1.0.3 de 11/10/2026 |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Baixe `Paperboat-Mulberry-Delta-Linux.zip` em https://github.com/HarbourMasters/PaperBoat/releases e extraia: `bsdtar -xf Paperboat-Mulberry-Delta-Linux.zip` (sugestão).
2. Coloque a sua ROM na mesma pasta do `paperboat.appimage`.
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x paperboat.appimage && ./paperboat.appimage`

**Compilar, opcional** (`docs/BUILDING.md`):

1. Instale as ferramentas (o documento pede cmake, ninja e um compilador C/C++): `sudo pacman -S --needed cmake ninja gcc git`
2. Clone com os submódulos: `git clone --recurse-submodules https://github.com/HarbourMasters/PaperBoat.git && cd PaperBoat`
3. Configure e compile:
   ```bash
   cmake --preset ninja-debug
   cmake --build --preset ninja-debug -j
   ```

## Windows

1. Baixe `Paperboat-Mulberry-Delta-Win64.zip` em https://github.com/HarbourMasters/PaperBoat/releases e extraia.
2. Abra `paperboat.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

**Compilar, opcional:**
1. Instale o Visual Studio 2022 com "Desktop development with C++", "C++ Clang tools for Windows" e "CMake tools for Windows".
2. Num **Developer PowerShell for VS 2022**, rode:
   ```powershell
   cmake --preset windows-debug
   cmake --build --preset windows-debug -j
   ```
O compilador MSVC puro (`cl.exe`) não é suportado. O caminho suportado é Ninja + `clang-cl`.

## Controles e configurações

| N64 | A | B | Z | Start | Analógico | Botões C | Direcional |
|---|---|---|---|---|---|---|---|
| Teclado | X | C | Z | Espaço | W A S D | Setas | T F G H |

Assets personalizados (`.o2r` ou `.otr`) vão na pasta `mods`.

## Fontes

- [README › Quick Start, Configuration e Custom Assets](https://github.com/HarbourMasters/PaperBoat#readme)
- [docs/BUILDING.md](https://github.com/HarbourMasters/PaperBoat/blob/develop/docs/BUILDING.md)
- [Releases](https://github.com/HarbourMasters/PaperBoat/releases)

<!-- verificado: 2026-10-15 -->
