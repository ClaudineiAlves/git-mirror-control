# Pokémon FireRed e LeafGreen · FireRedLeafGreenRecomp (GBA)

Repositório: https://github.com/mstan/FireRedLeafGreenRecomp · Espelho: https://github.com/alves-r/mirror-mstan-fireredleafgreenrecomp

Recompilação estática do Pokémon FireRed e do LeafGreen para PC, feita com o framework `gbarecomp`, com um executável para cada jogo. É uma prévia em desenvolvimento, com binário pronto só para Windows.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim, só Windows (v0.0.3, de 17/07/2026: `FireRedRecomp-windows-x64-v0.0.3.zip` e `LeafGreenRecomp-windows-x64-v0.0.3.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM dos EUA v1.0 do FireRed (SHA-1 `41cb23d8dccc8ebd7c649cd8fbb58eeace6e2fdc`) ou do LeafGreen (`574fa542ffebb14be69902d1d36f1ec0a4afd71e`), já que o programa recusa outras ROMs, e a BIOS original do GBA. ⚠️ Você indicou que não consegue dumpar GBA, e a BIOS também tem de sair do seu próprio aparelho. |
| Arch Linux | Via Proton (não oficial) |
| Windows | Nativo |
| Estado | Prévia em desenvolvimento. Os dois jogos chegam ao gameplay, mas nem todo o código já foi recompilado. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

O código que ainda não foi recompilado roda primeiro num interpretador e depois é compilado e guardado em disco. Por isso o jogo fica mais rápido conforme você joga.

## Arch Linux

O projeto só publica e documenta a versão de Windows. Dá para tentar pelo Proton, mas não é suportado oficialmente:

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam: `sudo pacman -Syu steam`
3. Baixe o zip do jogo em https://github.com/mstan/FireRedLeafGreenRecomp/releases e extraia numa pasta.
4. Na Steam, vá em **Adicionar jogo → Adicionar jogo não Steam** e escolha o executável do jogo (`FireRedRecomp` ou `LeafGreenRecomp`).
5. Em **Propriedades → Compatibilidade**, force o **Proton Experimental**.
6. Abra pela Steam e escolha a ROM e a BIOS no launcher.

Como alternativa nativa, o decomp `pret/pokefirered` gera a ROM sem precisar de dump ([guia](pret-pokefirered.md)). Ela roda no mGBA (sugestão).

## Windows

1. Baixe `FireRedRecomp-windows-x64-v0.0.3.zip` ou `LeafGreenRecomp-windows-x64-v0.0.3.zip` em https://github.com/mstan/FireRedLeafGreenRecomp/releases e extraia.
2. Abra o executável do jogo. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. No launcher, escolha a ROM e a BIOS e ajuste vídeo, áudio e controles. O caminho da ROM fica salvo ao lado do programa.

**Compilar, opcional:** o README pede o MSYS2 com o ambiente mingw64 (`gcc`/`g++`), CMake 3.16+, Ninja e SDL2.
1. Clone o `gbarecomp` e este repositório lado a lado.
2. Coloque a ROM em `variants/firered/roms/firered_usa.gba`.
3. No PowerShell, com o mingw64 no `PATH`, rode:
   ```
   gba_recompile --rom variants/firered/roms/firered_usa.gba --config variants/firered/symbols/firered.toml --out variants/firered/generated
   cmake -S . -B build -G Ninja
   cmake --build build --target FireRedRecomp
   ```

## Controles e configurações

| GBA | Tecla |
|---|---|
| Direcional | Setas |
| A / B | Z / X |
| Start / Select | Enter / Backspace |

- **Save states:** **Shift+F1–F9** salva num slot e **F1–F9** carrega.
- As teclas podem ser trocadas no launcher, antes de começar.

## Fontes

- [README › Variants, Quick start, Controls e Building from source](https://github.com/mstan/FireRedLeafGreenRecomp#readme)
- [Releases (v0.0.3), com as notas do launcher](https://github.com/mstan/FireRedLeafGreenRecomp/releases)

<!-- verificado: 2026-10-15 -->
