# Grand Theft Auto: San Andreas · CLEO 5 (PC)

Repositório: https://github.com/cleolibrary/CLEO5 · Espelho: https://github.com/alves-r/mirror-cleolibrary-cleo5

Biblioteca que permite ao GTA San Andreas rodar "scripts CLEO", milhares de mods feitos por fãs que mudam ou ampliam o jogo. A versão 5 é a continuação do CLEO 4.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (v5.4.0, de 16/03/2026: `SA.CLEO-v5.4.0+Silent_ASI_Loader.zip`, `SA.CLEO-v5.4.0+Ultimate_ASI_Loader.zip`, `SA.CLEO-v5.4.0.zip` e o SDK; há também uma prévia de 13/10/2026) |
| Precisa de emulador | Não |
| Você precisa fornecer | O GTA San Andreas para Windows (PC). ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton ou Wine (não documentado) |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

Não documentado no repositório. O CLEO é carregado por um ASI Loader, que substitui o `vorbisFile.dll` do jogo. No Proton ou no Wine, esse arquivo precisa ser carregado como nativo (sugestão, não oficial):

1. Instale o CLEO na pasta do jogo, como na seção Windows.
2. Se o jogo estiver na Steam, coloque nas **Opções de inicialização**: `WINEDLLOVERRIDES="vorbisFile=n,b" %command%`.

## Windows

1. Escolha o pacote:
   - não tem ASI Loader ou não sabe se tem: **CLEO with Silent's ASI Loader**;
   - prefere o Ultimate ASI Loader: **CLEO with Ultimate ASI Loader**;
   - já tem um ASI Loader: o pacote **só com o CLEO 5**.
2. Baixe em https://github.com/cleolibrary/CLEO5/releases.
3. Faça backup do `vorbisFile.dll` do jogo, porque o ASI Loader o substitui.
4. Extraia o zip na pasta do GTA San Andreas.
5. Se a instalação deu certo, o texto **CLEO** aparece no canto inferior esquerdo do menu principal.

**Compilar, opcional:**
1. Instale o Visual Studio 2022 ou 2026 com **Desktop development with C++** (toolset v143) e clone com submódulos: `git clone --recursive https://github.com/cleolibrary/CLEO5.git`
2. Gere o projeto com `project_utils\generate-project-2022.bat` (ou `-2026.bat`).
3. Compile a configuração Release (Win32). Os arquivos saem em `.output/Release/`.

## Controles e configurações

- **Scripts:** os scripts CLEO (`.cs`) são feitos por fãs e não têm suporte dos autores da biblioteca.
- **Modo de compatibilidade:** se um script antigo falhar, renomeie a extensão para `.cs4` (comportamento do CLEO 4) ou `.cs3` (CLEO 3).
- **Plugins opcionais:** ficam em `cleo\cleo_plugins\`. Exemplos: áudio, arquivos `.ini`, entrada de teclado e mouse, texto e memória. Alguns scripts precisam deles.

## Fontes

- [README › Installation, CLEO Scripts, CLEO Plugins, Compatibility Mode e Building from Source](https://github.com/cleolibrary/CLEO5#readme)
- [Releases (v5.4.0)](https://github.com/cleolibrary/CLEO5/releases)

<!-- verificado: 2026-10-15 -->
