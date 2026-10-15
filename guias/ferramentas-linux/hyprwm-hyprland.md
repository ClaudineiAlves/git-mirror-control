# Hyprland · Hyprland (Linux)

Repositório: https://github.com/hyprwm/Hyprland · Espelho: https://github.com/alves-r/mirror-hyprwm-hyprland

Compositor Wayland independente, com tiling dinâmico, muito configurável, com animações, plugins e IPC simples. É a base dos [dotfiles do Caelestia](caelestia-dots-caelestia.md).

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim, pelos repositórios oficiais do Arch (`hyprland`). Os Releases trazem só o código (v0.56.2, de 05/08/2026: `source-v0.56.2.tar.gz`). |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Não suportado (é um compositor Wayland para Linux) |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

O README remete à wiki do projeto para instalar, começar a usar e configurar. Os links ficam nos botões "Install", "Quick Start" e "Configure".

## Arch Linux

1. Instale o pacote oficial. Os dotfiles do Caelestia usam esta linha: `sudo pacman -S --needed hyprland xdg-desktop-portal-hyprland xdg-desktop-portal-gtk`
2. Para iniciar e configurar, siga a seção "Quick Start" da wiki, linkada no README.

## Windows

Não suportado: o Hyprland é um compositor Wayland, o próprio ambiente gráfico do Linux. O WSL2 (`wsl --install -d Ubuntu`) não substitui o desktop do Windows, então não serve aqui.

## Fontes

- [README](https://github.com/hyprwm/Hyprland#readme)
- [Releases (v0.56.2)](https://github.com/hyprwm/Hyprland/releases)
- [README dos dotfiles do Caelestia › Manual installation](https://github.com/caelestia-dots/caelestia#manual-installation)

<!-- verificado: 2026-10-15 -->
