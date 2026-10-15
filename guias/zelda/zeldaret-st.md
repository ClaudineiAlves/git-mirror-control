# The Legend of Zelda: Spirit Tracks · st (DS)

Repositório: https://github.com/zeldaret/st · Espelho: https://github.com/alves-r/mirror-zeldaret-st

Decompilação em andamento do Spirit Tracks, feita à mão, que gera a ROM do jogo a partir da sua cópia. Para jogar, a ROM roda num emulador de DS.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar |
| Precisa de emulador | Sim. No Linux: melonDS (AUR `melonds`) ou DeSmuME (oficial `desmume`). No Windows: melonDS. (Sugestão.) |
| Você precisa fornecer | Uma ROM decriptada em `extract/`, com o nome certo: `baserom_st_eur.nds` (padrão), `baserom_st_eur_rev1.nds`, `baserom_st_usa.nds` ou `baserom_st_jp.nds`. Os SHA-1 estão no `extract/README.md`. Para uma ROM idêntica à original (opcional), também a BIOS ARM7 (`arm7_bios.bin`) do seu próprio DS. ⚠️ Você indicou que não consegue dumpar DS. |
| Arch Linux | Nativo |
| Windows | Nativo (recomendado pelo projeto) |
| Estado | Em andamento. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O projeto pede Python 3.11+, pip, GCC 9+ e Ninja. No Linux ele usa o Wibo por padrão; para usar o Wine, rode o `configure.py` com `-w <caminho/do/wine>`.

1. Instale as ferramentas: `sudo pacman -S --needed git python python-pip gcc ninja pre-commit`
2. Clone: `git clone https://github.com/zeldaret/st.git && cd st`
3. Instale as dependências Python num ambiente virtual:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   python -m pip install -r tools/requirements.txt
   pre-commit install
   ```
4. Coloque a sua ROM em `extract/`, com o nome da tabela (ex.: `baserom_st_eur.nds`).
5. Configure: `python tools/configure.py`. Para uma versão específica: `python tools/configure.py -v eur`.
6. Compile: `ninja`
7. Abra a ROM gerada num emulador de DS (sugestão: `yay -S melonds`).

## Windows

O projeto recomenda o Windows.

1. Instale o Python 3.11+ (python.org, marcando **Add python.exe to PATH**), um GCC 9+, o Ninja (`pip install ninja`) e o Git.
2. No PowerShell, clone o repositório e instale as dependências: `python -m pip install -r tools/requirements.txt` e `pre-commit install`.
3. Coloque a ROM em `extract\`, rode `python tools/configure.py` e depois `ninja`.
4. Abra a ROM gerada no melonDS (sugestão).

## Fontes

- [README](https://github.com/zeldaret/st#readme)
- [INSTALL.md](https://github.com/zeldaret/st/blob/main/INSTALL.md)
- [extract/README.md](https://github.com/zeldaret/st/blob/main/extract/README.md)

<!-- verificado: 2026-10-15 -->
