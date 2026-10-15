# PhotoCraft · photocraft (PC)

Repositório: https://github.com/storytold/photocraft · Espelho: https://github.com/alves-r/mirror-storytold-photocraft

Editor de imagens de código aberto, escrito do zero em Rust, no estilo do Photoshop e com suporte a arquivos PSD. Faz parte dos "Crafting Apps" do ArtCraft.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.9.0, de 14/10/2026: `photocraft-0.9.0-windows-x64.msi`, `photocraft-0.9.0-linux-x86_64.AppImage`, `.deb`, `.rpm`, Flatpak, tarball, macOS e versão web, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Alpha inicial. Boa parte dos recursos do Photoshop já existe de alguma forma, mas ainda não substitui o Photoshop no trabalho profissional diário. |
| Dificuldade | Fácil (baixar e rodar) |

O README informa que os instaladores e executáveis são assinados digitalmente.

O README também indica a página do app, https://getartcraft.com/apps/photocraft, como o jeito mais fácil de instalar.

## Arch Linux

1. Baixe `photocraft-0.9.0-linux-x86_64.AppImage` e `SHA256SUMS.txt` em https://github.com/storytold/photocraft/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x photocraft-0.9.0-linux-x86_64.AppImage && ./photocraft-0.9.0-linux-x86_64.AppImage`

Também dá para usar o Flatpak:
```bash
flatpak install --user photocraft-0.9.0-linux-x86_64.flatpak
flatpak run ai.storyteller.photocraft
```

**Compilar, opcional:**
1. Instale o Rust (sugestão): `sudo pacman -S --needed rustup && rustup default stable`
2. Clone: `git clone https://github.com/storytold/photocraft && cd photocraft`
3. Rode: `cargo run --release -p photocraft -- imagem.psd`

As fontes extras vêm do repositório `craft-fonts`, que é opcional. Clone-o ao lado do projeto (`../craft-fonts`). Sem ele, o app usa as fontes do sistema.

## Windows

1. Baixe `photocraft-0.9.0-windows-x64.msi` (instalador) ou `photocraft-0.9.0-windows-x64-portable.zip` (versão portátil) em https://github.com/storytold/photocraft/releases. Também há builds para ARM64 e 32 bits.
2. Confira o hash no PowerShell: `Get-FileHash .\photocraft-0.9.0-windows-x64.msi` e compare com o `SHA256SUMS.txt`.
3. Instale, ou extraia a versão portátil, e abra o app.

Para compilar no Windows, use os mesmos comandos `cargo` da seção Arch Linux, com o Rust instalado.

## Problemas conhecidos

- Numa sessão Wayland, arrastar arquivos para a janela ainda não funciona, por limitação do winit 0.30. Use **File › Open** ou copie a imagem no gerenciador de arquivos e cole com Ctrl+V.
- Na primeira execução, o AppImage registra o ícone e a entrada no menu em `~/.local/share`. Para evitar isso, defina `PHOTOCRAFT_NO_DESKTOP_INTEGRATION=1`.

## Fontes

- [README › Get started e Downloads](https://github.com/storytold/photocraft#readme)
- [Releases (v0.9.0)](https://github.com/storytold/photocraft/releases)

<!-- verificado: 2026-10-15 -->
