# PlayStation 2 · PS2Recomp (PS2)

Repositório: https://github.com/ran-j/PS2Recomp · Espelho: https://github.com/alves-r/mirror-ran-j-ps2recomp

Recompilador estático experimental que converte executáveis ELF de PS2 em C++ e traz um runtime para rodar o código gerado. É a base para criar ports nativos de PC.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Não (as pré-releases v0.3 e v0.4 não têm arquivos) |
| Precisa de emulador | Não |
| Você precisa fornecer | O ELF do jogo de PS2, tirado do seu disco. Para jogos comerciais, o fluxo recomendado usa o Ghidra. ⚠️ Você indicou que não consegue dumpar PS2. |
| Arch Linux | Nativo (compilando; o projeto é testado principalmente com MSVC) |
| Windows | Nativo (compilando) |
| Estado | Experimental |
| Dificuldade | Difícil (toolchain manual) |

É uma ferramenta para quem cria ports. O runtime ainda tem só stubs básicos de GS, VU, arquivos e sistema. A documentação extra fica na wiki do projeto.

## Arch Linux

O README pede CMake 3.20+, um compilador C++20 e CPU com SSE4/AVX.

1. Instale o básico (sugestão): `sudo pacman -S --needed git cmake base-devel`
2. Clone com submódulos e compile:
   ```bash
   git clone --recurse-submodules https://github.com/ran-j/PS2Recomp.git && cd PS2Recomp
   cmake -S . -B out/build
   cmake --build out/build --config Debug
   ```
3. Fluxo recomendado para jogos comerciais:
   1. Abra o ELF no Ghidra e rode o script `ps2xRecomp/tools/ghidra/ExportPS2Functions.java`.
   2. Recompile com o TOML exportado: `./ps2_recomp config.toml`
4. Fluxo rápido, para ELFs com símbolos de depuração: `./ps2_analyzer seu_jogo.elf config.toml`
5. Compile a saída gerada junto com o `ps2xRuntime`.

## Windows

1. Instale o Visual Studio com C++ e CMake. O MSVC é o compilador mais testado pelo projeto.
2. Siga os passos 2 a 5 da seção Arch Linux.

## Fontes

- [README › Requirements, Build, Usage, Configuration e Runtime](https://github.com/ran-j/PS2Recomp#readme)
- [ps2xAnalyzer/Readme.md (fluxo com o Ghidra)](https://github.com/ran-j/PS2Recomp/blob/main/ps2xAnalyzer/Readme.md)

<!-- verificado: 2026-10-15 -->
