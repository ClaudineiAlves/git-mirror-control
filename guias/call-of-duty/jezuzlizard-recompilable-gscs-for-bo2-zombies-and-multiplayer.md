# Call of Duty: Black Ops II · Recompilable GSCs (PC)

Repositório: https://github.com/JezuzLizard/Recompilable-gscs-for-BO2-zombies-and-multiplayer · Espelho: https://github.com/alves-r/mirror-jezuzlizard-recompilable-gscs-for-bo2-zombies-and-multiplayer

> **Projeto movido.** O README aponta para o repositório novo, https://github.com/plutoniummod/t6-scripts, atualizado pela última vez em 13/08/2025. O novo não tem README nem releases, só as pastas `MP` e `ZM` com os scripts.

Scripts GSC do Black Ops II (multiplayer e zumbis), decompilados e corrigidos para poderem ser recompilados. São feitos principalmente para o cliente Plutonium T6; em outros clientes, o uso é por sua conta e risco.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Não (são scripts GSC, sem releases) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Black Ops II de PC e um cliente que carregue os scripts, como o Plutonium T6, que fica fora deste repositório. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Não documentado no repositório |
| Windows | Não documentado no repositório |
| Estado | Movido. O repositório antigo está parado desde 2023. |
| Dificuldade | Difícil (toolchain manual) |

O repositório é voltado a quem quer conferir e corrigir scripts. Como instalar os scripts no jogo não está documentado. O README também aponta pastas externas com dumps de scripts e do jogo; este guia não as reproduz.

## Arch Linux

Não documentado no repositório.

## Windows

Não documentado no repositório. Para quem quer contribuir, os guias do repositório mostram como trabalhar:
- **`CHECKING_GUIDE.md`:** usa o decompilador Cerberus (https://github.com/Scobalula/Cerberus-Repo) para comparar scripts e um editor com destaque de GSC, como o VS Code com a extensão `atrX.vscode-codscript`.
- **`debugging_guide.md`:** explica os erros comuns de cada decompilador.
- **`compiler limitations.md`:** lista o que o compilador não aceita, como `foreach` aninhado, `continue` em laços e mais de duas condições com OU num mesmo `if`.

## Fontes

- [README](https://github.com/JezuzLizard/Recompilable-gscs-for-BO2-zombies-and-multiplayer#readme)
- [CHECKING_GUIDE.md](https://github.com/JezuzLizard/Recompilable-gscs-for-BO2-zombies-and-multiplayer/blob/master/CHECKING_GUIDE.md)
- [compiler limitations.md](https://github.com/JezuzLizard/Recompilable-gscs-for-BO2-zombies-and-multiplayer/blob/master/compiler%20limitations.md)
- [Repositório novo: plutoniummod/t6-scripts](https://github.com/plutoniummod/t6-scripts)

<!-- verificado: 2026-10-15 -->
