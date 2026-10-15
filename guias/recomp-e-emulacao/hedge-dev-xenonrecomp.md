# Xbox 360 · XenonRecomp (Xbox 360)

Repositório: https://github.com/hedge-dev/XenonRecomp · Espelho: https://github.com/alves-r/mirror-hedge-dev-xenonrecomp

Ferramenta que converte executáveis de Xbox 360 (`.xex`) em código C++, que depois pode ser compilado para qualquer plataforma. Foi usada no Unleashed Recompiled, o port de PC do Sonic Unleashed.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Não (sem releases) |
| Precisa de emulador | Não |
| Você precisa fornecer | O executável `.xex` do jogo, da sua cópia, e um runtime próprio. O projeto **não** fornece runtime, e sem ele o código gerado não funciona. ⚠️ Você não soube dizer se consegue dumpar Xbox 360. |
| Arch Linux | Nativo (compilando) |
| Windows | Nativo (compilando) |
| Estado | Sem mudanças desde 08/2025. |
| Dificuldade | Difícil (toolchain manual) |

É uma ferramenta para quem cria ports: fazer o jogo funcionar é responsabilidade de quem a usa, como o próprio README avisa.

## Arch Linux

O README pede CMake 3.20+ e Clang 18+. Outros compiladores não foram testados e não são recomendados.

1. Instale (sugestão): `sudo pacman -S --needed git cmake ninja clang`
2. Clone com submódulos e compile com o Clang:
   ```bash
   git clone --recursive https://github.com/hedge-dev/XenonRecomp.git && cd XenonRecomp
   cmake -S . -B build -G Ninja -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++
   cmake --build build
   ```
3. Use:
   - `XenonAnalyse <arquivo.xex> <tabelas.toml>` encontra as tabelas de salto do executável;
   - `XenonRecomp <config.toml> <XenonUtils/ppc_context.h>` gera o C++.

   Os TOMLs do Unleashed Recompiled servem de exemplo.

## Windows

1. Instale o Visual Studio com o conjunto de ferramentas **clang-cl** e abra o projeto pela integração com CMake.
2. Clone com `--recursive` antes de abrir.
3. Use as ferramentas como no passo 3 da seção Arch Linux.

## Fontes

- [README › Usage e Building](https://github.com/hedge-dev/XenonRecomp#readme)

<!-- verificado: 2026-10-15 -->
