# DeckCraft · deckcraft (PC)

Repositório: https://github.com/storytold/deckcraft · Espelho: https://github.com/alves-r/mirror-storytold-deckcraft

Editor de apresentações de código aberto: uma reimplementação "clean-room" do PowerPoint, em Rust. Faz parte dos "Crafting Apps" do ArtCraft.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.7.0, de 14/10/2026: `deckcraft-0.7.0-windows-x64.msi`, `deckcraft-0.7.0-linux-x86_64.AppImage`, `.deb`, `.rpm`, Flatpak, tarball, macOS e versão web, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Alpha, rumo ao beta: 84% dos recursos do PowerPoint em amplitude e 92% do núcleo. |
| Dificuldade | Fácil (baixar e rodar) |

O README informa que os instaladores e executáveis são assinados digitalmente.

O README também aponta a página do app: https://getartcraft.com/apps/deckcraft

## Arch Linux

1. Baixe `deckcraft-0.7.0-linux-x86_64.AppImage` e `SHA256SUMS.txt` em https://github.com/storytold/deckcraft/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x deckcraft-0.7.0-linux-x86_64.AppImage && ./deckcraft-0.7.0-linux-x86_64.AppImage`

Os Releases também trazem o pacote Flatpak e um tarball para Linux.

**Compilar, opcional:**
1. Instale o Rust (sugestão): `sudo pacman -S --needed rustup && rustup default stable`
2. Clone: `git clone https://github.com/storytold/deckcraft && cd deckcraft`
3. Rode: `cargo run --release -p deckcraft-cli -- render --sample --all --scale 1 out/`
4. O README só mostra a ferramenta de linha de comando, que renderiza a apresentação de exemplo em `out/`. No Linux, o build precisa dos headers do ALSA, para o som das apresentações: no Arch, `sudo pacman -S --needed alsa-lib`.

As fontes extras vêm do repositório `craft-fonts`, que é opcional. Clone-o ao lado do projeto (`../craft-fonts`). Sem ele, o app usa as fontes do sistema.

## Windows

1. Baixe `deckcraft-0.7.0-windows-x64.msi` (instalador) ou `deckcraft-0.7.0-windows-x64-portable.zip` (versão portátil) em https://github.com/storytold/deckcraft/releases. Também há builds para ARM64 e 32 bits.
2. Confira o hash no PowerShell: `Get-FileHash .\deckcraft-0.7.0-windows-x64.msi` e compare com o `SHA256SUMS.txt`.
3. Instale, ou extraia a versão portátil, e abra o app.

Para compilar no Windows, use os mesmos comandos `cargo` da seção Arch Linux, com o Rust instalado.

## Problemas conhecidos

- Os logs ficam em `~/.config/deckcraft/logs/deckcraft.log` no Linux e em `%APPDATA%\DeckCraft\logs\` no Windows. Anexe esse arquivo ao relatar um erro.

## Fontes

- [README › Get started e Downloads](https://github.com/storytold/deckcraft#readme)
- [Releases (v0.7.0)](https://github.com/storytold/deckcraft/releases)

<!-- verificado: 2026-10-15 -->
