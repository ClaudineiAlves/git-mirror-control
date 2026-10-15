# Grand Theft Auto V e Red Dead Redemption 2 · FiveM e RedM (PC)

Repositório: https://github.com/citizenfx/fivem · Espelho: https://github.com/alves-r/mirror-citizenfx-fivem

Código-fonte dos frameworks de modificação da Cfx.re: o FiveM (multiplayer personalizado do GTA V), o RedM (do Red Dead Redemption 2) e o servidor FXServer.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim, pelo launcher do site oficial (https://fivem.net ou https://redm.net). O repositório não publica binários. |
| Precisa de emulador | Não |
| Você precisa fornecer | O GTA V de PC (para o FiveM) ou o Red Dead Redemption 2 de PC (para o RedM). ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Não documentado no repositório |
| Windows | Nativo |
| Estado | Ativo |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

Não documentado no repositório: o README só fala do launcher do site, que é para Windows. Rodar o cliente pelo Proton seria uma tentativa não oficial, que pode não funcionar (sugestão):

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam: `sudo pacman -Syu steam`
3. Adicione o instalador do FiveM como **jogo não Steam** e force o **Proton Experimental** em **Propriedades → Compatibilidade**.

Para hospedar um servidor, o README manda para a página de hospedagem do site oficial (https://fivem.net/server-hosting).

## Windows

1. Baixe o launcher no site oficial: https://fivem.net (GTA V) ou https://redm.net (RDR2).
2. Instale e abra. Ele encontra o jogo e entra na lista de servidores.

**Compilar, opcional** (`docs/building.md`, para quem quer contribuir):
1. Instale os requisitos:
   - Visual Studio 2022 com as cargas **.NET desktop development**, **Desktop development with C++** e **Windows application development**, mais o .NET Framework 4.6 targeting pack e o Windows 11 SDK (10.0.22000.0);
   - PowerShell 7;
   - Python 3.8+ com o launcher `py`;
   - MSYS2 em `C:\msys64\`;
   - Node.js e Yarn.
2. Num `cmd.exe`:
   ```bat
   git clone https://github.com/citizenfx/fivem.git -c core.symlinks=true
   cd fivem
   git submodule update --jobs=16 --init
   pip install setuptools
   fxd get-chrome
   prebuild
   fxd gen -game five
   fxd vs -game five
   ```
3. Abra e compile a solução gerada. Para o RedM, use `-game rdr3`; para o servidor, `-game server`.

## Problemas conhecidos

- **No build próprio, só aparecem o fundo do menu, o cursor e o console (F8):** falta a pasta `code/bin/five/debug/citizen/ui`. Copie `%LocalAppData%/FiveM/FiveM.app/citizen/ui` da sua instalação normal.

## Fontes

- [README › Getting started](https://github.com/citizenfx/fivem#readme)
- [docs/building.md](https://github.com/citizenfx/fivem/blob/master/docs/building.md)

<!-- verificado: 2026-10-15 -->
