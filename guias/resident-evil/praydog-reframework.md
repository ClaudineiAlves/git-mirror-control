# Jogos da RE Engine · REFramework (PC)

Repositório: https://github.com/praydog/REFramework · Espelho: https://github.com/alves-r/mirror-praydog-reframework

Carregador de mods, plataforma de scripts em Lua e suporte a VR para os jogos da RE Engine da Capcom, como RE2, RE3, RE4, RE7, Village, DMC5, Street Fighter 6 e Monster Hunter.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (v1.5.9.1, de 05/03/2025: um zip por jogo, como `RE2.zip`, `RE4.zip`, `RE8.zip` e `SF6.zip`). Builds mais novos ficam no repositório REFramework-nightly. |
| Precisa de emulador | Não |
| Você precisa fornecer | Um jogo suportado da RE Engine para PC. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton (suporte documentado) |
| Windows | Nativo |
| Estado | Ativo; funciona com DirectX 11 e 12. |
| Dificuldade | Fácil (baixar e rodar) |

Para RE2, RE3 e RE7 há também os zips `RE2_TDB66`, `RE3_TDB67` e `RE7_TDB49`. O README não explica a diferença.

## Arch Linux

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o jogo.
3. Baixe o zip do seu jogo em https://github.com/praydog/REFramework/releases.
4. Extraia só o `dinput8.dll` na pasta do jogo. Para VR, extraia o zip inteiro.
5. Nas **Propriedades** do jogo, em **Opções de inicialização**, coloque `WINEDLLOVERRIDES="dinput8.dll=n,b" %command%`.

## Windows

1. Baixe o zip do seu jogo em https://github.com/praydog/REFramework/releases.
2. **Sem VR:** extraia só o `dinput8.dll` na pasta do jogo, ex.: `steamapps\common\RESIDENT EVIL 2 BIOHAZARD RE2`.
3. **Com VR:** instale o SteamVR (a não ser que use OpenXR num headset compatível) e extraia o zip inteiro na pasta do jogo.
4. Abra o jogo normalmente.

**Compilar, opcional** (`COMPILING.md`): exige um compilador C++23 (recomenda o Visual Studio 2022) e o CMake. Clone o repositório, rode `git submodule update --init --recursive` e use os scripts `build_vs2022.bat` ou `build_vs2026.bat`.

## Controles e configurações

Mods incluídos:
- API de scripts em Lua e sistema de plugins (documentação em https://refdocs.praydog.com);
- VR com 6DOF em todos os jogos e controles de movimento em RE2, RE3, RE7 e RE8;
- primeira pessoa em RE2 e RE3;
- lanterna manual em RE2, RE3 e RE8;
- câmera livre, controle de velocidade da cena, FOV, remoção de vinheta, correções de ultrawide e esconder a interface, em todos os jogos.

## Fontes

- [README › Installation, Proton/Linux, Included Mods e Supported Games](https://github.com/praydog/REFramework#readme)
- [COMPILING.md](https://github.com/praydog/REFramework/blob/master/COMPILING.md)
- [Releases (v1.5.9.1)](https://github.com/praydog/REFramework/releases)

<!-- verificado: 2026-10-15 -->
