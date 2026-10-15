# Super Mario World · smw (SNES)

Repositório: https://github.com/snesrev/smw · Espelho: https://github.com/alves-r/mirror-snesrev-smw

Reimplementação do Super Mario World feita por engenharia reversa, do mesmo autor do zelda3. O README diz que dá para jogar do início ao fim.

| Item | Detalhe |
|---|---|
| Tipo | Port / Recomp para compilar |
| Executável pronto | Não, precisa compilar. O README manda compilar; o release v0.1 traz um `smw.exe` sem instruções de uso. |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Super Mario World (EUA), com o nome `smw.sfc`. Ela só é usada para extrair os recursos do jogo e depois não é mais necessária. ⚠️ Você indicou que não consegue dumpar SNES. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Jogável do início ao fim. Inclui vários mods do Lunar Magic. Último push em 22/01/2024. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. Instale as dependências. O BUILDING.md pede `sdl2`, que no Arch é fornecido pelo `sdl2-compat`: `sudo pacman -S --needed git base-devel python sdl2-compat`
2. Clone com os submódulos: `git clone --recursive https://github.com/snesrev/smw && cd smw`
3. Coloque a sua ROM na pasta raiz, com o nome `smw.sfc`.
4. Compile: `make -j$(nproc)`. O `make` também extrai os recursos (`smw_assets.dat`) com o Python.
5. Rode: `./smw`
6. Ajuste as opções no `smw.ini`.

## Windows

Jeito fácil, sem terminal:

1. Instale o Python (python.org) e marque **Add to PATH**.
2. No GitHub, clique em **Code → Download ZIP** e extraia.
3. Coloque a sua ROM dos EUA, com o nome `smw.sfc`, nessa pasta.
4. Baixe o TCC e o SDL2 pelos links do README e extraia os dois na subpasta `third_party`.
5. Dê dois cliques em `extract_assets.bat`. Isso cria `smw_assets.dat`.
6. Dê dois cliques em `run_with_tcc.bat`. Isso compila o `smw.exe` e o abre.
7. Ajuste as opções no `smw.ini` com um editor de texto.

O BUILDING.md também documenta build com MSYS2 (MINGW64, `pacman -S mingw-w64-x86_64-SDL2 make mingw-w64-x86_64-gcc` e depois `make`) e com o Visual Studio 2022 (`smw.sln`, configuração Release).

## Controles e configurações

| SNES | Tecla |
|---|---|
| Direcional | Setas |
| A / B / X / Y | X / Z / S / A |
| L / R | C / V |
| Start / Select | Enter / Shift direito |

| Ação | Tecla |
|---|---|
| Turbo | Tab |
| Pausa (com / sem escurecer) | P / Shift+P |
| Tamanho da janela | Ctrl+↑ / Ctrl+↓ |
| Carregar / salvar / repetir snapshot | F1–F10 / Shift+F1–F10 / Ctrl+F1–F10 |
| Tela cheia | Alt+Enter |

As teclas mudam no `smw.ini`. O mesmo projeto roda Super Mario Bros. e Lost Levels a partir de uma ROM do Super Mario All-Stars (EUA) chamada `smas.sfc` (veja o BUILDING.md).

## Problemas conhecidos

O jogo roda uma versão emulada em paralelo e compara a memória a cada quadro. Se achar diferença, salva um snapshot em `saves/` e mostra uma contagem na tela. O autor pede que esses snapshots sejam enviados no Discord.

## Fontes

- [README › About, Building e Usage and controls](https://github.com/snesrev/smw#readme)
- [BUILDING.md](https://github.com/snesrev/smw/blob/main/BUILDING.md)
- [Releases](https://github.com/snesrev/smw/releases)

<!-- verificado: 2026-10-15 -->
