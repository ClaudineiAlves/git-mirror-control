# The Legend of Zelda: Majora's Mask · 2 Ship 2 Harkinian (N64)

Repositório: https://github.com/2ship2harkinian/2ship2harkinian · Espelho: https://github.com/alves-r/mirror-2ship2harkinian-2ship2harkinian

Port de PC do Majora's Mask, da mesma família do Ship of Harkinian, com binário pronto para Windows, Linux e macOS. Gera os recursos do jogo a partir da sua ROM.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (5.0.1, de 25/08/2026: `2Ship-Battler-Bravo-Win64.zip`, `2Ship-Battler-Bravo-Linux.zip` e Mac) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Majora's Mask NTSC-U 1.0 de N64 (SHA-1 `d6133ace5afaa0882cf214cf88daba39e266c078`) ou a versão de GameCube dos EUA (`9743aa026e9269b339eb0e3044cd5830a440c1fd`). O site https://2ship.equipment/ confere o seu arquivo. ⚠️ Você indicou que não consegue dumpar N64 nem GameCube. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Baixe `2Ship-Battler-Bravo-Linux.zip` em https://github.com/2ship2harkinian/2ship2harkinian/releases e extraia: `bsdtar -xf 2Ship-Battler-Bravo-Linux.zip` (sugestão).
2. Coloque a sua cópia do jogo na mesma pasta do `2ship.appimage`.
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x 2ship.appimage && ./2ship.appimage`

**Compilar, opcional** (`docs/BUILDING.md`):

1. Instale as dependências pela linha do documento para o Arch. O `sdl2` é fornecido pelo `sdl2-compat`:
   `sudo pacman -S gcc git cmake ninja lsb-release sdl2 libpng libzip nlohmann-json tinyxml2 spdlog sdl2_net libogg libvorbis opus opusfile`
2. Clone, baixe os submódulos e compile:
   ```bash
   git clone https://github.com/2ship2harkinian/2ship2harkinian.git && cd 2ship2harkinian
   git submodule update --init
   cmake -H. -Bbuild-cmake -GNinja
   cmake --build build-cmake --target Generate2ShipOtr
   cmake --build build-cmake
   ```
3. Rode `./build-cmake/mm/2s2h.elf`.

## Windows

1. Baixe `2Ship-Battler-Bravo-Win64.zip` em https://github.com/2ship2harkinian/2ship2harkinian/releases e extraia.
2. Abra `2ship.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Quando pedir, escolha a sua cópia do jogo.

Há builds de teste, mais instáveis, para cada sistema nos links "Nightly Builds" do README.

## Controles e configurações

| N64 | A | B | Z | Start | Analógico | Botões C | Direcional |
|---|---|---|---|---|---|---|---|
| Teclado | X | C | Z | Espaço | WASD | Setas | TFGH |

- **F1:** mostra ou esconde a barra de menus.
- **F11:** tela cheia.
- **Tab:** liga ou desliga os recursos alternativos.
- **Ctrl+R:** reinicia.

Recursos personalizados (arquivos `.o2r` ou `.otr`) vão na pasta `mods`.

## Problemas conhecidos

- **O jogo fecha:** troque a API gráfica no menu **Settings**. Ela também pode ser trocada no `2ship2harkinian.json`, na seção `"Backend"`, com os IDs `0` (DirectX 11, padrão no Windows), `1` (OpenGL) ou `2` (Metal, padrão no macOS).

## Fontes

- [README › Quick Start, Configuration e Graphics Backends](https://github.com/2ship2harkinian/2ship2harkinian#readme)
- [docs/BUILDING.md](https://github.com/2ship2harkinian/2ship2harkinian/blob/develop/docs/BUILDING.md)
- [docs/supportedHashes.json](https://github.com/2ship2harkinian/2ship2harkinian/blob/develop/docs/supportedHashes.json)
- [Releases (5.0.1)](https://github.com/2ship2harkinian/2ship2harkinian/releases)

<!-- verificado: 2026-10-15 -->
