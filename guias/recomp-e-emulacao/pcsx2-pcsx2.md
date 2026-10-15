# Emulador de PlayStation 2 · PCSX2 (PS2)

Repositório: https://github.com/PCSX2/pcsx2 · Espelho: https://github.com/alves-r/mirror-pcsx2-pcsx2

Emulador de PlayStation 2 livre e de código aberto, para Windows, Linux e macOS.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim (v2.8.2, estável, de 04/09/2026: `pcsx2-v2.8.2-linux-appimage-x64-Qt.AppImage`, Flatpak, `pcsx2-v2.8.2-windows-x64-installer.exe`, `.7z` e macOS). Também há builds de desenvolvimento quase diários, como a v2.9.127. |
| Precisa de emulador | Não se aplica: este é o emulador |
| Você precisa fornecer | O dump da BIOS do seu próprio PS2, que é obrigatório, e os jogos copiados dos seus discos. ⚠️ Você indicou que não consegue dumpar PS2, e a BIOS também tem de sair do seu próprio console. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

Os requisitos de hardware e software e o passo a passo da BIOS ficam na documentação do site: https://pcsx2.net/docs/setup/requirements e https://pcsx2.net/docs/setup/bios/

## Arch Linux

1. Baixe `pcsx2-v2.8.2-linux-appimage-x64-Qt.AppImage` em https://github.com/PCSX2/pcsx2/releases.
2. Instale o FUSE 2 (sugestão): `sudo pacman -S --needed fuse2`
3. Rode: `chmod +x pcsx2-v2.8.2-linux-appimage-x64-Qt.AppImage && ./pcsx2-v2.8.2-linux-appimage-x64-Qt.AppImage`
4. Na primeira execução, aponte a pasta da sua BIOS e a dos seus jogos (sugestão).

Também há um pacote no AUR (sugestão): `yay -S pcsx2`.

## Windows

1. Baixe `pcsx2-v2.8.2-windows-x64-installer.exe` (instalador) ou o `.7z` (versão portátil) em https://github.com/PCSX2/pcsx2/releases.
2. Instale ou extraia e abra o PCSX2.
3. Na primeira execução, aponte a pasta da sua BIOS e a dos seus jogos (sugestão).

O README não documenta o build. Ele remete ao guia de contribuição do site: https://pcsx2.net/docs/contributing/

## Fontes

- [README › System Requirements e Contributing / Building](https://github.com/PCSX2/pcsx2#readme)
- [Releases (v2.8.2)](https://github.com/PCSX2/pcsx2/releases/tag/v2.8.2)

<!-- verificado: 2026-10-15 -->
