# Emulador de PlayStation 3 · RPCS3 (PS3)

Repositório: https://github.com/RPCS3/rpcs3 · Espelho: https://github.com/alves-r/mirror-rpcs3-rpcs3

Primeiro emulador e depurador de PlayStation 3 livre e de código aberto, para Windows, Linux, macOS e FreeBSD.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim, pelo site oficial (https://rpcs3.net/download). As tags do GitHub, como a v0.0.43 de 30/09/2026, não têm arquivos e não são versões estáveis. |
| Precisa de emulador | Não se aplica: este é o emulador |
| Você precisa fornecer | O firmware oficial do PS3 (`PS3UPDAT.PUP`) e os jogos copiados do seu console ou dos seus discos. O guia de início rápido do site explica o firmware. ⚠️ Você indicou que não consegue dumpar PS3. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo. Não há versões estáveis: o projeto é "rolling release". |
| Dificuldade | Fácil (baixar e rodar) |

Antes de começar, confira os requisitos mínimos no guia de início rápido (https://rpcs3.net/quickstart) e atualize o driver de vídeo.

## Arch Linux

1. Instale por um destes caminhos (sugestão):
   - pelo AUR: `yay -S rpcs3-bin`;
   - ou baixe o AppImage em https://rpcs3.net/download, instale o FUSE 2 (`sudo pacman -S --needed fuse2`) e rode `chmod +x rpcs3-*.AppImage && ./rpcs3-*.AppImage`.
2. Siga o guia de início rápido: instale o firmware e adicione os seus jogos.

**Compilar, opcional** (`BUILDING.md`):
1. Instale as dependências pela linha do documento para o Arch:
   `sudo pacman -S glew openal cmake ninja vulkan-validation-layers qt6-base qt6-declarative qt6-multimedia qt6-svg sdl3 sndio jack2 base-devel`
2. Com placa NVIDIA, pode ser preciso também o `libglvnd`.
3. Clone e compile:
   ```bash
   git clone --recurse-submodules https://github.com/RPCS3/rpcs3.git && cd rpcs3
   cmake -B build -G Ninja
   cmake --build build
   ```
4. Rode: `build/bin/rpcs3`

O documento pede Clang 17+ ou GCC 13+, CMake 3.28+, Qt 6.12.0, Vulkan SDK 1.4.341.1 e SDL3.

## Windows

1. Instale o Visual C++ Redistributable para Visual Studio 2022, como o README pede.
2. Baixe o RPCS3 em https://rpcs3.net/download e extraia numa pasta.
3. Abra o `rpcs3.exe` e siga o guia de início rápido para instalar o firmware e adicionar os jogos.

Para compilar no Windows, o `BUILDING.md` pede o Visual Studio 2022 ou 2026, Python 3.6+, Qt 6.12.0 e o Vulkan SDK 1.4.341.1. A solução `.sln` é o caminho preferido.

## Fontes

- [README › Building e Running](https://github.com/RPCS3/rpcs3#readme)
- [BUILDING.md](https://github.com/RPCS3/rpcs3/blob/master/BUILDING.md)
- [Notas da tag v0.0.43, que mandam baixar pelo site](https://github.com/RPCS3/rpcs3/releases/tag/v0.0.43)

<!-- verificado: 2026-10-15 -->
