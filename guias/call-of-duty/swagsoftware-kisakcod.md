# Call of Duty 4: Modern Warfare · KisakCOD (PC)

Repositório: https://github.com/SwagSoftware/KisakCOD · Espelho: https://github.com/alves-r/mirror-swagsoftware-kisakcod

Reimplementação de código aberto do Call of Duty 4 (2007), com campanha, multiplayer e servidor dedicado. Usa os arquivos da sua cópia da Steam.

| Item | Detalhe |
|---|---|
| Tipo | Port / Recomp para compilar |
| Executável pronto | Não, precisa compilar. A release v0.1, de 28/07/2026, não tem arquivos. |
| Precisa de emulador | Não |
| Você precisa fornecer | O Call of Duty 4 da Steam. Copie todos os arquivos do jogo: arquivos pequenos, como `localization.txt`, também são necessários. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Não suportado (o build é só para Windows) |
| Windows | Nativo |
| Estado | Em desenvolvimento |
| Dificuldade | Média (compilar com script) |

> O README avisa que é um jogo de quase 20 anos com falhas conhecidas, e que há risco de exploração de binário ao jogar online. Ele sugere rodar numa sandbox, como o Sandboxie.

## Arch Linux

Não há binário pronto, e o README só documenta o build no Windows, com Visual Studio e DirectX SDK. Um executável compilado no Windows poderia, em tese, rodar pelo Proton, mas isso não é documentado.

## Windows

1. Instale os requisitos:
   - Visual Studio 2022;
   - CMake 3.16 ou mais novo;
   - DirectX SDK de junho de 2010 (link no README);
   - a Steam com o Call of Duty 4.
2. Clone o repositório e rode `generate-project.bat` num terminal.
3. Abra as soluções geradas em `build-sp` (campanha), `build-mp` (multiplayer) e `build-dedi` (servidor dedicado) e compile.
4. Copie para `bin/<tipo de build>/`:
   - todos os arquivos do jogo;
   - `deps/binklib/binkw32.dll`;
   - todos os arquivos de `deps/msslib/dlls/`;
   - `deps/steamsdk/steam_api.dll`.
5. Rode pelo botão de execução do Visual Studio ou direto pelo `.exe`.

## Problemas conhecidos

Os problemas ficam na página de issues do repositório: https://github.com/SwagSoftware/KisakCOD/issues

## Fontes

- [README › Current Requirements, How to build e FAQ](https://github.com/SwagSoftware/KisakCOD#readme)

<!-- verificado: 2026-10-15 -->
