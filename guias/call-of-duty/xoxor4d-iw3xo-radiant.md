# Call of Duty 4: Modern Warfare · IW3xRadiant (PC)

Repositório: https://github.com/xoxor4d/iw3xo-radiant · Espelho: https://github.com/alves-r/mirror-xoxor4d-iw3xo-radiant

Versão modificada do Radiant, o editor de mapas do Call of Duty 4. Corrige bugs, amplia funções e troca a interface antiga do Windows por uma feita com Dear ImGui.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim (411, de 28/05/2023: `iw3xradiant_411_230528.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Call of Duty 4 de PC com as CoD4 Mod Tools instaladas. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton ou Wine (não documentado) |
| Windows | Nativo |
| Estado | Última versão em 05/2023; há builds noturnos mais novos. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

## Arch Linux

Não documentado no repositório. O editor é um programa de Windows. Um caminho possível é rodá-lo pelo Wine ou pelo Proton, na mesma pasta do jogo (sugestão, não oficial).

## Windows

1. Instale as CoD4 Mod Tools na pasta do jogo.
2. Baixe a versão mais recente em https://github.com/xoxor4d/iw3xo-radiant/releases.
3. Copie o conteúdo para a pasta raiz do CoD4.
4. Abra `bin/IW3xRadiant.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

- **Build noturno:** com a versão normal instalada, troque o `iw3r.dll` da pasta `bin` pelo do build noturno.
- **Opcional:** extraia o `bo3-tool-textures.zip` e coloque os `.iwi` em `bin\IW3xRadiant\images`.

**Compilar, opcional:**
1. Clone o repositório. O zip não traz as dependências.
2. Copie o conteúdo da pasta `assets` para a raiz do CoD4.
3. Rode `update_submodules.bat` e depois `generate-buildfiles_vs22.bat`.
4. Abra `build/iw3xo-radiant.sln`, ajuste os caminhos (ou crie a variável `COD4_ROOT`) e compile.

## Fontes

- [README › Installation e Build / Compile](https://github.com/xoxor4d/iw3xo-radiant#readme)
- [Releases (411)](https://github.com/xoxor4d/iw3xo-radiant/releases)

<!-- verificado: 2026-10-15 -->
