# GridCraft · gridcraft (PC)

Repositório: https://github.com/storytold/gridcraft · Espelho: https://github.com/alves-r/mirror-storytold-gridcraft

Planilha eletrônica de código aberto, no estilo do Excel, feita "clean-room" em Rust. Faz parte dos "Crafting Apps" do ArtCraft.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.7.0, de 14/10/2026: `gridcraft-0.7.0-windows-x64.msi`, `gridcraft-0.7.0-linux-x86_64.AppImage`, `.deb`, `.rpm`, Flatpak, tarball, macOS e versão web, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Alpha: o fluxo principal funciona de ponta a ponta, mas ainda faltam profundidade, fidelidade e compatibilidade de arquivos. |
| Dificuldade | Fácil (baixar e rodar) |

O README informa que os instaladores e executáveis são assinados digitalmente.

O README também aponta a página do app: https://getartcraft.com/apps/gridcraft

## Arch Linux

1. Baixe `gridcraft-0.7.0-linux-x86_64.AppImage` e `SHA256SUMS.txt` em https://github.com/storytold/gridcraft/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x gridcraft-0.7.0-linux-x86_64.AppImage && ./gridcraft-0.7.0-linux-x86_64.AppImage`

Os Releases também trazem o pacote Flatpak e um tarball para Linux.

**Compilar, opcional:**
1. Instale o Rust (sugestão): `sudo pacman -S --needed rustup && rustup default stable`
2. Clone: `git clone https://github.com/storytold/gridcraft && cd gridcraft`
3. Rode: `cargo run --release -p gridcraft`

## Windows

1. Baixe `gridcraft-0.7.0-windows-x64.msi` (instalador) ou `gridcraft-0.7.0-windows-x64-portable.zip` (versão portátil) em https://github.com/storytold/gridcraft/releases. Também há builds para ARM64 e 32 bits.
2. Confira o hash no PowerShell: `Get-FileHash .\gridcraft-0.7.0-windows-x64.msi` e compare com o `SHA256SUMS.txt`.
3. Instale, ou extraia a versão portátil, e abra o app. O instalador MSI oferece um atalho opcional na área de trabalho.

Para compilar no Windows, use os mesmos comandos `cargo` da seção Arch Linux, com o Rust instalado.

## Fontes

- [README › Get started e Downloads](https://github.com/storytold/gridcraft#readme)
- [Releases (v0.7.0)](https://github.com/storytold/gridcraft/releases)

<!-- verificado: 2026-10-15 -->
