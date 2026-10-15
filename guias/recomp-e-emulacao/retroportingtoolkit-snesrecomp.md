# Super Nintendo · SNESRecomp (SNES)

Repositório: https://github.com/RetroPortingToolKit/snesrecomp · Espelho: https://github.com/alves-r/mirror-retroportingtoolkit-snesrecomp

Ecossistema de recompilação estática de jogos de Super Nintendo. Transforma uma ROM num projeto em C, que depois vira um port nativo com trabalho específico para cada jogo. Os ports prontos ficam em repositórios próprios.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim, só Windows: a CLI que gera projetos (v0.3.0-alpha, de 14/10/2026: `snesrecomp-cli-windows-x86_64.zip`, com `SHA256SUMS.txt`). Não é um jogo. |
| Precisa de emulador | Não |
| Você precisa fornecer | Uma ROM de SNES sua (`.sfc` ou `.smc`). ⚠️ Você indicou que não consegue dumpar SNES. |
| Arch Linux | Nativo (pelo código-fonte) |
| Windows | Nativo |
| Estado | Alpha. Ports publicados: Super Mario World ([guia](../mario/mstan-supermarioworldrecomp.md)), Zelda: A Link to the Past e Mega Man X. |
| Dificuldade | Difícil (toolchain manual) |

> Projeto de um único autor, com executável não assinado. Baixe só pela página de Releases, confira com o `SHA256SUMS.txt` e passe o arquivo no VirusTotal.

O projeto gerado compila, mas ainda não é um port jogável. O trabalho específico do jogo começa em `src/game_rtl.c`.

## Arch Linux

Não há CLI pronta para Linux. O caminho é o código-fonte:

1. Instale Git, Python 3, CMake, Ninja e um compilador C (sugestão): `sudo pacman -S --needed git python cmake ninja base-devel`
2. Clone: `git clone --recursive https://github.com/RetroPortingToolKit/snesrecomp.git && cd snesrecomp`
3. Gere um projeto a partir da sua ROM: `sh tools/new_project/setup_project.sh ~/roms/jogo.sfc --dir ~/src`. O script faz perguntas (título, jogadores, netplay, launcher etc.), todas com resposta padrão.
4. No projeto gerado, compile com o `build.sh`.

Para gerar a própria CLI, é preciso Python 3.9+, Rust 1.85+ e PyInstaller 6.21.0. Rode `python tools/build_cli.py release`, e o zip sai em `dist/`.

## Windows

1. Baixe `snesrecomp-cli-windows-x86_64.zip` e `SHA256SUMS.txt` em https://github.com/RetroPortingToolKit/snesrecomp/releases.
2. Confira o hash no PowerShell: `Get-FileHash .\snesrecomp-cli-windows-x86_64.zip` e compare com o `SHA256SUMS.txt`.
3. Extraia o arquivo inteiro numa pasta e, no PowerShell, rode:
   ```powershell
   .\snesrecomp.exe build --rom "C:\Jogos\jogo.sfc" --output "C:\Projetos\MeuJogoRecomp"
   ```
4. Instale CMake, Ninja e um compilador C e compile o projeto gerado:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "C:\Projetos\MeuJogoRecomp\build.ps1"
   ```

Pelo código-fonte, o comando é `powershell -File tools\new_project\setup_project.ps1 -Rom C:\roms\jogo.sfc -Dir C:\src`. Ele precisa do Git for Windows, do Python 3 e do CMake no `PATH`.

## Fontes

- [README › Games, ROM compatibility, What it is e How to use SNESRecomp](https://github.com/RetroPortingToolKit/snesrecomp#readme)
- [docs/GAME_PROJECT_SETUP.md](https://github.com/RetroPortingToolKit/snesrecomp/blob/main/docs/GAME_PROJECT_SETUP.md)
- [Releases (v0.3.0-alpha)](https://github.com/RetroPortingToolKit/snesrecomp/releases)

<!-- verificado: 2026-10-15 -->
