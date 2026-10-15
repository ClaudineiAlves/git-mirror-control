# Pokémon Emerald · EmeraldRecomp (GBA)

Repositório: https://github.com/mstan/EmeraldRecomp · Espelho: https://github.com/alves-r/mirror-mstan-emeraldrecomp

Recompilação estática do Pokémon Emerald para PC, feita com o framework `gbarecomp`. Tem netplay para dois jogadores por cabo link ou adaptador sem fio virtual. É uma prévia em desenvolvimento.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v0.1.1, de 27/09/2026: `EmeraldRecomp-windows-x64-v0.1.1.zip` e `EmeraldRecomp-linux-x86_64-v0.1.1.AppImage`, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Pokémon Emerald dos EUA (SHA-1 `f3ae088181bf583e55daf962a92bb46f4f1d07b7`), já que o programa recusa outras ROMs, e a BIOS original do GBA. ⚠️ Você indicou que não consegue dumpar GBA, e a BIOS também tem de sair do seu próprio aparelho. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Prévia em desenvolvimento. Chega ao gameplay, mas nem todo o código já foi recompilado. O netplay por cabo foi testado; o adaptador sem fio é experimental. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado. Baixe só pela página de Releases, confira com o `SHA256SUMS.txt` e passe o arquivo no VirusTotal.

O código que ainda não foi recompilado roda primeiro num interpretador e depois é compilado e guardado em disco. Por isso o jogo fica mais rápido conforme você joga.

## Arch Linux

1. Baixe `EmeraldRecomp-linux-x86_64-v0.1.1.AppImage` e `SHA256SUMS.txt` em https://github.com/mstan/EmeraldRecomp/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x EmeraldRecomp-linux-x86_64-v0.1.1.AppImage && ./EmeraldRecomp-linux-x86_64-v0.1.1.AppImage`
5. Escolha a sua ROM e a BIOS quando pedir.

## Windows

1. Baixe `EmeraldRecomp-windows-x64-v0.1.1.zip` e `SHA256SUMS.txt` em https://github.com/mstan/EmeraldRecomp/releases.
2. Confira o hash no PowerShell: `Get-FileHash .\EmeraldRecomp-windows-x64-v0.1.1.zip` e compare com o `SHA256SUMS.txt`.
3. Extraia e abra o `EmeraldRecomp`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. Escolha a sua ROM dos EUA e a BIOS quando pedir. O caminho fica salvo ao lado do programa.

**Compilar, opcional:** o README pede o MSYS2 com o ambiente mingw64 (`gcc`/`g++`), CMake 3.16+, Ninja e SDL2.
1. Clone o `gbarecomp` e este repositório lado a lado.
2. Coloque a ROM em `variants/emerald/roms/emerald_usa.gba`.
3. No PowerShell, com o mingw64 no `PATH`, rode:
   ```
   gba_recompile --rom variants/emerald/roms/emerald_usa.gba --config variants/emerald/symbols/emerald_usa.toml --out variants/emerald/generated
   cmake -S . -B build -G Ninja
   cmake --build build --target EmeraldRecomp
   ```

A compilação leva alguns minutos.

## Controles e configurações

| GBA | Tecla |
|---|---|
| Direcional | Setas |
| A / B | Z / X |
| Start / Select | Enter / Backspace |

- **Save states:** **Shift+F1–F9** salva num slot e **F1–F9** carrega.
- **Netplay para dois jogadores:**
  1. Os dois precisam do mesmo build e da ROM dos EUA.
  2. Abra **Netplay**, crie ou entre num lobby e use um save de treinador separado para cada jogador.
  3. O anfitrião escolhe **Lobby Settings → Connection type**: **Link Cable** (padrão) ou **Wireless Adapter**.
  4. No jogo, use o balcão do andar de cima do Centro Pokémon.
- **Widescreen experimental** (16:9, 21:9, 32:9 ou "Fit to window"): ligue no catálogo de **Mods**. Vem desligado.

## Fontes

- [README › ROM, Quick start, Multiplayer, Controls e Building from source](https://github.com/mstan/EmeraldRecomp#readme)
- [Releases (v0.1.1), com as notas que pedem a ROM e a BIOS](https://github.com/mstan/EmeraldRecomp/releases)

<!-- verificado: 2026-10-15 -->
