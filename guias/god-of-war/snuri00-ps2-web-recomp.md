# God of War II e Gran Turismo 4 · ps2-web-recomp (PS2)

Repositório: https://github.com/snuri00/ps2-web-recomp · Espelho: https://github.com/alves-r/mirror-snuri00-ps2-web-recomp

Ferramenta que transforma a ISO de um jogo de PS2 seu numa página web (WebAssembly e WebGPU) ou num executável nativo. O God of War II joga dos menus ao combate a 60 fps.

| Item | Detalhe |
|---|---|
| Tipo | Port / Recomp para compilar |
| Executável pronto | Não, precisa compilar. Os scripts geram a página e o executável a partir da sua ISO. |
| Precisa de emulador | Não |
| Você precisa fornecer | A imagem de disco (ISO, ou ZIP/7z com a ISO) de um jogo de PS2 seu. Testados: God of War II e Gran Turismo 4 (PAL). ⚠️ Você indicou que não consegue dumpar PS2. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Dois jogos funcionam. Gran Turismo 4 vai do boot às corridas, a 50 fps (PAL). God of War II roda menus, cutscenes e combate a 60 fps. Outros jogos devem parar em chamadas de sistema ainda não implementadas. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O projeto foi testado em Linux x86-64. Reserve uns 300 MB por jogo.

1. Instale as ferramentas. O `sdl2-compat` só é necessário para o executável nativo:
   `sudo pacman -S --needed git cmake ninja clang python 7zip sdl2-compat`
2. Clone: `git clone https://github.com/snuri00/ps2-web-recomp.git && cd ps2-web-recomp`
3. Gere o jogo a partir da sua ISO: `scripts/port.sh gow2 "God of War II.iso"`
   - Na primeira vez, o script instala o Emscripten SDK em `tools/emsdk` e baixa o wgpu-native.
   - Ele traduz o executável, roda o jogo algumas vezes para achar as funções e monta a página em `build/web-gow2` e o executável em `build/native-gow2`.
4. Sirva a página: `python3 scripts/serve.py build/web-gow2 games/gow2/disc.iso` e abra http://localhost:8620/
5. **Navegador:** a página precisa de WebGPU. No Linux, o Chrome e o Chromium vêm com ela desligada.
   1. Instale o Chromium (sugestão): `sudo pacman -S chromium`
   2. Ligue `chrome://flags/#enable-unsafe-webgpu` e `chrome://flags/#enable-vulkan`.
   3. Reinicie o navegador.
6. **Ou jogue numa janela nativa**, sem navegador:
   ```bash
   build/native-gow2/ps2run games/gow2/disc/<ARQUIVO_DE_BOOT> --disc games/gow2/disc.iso --window --memcard gow2.ps2
   ```
   O nome do arquivo de boot vem do `SYSTEM.CNF` do disco, no formato `SLUS_123.45`. Para gerar só o executável nativo, use `scripts/port.sh gow2 "God of War II.iso" --native-only`. `--fullscreen` abre em tela cheia, F11 alterna e `PS2_SCALE=2` ou `3` aumenta a resolução interna.

## Windows

O projeto não documenta build no Windows. Compile no WSL2 e jogue no navegador do Windows:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, instale as ferramentas (nomes do Ubuntu, sugestão):
   `sudo apt update && sudo apt install -y git cmake ninja-build clang python3 7zip`
3. Siga os passos 2 a 4 da seção Arch Linux dentro do Ubuntu.
4. No Windows, abra http://localhost:8620/ no Chrome ou no Edge, que já têm WebGPU no Windows.

## Controles e configurações

| Tecla | Botão |
|---|---|
| Z / X / A / S | X / Círculo / Quadrado / Triângulo |
| Q / W / 1 / 2 | L1 / R1 / L2 / R2 |
| Enter / Backspace | Start / Select |
| Setas | Direcional |
| I, J, K, L | Analógico esquerdo |
| F | Tela cheia |

Controles funcionam pela API de gamepad do navegador, inclusive gatilhos analógicos e vibração (no Chrome e no Edge).

O memory card fica salvo no navegador. **Export card** baixa um arquivo `.ps2` no formato do PCSX2, e **Import card** carrega um de volta.

## Problemas conhecidos

- **Sem WebGPU:** o renderizador por software assume, e fica lento demais para 3D (todos os sistemas).
- **Notebooks com duas GPUs:** às vezes a imagem não aparece. A página tenta os dois adaptadores.
- **Servidor exposto:** qualquer um que alcance o servidor carrega o jogo. Mantenha-o só para você.

## Fontes

- [README › PS2 Web Recomp, A second game e Port a game of your own](https://github.com/snuri00/ps2-web-recomp#readme)
- [README › Browsers, Playing natively, Saves e Hosting](https://github.com/snuri00/ps2-web-recomp#browsers)

<!-- verificado: 2026-10-15 -->
