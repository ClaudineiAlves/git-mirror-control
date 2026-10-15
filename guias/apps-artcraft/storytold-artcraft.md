# ArtCraft · artcraft (PC)

Repositório: https://github.com/storytold/artcraft · Espelho: https://github.com/alves-r/mirror-storytold-artcraft

IDE para criar imagens e vídeos com IA de forma interativa. Você compõe em 2D, monta cenas em 3D e escolhe os modelos de IA de cada trabalho. É o app principal da família "Crafting Apps", feito em Rust com Tauri.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim, só Windows e macOS (artcraft-v0.41.0, de 26/09/2026: `ArtCraft_0.41.0_x64-setup.exe`, `ArtCraft_0.41.0_x64_en-US.msi` e `ArtCraft_0.41.0_universal.dmg`). As versões estáveis ficam em https://getartcraft.com/. |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada. A geração usa modelos de IA de provedores: o próprio ArtCraft, Grok, Midjourney, Sora e World Labs. O README não detalha contas nem custos. |
| Arch Linux | Nativo (só compilando; o documento cobre o modo de desenvolvimento) |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Média (compilar com script) |

> O README não diz se os instaladores são assinados. Baixe só pela página de Releases ou pelo site oficial e passe o arquivo no VirusTotal.

## Arch Linux

Não há binário para Linux: o README manda compilar pelo `_docs/dev_setup.md`, que descreve o modo de desenvolvimento.

1. Instale o Rust e o Node.js 20+ (sugestão): `sudo pacman -S --needed rustup nodejs npm && rustup default stable`
2. Instale o Tauri CLI. O documento cita a versão `tauri-cli 2.10.0` e remete à documentação do Tauri.
3. Clone: `git clone https://github.com/storytold/artcraft && cd artcraft`
4. Inicie o front-end e o app juntos: `./script/artcraft/unix_dev.sh`. Ele instala as dependências do front-end se faltarem e procura uma porta livre a partir da 5193.
5. Ctrl+C encerra tudo.

O documento não lista as dependências de sistema do Tauri no Linux, como WebKitGTK. Ele só diz que o launcher aplica contornos para o WebKit no Linux.

## Windows

1. Baixe `ArtCraft_0.41.0_x64-setup.exe` (ou o `.msi`) em https://github.com/storytold/artcraft/releases. A versão estável fica em https://getartcraft.com/.
2. Instale e abra o ArtCraft. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

**Modo de desenvolvimento, opcional:** com Rust, Node.js e o Tauri CLI instalados, rode `.\script\artcraft\windows_frontend_dev.ps1` e, em outro terminal, `.\script\artcraft\windows_rust_dev.ps1`.

## Controles e configurações

- **Texto para imagem e edição por prompt:** com modelos como Nano Banana Pro e GPT Image.
- **Edição no canvas:** desenho, máscaras e inpainting.
- **Imagem para vídeo:** com o modelo de vídeo escolhido.
- **Cenas em 3D:** para compor as imagens com precisão.

## Fontes

- [README › Quick and Easy Prompting, Models and Providers, Downloads e Documentation](https://github.com/storytold/artcraft#readme)
- [_docs/dev_setup.md](https://github.com/storytold/artcraft/blob/main/_docs/dev_setup.md)
- [Releases (artcraft-v0.41.0)](https://github.com/storytold/artcraft/releases)

<!-- verificado: 2026-10-15 -->
