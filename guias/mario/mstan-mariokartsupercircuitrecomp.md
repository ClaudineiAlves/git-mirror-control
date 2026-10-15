# Mario Kart: Super Circuit · MarioKartSuperCircuitRecomp (GBA)

Repositório: https://github.com/mstan/MarioKartSuperCircuitRecomp · Espelho: https://github.com/alves-r/mirror-mstan-mariokartsupercircuitrecomp

Recompilação estática do Mario Kart: Super Circuit, com mods opcionais de 60 FPS e widescreen e netplay por cabo link emulado. Ainda é uma prévia experimental.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v0.1.4, de 04/10/2026: `MarioKartSuperCircuitRecomp-windows-x64-v0.1.4.zip` e `MarioKartSuperCircuitRecomp-linux-x86_64-v0.1.4.AppImage`, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Mario Kart: Super Circuit (EUA) e a BIOS original do GBA. ⚠️ Você indicou que não consegue dumpar GBA, e a BIOS também tem de sair do seu próprio aparelho. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Prévia experimental. Menus, seleção de copa, corridas e resultados funcionam, e o netplay funciona pela internet ou LAN. A v0.1.3 corrigiu os saves. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado. Baixe só pela página de Releases, confira com o `SHA256SUMS.txt` e passe o arquivo no VirusTotal.

## Arch Linux

1. Baixe `MarioKartSuperCircuitRecomp-linux-x86_64-v0.1.4.AppImage` e `SHA256SUMS.txt` em https://github.com/mstan/MarioKartSuperCircuitRecomp/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x MarioKartSuperCircuitRecomp-linux-x86_64-v0.1.4.AppImage && ./MarioKartSuperCircuitRecomp-linux-x86_64-v0.1.4.AppImage`
5. No launcher, escolha a ROM (EUA) e a BIOS do GBA, ajuste vídeo, áudio, controles e mods e clique em **Play**.

O README só documenta compilação no Windows.

## Windows

1. Baixe `MarioKartSuperCircuitRecomp-windows-x64-v0.1.4.zip` em https://github.com/mstan/MarioKartSuperCircuitRecomp/releases e extraia.
2. Abra `MarioKartSuperCircuitRecomp.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. No launcher, escolha a ROM (EUA) e a BIOS do GBA e clique em **Play**. Com **Skip launcher on boot**, as próximas aberturas vão direto para o jogo.

**Compilar, opcional:** precisa de CMake, Ninja, MSYS2 MinGW64 e SDL2. No PowerShell:

```powershell
git clone --recurse-submodules https://github.com/mstan/MarioKartSuperCircuitRecomp.git
cd MarioKartSuperCircuitRecomp
cmake -S gbarecomp -B gbarecomp/build -G Ninja
cmake --build gbarecomp/build --target gba_recompile
pwsh tools/regen.ps1
cmake -S . -B build -G Ninja
cmake --build build --target MarioKartSuperCircuitRecomp
```

## Controles e configurações

| GBA | Tecla |
|---|---|
| Direcional | Setas |
| A / B | X / Z |
| L / R | C / V |
| Start / Select | Enter / Shift direito |

- **Estados:** Shift+F1–F9 salva e F1–F9 carrega.
- **Controles:** mudam no launcher.
- **Mods** (página **Mods**, ambos desligados por padrão): **60 FPS Track Rendering** e **Adaptive Widescreen**.
- **Netplay:** ver `docs/NETPLAY.md`.

## Problemas conhecidos

- É uma prévia experimental: faça backup dos saves importantes.

## Fontes

- [README › Status, Quick start, Included mods, Controls e Building from source](https://github.com/mstan/MarioKartSuperCircuitRecomp#readme)
- [Releases](https://github.com/mstan/MarioKartSuperCircuitRecomp/releases)

<!-- verificado: 2026-10-15 -->
