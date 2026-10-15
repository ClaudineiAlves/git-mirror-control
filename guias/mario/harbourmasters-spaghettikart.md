# Mario Kart 64 · SpaghettiKart (N64)

Repositório: https://github.com/HarbourMasters/SpaghettiKart · Espelho: https://github.com/alves-r/mirror-harbourmasters-spaghettikart

Port de PC do Mario Kart 64 feito pela HarbourMasters, com binário pronto para Windows, Linux e macOS. Gera os recursos do jogo a partir da sua ROM.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (1.0.0, de 25/02/2026: `spaghetti-windows.zip`, `spaghetti-linux.zip` e Mac) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Mario Kart 64 dos EUA, a única suportada, em `.z64` (SHA-1 `579C48E211AE952530FFC8738709F078D5DD215E`). ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Versão 1.0.0 estável, de 25/02/2026 |
| Dificuldade | Fácil (baixar e rodar) |

Se a ROM estiver em `.n64`, ela precisa ser convertida para `.z64`. O README indica uma ferramenta online para isso.

## Arch Linux

1. Baixe `spaghetti-linux.zip` em https://github.com/HarbourMasters/SpaghettiKart/releases e extraia todos os arquivos: `bsdtar -xf spaghetti-linux.zip` (sugestão).
2. O README exige o `zenity` ou o `kdialog` instalado: `sudo pacman -S --needed zenity`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x spaghetti.appimage && ./spaghetti.appimage`
5. Escolha a sua ROM dos EUA. O jogo gera os arquivos `.o2r` a partir dela.

**Compilar, opcional** (`docs/BUILDING.md`):

1. Instale as dependências pela linha do documento para o Arch (o `sdl2` é fornecido pelo `sdl2-compat`):
   `sudo pacman -S gcc git cmake ninja lsb-release sdl2 libpng libzip nlohmann-json tinyxml2 spdlog sdl2_net boost libogg libvorbis`
2. Clone, baixe os submódulos e compile:
   ```bash
   git clone https://github.com/HarbourMasters/SpaghettiKart.git && cd SpaghettiKart
   git submodule update --init
   cmake -H. -Bbuild-cmake -GNinja
   cmake --build build-cmake --target ExtractAssets
   cmake --build build-cmake
   ```
3. O documento indica rodar `./build/Spaghettify`.

## Windows

1. Baixe `spaghetti-windows.zip` em https://github.com/HarbourMasters/SpaghettiKart/releases e extraia todos os arquivos numa pasta.
2. Abra `Spaghettify.exe` e escolha a sua ROM dos EUA. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Depois disso, é só abrir `Spaghettify.exe` para jogar.

## Controles e configurações

| N64 | A | B | L | R | Z | Start | Analógico | Botões C | Direcional |
|---|---|---|---|---|---|---|---|---|---|
| Teclado | Shift | Ctrl | Q | Espaço | Z | Enter | Setas | T G F H | Num 8 2 4 6 |
| Controle SDL | A | X | LB | RB | LT | Start | Analógico esq. | Analógico dir. ↑, B, Y, analógico dir. → | Direcional |

## Problemas conhecidos

- **O jogo fecha ao abrir:** tente de novo. Se continuar, apague `spaghettify.cfg.json` e, se ainda assim falhar, apague também `imgui.ini`.
- **A câmera livre não gira com o controle:** adicione um analógico direito extra nos controles.

## Fontes

- [README › Quick Start, Generating the O2R from the ROM e Default controls](https://github.com/HarbourMasters/SpaghettiKart#readme)
- [docs/BUILDING.md](https://github.com/HarbourMasters/SpaghettiKart/blob/main/docs/BUILDING.md)
- [docs/faq.md](https://github.com/HarbourMasters/SpaghettiKart/blob/main/docs/faq.md)
- [Releases](https://github.com/HarbourMasters/SpaghettiKart/releases)

<!-- verificado: 2026-10-15 -->
