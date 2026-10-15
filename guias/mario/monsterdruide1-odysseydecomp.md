# Super Mario Odyssey · OdysseyDecomp (Switch)

Repositório: https://github.com/MonsterDruide1/OdysseyDecomp · Espelho: https://github.com/alves-r/mirror-monsterdruide1-odysseydecomp

Decompilação em andamento do Super Mario Odyssey 1.0.0. O próprio README avisa que ela **não produz um jogo jogável**.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Não se aplica. O jogo original roda no Switch; o README não indica emulador. |
| Você precisa fornecer | O executável `main` (NSO) original da versão 1.0, tirado do ExeFS. ⚠️ Você indicou que não consegue dumpar Switch. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Em andamento; o progresso aparece no decomp.dev. |
| Dificuldade | Difícil (toolchain manual) |

**Como jogar o jogo, como alternativa:** o README só cita o Switch. Não há port para PC conhecido.

## Arch Linux

1. Instale as dependências. O README cita os nomes do Ubuntu; a conversão é sugestão:
   `sudo pacman -S --needed git python python-pip ninja cmake ccache openssl llvm rustup`
2. Prepare o Rust: `rustup default stable`
3. Clone e baixe os submódulos:
   ```bash
   git clone https://github.com/MonsterDruide1/OdysseyDecomp.git && cd OdysseyDecomp
   git submodule update --init --recursive
   ```
4. Instale os módulos Python num ambiente virtual (o Arch não deixa o `pip` instalar no sistema):
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install capstone colorama cxxfilt pyelftools watchdog python-Levenshtein toml
   ```
5. Prepare o projeto com o seu NSO: `tools/setup.py /caminho/para/main.nso`. Ele instala o verificador, baixa o clang e o ld.lld usados pelo projeto e cria a pasta `build/`.
6. Compile: `tools/build.py` (`--clean` limpa o build e `--verbose` mostra detalhes).
7. Confira o resultado: `tools/check`

O README também documenta um Dev Container do VS Code e o caminho com Nix (`flake.nix` com `direnv`).

## Windows

O README recomenda fortemente o WSL, com Ubuntu 24.04:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu-24.04` e reinicie.
2. No Ubuntu, instale as dependências: `sudo apt install python3 ninja-build cmake ccache libssl-dev llvm`
3. Instale o Rust pelas instruções de rust-lang.org e os módulos Python do passo 4 da seção Arch Linux.
4. Clone **dentro do WSL**, não no lado do Windows (por desempenho), e siga os passos 3 a 7 da seção Arch Linux.

## Fontes

- [README › Building (Set up dependencies, Set up the project e Build)](https://github.com/MonsterDruide1/OdysseyDecomp#building)

<!-- verificado: 2026-10-15 -->
