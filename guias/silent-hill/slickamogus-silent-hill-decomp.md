# Silent Hill · Silent Hill PC Port (PS1)

Repositório: https://github.com/SlickAmogus/silent-hill-decomp · Espelho: https://github.com/alves-r/mirror-slickamogus-silent-hill-decomp

Port nativo do primeiro Silent Hill para PC e outras plataformas, feito a partir da decompilação do jogo de PS1 com a camada PsyCross. Traz launcher, câmeras alternativas, menu rápido de opções e ferramentas de mod. Está em beta.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (release `crossplatform-beta`: `SHPC_beta-2026.10.12.1.zip` para Windows, `SHPC-linux-x64_2026.09.27.1.tar.gz` para Linux, macOS, Android, iOS e uma prévia para Xbox) |
| Precisa de emulador | Não |
| Você precisa fornecer | A imagem do disco do Silent Hill de PS1 em `.bin`, de preferência a americana (`SLUS-00707`). O launcher detecta a região pelo arquivo. ⚠️ Você indicou que não consegue dumpar PS1. |
| Arch Linux | Nativo (o README avisa que o build de Linux ainda tem problemas) |
| Windows | Nativo |
| Estado | Beta em desenvolvimento ativo. As atualizações saem principalmente pelo launcher e por builds noturnos. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal. A descrição do repositório diz que o port foi feito com o Claude (IA).

## Arch Linux

O README avisa que os builds de Linux e macOS ainda têm problemas e recomenda o Windows ou o Wine quando possível.

1. Instale as dependências que o `README-linux.txt` pede (SDL2, OpenAL e drivers OpenGL). No Arch, o SDL2 vem do `sdl2-compat` (sugestão): `sudo pacman -S --needed sdl2-compat openal`
2. Baixe `SHPC-linux-x64_2026.09.27.1.tar.gz` em https://github.com/SlickAmogus/silent-hill-decomp/releases e extraia: `tar -xzf SHPC-linux-x64_2026.09.27.1.tar.gz`
3. Coloque a imagem do disco em `SHPC-linux-x64/gamedata/`. Qualquer nome serve; `Silent Hill (USA).bin` é o padrão seguro.
4. Rode: `cd SHPC-linux-x64 && ./SilentHillPC`

O pacote de Linux não traz o launcher. As opções ficam no `config.cfg`.

## Windows

1. Baixe `SHPC_beta-2026.10.12.1.zip` em https://github.com/SlickAmogus/silent-hill-decomp/releases e extraia em qualquer pasta.
2. Coloque a imagem do disco na pasta `gamedata`. Qualquer nome serve; `Silent Hill (USA).bin` é o padrão seguro.
3. Rode o `SilentHillPC` uma vez para jogar. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. Depois disso, use o `SilentHillPC_Launcher` para configurar.

**Compilar, opcional** (README, seção Building):

1. Instale o MSYS2. No shell **MSYS2 MinGW x64**, instale:
   `pacman -S --needed mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-ninja mingw-w64-x86_64-SDL2 mingw-w64-x86_64-openal mingw-w64-x86_64-libjpeg-turbo`
2. Na raiz do repositório, rode `git submodule update --init --recursive` para baixar o PsyCross.
3. Coloque o disco em `pc_port/build/gamedata/Silent Hill (USA).bin`.
4. Rode `pc_port\build.bat`. Ou faça à mão, no shell MinGW64:
   ```bash
   cd silent-hill-decomp/pc_port
   cmake -S . -B build -G Ninja -DSH_BUILD_MAP_DLLS=ON
   cmake --build build
   ```
   Sem `-DSH_BUILD_MAP_DLLS=ON`, só a área inicial fica disponível.

## Controles e configurações

| PS1 | Tecla | No jogo |
|---|---|---|
| X | C | Ação / atirar |
| Círculo | V | Lanterna |
| Triângulo | Z | Mapa |
| Quadrado | X | Correr |
| L1 / R1 | A / D | Passo lateral |
| L2 / R2 | Shift direito / Shift esquerdo | Olhar / mirar |
| Direcional | Setas | Andar |
| Start / Select | Enter / Espaço | Pausa / inventário |

- **R:** recarregar.
- **F6 / F8:** salvamento e carregamento rápidos.
- **F9:** troca o estilo de câmera.
- **F10:** menu rápido de opções (gráficos, HUD e áudio, trapaças e depuração).
- **Remapear:** no launcher, em **Controls**.
- **Mods:** o **Mod Manager** do launcher extrai o `.bin`, converte texturas para PNG e gerencia pacotes de texturas. Arquivos substitutos vão em `gamedata/load/`.

## Problemas conhecidos

- Os builds de Linux e macOS ainda têm problemas.
- Pode haver falhas visuais em alguns sistemas. Teste outra opção de `renderer=` na configuração: `d3d11`, `vulkan` ou `warp`.
- Ao recompilar, feche o jogo antes: o linker não sobrescreve o `SilentHillPC.exe` em uso.

## Fontes

- [README › Known Issues, Short Instructions, Controls, Building e Game Files / Modding](https://github.com/SlickAmogus/silent-hill-decomp/tree/pc-port#readme)
- [README-linux.txt, dentro do pacote Linux](https://github.com/SlickAmogus/silent-hill-decomp/releases)
- [Releases (crossplatform-beta)](https://github.com/SlickAmogus/silent-hill-decomp/releases)

<!-- verificado: 2026-10-15 -->
