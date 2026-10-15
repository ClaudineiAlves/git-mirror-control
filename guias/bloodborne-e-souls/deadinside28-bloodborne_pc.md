# Bloodborne · bbport (PS4)

Repositório: https://github.com/deadinside28/bloodborne_pc · Espelho: https://github.com/alves-r/mirror-deadinside28-bloodborne_pc

Port nativo para Linux que roda o executável original do Bloodborne 1.09 direto na CPU, com os gráficos traduzidos para Vulkan. Já é jogável, mas ninguém confirmou uma partida do início ao fim.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (`Bloodborne-bbport-x86_64.AppImage`, Linux x86-64, com `SHA256SUMS`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Dump decriptado do Bloodborne com a atualização 1.09 aplicada: a pasta `CUSA03173` (Europa, GOTY), `CUSA00900` (EUA) ou `CUSA03023` (Ásia), com `eboot.bin` e `sce_module`. A versão 1.00 sozinha trava, e um `eboot.bin` com o patch de 60 fps do Lance McDonald também (use um limpo). ⚠️ Você não soube dizer se consegue dumpar PS4, e sem esse dump não há como jogar. |
| Arch Linux | Nativo |
| Windows | Não suportado |
| Estado | Experimental e jogável. Abre, carrega saves e foi jogado no Sonho do Caçador e em áreas de Yharnam com som, controle e save. Uma partida completa não foi verificada, e só uma máquina foi testada a fundo (AMD RX 7800 XT, Mesa/RADV). Releases: 0.51 (10/10/2026) e 0.6-pre1 (15/10/2026). |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

O projeto pede Linux x86-64 e uma GPU com Vulkan 1.3. O novo modelo de memória ainda não foi testado em placas NVIDIA.

**Opção 1: AppImage (recomendada)**

1. Baixe `Bloodborne-bbport-x86_64.AppImage` e `SHA256SUMS` da release 0.51 em https://github.com/deadinside28/bloodborne_pc/releases.
2. Confira o download: `sha256sum -c SHA256SUMS`
3. Instale o FUSE 2, que os AppImages usam no Arch (sugestão): `sudo pacman -S --needed fuse2`
4. Dê permissão de execução: `chmod +x Bloodborne-bbport-x86_64.AppImage`
5. Abra: `./Bloodborne-bbport-x86_64.AppImage`. No launcher, escolha a pasta do jogo, ajuste as opções e clique em **Start**.
6. Para pular o launcher: `./Bloodborne-bbport-x86_64.AppImage --play`. Os dados ficam em `~/.local/share/bbport`.

**Opção 2: compilar**

1. Instale as dependências. O projeto as lista no `shell.nix`, no formato do Nix; a conversão para o Arch abaixo é uma sugestão:
   `sudo pacman -S --needed base-devel cmake ninja pkgconf python vulkan-headers vulkan-icd-loader sdl3 ffmpeg boost fmt robin-map xxhash glslang spirv-cross zydis spirv-headers miniz libx11 libxcb xorgproto wayland protobuf nlohmann-json openssl zlib miniupnpc gtk4`
   Três itens do `shell.nix` não estão nos repositórios oficiais (`magic_enum`, `vulkan-memory-allocator` e `xbyak`). Se o build pedir, procure-os no AUR com `yay`.
2. Clone com os submódulos: `git clone --recursive https://github.com/deadinside28/bloodborne_pc.git bbport && cd bbport`
3. Compile: `bash build.sh`
4. Rode indicando a pasta do jogo: `BB_GAME_DIR=/caminho/para/CUSA03173 bash run.sh`. Sem a variável, o jogo é procurado em `../CUSA03173`, ao lado do repositório.
5. Ou use o launcher: `bash launcher/bb-launcher.sh`. Para criar o atalho no menu: `bash launcher/install-desktop.sh`.

Saves e cache de shaders vão para `user/`. As configurações ficam em `bbport.ini`.

## Windows

Não disponível no Windows: o projeto é um port só para Linux. No Windows, use o BloodBorneButPc ([guia](awakenchan-bloodbornebutpc.md)), um derivado deste projeto feito para Windows.

## Controles e configurações

- Controles funcionam via SDL3. Com vários conectados, escolha em **Controls → Controller** ou com `BB_GAMEPAD=<GUID ou parte do nome>`.
- O teclado funciona junto com o controle. Os dois são remapeados no launcher, em **Controls**.
- Touchpad: a metade esquerda (Tab, Back/Select) abre os gestos e a metade direita (Backspace) abre os itens-chave.
- O menu de configurações do port abre com Insert ou L3+R3.
- Não há PSN: a tela "jogar online/offline" é pulada e o jogo abre offline. `BB_SKIP_NETWORK_CHOICE=0` volta a mostrar essa tela.
- Com vários monitores, escolha em **Screen → Monitor** ou com `BB_DISPLAY=<número ou parte do nome>`.
- Mods: pastas de arquivos soltos pelo launcher, com ordem de carga, ou uma pasta `CUSA03173-mods/` ao lado do jogo. Patches no formato do shadPS4 vão em `patches/`.
- DLC: os dumps vão em `user/addcont/<title id>/<rótulo>/`. Exemplo para The Old Hunters: `user/addcont/CUSA03173/SPEXPANSIONDLC03`.

## Problemas conhecidos

- **1.00 sem atualização:** a versão 1.00 do jogo trava ao iniciar.
- **Patch de 60 fps embutido:** um `eboot.bin` com o patch do Lance McDonald trava ao abrir o menu de gestos. O port já tem 60 fps próprio.
- **NVIDIA:** o novo modelo de memória ainda não foi testado nelas, que continuam no modelo antigo.
- **Steam sem FUSE** (ex.: NixOS): aparece "Cannot mount AppImage". O README traz as opções de inicialização para contornar.
- **Steam Deck:** a validação do AppImage ainda está pendente no roadmap.

## Fontes

- [README](https://github.com/deadinside28/bloodborne_pc#readme) (seções Requirements, Build and run e Roadmap)
- [shell.nix](https://github.com/deadinside28/bloodborne_pc/blob/master/shell.nix)
- [Releases](https://github.com/deadinside28/bloodborne_pc/releases)

<!-- verificado: 2026-10-15 -->
