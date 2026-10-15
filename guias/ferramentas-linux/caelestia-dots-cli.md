# Caelestia CLI · cli (Linux)

Repositório: https://github.com/caelestia-dots/cli · Espelho: https://github.com/alves-r/mirror-caelestia-dots-cli

Script de controle principal dos dotfiles do Caelestia. Ele controla o shell, as áreas especiais, o esquema de cores, as capturas e gravações de tela, o histórico da área de transferência e o papel de parede, e instala e atualiza os dotfiles.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim, pelo AUR (`caelestia-cli` 1.1.3). Os Releases trazem o pacote Python (v1.1.3, de 18/09/2026: `caelestia-1.1.3-py3-none-any.whl`). |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Não suportado (é parte de um desktop Linux/Wayland) |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Instale pelo AUR: `yay -S caelestia-cli`. Também existe o `caelestia-cli-git`, que acompanha o último commit e é instável.
2. Rode `caelestia -h` para ver os subcomandos.

**Instalação manual:**
1. Instale as dependências e as ferramentas de build:
   ```bash
   yay -S libnotify swappy grim dart-sass wl-clipboard slurp gpu-screen-recorder glib2 cliphist fuzzel python-build python-installer python-hatch python-hatch-vcs
   ```
2. Gere e instale o pacote, e copie os completamentos do fish:
   ```bash
   git clone https://github.com/caelestia-dots/cli.git && cd cli
   python -m build --wheel
   sudo python -m installer dist/*.whl
   sudo cp completions/caelestia.fish /usr/share/fish/vendor_completions.d/caelestia.fish
   ```

## Windows

Não suportado: a CLI controla um desktop Linux com Hyprland. O WSL2 (`wsl --install -d Ubuntu`) não serve aqui.

## Controles e configurações

- **Subcomandos:**
  - `shell`, `toggle`, `scheme`, `wallpaper` e `resizer`: controle do desktop;
  - `screenshot`, `record`, `clipboard` e `emoji`: capturas e utilitários;
  - `install` e `update`: instalação e atualização dos dotfiles.
- As opções ficam em `~/.config/caelestia/cli.json`:
  - temas aplicados a terminal, Hyprland, Discord, Spicetify, GTK, Qt, Chromium e outros;
  - ganchos depois de trocar o papel de parede;
  - as áreas especiais (`toggles`).
- Para o tema ao vivo em navegadores baseados em Chromium, a CLI precisa criar pastas em `/etc` via `sudo` sem senha. O README mostra o arquivo sudoers necessário.

## Fontes

- [README › Installation, Usage e Configuring](https://github.com/caelestia-dots/cli#readme)
- [Releases (v1.1.3)](https://github.com/caelestia-dots/cli/releases)

<!-- verificado: 2026-10-15 -->
