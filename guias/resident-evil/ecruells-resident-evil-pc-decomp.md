# Resident Evil · resident-evil-pc-decomp (PC)

Repositório: https://github.com/ecruells/resident-evil-pc-decomp · Espelho: https://github.com/alves-r/mirror-ecruells-resident-evil-pc-decomp

Decompilação da versão de PC do primeiro Resident Evil (1997), com binários nativos para Windows e Linux. Tem renderizador DirectX 11 ou OpenGL e um modo opcional com o conteúdo do Director's Cut de PS1.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v1.3.0, de 27/09/2026: `residentevil-1.3.0-windows-x86.zip`, `residentevil-1.3.0-linux-x86.tar.gz` e o migrador de arquivos `asset-migrator-1.3.0-windows-x64.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Os arquivos do Resident Evil de PC (a base é a versão GOG dos EUA, o mesmo binário de 1997; a versão japonesa de PC também serve). Para o modo Director's Cut, opcional, a imagem do disco de PS1 em `.bin`/`.cue`. ⚠️ Você não soube dizer se tem os jogos de PC, e indicou que não consegue dumpar PS1. |
| Arch Linux | Nativo (precisa do multilib) |
| Windows | Nativo |
| Estado | Ativo. 1716 das 1717 funções de lógica do jogo já estão implementadas. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

## Arch Linux

O binário de Linux é de 32 bits e precisa de uma distribuição com suporte a 32 bits (multilib) e glibc 2.39 ou mais nova.

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale o driver OpenGL de 32 bits que o pacote pede: `sudo pacman -Syu lib32-mesa`
3. Baixe `residentevil-1.3.0-linux-x86.tar.gz` em https://github.com/ecruells/resident-evil-pc-decomp/releases e extraia: `tar -xzf residentevil-1.3.0-linux-x86.tar.gz`
4. Coloque os arquivos do jogo ao lado do `residentevil.sh`, numa pasta `USA/` (ou `JPN/`, para a versão japonesa).
5. Rode: `cd residentevil-1.3.0-linux-x86 && ./residentevil.sh`
6. O `config.ini` é criado na primeira execução. Os saves ficam na pasta `save/`, ao lado do programa.

O migrador de arquivos publicado é só para Windows. No Linux, o README diz que as mesmas migrações podem ser feitas com os scripts Python do repositório: `tools/port_dc_assets.py`, `tools/bss_to_pak.py` e `tools/str_to_video.py`.

**Compilar, opcional** (README, seção Linux):

1. Com o multilib ligado, instale as dependências pela linha do README para o Arch:
   `sudo pacman -S --needed base-devel cmake lib32-glibc lib32-gcc-libs sdl2 lib32-sdl2 ffmpeg lib32-ffmpeg lib32-mesa`
2. Compile:
   ```bash
   cmake -S . -B build/linux -DCMAKE_BUILD_TYPE=Release
   cmake --build build/linux -j
   ```
3. Rode `./build/linux/residentevil`. Esse binário depende do ffmpeg do sistema. Para levar a outra máquina, gere um pacote com `bash tools/package_linux.sh`.

## Windows

1. Baixe `residentevil-1.3.0-windows-x86.zip` e `asset-migrator-1.3.0-windows-x64.zip` em https://github.com/ecruells/resident-evil-pc-decomp/releases e extraia os dois.
2. Abra o migrador. Na aba **PC Assets**, escolha a pasta da sua instalação (GOG ou CD) ou a imagem do disco, e o destino **USA** ou **Japanese**.
   - Converter os vídeos `Movie/*.avi` para `.mp4` é opcional e exige o `ffmpeg` no `PATH`.
   - A aba **Director's Cut** monta a pasta `DC/` a partir da imagem do disco de PS1 (`.bin`/`.cue`).
3. Deixe as pastas assim, ao lado do `residentevil.exe`:
   ```
   RE1/
     residentevil.exe
     config.ini
     USA/
     JPN/   (opcional)
     DC/    (opcional)
     SAVE/
   ```
4. Abra o `residentevil.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

**Compilar, opcional:** com o Visual Studio 2017 ou mais novo (C++ e MSBuild), rode `build.bat`. O resultado é `bin\Release\residentevil.exe`.

## Controles e configurações

| Tecla | Função |
|---|---|
| Setas ↑ / ↓ | Andar para frente / para trás |
| Setas ← / → | Virar |
| C, Enter ou Espaço | Ação e confirmar (atira enquanto mira) |
| V ou Ctrl | Cancelar; segure andando para correr |
| X | Segure para mirar |
| Z | Inventário |
| A | Opções |
| Esc | Voltar |

- **Controle:** Xbox, DualShock/DualSense e Switch Pro. A = ação, B = cancelar/correr, X/LB/RB/RT = mirar, Y/Start = inventário, LT = correr.
- **`config.ini`:**
  - `[Assets] Version` escolhe `USA` ou `JPN`.
  - `[Assets] Path` muda a pasta dos arquivos.
  - `[Game] Mode=DC` liga o Director's Cut.

## Problemas conhecidos

- **Steam Deck:** adicione o `residentevil.sh` como jogo não Steam, sem passar pelo Steam Linux Runtime. A glibc dele é antiga demais para o build.
- **Diagnóstico:** `RE1_DEBUGLOG=1` grava o log em `re1_debug.log`. Um travamento grava `crash.log` na pasta do programa.

## Fontes

- [README › How to build, Running the game, config.ini, Asset migration, Director's Cut mode e Controls](https://github.com/ecruells/resident-evil-pc-decomp#readme)
- [README-LINUX.txt, dentro do pacote Linux da v1.3.0](https://github.com/ecruells/resident-evil-pc-decomp/releases)
- [docs/LINUX_PORT.md](https://github.com/ecruells/resident-evil-pc-decomp/blob/main/docs/LINUX_PORT.md)

<!-- verificado: 2026-10-15 -->
