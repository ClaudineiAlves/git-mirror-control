# Super Mario 64 online · sm64coopdx (N64)

Repositório: https://github.com/coop-deluxe/sm64coopdx · Espelho: https://github.com/alves-r/mirror-coop-deluxe-sm64coopdx

Projeto de multiplayer online para o port de PC do Super Mario 64, que sincroniza inimigos e eventos entre os jogadores e aceita mods em Lua. É a continuação oficial do sm64ex-coop.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v1.5.1, de 01/06/2026: `sm64coopdx_Windows.zip`, `sm64coopdx_Linux.zip`, `sm64coopdx_SteamOS.zip` e macOS) |
| Precisa de emulador | Não |
| Você precisa fornecer | Uma cópia do Super Mario 64. O README e a wiki não detalham o arquivo esperado (não documentado no repositório). ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo. O objetivo inicial, o multiplayer, foi alcançado, e o foco agora é manutenção e a API Lua. |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

**Opção 1: release pronta**

1. Baixe `sm64coopdx_Linux.zip` em https://github.com/coop-deluxe/sm64coopdx/releases.
2. Extraia: `bsdtar -xf sm64coopdx_Linux.zip` (sugestão; o `unzip` não vem instalado na sua máquina).
3. Rode o executável `./sm64coopdx`. O pacote também traz `coopdx_updater`, a pasta `mods` e os idiomas.

**Opção 2: compilar** (wiki, "Compiling (Linux)")

1. Instale as dependências pela linha que a wiki dá para Arch e SteamOS:
   `sudo pacman -S base-devel glibc linux-api-headers python sdl2 glew zlib libglvnd curl libcurl-compat`
   No Arch, o `sdl2` é fornecido pelo `sdl2-compat`.
2. Clone: `git clone https://github.com/coop-deluxe/sm64coopdx.git && cd sm64coopdx`
3. Compile: `make -j`. Há opções de build documentadas na página "Build Flags" da wiki.

## Windows

1. Baixe `sm64coopdx_Windows.zip` em https://github.com/coop-deluxe/sm64coopdx/releases e extraia.
2. Abra o executável do jogo. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

**Compilar, opcional:** a página "Compiling (Windows)" da wiki usa o MSYS2:
1. Instale o MSYS2 e abra o **MINGW64**.
2. Rode `pacman -Syuu` para atualizar.
3. Instale os pacotes listados na wiki.
4. Rode `make` na pasta do projeto.

## Controles e configurações

- **Hospedar:** botão **Host** no menu. Com CoopNet, a senha em branco cria um lobby público, que aparece em **Join → Public Lobbies**. Também existe conexão direta.
- **Entrar:** botão **Join**, com lobbies públicos, privados ou conexão direta.
- **Conexão direta:** encaminhe a porta **7777/UDP** no roteador (ou use Hamachi). Para testar sozinho, abra duas janelas e conecte em `127.0.0.1`.
- **Convites pelo Discord:** exigem "Game Activity" ligada e não funcionam se você aparecer offline.
- **Mods em Lua:** documentação em `docs/lua/lua.md`.

## Fontes

- [README](https://github.com/coop-deluxe/sm64coopdx#readme)
- [Wiki › Compiling (Linux), Compiling (Windows) e Hosting and joining](https://github.com/coop-deluxe/sm64coopdx/wiki)
- [Releases](https://github.com/coop-deluxe/sm64coopdx/releases)

<!-- verificado: 2026-10-15 -->
