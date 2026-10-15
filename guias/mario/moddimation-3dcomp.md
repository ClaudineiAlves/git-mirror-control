# Super Mario 3D World + Bowser's Fury (demo de quiosque) · 3dcomp (Switch)

Repositório: https://github.com/Moddimation/3dcomp · Espelho: https://github.com/alves-r/mirror-moddimation-3dcomp

Decompilação da demo de quiosque de Super Mario 3D World + Bowser's Fury. O README avisa que ela **não produz um jogo jogável**. Este repositório é um fork de LDAsuku/3dcomp.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Não se aplica. O jogo original roda no Switch; o README não indica emulador. |
| Você precisa fornecer | O executável `main` (NSO) original da demo de quiosque 1.0, tirado do ExeFS. ⚠️ Você indicou que não consegue dumpar Switch. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Em andamento; último push em 03/04/2025. |
| Dificuldade | Difícil (toolchain manual) |

**Como jogar o jogo, como alternativa:** o README só cita o Switch. Não há port para PC conhecido.

## Arch Linux

1. Instale as dependências. O README cita os nomes do Ubuntu; a conversão é sugestão:
   `sudo pacman -S --needed git python python-pip ninja cmake ccache xdelta3 clang openssl rustup`
2. Instale a `libncurses5`, que o próprio README indica no AUR para distros baseadas em Arch: `yay -S ncurses5-compat-libs`
3. Prepare o Rust: `rustup default stable`
4. Clone e baixe os submódulos:
   ```bash
   git clone https://github.com/Moddimation/3dcomp.git && cd 3dcomp
   git submodule update --init --recursive
   ```
5. Instale os módulos Python num ambiente virtual:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install capstone colorama cxxfilt pyelftools watchdog python-Levenshtein toml
   ```
6. Prepare o projeto: `tools/setup.py /caminho/para/main.nso`. Ele baixa o Clang 8.0.0 do site do LLVM e cria `build/`.
7. Compile com `tools/build.py` e confira com `tools/check`.

## Windows

O README recomenda o WSL, com Ubuntu 22.04:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu-22.04` e reinicie.
2. No Ubuntu, instale as dependências: `sudo apt install python3 ninja-build cmake ccache xdelta3 clang libssl-dev libncurses5`
3. Instale o Rust pelas instruções de rust-lang.org e os módulos Python do passo 5 da seção Arch Linux.
4. Clone **dentro do WSL** e siga os passos 4 a 7 da seção Arch Linux.

## Fontes

- [README › Building](https://github.com/Moddimation/3dcomp#building)

<!-- verificado: 2026-10-15 -->
