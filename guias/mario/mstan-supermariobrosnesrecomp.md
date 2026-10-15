# Super Mario Bros. · SuperMarioBrosNESRecomp (NES)

Repositório: https://github.com/mstan/SuperMarioBrosNESRecomp · Espelho: https://github.com/alves-r/mirror-mstan-supermariobrosnesrecomp

Recompilação estática do Super Mario Bros. de NES, com launcher, mods opcionais (widescreen, co-op, troca de personagem) e binário pronto para Windows.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim, só Windows (v1.12.0, de 05/10/2026: `SuperMarioBrosRecomp-windows-x64.zip` e uma variante widescreen, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM Super Mario Bros. (World): CRC32 `3337EC46`, MD5 `811b027eaf99c2def7b933c5208636de`, SHA-1 `ea343f4e445a9050d4b4fbac2c77d0693b1d0922`. ⚠️ Você indicou que não consegue dumpar NES. |
| Arch Linux | Nativo (só compilando) |
| Windows | Nativo |
| Estado | Ativo. Sem mods, a recompilação em 4:3 é conferida byte a byte com o emulador de referência. Widescreen e trocas de personagem são experimentais. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado. Baixe só pela página de Releases, confira com o `SHA256SUMS.txt` e passe o arquivo no VirusTotal.

## Arch Linux

Não há binário para Linux; o caminho é compilar.

1. Instale o básico: `sudo pacman -S --needed git base-devel cmake`. Os demais pré-requisitos estão listados no script `tools/build-linux.sh`.
2. Clone e prepare os submódulos:
   ```bash
   git clone https://github.com/mstan/SuperMarioBrosNESRecomp && cd SuperMarioBrosNESRecomp
   chmod +x setup.sh && ./setup.sh
   ```
3. Coloque a ROM na raiz do repositório com o nome `baserom.nes` (o build também reconhece os nomes canônicos EUA/World).
4. Compile: `bash tools/build-linux.sh --no-package`
5. A ROM também é necessária na hora de jogar.

## Windows

1. Baixe `SuperMarioBrosRecomp-windows-x64.zip` e `SHA256SUMS.txt` em https://github.com/mstan/SuperMarioBrosNESRecomp/releases.
2. Confira o hash no PowerShell: `Get-FileHash .\SuperMarioBrosRecomp-windows-x64.zip` e compare com o `SHA256SUMS.txt`.
3. Extraia e abra `SuperMarioBrosRecomp.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. Escolha a sua ROM quando pedir. O caminho fica salvo.

**Compilar, opcional:**
1. Instale o Visual Studio 2022 com as ferramentas de C++ e o CMake 3.20+ (o SDL2 já vem junto).
2. Rode `setup.bat`.
3. Gere e compile o projeto:
   ```bash
   cmake -S . -B build -G "Visual Studio 17 2022" -A x64 -DNESRECOMP_ROM="C:/Jogos/Super Mario Bros. (World).nes"
   cmake --build build --config Release
   ```

## Controles e configurações

| NES | Tecla |
|---|---|
| Direcional | Setas |
| A / B | Z / X |
| Start / Select | Enter / Barra invertida |

Mods ficam na página **Mods** do launcher:
- **Widescreen** (16:9, 21:9 e 32:9) e **Voxel 3D**, que não podem ficar ligados ao mesmo tempo;
- co-op simultâneo;
- troca de personagem por Captain Falcon ou Pikachu, Samus, Link (Zelda II) ou Sonic.

Cada troca de personagem exige a ROM original correspondente, conferida por hash.

## Fontes

- [README › Quick Start, ROM, Controls e Building from Source](https://github.com/mstan/SuperMarioBrosNESRecomp#readme)
- [Releases](https://github.com/mstan/SuperMarioBrosNESRecomp/releases)

<!-- verificado: 2026-10-15 -->
