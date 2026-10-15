# The Legend of Zelda: A Link to the Past · zelda3 (SNES)

Repositório: https://github.com/snesrev/zelda3 · Espelho: https://github.com/alves-r/mirror-snesrev-zelda3

Reimplementação em C do A Link to the Past, que roda nativo no PC e lê os recursos da sua ROM. Traz extras opcionais, como widescreen e um renderizador novo.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim, só Windows e antigo (v0.3, de 17/08/2023: `zelda3_v0.3.zip`, com `zelda3.exe`). O código atual é mais novo, e o README manda compilar. |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM dos EUA com o nome `zelda3.sfc` e o SHA-256 `66871d66be19ad2c34c927d6b14cd8eb6fc3181965b6e517cb361f7316009cfb`. ⚠️ Você indicou que não consegue dumpar SNES. |
| Arch Linux | Nativo (compilando) |
| Windows | Nativo |
| Estado | Ativo; a última versão publicada é de 2023. |
| Dificuldade | Fácil (baixar e rodar) |

> Executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

## Arch Linux

1. Instale as dependências. O BUILDING.md pede `sdl2`, que no Arch é fornecido pelo `sdl2-compat`. As bibliotecas Python do `requirements.txt` (Pillow e PyYAML) vêm dos pacotes oficiais (sugestão):
   `sudo pacman -S --needed git base-devel python python-pillow python-yaml sdl2-compat`
2. Clone: `git clone https://github.com/snesrev/zelda3 && cd zelda3`
3. Coloque a sua ROM na pasta, com o nome `zelda3.sfc`.
4. Compile: `make -j$(nproc)`. O `make` também extrai os recursos da ROM para `zelda3_assets.dat`.
5. Rode: `./zelda3`. Para mudar o programa de lugar, leve junto o `zelda3_assets.dat`.
6. Ajuste as opções no `zelda3.ini`.

## Windows

**Jeito fácil, com a versão pronta (v0.3):**

1. Baixe `zelda3_v0.3.zip` em https://github.com/snesrev/zelda3/releases e extraia numa pasta.
2. Coloque a sua ROM nessa pasta, com o nome `zelda3.sfc`.
3. Abra `zelda3.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

**Compilar a versão atual (passos do README):**

1. Instale o Python 3.11 (python.org), marcando **Add to PATH**.
2. No GitHub, clique em **Code → Download ZIP** e extraia.
3. Coloque a ROM dos EUA nessa pasta, com o nome `zelda3.sfc`.
4. Baixe o TCC e o SDL2 pelos links do README e extraia os dois na subpasta `third_party`.
5. Dê dois cliques em `get_python_libs.bat`.
6. Dê dois cliques em `extract_assets.bat`. Isso cria `zelda3_assets.dat`.
7. Dê dois cliques em `run_with_tcc.bat`. Isso compila o `zelda3.exe` e o abre.
8. Ajuste as opções no `zelda3.ini` com um editor de texto.

## Controles e configurações

| SNES | Tecla |
|---|---|
| Direcional | Setas |
| Start / Select | Enter / Shift direito |
| A / B | X / Z |
| X / Y | S / A |
| L / R | C / V |

As teclas mudam no `zelda3.ini`. Atalhos úteis:
- **Alt+Enter:** tela cheia.
- **Ctrl+↑ / Ctrl+↓:** tamanho da janela.
- **Tab:** modo turbo.
- **Shift+F1–F10 / F1–F10:** salva e carrega snapshots.
- **Ctrl+E:** reinicia.
- **P:** pausa.

## Fontes

- [README › Building e Usage and controls](https://github.com/snesrev/zelda3#readme)
- [BUILDING.md](https://github.com/snesrev/zelda3/blob/master/BUILDING.md)
- [Releases (v0.3)](https://github.com/snesrev/zelda3/releases)

<!-- verificado: 2026-10-15 -->
