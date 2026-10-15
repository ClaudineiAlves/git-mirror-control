# Grand Theft Auto IV: The Complete Edition · FusionFix (PC)

Repositório: https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix · Espelho: https://github.com/alves-r/mirror-thirteenag-gtaiv.eflc.fusionfix

Mod que corrige problemas do GTA IV: The Complete Edition e acrescenta opções para sistemas modernos: FOV, visual de console, desfoque de movimento, luzes distantes, ícones de controle e dezenas de correções de modelos, missões e scripts.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (v5.1.2, de 15/10/2026: `GTAIV.EFLC.FusionFix.zip`, instalador web, instalador offline e o `GTAIV.EFLC.FusionFixLegacyAddon.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | O GTA IV: The Complete Edition original, da Steam ou do Rockstar Games Launcher. Versões antigas (ex.: 1.0.7.0 e 1.0.8.0) também precisam do Legacy Addon. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton (suporte documentado) |
| Windows | Nativo |
| Estado | Ativo. Só para um jogador: o multiplayer não é suportado. |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

O README traz instruções para Proton e Wine:

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o GTA IV: The Complete Edition.
3. Baixe `GTAIV.EFLC.FusionFix.zip` em https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases e extraia na pasta do jogo, onde fica o executável.
4. Diga ao Proton para usar o `dinput8.dll` do mod. No Proton Experimental, isso já acontece por padrão. Nos outros, use uma das formas:
   - nas **Opções de inicialização** do jogo, coloque `WINEDLLOVERRIDES="dinput8=n,b" %command%`;
   - ou rode `WINEPREFIX="$HOME/.steam/steam/steamapps/compatdata/12210/pfx" winecfg` e, na aba **Libraries**, adicione `dinput8`. Ele deve aparecer como `(native, builtin)`.
5. O README também manda instalar o `d3dx9_43` pelo Protontricks:
   1. Abra o Protontricks e escolha **Grand Theft Auto IV**.
   2. Clique em **Select the default Wineprefix → Install a Windows DLL or component**.
   3. Marque `d3dx9_43` e confirme.

## Windows

1. Baixe `GTAIV.EFLC.FusionFix.zip` em https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases e extraia na pasta do jogo, onde fica o executável.
2. Outra opção é usar o `GTAIV.EFLC.FusionFixWebInstaller.exe` ou o `GTAIV.EFLC.FusionFixOfflineInstaller.exe`.
3. Em versões antigas do jogo, instale também o `GTAIV.EFLC.FusionFixLegacyAddon.zip`.

**Compilar, opcional:** rode `premake5.bat` para gerar a solução do Visual Studio em `build` e compile. Para copiar o `.asi` para o jogo depois de cada build, crie um arquivo `.env` na raiz com `GTAIV_DIR=<pasta do GTAIV.exe>` e rode o `premake5.bat` de novo.

## Controles e configurações

- O mod acrescenta opções ao menu do jogo, que mudam na hora:
  - **Display:** FOV, idioma, nitidez e gama de console, desfoque de movimento, profundidade de campo e luzes distantes;
  - **Graphics, Game, Audio e Controls:** mais ajustes, incluindo o estilo dos ícones de controle (Xbox, PlayStation, Switch e Steam Deck).
- Usuários avançados podem ajustar mais coisas no arquivo de configuração.

## Problemas conhecidos

- Cópias ilegais do jogo não têm suporte.
- Derivados do projeto para multiplayer são proibidos pelo autor.

## Fontes

- [README › Installation, New menu options e Building](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix#readme)
- [Releases (v5.1.2)](https://github.com/ThirteenAG/GTAIV.EFLC.FusionFix/releases)

<!-- verificado: 2026-10-15 -->
