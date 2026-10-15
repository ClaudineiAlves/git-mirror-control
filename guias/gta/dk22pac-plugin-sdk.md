# GTA III, Vice City e San Andreas · plugin-sdk (PC)

Repositório: https://github.com/DK22Pac/plugin-sdk · Espelho: https://github.com/alves-r/mirror-dk22pac-plugin-sdk

Kit de desenvolvimento para criar plugins ASI e CLEO para o GTA San Andreas, o Vice City e o GTA III. O repositório também traz pastas para o GTA IV e as versões "Unreal" (Definitive Edition).

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Não, é um SDK para programar plugins (sem releases) |
| Precisa de emulador | Não |
| Você precisa fornecer | Ao menos um dos jogos suportados de PC, para testar os plugins. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Não suportado (o SDK depende do Visual Studio no Windows) |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Média (compilar com script) |

> O passo a passo está na wiki do projeto. O `installer-launcher.exe` vem dentro do repositório: passe-o no VirusTotal antes de abrir.

## Arch Linux

Não suportado: a wiki só documenta o uso com o Visual Studio, no Windows.

## Windows

1. Instale o Visual Studio 2022 ou mais novo, com **Desenvolvimento para desktop com C++**, **Common tools for VC++** e o **Windows SDK**.
2. Evite caminhos com espaços: na pasta do projeto, na do SDK, na do CLEO SDK e nas dos jogos.
3. Clone o repositório: `git clone https://github.com/DK22Pac/plugin-sdk.git`. Reserve cerca de 1 GB por jogo suportado.
4. Abra o `installer-launcher.exe` da pasta do SDK. Ele precisa do .NET Framework 4.8.
   1. Ele tenta achar sozinho o SDK e os jogos instalados. Complete os caminhos que faltarem com o botão `...`.
   2. É preciso informar o SDK e pelo menos um jogo.
5. No mesmo programa, gere a solução. O `plugin.sln` aparece na pasta do SDK.
6. Escolha os jogos e as configurações (Release para publicar, Debug para depurar) e clique em **Visual Studio** para compilar as bibliotecas.
7. Siga a página "Creating a new plugin in plugin sdk" da wiki para criar o primeiro plugin.

## Fontes

- [README › How to use plugin-sdk?](https://github.com/DK22Pac/plugin-sdk#readme)
- [Wiki › Installing development environment (IDE)](https://github.com/DK22Pac/plugin-sdk/wiki/Installing-development-environment-(IDE))
- [Wiki › Set up plugin sdk](https://github.com/DK22Pac/plugin-sdk/wiki/Set-up-plugin-sdk)

<!-- verificado: 2026-10-15 -->
