# Pokémon Crystal · pokecrystal (Game Boy Color)

Repositório: https://github.com/pret/pokecrystal · Espelho: https://github.com/alves-r/mirror-pret-pokecrystal

Desmontagem completa do Pokémon Crystal. Ela monta as ROMs só com o código e os recursos do repositório. Para jogar, a ROM roda num emulador de Game Boy Color.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `pokecrystal.gbc`, versão 1.0, e `pokecrystal11.gbc`, versão 1.1) |
| Precisa de emulador | Sim: mGBA, que também roda Game Boy Color, no Linux (oficial `mgba-qt`) e no Windows (sugestão) |
| Você precisa fornecer | Nada além das ferramentas: o build não pede ROM base. Você indicou que não consegue dumpar Game Boy Color, mas aqui isso não faz falta. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Ativo. As ROMs geradas batem com as originais (SHA-1 no README). |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. Instale as ferramentas, como o INSTALL.md indica para o Arch: `sudo pacman -S make gcc git rgbds`
2. O projeto pede o **rgbds 1.0.4**, e o pacote do Arch estava na 1.0.2 em 15/10/2026. Se o `make` falhar por causa da versão:
   1. Baixe ou compile o rgbds 1.0.4 (instruções em https://rgbds.gbdev.io/install).
   2. Coloque os arquivos em `pokecrystal/rgbds-1.0.4/`.
   3. Rode `make RGBDS=rgbds-1.0.4/`.
3. Clone: `git clone https://github.com/pret/pokecrystal && cd pokecrystal`
4. Compile: `make` gera o `pokecrystal.gbc`, e `make crystal11` gera o `pokecrystal11.gbc`.
5. Abra a ROM num emulador (sugestão: `sudo pacman -S mgba-qt`).

## Windows

O INSTALL.md manda usar o WSL e seguir os passos de Linux:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, atualize o sistema e instale o básico:
   ```bash
   sudo apt-get update && sudo apt-get upgrade
   sudo apt-get install make gcc git
   ```
3. Compile o rgbds 1.0.4 pelas instruções de https://rgbds.gbdev.io/install ("building from source").
4. Trabalhe numa pasta do Windows, ex.: `cd /mnt/c/Users/<usuário>/Desktop`
5. Clone e compile: `git clone https://github.com/pret/pokecrystal && cd pokecrystal && make`
6. Abra a ROM gerada no mGBA para Windows (sugestão).

No Windows 8 ou mais antigo, o INSTALL.md usa o Cygwin com os pacotes `make`, `git` e `gcc-core`.

## Fontes

- [README](https://github.com/pret/pokecrystal#readme)
- [INSTALL.md](https://github.com/pret/pokecrystal/blob/master/INSTALL.md)

<!-- verificado: 2026-10-15 -->
