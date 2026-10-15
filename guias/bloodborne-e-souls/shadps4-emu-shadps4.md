# shadPS4 (emulador de PS4)

Repositório: https://github.com/shadps4-emu/shadPS4 · Espelho: https://github.com/alves-r/mirror-shadps4-emu-shadps4

Emulador de PlayStation 4 para Windows, Linux e macOS. Já roda Bloodborne, Dark Souls Remastered, Red Dead Redemption e outros jogos, mas ainda está no início do desenvolvimento.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim (v0.20.0, de 14/10/2026: `shadps4-linux-sdl-0.20.0.zip`, que traz `Shadps4-sdl.AppImage`; `shadps4-win64-sdl-2026-0.20.0.zip`, que traz `shadPS4.exe`; e macOS) |
| Precisa de emulador | Não (é o próprio emulador) |
| Você precisa fornecer | Jogos de PS4 decriptados, em pastas com o ID do jogo (ex.: Bloodborne dos EUA é `CUSA00900`). Também os módulos de firmware listados no README (`libSceFont.sprx`, `libSceNgs2.sprx` e outros) na pasta `sys_modules`, dumpados do seu PS4. ⚠️ Você não soube dizer se consegue dumpar PS4. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Início do desenvolvimento: o próprio README pede para não esperar uma experiência perfeita. |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

**Opção 1: release pronta**

1. Baixe `shadps4-linux-sdl-0.20.0.zip` em https://github.com/shadps4-emu/shadPS4/releases.
2. Extraia: `bsdtar -xf shadps4-linux-sdl-0.20.0.zip`. O `unzip` não vem instalado na sua máquina; `bsdtar` faz o mesmo (sugestão).
3. Instale o FUSE 2, que os AppImages usam no Arch (sugestão): `sudo pacman -S --needed fuse2`
4. Dê permissão: `chmod +x Shadps4-sdl.AppImage`
5. Rode apontando para o executável do jogo: `./Shadps4-sdl.AppImage /caminho/para/CUSA00900/eboot.bin`. A lista de opções aparece com `./Shadps4-sdl.AppImage --help`.
6. Coloque os módulos de firmware na pasta `sys_modules` do shadPS4. O README não diz onde essa pasta fica.
7. Interface gráfica, opcional: o README recomenda o QtLauncher, que fica em outro repositório: https://github.com/shadps4-emu/shadps4-qtlauncher/releases.

**Opção 2: compilar** (pelo `documents/building-linux.md`)

1. Instale as dependências. O documento lista `sdl2`, que no Arch hoje se chama `sdl2-compat` (conversão sugerida):
   `sudo pacman -S --needed base-devel clang git cmake sndio jack2 openal sdl2-compat vulkan-validation-layers libpng`
2. Clone com os submódulos: `git clone --recursive https://github.com/shadps4-emu/shadPS4.git && cd shadPS4`
3. Configure com Clang: `cmake -S . -B build/ -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++`. O documento recomenda o Clang 19 e usa `clang-19`; no Arch, o pacote `clang` traz a versão atual (sugestão).
4. Compile: `cmake --build ./build --parallel$(nproc)`. Se o PC travar nessa etapa, tire o `--parallel$(nproc)`.
5. Rode: `./build/shadps4`

O pacote `shadps4-git` do AUR não é mantido pela equipe e usa o compilador padrão (GCC). Use por sua conta.

## Windows

1. Baixe `shadps4-win64-sdl-2026-0.20.0.zip` em https://github.com/shadps4-emu/shadPS4/releases e extraia.
2. No PowerShell, dentro da pasta extraída, rode: `.\shadPS4.exe C:\caminho\para\CUSA00900\eboot.bin`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Coloque os módulos de firmware na pasta `sys_modules` do shadPS4.
4. Interface gráfica, opcional: QtLauncher, em https://github.com/shadps4-emu/shadps4-qtlauncher/releases.

**Compilar, opcional** (pelo `documents/building-windows.md`):

1. Instale o Visual Studio 2022 Community com a carga "Desenvolvimento para desktop com C++" e, em Componentes individuais, "C++ Clang Compiler for Windows" e "MSBuild support for LLVM".
2. Instale o Git for Windows.
3. Clone: `git clone --depth 1 --recursive https://github.com/shadps4-emu/shadPS4`
4. No Visual Studio, use **Abrir uma pasta local** e escolha a pasta clonada.
5. Troque a configuração para **Clang x64 Release**, escolha o alvo `shadps4.exe` e use **Build → Build All**. O executável sai em `Build\x64-Clang-Release\`.

O Windows em ARM64 não é suportado.

## Controles e configurações

Atalhos:

| Tecla | Função |
|---|---|
| F10 | Contador de FPS |
| Ctrl+F10 | Informações de vídeo |
| F11 | Tela cheia |
| F12 | Captura do RenderDoc (ou screenshot do jogo, sem RenderDoc) |
| Alt+F12 | Screenshot com HUD e diálogos |

Controles de Xbox e DualShock funcionam sem configuração. Mapeamento padrão do teclado:

| Comando | Teclas |
|---|---|
| Analógico esquerdo | W A S D |
| Analógico direito | I J K L |
| Triângulo / Círculo / X / Quadrado | C / B / N / V (ou Numpad 8 / 6 / 2 / 4) |
| Direcional | Setas |
| L1 / R1 / L2 / R2 | Q / U / E / O |
| L3 / R3 | X / M |
| Options | Enter |
| Touchpad | Espaço |

Os atalhos podem ser trocados nas configurações, pelo botão Controller. O mapeamento é salvo por jogo.

## Problemas conhecidos

- O emulador está no começo, e o desempenho e os bugs variam de jogo para jogo.
- Windows em ARM64 não é suportado: não compila nem roda.

## Fontes

- [README › Status, Usage examples, Keyboard and Mouse Mappings e Firmware files](https://github.com/shadps4-emu/shadPS4#readme)
- [documents/building-linux.md](https://github.com/shadps4-emu/shadPS4/blob/main/documents/building-linux.md)
- [documents/building-windows.md](https://github.com/shadps4-emu/shadPS4/blob/main/documents/building-windows.md)
- [Releases](https://github.com/shadps4-emu/shadPS4/releases)

<!-- verificado: 2026-10-15 -->
