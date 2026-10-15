# Call of Duty (jogos antigos) · OpenAssetTools (PC)

Repositório: https://github.com/Laupetin/OpenAssetTools · Espelho: https://github.com/alves-r/mirror-laupetin-openassettools

Ferramentas de mod de código aberto para os Call of Duty antigos de PC: CoD4, MW2, MW3, World at War, Black Ops, Black Ops II e 007: Quantum of Solace. O **Unlinker** extrai recursos dos fastfiles (`.ff`), e o **Linker** monta fastfiles novos.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim (v0.33.0, de 31/08/2026: `oat-linux.tar.gz` e `oat-windows.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Os arquivos de um dos jogos suportados de PC (IW3, IW4, IW5, QOS, T4, T5 ou T6). ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em andamento. Só parte dos recursos de mod funciona, e o progresso varia por jogo. |
| Dificuldade | Fácil (baixar e rodar) |

O OAT pode ficar em qualquer pasta. O autor recomenda **não** colocá-lo na pasta do jogo, para não misturar os arquivos.

## Arch Linux

1. Baixe `oat-linux.tar.gz` em https://github.com/Laupetin/OpenAssetTools/releases e extraia numa pasta própria: `tar -xzf oat-linux.tar.gz`
2. Use as ferramentas pelo terminal, seguindo o guia "Getting started" da documentação (https://openassettools.dev/guide/getting-started.html).

**Compilar, opcional:** o build é de 32 bits. Precisa do g++ 13 ou mais novo e do suporte multilib, que está desligado na sua máquina.
1. Clone com Git, não pelo zip.
2. Rode `./generate.sh`.
3. Rode `make`, ou os scripts `./scripts/make-release.sh` ou `./scripts/make-debug.sh`.
4. Os binários ficam em `build/bin/Release_x86`.

## Windows

1. Baixe `oat-windows.zip` em https://github.com/Laupetin/OpenAssetTools/releases e extraia numa pasta própria.
2. Use as ferramentas seguindo o guia "Getting started" da documentação. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

**Compilar, opcional:** precisa do Visual Studio 2026. Rode `generate.bat`, abra `build\OpenAssetTools.sln` e compile. Os binários ficam em `build/bin/Release_x86`.

## Fontes

- [README › Tools, Using the tools e Building OAT](https://github.com/Laupetin/OpenAssetTools#readme)
- [docs/SupportedAssetTypes.md](https://github.com/Laupetin/OpenAssetTools/blob/main/docs/SupportedAssetTypes.md)
- [Releases (v0.33.0)](https://github.com/Laupetin/OpenAssetTools/releases)

<!-- verificado: 2026-10-15 -->
