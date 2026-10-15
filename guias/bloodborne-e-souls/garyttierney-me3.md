# me3 · carregador de mods da FromSoftware (PC)

Repositório: https://github.com/garyttierney/me3 · Espelho: https://github.com/alves-r/mirror-garyttierney-me3

Framework para carregar mods em Dark Souls III, Sekiro, Elden Ring, Armored Core VI e Elden Ring Nightreign. É o sucessor do Mod Engine 2.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (v0.13.0, de 11/08/2026: `me3_installer.exe` e `me3-windows-amd64.zip` para Windows; `me3-linux-amd64.tar.gz` e `installer.sh` para Linux) |
| Precisa de emulador | Não |
| Você precisa fornecer | Um jogo suportado, original para PC: Dark Souls III, Sekiro, Elden Ring, Armored Core VI ou Elden Ring Nightreign. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Nativo (suporte oficial: o me3 abre o jogo pelo Proton da Steam) |
| Windows | Nativo |
| Estado | Ativo; última versão em 11/08/2026 |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Os jogos rodam pela Steam com Proton. Habilite o multilib, que está desligado na sua máquina, descomentando `[multilib]` em `/etc/pacman.conf` (sugestão). Depois instale a Steam: `sudo pacman -Syu steam`
2. Instale o me3 de uma destas formas:
   - **Instalador oficial:** `curl --proto '=https' --tlsv1.2 -sSfL https://github.com/garyttierney/me3/releases/latest/download/installer.sh | sh`. Se quiser ler o script antes, baixe o `installer.sh` em Releases e rode `sh installer.sh`.
   - **Manual:** baixe `me3-linux-amd64.tar.gz` em https://github.com/garyttierney/me3/releases e rode:
     ```bash
     tar -xzf me3-linux-amd64.tar.gz
     cd me3-linux-amd64
     ./bin/me3 --windows-binaries-dir ./bin/win64 info
     ```
3. Crie um perfil de mods (passo 1 de "Controles e configurações").
4. Abra o jogo com o perfil: `me3 launch -p meuperfil.me3`. Também dá para usar um perfil padrão, ex.: `me3 launch -p eldenring-default`.

## Windows

1. Baixe `me3_installer.exe` em https://github.com/garyttierney/me3/releases e siga o assistente. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
2. Ou use a versão portátil: baixe `me3-windows-amd64.zip` e extraia numa pasta local, fora do OneDrive ou de programas parecidos.
3. Crie um perfil de mods (passo 1 de "Controles e configurações").
4. Dê dois cliques no arquivo `.me3` para abrir o jogo com os mods. Também dá para usar o menu Iniciar (perfis padrão) ou a linha de comando: `me3 launch -p meuperfil.me3`.

## Controles e configurações

1. **Perfil de mods.** Os perfis ficam por padrão em `%LOCALAPPDATA%/garyttierney/me3/config/profiles` (Windows) ou `$HOME/.config/me3/profiles` (Linux), mas um `.me3` pode ficar em qualquer pasta que não seja de rede. Ao lado dele, crie:
   - `mod/`, para arquivos de conteúdo (ex.: `regulation.bin` e pastas `parts/`);
   - `natives/`, para as DLLs.
2. **Arquivo de perfil**, em TOML. Exemplo da documentação, para Nightreign:
   ```toml
   profileVersion = "v1"
   [[supports]]
   game = "nightreign"
   [[packages]]
   id = "nightmods"
   path = 'mod'
   [[natives]]
   path = 'natives/SkipIntroLogos.dll'
   ```
   Os caminhos são relativos ao local do arquivo `.me3`.

## Fontes

- [README › Supported platforms, Supported games e Installation](https://github.com/garyttierney/me3#readme)
- [docs/index.md (instalação e início rápido)](https://github.com/garyttierney/me3/blob/main/docs/index.md)
- [docs/user-guide/creating-mod-profiles.md](https://github.com/garyttierney/me3/blob/main/docs/user-guide/creating-mod-profiles.md)
- [docs/user-guide/troubleshooting.md](https://github.com/garyttierney/me3/blob/main/docs/user-guide/troubleshooting.md)
- [Releases](https://github.com/garyttierney/me3/releases)

<!-- verificado: 2026-10-15 -->
