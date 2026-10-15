# Resident Evil – Code: Veronica X · recvx-decomp (PS2)

Repositório: https://github.com/AshfordFamily/recvx-decomp · Espelho: https://github.com/alves-r/mirror-ashfordfamily-recvx-decomp

Decompilação concluída do Code: Veronica X de PS2. Recompila o executável do jogo e pode remontar a ISO com ele, para rodar num emulador de PS2.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera o ELF do jogo e, opcionalmente, a ISO `RECVX_NEW.iso`) |
| Precisa de emulador | Sim: PCSX2 no Linux e no Windows ([guia](../recomp-e-emulacao/pcsx2-pcsx2.md)) |
| Você precisa fornecer | O arquivo `SLUS_201.84`, de dentro do disco americano, em `config/`. Para remontar a ISO, o dump do DVD em `iso/`. Também os arquivos do SDK oficial da Sony para PS2, versões 2.0.0 e 3.0.3, nos caminhos do `compile_config.json`. ⚠️ Você indicou que não consegue dumpar PS2. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Concluído: motor, gameplay, gráficos, IA dos inimigos e a biblioteca CRI ADXT estão decompilados. |
| Dificuldade | Difícil (toolchain manual) |

## Arch Linux

1. Instale o básico: `sudo pacman -S --needed git python python-pip`
2. Clone com submódulos: `git clone --recursive https://github.com/AshfordFamily/recvx-decomp.git && cd recvx-decomp`
3. Coloque o `SLUS_201.84` em `config/` e os arquivos do SDK nos caminhos do `compile_config.json`.
4. Instale as dependências Python. O README usa `pip install -r config/requirements.txt`; no Arch, faça isso num ambiente virtual (sugestão):
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r config/requirements.txt
   ```
   Outra opção é abrir o repositório como dev container (Docker ou Podman), como o README descreve.
5. Prepare o projeto uma vez: `python compile.py --setup`. Isso cria `objdiff.json` e a pasta `config/asm`.
6. Compile: `python compile.py`. No Linux, o compilador `mwccps2.exe` roda pelo wibo. Se o script não achar o wibo, ele mostra como instalar.
7. Para jogar o resultado, remonte a ISO:
   ```bash
   python mkiso.py -m extract --iso iso/RE_CVX.iso
   python mkiso.py -m insert
   ```
8. Abra o `RECVX_NEW.iso` no PCSX2.

## Windows

1. Instale o Python (python.org, marcando **Add python.exe to PATH**) e o Git.
2. Siga os passos 2 a 8 da seção Arch Linux no terminal, com `pip install -r config/requirements.txt` direto (sem ambiente virtual). No Windows, o `mwccps2.exe` roda sem o wibo.

## Fontes

- [README › About e Building](https://github.com/AshfordFamily/recvx-decomp#readme)

<!-- verificado: 2026-10-15 -->
