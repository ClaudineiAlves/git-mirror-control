# FigCraft · figcraft (PC)

Repositório: https://github.com/storytold/figcraft · Espelho: https://github.com/alves-r/mirror-storytold-figcraft

Ferramenta de design de interfaces, componentes e protótipos: uma reimplementação "clean-room" do Figma, em Rust. Faz parte dos "Crafting Apps" do ArtCraft.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.6.0, de 14/10/2026: `figcraft-0.6.0-windows-x64.msi`, `figcraft-0.6.0-linux-x86_64.AppImage`, `.deb`, `.rpm`, Flatpak, tarball, macOS e versão web, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Alpha. Pela estimativa do projeto, está a cerca de 49% de substituir o Figma. Abre arquivos `.fig` só como melhor esforço, e o multiplayer está em prévia. |
| Dificuldade | Fácil (baixar e rodar) |

> O README não diz se o executável de Windows é assinado. Baixe só pela página de Releases, confira com o `SHA256SUMS.txt` e passe o arquivo no VirusTotal.

O README também aponta a página do app: https://getartcraft.com/apps/figcraft

## Arch Linux

1. Baixe `figcraft-0.6.0-linux-x86_64.AppImage` e `SHA256SUMS.txt` em https://github.com/storytold/figcraft/releases.
2. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
3. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
4. Rode: `chmod +x figcraft-0.6.0-linux-x86_64.AppImage && ./figcraft-0.6.0-linux-x86_64.AppImage`

Os Releases também trazem o pacote Flatpak e um tarball para Linux.

Há também um servidor próprio, em prévia, para guardar e compartilhar arquivos da equipe: `figcraft-server-0.6.0-linux-x86_64.tar.gz`.

**Compilar, opcional:**
1. Instale o Rust (sugestão): `sudo pacman -S --needed rustup && rustup default stable`
2. Clone: `git clone https://github.com/storytold/figcraft && cd figcraft`
3. Rode: `cargo run --release -p figcraft`

As fontes extras vêm do repositório `craft-fonts`, que é opcional. Clone-o ao lado do projeto (`../craft-fonts`). Sem ele, o app usa as fontes do sistema.

## Windows

1. Baixe `figcraft-0.6.0-windows-x64.msi` (instalador) ou `figcraft-0.6.0-windows-x64-portable.zip` (versão portátil) em https://github.com/storytold/figcraft/releases. Também há builds para ARM64 e 32 bits.
2. Confira o hash no PowerShell: `Get-FileHash .\figcraft-0.6.0-windows-x64.msi` e compare com o `SHA256SUMS.txt`.
3. Instale, ou extraia a versão portátil, e abra o app. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

Para compilar no Windows, use os mesmos comandos `cargo` da seção Arch Linux, com o Rust instalado.

## Fontes

- [README › Get started e Downloads](https://github.com/storytold/figcraft#readme)
- [Releases (v0.6.0)](https://github.com/storytold/figcraft/releases)

<!-- verificado: 2026-10-15 -->
