# Paper Mario · papermario (N64)

Repositório: https://github.com/pmret/papermario · Espelho: https://github.com/alves-r/mirror-pmret-papermario

Decompilação em andamento do Paper Mario de N64 que reconstrói a ROM original das versões EUA, Japão, PAL e iQue. Para jogar, a ROM gerada roda num emulador de N64.

| Item | Detalhe |
|---|---|
| Tipo | Decomp que gera ROM |
| Executável pronto | Não, precisa compilar |
| Precisa de emulador | Sim. No Linux: RMG (AUR `rmg`) ou mupen64plus (oficial). No Windows: RMG ou simple64. (Sugestão.) |
| Você precisa fornecer | Pelo menos uma ROM base como `ver/<região>/baserom.z64`: EUA `3837f44cda784b466c9a2d99df70d77c322b97a0`, Japão `b9cca3ff260b9ff427d981626b82f96de73586d3`, PAL `2111d39265a317414d359e35a7d971c4dfa5f9e1` ou iQue `5c724685085eba796537573dd6f84aaddedc8582` (SHA-1). ⚠️ Você indicou que não consegue dumpar N64. |
| Arch Linux | Nativo (via container Ubuntu, sugestão) |
| Windows | Via WSL (só para compilar) |
| Estado | Em andamento; o progresso por região aparece em papermar.io. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O SETUP.md suporta Linux, macOS, WSL 2 e Nix. Os scripts de dependência cobrem só Debian e Ubuntu, Fedora e macOS. O caminho por Nix exige as quatro ROMs base. Sugestão: rode o caminho do Ubuntu num container com distrobox.

1. Instale o distrobox (sugestão): `sudo pacman -S --needed distrobox podman`
2. Crie e entre num Ubuntu: `distrobox create --name pm --image ubuntu:24.04 && distrobox enter pm`
3. Dentro do container, clone o repositório:
   ```bash
   git clone https://github.com/pmret/papermario && cd papermario
   ```
4. Instale o pigment64 (ferramenta de imagens do projeto) e confira se ele ficou no PATH:
   ```bash
   curl https://sh.rustup.rs -sSf | sh
   cargo install pigment64
   ```
5. Instale as dependências e os compiladores: `./install_deps.sh && ./install_compilers.sh`
6. Copie a sua ROM para `ver/us/baserom.z64` (ou para a pasta da sua região).
7. Configure e extraia os assets: `./configure`
8. Compile: `ninja`. A mensagem `papermario.z64: OK` no fim indica que a ROM gerada bate com a original.
9. Fora do container, instale um emulador de N64 (sugestão: `yay -S rmg`) e abra a ROM gerada.

## Windows

1. Instale o WSL 2 com Ubuntu: no PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu: `sudo apt update && sudo apt upgrade && cd ~`
3. Siga os passos 3 a 8 da seção Arch Linux dentro do Ubuntu, já sem container.
4. O Explorador de Arquivos acessa o projeto em `\\wsl$\Ubuntu\home\<usuário>\papermario`. Copie a ROM gerada e abra-a num emulador de N64 do Windows, como RMG ou simple64 (sugestão).

## Fontes

- [README](https://github.com/pmret/papermario#readme)
- [SETUP.md](https://github.com/pmret/papermario/blob/main/SETUP.md)

<!-- verificado: 2026-10-15 -->
