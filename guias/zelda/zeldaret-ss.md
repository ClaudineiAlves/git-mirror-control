# The Legend of Zelda: Skyward Sword · ss (Wii)

Repositório: https://github.com/zeldaret/ss · Espelho: https://github.com/alves-r/mirror-zeldaret-ss

Decompilação em andamento do Skyward Sword de Wii. Não gera nada jogável: o build recria o executável do jogo para conferir se bate com o original.

| Item | Detalhe |
|---|---|
| Tipo | Decomp de pesquisa |
| Executável pronto | Não, precisa compilar (e o resultado não é jogável) |
| Precisa de emulador | Sim, só para jogar o original: Dolphin no Linux (`dolphin-emu`) e no Windows (sugestão) |
| Você precisa fornecer | O jogo `SOUE01` (EUA 1.0, a única versão suportada), extraído pelo Dolphin para `orig/SOUE01/`. Bastam `sys/main.dol` e `files/rels.arc`. ⚠️ Você indicou que não consegue dumpar Wii. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento; só a versão EUA 1.0 é suportada. |
| Dificuldade | Média (compilar com script) |

**Como jogar o jogo, como alternativa:** o Skyward Sword original roda no Dolphin com a sua cópia (sugestão).

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed git python ninja dolphin-emu`
2. Clone: `git clone https://github.com/zeldaret/ss.git && cd ss`
3. No Dolphin:
   1. Clique com o botão direito no jogo e abra **Properties**.
   2. Vá na aba **Filesystem**.
   3. Clique com o botão direito em **Data Partition** e escolha **Extract Entire Partition...**, com destino `orig/SOUE01`.
4. Configure com `python configure.py` e compile com `ninja`.

## Windows

1. Instale o Python (python.org, marcando **Add python.exe to PATH**), o ninja (`pip install ninja`), o Git for Windows e o Dolphin.
2. Clone o repositório.
3. Extraia o jogo pelo Dolphin para `orig\SOUE01`, como no passo 3 da seção Arch Linux.
4. Rode `python configure.py` e depois `ninja`.

## Fontes

- [README › Dependencies e Building](https://github.com/zeldaret/ss#readme)

<!-- verificado: 2026-10-15 -->
