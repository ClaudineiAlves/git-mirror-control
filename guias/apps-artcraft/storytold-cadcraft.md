# CADCraft · cadcraft (PC)

Repositório: https://github.com/storytold/cadcraft · Espelho: https://github.com/alves-r/mirror-storytold-cadcraft

Programa de desenho técnico e CAD de código aberto, no estilo do AutoCAD, feito "clean-room" em Rust. Faz parte dos "Crafting Apps" do ArtCraft.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.7.0, de 14/10/2026: `cadcraft-0.7.0-windows-x64.msi`, `cadcraft-0.7.0-linux-x86_64.AppImage`, `.deb`, `.rpm`, Flatpak, tarball, macOS e versão web, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Desenvolvimento inicial e acelerado. Os detalhes estão no `ROADMAP.md`. |
| Dificuldade | Fácil (baixar e rodar) |

O README informa que os instaladores e executáveis são assinados digitalmente.

O README também aponta a página do app: https://getartcraft.com/apps/cadcraft

## Arch Linux

1. Baixe `cadcraft-0.7.0-linux-x86_64.AppImage` e `SHA256SUMS.txt` em https://github.com/storytold/cadcraft/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x cadcraft-0.7.0-linux-x86_64.AppImage && ./cadcraft-0.7.0-linux-x86_64.AppImage`

Os Releases também trazem o pacote Flatpak e um tarball para Linux.

**Compilar, opcional:**
1. Instale o Rust (sugestão): `sudo pacman -S --needed rustup && rustup default stable`
2. Clone: `git clone https://github.com/storytold/cadcraft && cd cadcraft`
3. Rode: `cargo run --release -p cadcraft -- --sample`
4. Ele abre o desenho de exemplo.

As fontes extras vêm do repositório `craft-fonts`, que é opcional. Clone-o ao lado do projeto (`../craft-fonts`). Sem ele, o app usa as fontes do sistema.

## Windows

1. Baixe `cadcraft-0.7.0-windows-x64.msi` (instalador) ou `cadcraft-0.7.0-windows-x64-portable.zip` (versão portátil) em https://github.com/storytold/cadcraft/releases. Também há builds para ARM64 e 32 bits.
2. Confira o hash no PowerShell: `Get-FileHash .\cadcraft-0.7.0-windows-x64.msi` e compare com o `SHA256SUMS.txt`.
3. Instale, ou extraia a versão portátil, e abra o app.

Para compilar no Windows, use os mesmos comandos `cargo` da seção Arch Linux, com o Rust instalado.

## Fontes

- [README › Get started e Downloads](https://github.com/storytold/cadcraft#readme)
- [Releases (v0.7.0)](https://github.com/storytold/cadcraft/releases)

<!-- verificado: 2026-10-15 -->
