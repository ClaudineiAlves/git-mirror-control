# Caelestia (dotfiles) · caelestia (Linux)

Repositório: https://github.com/caelestia-dots/caelestia · Espelho: https://github.com/alves-r/mirror-caelestia-dots-caelestia

Dotfiles do Caelestia: uma interface fluida e animada para o desktop Linux sobre o Hyprland. Configuram Hyprland, terminal, shell fish, navegador, editores e outros programas. Junto com o [shell](caelestia-dots-shell.md) e a [CLI](caelestia-dots-cli.md), formam o ecossistema Caelestia.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Não (são arquivos de configuração, instalados pela CLI) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Não suportado (é um desktop Linux/Wayland) |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Instale a CLI pelo AUR e rode o instalador: `paru -S caelestia-cli && caelestia install`
2. Os dotfiles não trazem gerenciador de login. Instale um ou entre pelo TTY. O autor recomenda o `greetd` com o `tuigreet`.
3. Para atualizar o sistema e os dotfiles: `caelestia update`

**Instalação manual, por componente:** clone o repositório, veja no `manifest.toml` os pacotes e arquivos de cada componente e copie só os que quiser. Exemplo para o Hyprland:
```bash
git clone https://github.com/caelestia-dots/caelestia.git && cd caelestia
sudo pacman -S --needed hyprland xdg-desktop-portal-hyprland xdg-desktop-portal-gtk ttf-jetbrains-mono-nerd
mkdir -p $XDG_CONFIG_HOME/hypr
cp -r hypr/. $XDG_CONFIG_HOME/hypr/
```

## Windows

Não suportado: é um ambiente de desktop Linux, sobre o compositor Wayland Hyprland. O WSL2 (`wsl --install -d Ubuntu`) roda programas Linux, mas não substitui o desktop do Windows, então não serve aqui.

## Controles e configurações

- **Nunca edite** os arquivos de `~/.config/hypr/`: isso cria conflitos nas atualizações. Ponha as mudanças em `~/.config/caelestia/hypr-user.lua` ou `hypr-vars.lua`, que a instalação e a atualização nunca alteram.
- O shell é configurado em `~/.config/caelestia/shell.json`, e a CLI em `~/.config/caelestia/cli.json`.
- Atalhos padrão (dá para trocar pelas variáveis em `hypr-vars.lua`):
  | Atalho | Ação |
  |---|---|
  | `Super` (apertar e soltar) | Abre o launcher |
  | `Super + 1~9, 0` | Vai para a área de trabalho 1~10 |
  | `Super + Alt + 1~9, 0` | Move a janela para a área 1~10 |
  | `Super + S` | Área especial |
  | `Super + M` / `Super + D` / `Super + R` | Áreas de música / comunicação / tarefas |
  | `Ctrl + Shift + Esc` | Monitor do sistema |
  | `Super + setas` | Foca a janela na direção |

## Fontes

- [README › Installation, Manual installation, Updating, Usage, Configuring e Default keybinds](https://github.com/caelestia-dots/caelestia#readme)
- [manifest.toml](https://github.com/caelestia-dots/caelestia/blob/main/manifest.toml)

<!-- verificado: 2026-10-15 -->
