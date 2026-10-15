# The Legend of Zelda: Ocarina of Time · Ship of Harkinian (N64)

Repositório: https://github.com/HarbourMasters/Shipwright · Espelho: https://github.com/alves-r/mirror-harbourmasters-shipwright

Port de PC do Ocarina of Time feito pela HarbourMasters, com binário pronto para Windows, Linux e macOS. Gera os recursos do jogo a partir da sua ROM.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (9.3.0, de 06/10/2026: `SoH-Dewey-Alpha-Win64.zip`, `SoH-Dewey-Alpha.appimage` e Mac) |
| Precisa de emulador | Não |
| Você precisa fornecer | Uma versão suportada do Ocarina of Time: N64 (NTSC 1.0, 1.1 e 1.2 dos EUA e do Japão; PAL 1.0 e 1.1) ou GameCube (normal, Master Quest e Debug). Os SHA-1 estão em `docs/supportedHashes.json`, e o site https://ship.equipment/ confere o seu arquivo. ⚠️ Você indicou que não consegue dumpar N64 nem GameCube. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Baixe `SoH-Dewey-Alpha.appimage` em https://github.com/HarbourMasters/Shipwright/releases.
2. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
3. Rode: `chmod +x SoH-Dewey-Alpha.appimage && ./SoH-Dewey-Alpha.appimage`
4. Quando pedir, escolha a sua cópia do jogo. O programa gera o `oot.o2r`.
5. Saves, configurações e o `oot.o2r` ficam em `~/.local/share/soh/`. Para usar outra pasta, defina `SHIP_HOME`.

**Compilar, opcional** (`docs/BUILDING.md`):

1. Instale as dependências pela linha do documento para o Arch. O `sdl2` é fornecido pelo `sdl2-compat`:
   `sudo pacman -S gcc git cmake ninja lsb-release sdl2 libpng libzip nlohmann-json tinyxml2 spdlog sdl2_net opusfile libvorbis python`
2. Clone, baixe os submódulos e compile:
   ```bash
   git clone https://github.com/HarbourMasters/Shipwright.git && cd Shipwright
   git submodule update --init
   cmake -H. -Bbuild-cmake -GNinja
   cmake --build build-cmake --target GenerateSohOtr
   cmake --build build-cmake
   ```
3. Rode `./build-cmake/soh/soh.elf`.

## Windows

1. Baixe `SoH-Dewey-Alpha-Win64.zip` em https://github.com/HarbourMasters/Shipwright/releases e extraia.
2. Abra `soh.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Quando pedir, escolha a sua cópia do jogo.

Para compilar no Windows, o `docs/BUILDING.md` pede:
- pelo menos 8 GB de RAM;
- Visual Studio 2022 com **Desktop development with C++** e o conjunto de ferramentas v143;
- Python 3, Git e CMake.

Há builds de teste, mais instáveis, para cada sistema nos links "Playtesting" do README.

## Controles e configurações

| N64 | A | B | Z | Start | Analógico | Botões C | Direcional |
|---|---|---|---|---|---|---|---|
| Teclado | X | C | Z | Espaço | WASD | Setas | TFGH |

Recursos personalizados (arquivos `.otr`) vão na pasta `mods`.

## Fontes

- [README › Quick Start e Configuration](https://github.com/HarbourMasters/Shipwright#readme)
- [docs/BUILDING.md](https://github.com/HarbourMasters/Shipwright/blob/develop/docs/BUILDING.md)
- [docs/supportedHashes.json](https://github.com/HarbourMasters/Shipwright/blob/develop/docs/supportedHashes.json)
- [Releases (9.3.0)](https://github.com/HarbourMasters/Shipwright/releases)

<!-- verificado: 2026-10-15 -->
