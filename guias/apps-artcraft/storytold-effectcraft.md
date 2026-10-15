# EffectCraft · effectcraft (PC)

Repositório: https://github.com/storytold/effectcraft · Espelho: https://github.com/alves-r/mirror-storytold-effectcraft

Ferramenta de motion graphics e composição de código aberto, escrita do zero em Rust, no estilo do After Effects. Faz parte dos "Crafting Apps" do ArtCraft.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.10.0, de 14/10/2026: `effectcraft-0.10.0-windows-x64.msi`, `effectcraft-0.10.0-linux-x86_64.AppImage`, `.deb`, `.rpm`, Flatpak, tarball, macOS e versão web, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Em desenvolvimento. Pela estimativa do projeto, está a cerca de 45% de substituir o After Effects no trabalho profissional. |
| Dificuldade | Fácil (baixar e rodar) |

O README informa que os instaladores e executáveis são assinados digitalmente.

O README também indica a página do app, https://getartcraft.com/apps/effectcraft, como o jeito mais fácil de instalar.

## Arch Linux

1. Baixe `effectcraft-0.10.0-linux-x86_64.AppImage` e `SHA256SUMS.txt` em https://github.com/storytold/effectcraft/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x effectcraft-0.10.0-linux-x86_64.AppImage && ./effectcraft-0.10.0-linux-x86_64.AppImage`

Os Releases também trazem o pacote Flatpak e um tarball para Linux.

**Compilar, opcional:**
1. Instale o Rust (sugestão): `sudo pacman -S --needed rustup && rustup default stable`
2. Clone: `git clone https://github.com/storytold/effectcraft && cd effectcraft`
3. Rode: `cargo run --release -p effectcraft`

## Windows

1. Baixe `effectcraft-0.10.0-windows-x64.msi` (instalador) ou `effectcraft-0.10.0-windows-x64-portable.zip` (versão portátil) em https://github.com/storytold/effectcraft/releases. Também há builds para ARM64 e 32 bits.
2. Confira o hash no PowerShell: `Get-FileHash .\effectcraft-0.10.0-windows-x64.msi` e compare com o `SHA256SUMS.txt`.
3. Instale, ou extraia a versão portátil, e abra o app. O instalador pergunta onde instalar.

Para compilar no Windows, use os mesmos comandos `cargo` da seção Arch Linux, com o Rust instalado.

## Fontes

- [README › Get started e Downloads](https://github.com/storytold/effectcraft#readme)
- [Releases (v0.10.0)](https://github.com/storytold/effectcraft/releases)

<!-- verificado: 2026-10-15 -->
