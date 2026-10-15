# Resident Evil (protótipo) · residentevilgbc (Game Boy Color)

Repositório: https://github.com/ecruells/residentevilgbc · Espelho: https://github.com/alves-r/mirror-ecruells-residentevilgbc

Desmontagem completa do Resident Evil de Game Boy Color, que nunca foi lançado (protótipo "Cart 1"). Ela monta a ROM `REGBC Cart 1.gbc` (MD5 `fd91d5d69c43f2f0406b3626d625b6e6`) a partir do repositório.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar |
| Precisa de emulador | Sim: mGBA, que também roda Game Boy Color, no Linux (oficial `mgba-qt`) e no Windows (sugestão) |
| Você precisa fornecer | Nada: o repositório traz todo o necessário para montar a ROM. Você indicou que não consegue dumpar Game Boy Color, mas aqui isso não faz falta. |
| Arch Linux | Não documentado no repositório |
| Windows | Não documentado no repositório |
| Estado | Parado desde 2020. |
| Dificuldade | Média (compilar com script) |

O README não tem instruções de build. O `Makefile` do repositório usa o RGBDS (`rgbasm`, `rgblink` e `rgbfix`) e um script Python com a biblioteca Pillow.

## Arch Linux

Passos deduzidos do `Makefile` (sugestão, não documentados):

1. Instale: `sudo pacman -S --needed git make rgbds python python-pillow`
2. Clone e compile: `git clone https://github.com/ecruells/residentevilgbc && cd residentevilgbc && make`
3. Se der certo, sai o `resevil.gbc`. Abra num emulador (sugestão: `sudo pacman -S mgba-qt`).

O código é de 2020, e o RGBDS atual (1.0.x) pode não aceitar a sintaxe antiga. Nesse caso, seria preciso uma versão antiga do RGBDS, que o repositório não especifica.

## Windows

Não documentado no repositório. Pelo WSL (`wsl --install -d Ubuntu`), dá para tentar os mesmos passos da seção Arch Linux, instalando `make`, `python3-pil` e o RGBDS (sugestão).

## Fontes

- [README](https://github.com/ecruells/residentevilgbc#readme)
- [Makefile](https://github.com/ecruells/residentevilgbc/blob/master/Makefile)

<!-- verificado: 2026-10-15 -->
