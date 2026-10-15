# Pokémon Yellow · pokeyellow (Game Boy)

Repositório: https://github.com/pret/pokeyellow · Espelho: https://github.com/alves-r/mirror-pret-pokeyellow

Desmontagem completa do Pokémon Yellow. Ela monta a ROM só com o código e os recursos do repositório. Para jogar, a ROM roda num emulador de Game Boy.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar (gera `pokeyellow.gbc`) |
| Precisa de emulador | Sim: mGBA, que também roda Game Boy, no Linux (oficial `mgba-qt`) e no Windows (sugestão) |
| Você precisa fornecer | Nada além das ferramentas: o build não pede ROM base. Você indicou que não consegue dumpar Game Boy, mas aqui isso não faz falta. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Ativo. A ROM gerada bate com a original (SHA-1 no README). |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. Instale as ferramentas, como o INSTALL.md indica para o Arch: `sudo pacman -S make gcc git rgbds`
2. O projeto pede o **rgbds 1.0.3**, e o pacote do Arch estava na 1.0.2 em 15/10/2026. Se o `make` falhar por causa da versão:
   1. Baixe ou compile o rgbds 1.0.3 (instruções em https://rgbds.gbdev.io/install).
   2. Coloque os arquivos em `pokeyellow/rgbds-1.0.3/`.
   3. Rode `make RGBDS=rgbds-1.0.3/`.
3. Clone: `git clone https://github.com/pret/pokeyellow && cd pokeyellow`
4. Compile: `make`. Sai o `pokeyellow.gbc`.
5. Abra a ROM num emulador (sugestão: `sudo pacman -S mgba-qt`).

## Windows

O INSTALL.md manda usar o WSL e seguir os passos de Linux:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, atualize o sistema e instale o básico:
   ```bash
   sudo apt-get update && sudo apt-get upgrade
   sudo apt-get install make gcc git
   ```
3. Compile o rgbds 1.0.3 pelas instruções de https://rgbds.gbdev.io/install ("building from source").
4. Trabalhe numa pasta do Windows, ex.: `cd /mnt/c/Users/<usuário>/Desktop`
5. Clone e compile: `git clone https://github.com/pret/pokeyellow && cd pokeyellow && make`
6. Abra a ROM gerada no mGBA para Windows (sugestão).

No Windows 8 ou mais antigo, o INSTALL.md usa o Cygwin com os pacotes `make`, `git` e `gcc-core`.

## Fontes

- [README](https://github.com/pret/pokeyellow#readme)
- [INSTALL.md](https://github.com/pret/pokeyellow/blob/master/INSTALL.md)

<!-- verificado: 2026-10-15 -->
