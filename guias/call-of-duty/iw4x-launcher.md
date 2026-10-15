# Call of Duty: Modern Warfare 2 (2009) · IW4x Launcher (PC)

Repositório: https://github.com/iw4x/launcher · Espelho: https://github.com/alves-r/mirror-iw4x-launcher

Launcher e atualizador multiplataforma do IW4x, o cliente multiplayer da comunidade para o Modern Warfare 2 de 2009. Instala os dois clientes (IW4x e IW4x mm), cria atalhos e, no Linux, abre o jogo pelo Proton.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim (v1.1.8-b.25, de 13/10/2026: `launcher-1.1.8-b.25-x86_64-linux-glibc.tar.xz` e `launcher-1.1.8-b.25-x86_64-windows.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Modern Warfare 2 (2009) instalado pela Steam. Cópias da Microsoft Store não são compatíveis. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Nativo (o launcher abre o jogo pelo Proton) |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

O README só explica como compilar. O uso abaixo vem do texto de ajuda do programa (`--help`), definido em `launcher/launcher/launcher.cli`. O README não diz em que pasta colocar o launcher.

## Arch Linux

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o Modern Warfare 2 (2009).
3. Baixe `launcher-1.1.8-b.25-x86_64-linux-glibc.tar.xz` em https://github.com/iw4x/launcher/releases e extraia: `tar -xJf launcher-1.1.8-b.25-x86_64-linux-glibc.tar.xz`
4. Rode `./iw4x-launcher`. Ele baixa os arquivos do IW4x, cria atalhos, adiciona os dois clientes à Steam como jogos não Steam e abre o jogo pelo Proton.
5. Para usar o contêiner Steam Linux Runtime em vez do Proton avulso, rode com `--force-steam-runtime`.

## Windows

1. Baixe `launcher-1.1.8-b.25-x86_64-windows.zip` em https://github.com/iw4x/launcher/releases e extraia.
2. Abra o launcher. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Ele baixa e atualiza o IW4x e cria os atalhos.

**Compilar, opcional:** o projeto usa o sistema de build build2 (toolchain "staged") com GCC no Linux ou MinGW no Windows. Os comandos `bpkg create`, `bpkg build` e `bpkg install` estão no README.

## Controles e configurações

Opções do launcher:
- `--arch x86` abre o **IW4x**, com servidores dedicados da comunidade. `--arch x64` abre o **IW4x (mm)**, com matchmaking, amigos e grupos. Sem a opção, o launcher pergunta.
- `--prerelease`: recebe as versões beta.
- `--skip-launch`: só atualiza, sem abrir o jogo.
- `--no-shortcuts`: não recria atalhos nem as entradas na Steam.
- `--game-args <arg>`: passa argumentos ao jogo.
- `--proxy <url>`: usa um proxy HTTP, HTTPS ou SOCKS5.
- O launcher também registra o protocolo `iw4x://`.

## Fontes

- [README › Getting Started e Consumption](https://github.com/iw4x/launcher#readme)
- [launcher/launcher/launcher.cli (texto do `--help`)](https://github.com/iw4x/launcher/blob/main/launcher/launcher/launcher.cli)
- [Releases (v1.1.8-b.25)](https://github.com/iw4x/launcher/releases)

<!-- verificado: 2026-10-15 -->
