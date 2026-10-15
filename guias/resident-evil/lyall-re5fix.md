# Resident Evil 5 · RE5Fix (PC)

Repositório: https://github.com/Lyall/RE5Fix · Espelho: https://github.com/alves-r/mirror-lyall-re5fix

Mod em DLL que corrige o Resident Evil 5 de PC em telas ultrawide e acrescenta ajustes: FOV, FPS acima de 120, remoção do filtro amarelo e qualidade das sombras.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (v1.0.4, de 03/05/2022: `RE5Fix_v1.0.4.zip`, com `xinput1_3.dll` e `RE5Fix.ini`) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Resident Evil 5 de PC. O mod foi feito para a versão da Steam com o mod "QOL Fixes" e **pode** funcionar com outras versões. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton (não oficial) |
| Windows | Nativo |
| Estado | Sem atualizações desde 2022. O ajuste de FOV ainda é experimental. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com DLL não assinada e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

## Arch Linux

O README só fala do Windows. O jogo da Steam roda pelo Proton, e o mod pode ser carregado assim (sugestão):

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o Resident Evil 5.
3. Extraia o `RE5Fix_v1.0.4.zip` na pasta do jogo, ex.: `~/.local/share/Steam/steamapps/common/Resident Evil 5`.
4. Nas **Propriedades** do jogo, em **Opções de inicialização**, coloque `WINEDLLOVERRIDES="xinput1_3=n,b" %command%` para o Proton carregar a DLL do mod.
5. Ajuste o `RE5Fix.ini` e abra o jogo.

## Windows

1. Baixe `RE5Fix_v1.0.4.zip` em https://github.com/Lyall/RE5Fix/releases.
2. Extraia na pasta do jogo, ex.: `steamapps\common\Resident Evil 5`.
3. Ajuste o `RE5Fix.ini` para ligar e configurar os recursos.
4. Abra o jogo normalmente.

## Problemas conhecidos

- **Erro "xlive.dll is missing":** o GFWL que vem com a versão da Steam não instala direito no Windows 10/11. O README indica um instalador do GFWL.
- **O `xinput1_3.dll` conflita com outro mod:** renomeie para `dinput8.dll` ou coloque na pasta de plugins do carregador de DLLs do outro mod.
- **Nada funciona:** reinstale o RE5 da Steam do zero, instale o mod "QOL Fixes" e depois o RE5Fix.

## Fontes

- [README › Features, Installation, Troubleshooting e Known Issues](https://github.com/Lyall/RE5Fix#readme)
- [Releases (v1.0.4)](https://github.com/Lyall/RE5Fix/releases)

<!-- verificado: 2026-10-15 -->
