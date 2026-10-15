# Spotifast · spotifast (PC)

Repositório: https://github.com/crmne/spotifast · Espelho: https://github.com/alves-r/mirror-crmne-spotifast

Cliente de Spotify nativo e leve, escrito em Rust, para Linux, macOS e Windows. Não usa motor de navegador, toca pelo librespot e costuma ocupar de 100 a 250 MB de RAM.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (v0.13.2, de 14/10/2026: AppImage, `.deb`, `.rpm`, Flatpak e tarball para Linux; `.msi`, instalador `.exe` e `.zip` para Windows; macOS; com `checksums.txt` assinado) |
| Precisa de emulador | Não |
| Você precisa fornecer | Uma conta Spotify **Premium** para tocar música. Contas grátis só navegam e buscam. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

A documentação completa fica em https://spotifast.rocks. O site tem uma página sobre o risco de banimento da conta ("Will my Spotify account get banned?"); leia antes de usar.

## Arch Linux

1. Instale pelo AUR, como o README indica: `yay -S spotifast-bin`. O pacote é mantido pelo próprio autor.
2. Também há AppImage, Flatpak e tarball em https://github.com/crmne/spotifast/releases.

## Windows

1. Baixe `spotifast-v0.13.2-x86_64-pc-windows-msvc-setup.exe` (ou o `.msi`) em https://github.com/crmne/spotifast/releases, ou escolha o build na página de download do site (https://spotifast.rocks/download/).
2. Instale e abra o Spotifast.

Para compilar a partir do código, o README remete à seção "Build from source" do site.

## Controles e configurações

1. Abra o Spotifast e clique em **Sign in with Spotify**. Aprove o acesso no navegador e volte ao app.
2. Para tocar neste computador, abra o menu de dispositivos na barra do player e escolha **Set up playback here**. Isso também fica nas configurações.
3. Faça a segunda aprovação no navegador. O computador aparece como o dispositivo Spotify Connect **Spotifast**.

Outros recursos:
- **Mini player do Winamp:** **Ctrl+M** abre o mini player, com skins `.wsz`, equalizador e playlist.
- **MilkDrop:** visualizações que reagem à música, em janela separada ou tela cheia. Não vem no build para Windows ARM.
- **Sonos:** ligue a reprodução local primeiro e depois escolha a caixa de som no seletor de dispositivos.

## Fontes

- [README › Install, Start listening, The Winamp mini player, Music in motion e Guides and help](https://github.com/crmne/spotifast#readme)
- [Releases (v0.13.2)](https://github.com/crmne/spotifast/releases)

<!-- verificado: 2026-10-15 -->
