# Caelestia Shell · shell (Linux)

Repositório: https://github.com/caelestia-dots/shell · Espelho: https://github.com/alves-r/mirror-caelestia-dots-shell

Shell de desktop fluido e animado do Caelestia, feito em QML com o [Quickshell](quickshell-mirror-quickshell.md): barra, launcher, dashboard, notificações, tela de bloqueio e mais. Para o conjunto completo, com Hyprland e programas, veja os [dotfiles](caelestia-dots-caelestia.md).

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim, pelo AUR (`caelestia-shell` 2.5.0). Os Releases têm só o código (v2.5.0, de 18/09/2026: `caelestia-shell-v2.5.0.tar.gz`). |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Não suportado (é um shell de desktop Linux/Wayland) |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Instale pelo AUR: `paru -S caelestia-shell`. Também existe o `caelestia-shell-git`, que acompanha o último commit e é instável.
2. Inicie com `caelestia shell -d` (preferido) ou `qs -c caelestia -n -d`. Sem o `-d`, ele fica preso ao terminal.
3. Com os dotfiles do Caelestia, o shell já abre sozinho no login.
4. Para atualizar:
   - com os dotfiles ou a CLI: `caelestia update`;
   - só o shell: pelo seu gerenciador do AUR, ex.: `paru`.

Não edite os arquivos instalados pelo pacote do AUR. Para mexer no shell, use a instalação manual.

**Instalação manual:**
1. Instale as dependências listadas no README. Entre elas:
   - `caelestia-cli`, `quickshell-git` (tem de ser a versão git), `qt6-m3shapes-git`;
   - `ddcutil`, `brightnessctl`, `libcava`, `networkmanager`, `lm_sensors`, `aubio`, `libpipewire`, `libqalculate`, `power-profiles-daemon`, `swappy`, `fish`;
   - as fontes `ttf-material-symbols-variable`, `ttf-rubik-vf` e `ttf-cascadia-code-nerd`;
   - para compilar, `cmake`, `ninja` e `qt6-shadertools`.
2. Clone e instale:
   ```bash
   cd $XDG_CONFIG_HOME/quickshell
   git clone https://github.com/caelestia-dots/shell.git caelestia
   cd caelestia
   cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/
   cmake --build build
   sudo cmake --install build
   ```
3. Para atualizar: `git pull` na pasta clonada.

## Windows

Não suportado: é um shell de desktop Linux para Wayland. O WSL2 (`wsl --install -d Ubuntu`) não substitui o desktop do Windows, então não serve aqui.

## Controles e configurações

- Todas as opções ficam em `~/.config/caelestia/shell.json`. O arquivo não é criado sozinho: crie-o à mão. O que ficar de fora usa o valor padrão.
- **Por monitor:** crie `~/.config/caelestia/monitors/<nome>/shell.json`. Liste os nomes com `hyprctl monitors -j | jq -r '.[].name'`. Algumas opções só valem na configuração global; a lista está no README.

## Fontes

- [README › Installation, Usage, Updating, Configuring e Per-monitor configuration](https://github.com/caelestia-dots/shell#readme)
- [Releases (v2.5.0)](https://github.com/caelestia-dots/shell/releases)

<!-- verificado: 2026-10-15 -->
