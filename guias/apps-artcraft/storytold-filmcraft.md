# FilmCraft · filmcraft (PC)

Repositório: https://github.com/storytold/filmcraft · Espelho: https://github.com/alves-r/mirror-storytold-filmcraft

Editor de vídeo não linear de código aberto, com cor e som, escrito do zero em Rust, no estilo do Premiere Pro. Faz parte dos "Crafting Apps" do ArtCraft.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.8.0, de 14/10/2026: `filmcraft-0.8.0-windows-x64.msi`, `filmcraft-0.8.0-linux-x86_64.AppImage`, `.deb`, `.rpm`, Flatpak, tarball, macOS e versão web, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Alpha. Cerca de 86% dos recursos do Premiere Pro existem, e o projeto estima estar a 56% de substituí-lo em projetos reais (medição de 10/10/2026). |
| Dificuldade | Fácil (baixar e rodar) |

O README informa que os instaladores e executáveis são assinados digitalmente.

O README também indica a página do app, https://getartcraft.com/apps/filmcraft, como o jeito mais fácil de instalar.

## Arch Linux

1. Baixe `filmcraft-0.8.0-linux-x86_64.AppImage` e `SHA256SUMS.txt` em https://github.com/storytold/filmcraft/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x filmcraft-0.8.0-linux-x86_64.AppImage && ./filmcraft-0.8.0-linux-x86_64.AppImage`

Os Releases também trazem o pacote Flatpak e um tarball para Linux.

**Compilar, opcional:**
1. Instale o Rust (sugestão): `sudo pacman -S --needed rustup && rustup default stable`
2. Clone: `git clone https://github.com/storytold/filmcraft && cd filmcraft`
3. Rode: `cargo run --release -p filmcraft`
4. Ele abre com um projeto de demonstração.

As fontes extras vêm do repositório `craft-fonts`, que é opcional. Clone-o ao lado do projeto (`../craft-fonts`). Sem ele, o app usa as fontes do sistema.

## Windows

1. Baixe `filmcraft-0.8.0-windows-x64.msi` (instalador) ou `filmcraft-0.8.0-windows-x64-portable.zip` (versão portátil) em https://github.com/storytold/filmcraft/releases. Também há builds para ARM64 e 32 bits.
2. Confira o hash no PowerShell: `Get-FileHash .\filmcraft-0.8.0-windows-x64.msi` e compare com o `SHA256SUMS.txt`.
3. Instale, ou extraia a versão portátil, e abra o app.

Para compilar no Windows, use os mesmos comandos `cargo` da seção Arch Linux, com o Rust instalado.

## Fontes

- [README › Get started e Downloads](https://github.com/storytold/filmcraft#readme)
- [Releases (v0.8.0)](https://github.com/storytold/filmcraft/releases)

<!-- verificado: 2026-10-15 -->
