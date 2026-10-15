# The Legend of Zelda: Majora's Mask · Zelda 64: Recompiled (N64)

Repositório: https://github.com/Zelda64Recomp/Zelda64Recomp · Espelho: https://github.com/alves-r/mirror-zelda64recomp-zelda64recomp

Recompilação estática do Majora's Mask para PC, com taxa de quadros alta, widescreen, mira por giroscópio e suporte a mods. O Ocarina of Time está prometido para o futuro.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v1.2.2, de 27/08/2025: zips para Windows, Linux x64, Linux ARM64, Linux Flatpak e macOS) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Majora's Mask de N64 dos EUA (SHA-1 `d6133ace5afaa0882cf214cf88daba39e266c078`). Outros formatos além de `.z64` são convertidos sozinhos, desde que a ROM seja a certa. ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo. Exige placa de vídeo com Direct3D 12, Vulkan 1.2 ou Metal e, em x86-64, CPU com SSE4.1. |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Baixe `Zelda64Recompiled-v1.2.2-Linux-X64.zip` em https://github.com/Zelda64Recomp/Zelda64Recomp/releases.
2. Extraia. O zip traz um `Zelda64Recompiled.tar.gz`:
   ```bash
   bsdtar -xf Zelda64Recompiled-v1.2.2-Linux-X64.zip   # bsdtar: sugestão, já que o unzip não está instalado
   tar -xzf Zelda64Recompiled.tar.gz
   ```
3. Rode: `./Zelda64Recompiled`
4. No menu principal, escolha a sua ROM e jogue. Não há etapa separada de extração.
5. Os saves ficam em `~/.config/Zelda64Recompiled/saves`.

Há também uma versão Flatpak (`Zelda64Recompiled-v1.2.2-Linux-Flatpak-X64.zip`), mas o README não detalha a instalação dela.

**Compilar, opcional** (`BUILDING.md`; dá mais trabalho):

1. Instale as dependências. O documento lista os pacotes do Ubuntu; os equivalentes no Arch são (sugestão): `sudo pacman -S --needed cmake ninja sdl2-compat gtk3 lld llvm clang`
2. Clone com submódulos: `git clone --recurse-submodules https://github.com/Zelda64Recomp/Zelda64Recomp.git`
3. Descomprima a ROM dos EUA, com o script `tools/decompress_baserom.py` do decomp `zeldaret/mm` ou com o `z64decompress`. Salve o resultado na raiz do repositório como `mm.us.rev1.rom_uncompressed.z64`.
4. Compile o [N64Recomp](https://github.com/Mr-Wiseguy/N64Recomp) e, na raiz do repositório, gere o código C:
   ```bash
   ./N64Recomp us.rev1.toml
   ./RSPRecomp aspMain.us.rev1.toml
   ./RSPRecomp njpgdspMain.us.rev1.toml
   ```
5. Compile:
   ```bash
   cmake -S . -B build-cmake -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang -G Ninja -DCMAKE_BUILD_TYPE=Release
   cmake --build build-cmake --target Zelda64Recompiled -j$(nproc) --config Release
   ```

## Windows

1. Baixe `Zelda64Recompiled-v1.2.2-Windows.zip` em https://github.com/Zelda64Recomp/Zelda64Recomp/releases e extraia.
2. Abra o executável `Zelda64Recompiled`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. No menu principal, escolha a sua ROM e jogue.
4. Os saves ficam em `%LOCALAPPDATA%\Zelda64Recompiled\saves`.

Para compilar no Windows, o `BUILDING.md` pede o Visual Studio 2022 com **Desktop development with C++**, **C++ Clang Compiler for Windows** e **C++ CMake tools for Windows**, além do `make` (`choco install make`). Os passos 2 a 5 da seção Arch Linux são os mesmos.

## Controles e configurações

- Jogo, gráficos, controles e áudio são ajustados no menu do jogo, com mouse, controle ou teclado.
- **Taxa de quadros:** por padrão acompanha a frequência do monitor. Há um controle manual no menu de gráficos.
- **Mira por giroscópio:** funciona com DualShock 4, DualSense, Switch Pro e outros. Programas como BetterJoy e DS4Windows podem bloquear o giroscópio.
- **Mods:** arraste os arquivos para a janela antes de começar ou clique em **Install Mods**. No Thunderstore (https://thunderstore.io/c/zelda-64-recompiled/), use **Manual Download**; o r2modman não é suportado.

## Problemas conhecidos

- Sobreposições como MSI Afterburner e programas como Wallpaper Engine podem atrapalhar a renderização. Desligue-os.
- Limitadores de FPS externos, como o do painel da NVIDIA, podem causar travadas. Use o controle do menu do jogo.
- Se o jogo fechar ao abrir, atualize o driver de vídeo. Na Intel, baixe o driver direto do site da Intel.

## Fontes

- [README › System Requirements, Plug and Play, Mod Support, FAQ e Known Issues](https://github.com/Zelda64Recomp/Zelda64Recomp#readme)
- [BUILDING.md](https://github.com/Zelda64Recomp/Zelda64Recomp/blob/dev/BUILDING.md)
- [Releases (v1.2.2)](https://github.com/Zelda64Recomp/Zelda64Recomp/releases)

<!-- verificado: 2026-10-15 -->
