# The Legend of Zelda: The Minish Cap · MinishCapRecomp (GBA)

Repositório: https://github.com/mstan/MinishCapRecomp · Espelho: https://github.com/alves-r/mirror-mstan-minishcaprecomp

Recompilação estática do The Minish Cap para PC, feita com o framework `gbarecomp`. É uma prévia em desenvolvimento, com binário pronto só para Windows.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim, só Windows (v0.0.5, de 29/08/2026: `MinishCapRecomp-windows-x64-v0.0.5.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Minish Cap dos EUA (SHA-1 `b4bd50e4131b027c334547b4524e2dbbd4227130`), já que o programa recusa outras ROMs, e a BIOS original do GBA. ⚠️ Você indicou que não consegue dumpar GBA, e a BIOS também tem de sair do seu próprio aparelho. |
| Arch Linux | Via Proton (não oficial) |
| Windows | Nativo |
| Estado | Prévia em desenvolvimento. Chega ao gameplay (mundo aberto, diálogos e save states), mas nem todo o código já foi recompilado. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

O código que ainda não foi recompilado roda primeiro num interpretador e depois é compilado e guardado em disco. Por isso o jogo fica mais rápido conforme você joga.

## Arch Linux

O projeto só publica e documenta a versão de Windows. Dá para tentar pelo Proton, mas não é suportado oficialmente:

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam: `sudo pacman -Syu steam`
3. Baixe o zip da versão de Windows em https://github.com/mstan/MinishCapRecomp/releases e extraia numa pasta.
4. Na Steam, vá em **Adicionar jogo → Adicionar jogo não Steam** e escolha o `MinishCapRecomp.exe`.
5. Em **Propriedades → Compatibilidade**, force o **Proton Experimental**.
6. Abra pela Steam e escolha a sua ROM e a BIOS quando pedir.

Como alternativa nativa, o decomp `zeldaret/tmc` gera a ROM a partir da sua cópia ([guia](zeldaret-tmc.md)). Ela roda no mGBA (sugestão).

## Windows

1. Baixe `MinishCapRecomp-windows-x64-v0.0.5.zip` em https://github.com/mstan/MinishCapRecomp/releases e extraia.
2. Abra o `MinishCapRecomp`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Escolha a sua ROM dos EUA e a BIOS quando pedir. O caminho fica salvo ao lado do programa.
4. No começo, o interpretador pode aparecer rapidamente enquanto aquece trechos novos. Depois eles rodam nativos.

**Compilar, opcional:** o README pede o MSYS2 com o ambiente mingw64 (`gcc`/`g++`), CMake 3.16+, Ninja e SDL2.
1. Clone o `gbarecomp` e este repositório lado a lado.
2. Coloque a ROM em `roms/minishcap_usa.gba`.
3. No PowerShell, com o mingw64 no `PATH`, rode:
   ```
   gba_recompile --rom roms/minishcap_usa.gba --config symbols/minishcap.toml --out generated
   cmake -S . -B build -G Ninja -DGBARECOMP_ROOT=../gbarecomp
   cmake --build build --target MinishCapRecomp
   ```

O `gba_recompile` é compilado a partir do `gbarecomp`; veja o README dele.

## Controles e configurações

| GBA | Tecla |
|---|---|
| Direcional | Setas |
| A / B | Z / X |
| L / R | A / S |
| Start / Select | Enter / Backspace |

- **Save states:** **Shift+F1–F9** salva num slot e **F1–F9** carrega.
- **Widescreen adaptativo:** ligue em **Mods**, no launcher, antes de começar. Vem desligado; o padrão é a tela original de 240×160.

## Fontes

- [README › ROM, Quick start, Controls, Adaptive Widescreen mod e Building from source](https://github.com/mstan/MinishCapRecomp#readme)
- [Releases (v0.0.5), com as notas que pedem a ROM e a BIOS](https://github.com/mstan/MinishCapRecomp/releases)

<!-- verificado: 2026-10-15 -->
