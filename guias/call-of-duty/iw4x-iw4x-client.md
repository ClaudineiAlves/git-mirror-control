# Call of Duty: Modern Warfare 2 (2009) · IW4x Client (PC)

Repositório: https://github.com/iw4x/iw4x-client · Espelho: https://github.com/alves-r/mirror-iw4x-iw4x-client

Cliente multiplayer da comunidade para o Modern Warfare 2 de 2009, com servidores dedicados mantidos pelos jogadores. É distribuído pelo IW4x Launcher.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (r5167, de 13/10/2026: `iw4x.dll`), instalado e atualizado pelo [IW4x Launcher](iw4x-launcher.md) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Modern Warfare 2 (2009) instalado pela Steam. Cópias da Microsoft Store **não são compatíveis**. Também é preciso o pacote IW4x Rawfiles. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton (o launcher roda o jogo pelo Proton) |
| Windows | Nativo |
| Estado | Ativo, com versões frequentes |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

Use o [IW4x Launcher](iw4x-launcher.md), que tem versão nativa para Linux e abre o jogo pelo Proton.

## Windows

1. O jeito recomendado é o [IW4x Launcher](iw4x-launcher.md), que instala e atualiza o cliente.
2. Para usar o `iw4x.dll` sem o launcher, o MW2 precisa estar instalado com o IW4x Rawfiles (https://github.com/iw4x/iw4x-rawfiles).

**Compilar, opcional:**
1. Clone o repositório. O zip do GitHub não funciona: `git clone https://github.com/iw4x/iw4x-client.git`
2. Rode `generate.bat`, que baixa os submódulos e gera a solução do Visual Studio.
3. Abra e compile `build\iw4x.sln` no Visual Studio.

Para depurar, o README sugere apontar a saída do projeto para a pasta do MW2 e o comando de depuração para o `iw4x.exe`.

## Fontes

- [README › IW4x: Client e Compiling from Source](https://github.com/iw4x/iw4x-client#readme)
- [Releases (r5167)](https://github.com/iw4x/iw4x-client/releases)

<!-- verificado: 2026-10-15 -->
