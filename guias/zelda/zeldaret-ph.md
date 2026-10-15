# The Legend of Zelda: Phantom Hourglass · ph (DS)

Repositório: https://github.com/zeldaret/ph · Espelho: https://github.com/alves-r/mirror-zeldaret-ph

Decompilação em andamento do Phantom Hourglass, feita à mão, que gera a ROM do jogo a partir da sua cópia. Para jogar, a ROM roda num emulador de DS.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar |
| Precisa de emulador | Sim. No Linux: melonDS (AUR `melonds`) ou DeSmuME (oficial `desmume`). No Windows: melonDS. (Sugestão.) |
| Você precisa fornecer | Uma ROM decriptada em `extract/`: `baserom_ph_eur.nds` (SHA-1 `02be55db55cf254bd064d2b3eb368b92a5b4156d`) ou `baserom_ph_usa.nds` (`4c8f52dd719918bbcd46e73a8bae8628139c1b85`). Para uma ROM idêntica à original (opcional), também a BIOS ARM7 (`arm7_bios.bin`) do seu próprio DS. ⚠️ Você indicou que não consegue dumpar DS. |
| Arch Linux | Nativo |
| Windows | Nativo (recomendado pelo projeto) |
| Estado | Em andamento; versões europeia e americana. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O projeto pede Python 3.11+, pip, GCC 9+ e Ninja. No Linux ele usa o Wibo por padrão (ou o Wine, com `-w <caminho/do/wine>`).

1. Instale as ferramentas: `sudo pacman -S --needed git python python-pip gcc ninja pre-commit`
2. Clone: `git clone https://github.com/zeldaret/ph.git && cd ph`
3. Instale as dependências Python num ambiente virtual:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   python -m pip install -r tools/requirements.txt
   pre-commit install
   ```
4. Coloque a sua ROM em `extract/` com o nome da tabela.
5. Configure para a sua versão: `python tools/configure.py eur` (ou `usa`).
6. Compile: `ninja`
7. Abra a ROM gerada num emulador de DS (sugestão: `yay -S melonds`).

## Windows

O projeto recomenda o Windows.

1. Instale o Python 3.11+ (python.org, marcando **Add python.exe to PATH**), um GCC 9+, o Ninja (`pip install ninja`) e o Git.
2. No PowerShell, clone o repositório e instale as dependências: `python -m pip install -r tools/requirements.txt` e `pre-commit install`.
3. Coloque a ROM em `extract\`, rode `python tools/configure.py eur` e depois `ninja`.
4. Abra a ROM gerada no melonDS (sugestão).

## Fontes

- [README](https://github.com/zeldaret/ph#readme)
- [INSTALL.md](https://github.com/zeldaret/ph/blob/main/INSTALL.md)
- [extract/README.md](https://github.com/zeldaret/ph/blob/main/extract/README.md)

<!-- verificado: 2026-10-15 -->
