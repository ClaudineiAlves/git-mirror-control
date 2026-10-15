# Super Mario 64 · Ghostship (N64)

Repositório: https://github.com/HarbourMasters/Ghostship · Espelho: https://github.com/alves-r/mirror-harbourmasters-ghostship

Port de PC do Super Mario 64 feito pela HarbourMasters, com binário pronto para Windows, Linux, macOS, Android e iOS. Gera os recursos do jogo a partir da sua ROM.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (3.0.0, de 07/09/2026: `Nautilus-Alfa-Win64.zip`, `Nautilus-Alfa-Linux.zip`, Mac, Android e iOS) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Super Mario 64 em `.z64`, versão EUA (SHA-1 `9bef1128717f958171a4afac3ed78ee2bb4e86ce`) ou Japão (SHA-1 `8a20a5c83d6ceb0f0506cfc9fa20d8f438cafe51`). ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo; versão 3.0.0 de 07/09/2026 |
| Dificuldade | Fácil (baixar e rodar) |

Se a ROM estiver em `.n64`, ela precisa ser convertida para `.z64`. O README indica uma ferramenta online para isso.

## Arch Linux

1. Baixe `Nautilus-Alfa-Linux.zip` em https://github.com/HarbourMasters/Ghostship/releases.
2. Extraia todos os arquivos: `bsdtar -xf Nautilus-Alfa-Linux.zip` (sugestão; o `unzip` não vem instalado na sua máquina).
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x Ghostship.appimage && ./Ghostship.appimage`
5. Escolha a sua ROM (EUA ou Japão) quando o jogo pedir.

**Compilar, opcional** (`docs/building.md`):

1. Instale as dependências pela linha do documento para o Arch (o `sdl2` é fornecido pelo `sdl2-compat`):
   `sudo pacman -S gcc git cmake ninja lsb-release sdl2 libpng libzip nlohmann-json tinyxml2 spdlog sdl2_net boost libogg libvorbis mbedtls`
2. Clone e baixe os submódulos:
   ```bash
   git clone https://github.com/HarbourMasters/ghostship.git && cd ghostship
   git submodule update --init
   ```
3. Configure e compile:
   ```bash
   cmake -H. -Bbuild-cmake -GNinja
   cmake --build build-cmake --target ExtractAssets
   cmake --build build-cmake --target GeneratePortO2R
   cmake --build build-cmake
   ```
O documento tem trechos herdados de outros projetos: cita `sf64.o2r` e um executável `2s2h.elf`. O caminho exato do binário gerado não está documentado corretamente.

## Windows

1. Baixe `Nautilus-Alfa-Win64.zip` em https://github.com/HarbourMasters/Ghostship/releases e extraia todos os arquivos numa pasta.
2. Abra `Ghostship.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Escolha a sua ROM (EUA ou Japão).

**Compilar, opcional:** o `docs/building.md` pede pelo menos 8 GB de RAM, Visual Studio 2022 Community com C++ (conjunto de ferramentas v143), Python 3, Git e CMake. Clone com `--recursive` e gere o projeto com `cmake -S . -B "build/x64" -G "Visual Studio 17 2022" -T v143 -A x64`.

## Controles e configurações

| N64 | A | B | Z | Start | Analógico | Botões C | Direcional |
|---|---|---|---|---|---|---|---|
| Teclado | X | C | Z | Espaço | W A S D | Setas | T F G H |

Assets personalizados (`.o2r` ou `.otr`) vão na pasta `mods`.

## Fontes

- [README › Quick Start, Windows, Linux, Configuration e Custom Assets](https://github.com/HarbourMasters/Ghostship#readme)
- [docs/building.md](https://github.com/HarbourMasters/Ghostship/blob/develop/docs/building.md)
- [Releases](https://github.com/HarbourMasters/Ghostship/releases)

<!-- verificado: 2026-10-15 -->
