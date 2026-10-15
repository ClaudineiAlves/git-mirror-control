# God of War III Remastered · gow3_pc (PS4)

Repositório: https://github.com/FelipePrado0/gow3_pc · Espelho: https://github.com/alves-r/mirror-felipeprado0-gow3_pc

Port para Windows e Linux (AppImage experimental) que roda o código x86-64 original do God of War III Remastered direto na CPU. Abertura, menus, cutscenes e gameplay funcionam, mas ainda há falhas por GPU em investigação.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (windows-v2.3.0, de 15/10/2026: `gow3-windows.zip` e `gow3-x86_64.AppImage`, cada um com o seu `.sha256`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Sua cópia do jogo de PS4: a pasta com `eboot.bin`, `sce_module` e `sce_sys`. Testado com CUSA01623 e CUSA01715, versões 01.00 e 01.02. Se a atualização foi dumpada à parte, ela é escolhida em **Game → Update folder**. ⚠️ Você não soube dizer se consegue dumpar PS4. |
| Arch Linux | Nativo (AppImage experimental, testado no Arch com RX 7800 XT) |
| Windows | Nativo |
| Estado | Abertura, menus, cutscenes, gameplay, áudio, saves e controle funcionam. Falhas de renderização por GPU, crashes, problemas de áudio e travas de progresso seguem em investigação. |
| Dificuldade | Fácil (baixar e rodar) |

> O `.exe` não é assinado digitalmente. Baixe só pela página de Releases do repositório, confira o `.sha256` e passe o arquivo no VirusTotal.

Requisitos do projeto: CPU de 64 bits com AVX (Intel Sandy Bridge ou AMD FX em diante) e placa de vídeo com Vulkan 1.3 e driver atualizado.

## Arch Linux

O AppImage pede glibc 2.39 ou mais nova, que o Arch já tem.

1. Baixe `gow3-x86_64.AppImage` e `gow3-x86_64.AppImage.sha256` em https://github.com/FelipePrado0/gow3_pc/releases/latest.
2. Confira o download: rode `sha256sum gow3-x86_64.AppImage` e compare com o conteúdo do `.sha256`.
3. Instale o FUSE 2, que os AppImages usam no Arch (sugestão): `sudo pacman -S --needed fuse2`
4. Dê permissão e abra:
   ```bash
   chmod +x gow3-x86_64.AppImage
   ./gow3-x86_64.AppImage
   ```
5. Escolha a pasta do jogo, salve as configurações e clique em **PLAY**.

Saves, configurações, cache de shaders e log ficam em `~/.local/share/gow3`. As configurações do launcher ficam em `~/.config/gow3-launcher`.

O atualizador automático só existe no Windows: no Linux, baixe um AppImage novo para atualizar.

Em **Advanced → Linux** dá para escolher Wayland ou X11 e ligar o GameMode e o MangoHud, se estiverem instalados. **Advanced → Add to Steam** adiciona o jogo na Steam com capa e ícones (feche a Steam antes).

Compilar no Arch não é documentado. O build do README é para Ubuntu 24.04, com um script de dependências que usa `apt`.

## Windows

O projeto pede Windows 10 (versão 1903 ou mais nova) ou Windows 11, de 64 bits.

1. Baixe `gow3-windows.zip` em https://github.com/FelipePrado0/gow3_pc/releases/latest.
2. Extraia numa pasta, por exemplo `C:\Games\gow3-windows`. Não rode de dentro do zip.
3. Abra **`God of War III.exe`**. Se aparecer "O Windows protegeu o computador", clique em **Mais informações → Executar assim mesmo**.
4. Clique em **Choose the game folder**. Na página **Game**, ao lado de **Game folder**, clique em **Browse…** e escolha a pasta que tem o `eboot.bin`.
5. Volte para **Home**. A capa e a versão do jogo aparecem ali. Ajuste as **Quick settings** se quiser: modo de tela, limite de FPS, resolução e taxa de quadros da engine.
6. Clique em **Save** e depois em **PLAY**. A primeira abertura prepara a imagem do jogo e compila shaders, por isso demora mais.

Correção de texturas, pular vídeos com X e 120 FPS já vêm ligados.

**Compilar (opcional):**

1. Instale o Python 3.10 ou mais novo (de python.org, com suporte a Tk). No PowerShell, rode: `python -m pip install pillow iced-x86==1.21.0`
2. Instale o MSYS2: `winget install MSYS2.MSYS2`. No terminal **MSYS2 CLANG64**, instale os pacotes listados em `packaging/windows/README.md`.
3. Ainda no CLANG64, clone e compile:
   ```bash
   git clone --recursive https://github.com/FelipePrado0/gow3_pc
   cd gow3_pc
   bash build.sh
   ```
4. No PowerShell, na pasta do projeto: `python launcher/gow3_launcher_win.py`

## Controles e configurações

O menu do port (trapaças, multiplicadores, imagem, desempenho e overlay) abre com **Insert** no teclado ou **R3 + L2** no controle.

Teclado padrão (troque na página **Game**, seção **Controls**):

| Tecla | Botão |
|---|---|
| W A S D | Analógico esquerdo |
| Setas | Analógico direito (câmera) |
| Espaço / Left Shift / E / Q | X / Círculo / Quadrado / Triângulo |
| 1 e 3 | L1 e R1 |
| R e F | L2 e R2 |
| Z e C | L3 e R3 |
| I, K, J, L | Direcional |
| Enter | Options |
| Tab | Touchpad esquerdo (modo foto) |
| Backspace | Touchpad direito (pausa) |

Em controles sem touchpad (Xbox e outros), **View** abre a pausa e **L1 + View** abre o modo foto.

## Problemas conhecidos

- **Tela preta ao iniciar:** use a release mais recente, que corrige o travamento na abertura.
- **"cannot create ... guest memory (error 1450)"** (Windows): faltou memória virtual. Aumente o arquivo de paginação em `SystemPropertiesAdvanced` → **Desempenho** → **Avançado** → **Memória virtual** (ex.: 16384 MB inicial e 24576 MB máximo) e reinicie.
- **Texturas amarelas, laranjas ou brancas, ou luz errada:** desligue **Performance → GPU data → Deferred GPU readbacks** e reinicie. Isso pode causar engasgos.
- **`GLIBC_2.44 not found`** (Linux): baixe de novo o AppImage, que foi recompilado.
- **Corrupção gráfica no Steam Deck/RADV:** problema conhecido do AppImage 2.2.0.
- **Overlays (RTSS, ReShade)** (Windows): o processo do jogo é `bin\gow3-probe.exe`, não o `God of War III.exe`.

## Fontes

- [README › Download and play, Linux (AppImage, experimental), What works, Keyboard controls e Troubleshooting](https://github.com/FelipePrado0/gow3_pc#readme)
- [README › Building from source](https://github.com/FelipePrado0/gow3_pc#building-from-source)
- [Releases](https://github.com/FelipePrado0/gow3_pc/releases)

<!-- verificado: 2026-10-15 -->
