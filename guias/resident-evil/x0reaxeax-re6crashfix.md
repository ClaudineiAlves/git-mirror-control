# Resident Evil 6 · RE6CrashFix (PC)

Repositório: https://github.com/x0reaxeax/RE6CrashFix · Espelho: https://github.com/alves-r/mirror-x0reaxeax-re6crashfix

Correção em DLL para o Resident Evil 6 da Steam, que fecha logo ao abrir em monitores com mais de 256 modos de vídeo.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (1.0, de 08/03/2026: `d3d9.dll`; há uma pré-release experimental para quem usa DXVK) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Resident Evil 6 da Steam. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton (não documentado) |
| Windows | Nativo |
| Estado | Estável (1.0). A variante para DXVK é experimental. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com DLL não assinada e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

**Por que o jogo fecha:** ele guarda os modos de vídeo do monitor numa tabela de só 256 posições, sem checar o limite. Monitores modernos costumam ter mais modos que isso.

## Arch Linux

O README só trata do Windows e não diz se o problema acontece pelo Proton. Se o jogo fechar ao abrir no Proton, dá para testar a DLL assim (sugestão):

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o Resident Evil 6.
3. Coloque o `d3d9.dll` da versão 1.0 na pasta do `BH6.exe`, ex.: `~/.local/share/Steam/steamapps/common/Resident Evil 6`.
4. Nas **Propriedades** do jogo, em **Opções de inicialização**, coloque `WINEDLLOVERRIDES="d3d9=n,b" %command%`.

## Windows

1. Baixe o `d3d9.dll` da versão 1.0 em https://github.com/x0reaxeax/RE6CrashFix/releases.
2. Coloque na pasta do `BH6.exe`, ex.: `steamapps\common\Resident Evil 6`.
3. Abra o jogo normalmente.

**Se você usa o DXVK no Windows** (pré-release `dxvk-compat-experimental`):
1. Coloque o `d3d9.dll` do mod na pasta do jogo.
2. Renomeie o `d3d9.dll` do DXVK, ex.: para `DXVK.dll`.
3. Coloque o `re6cfg.json` em `resource\`.
4. Aponte o `d3dTargetPath` do arquivo para o `DXVK.dll` renomeado.
5. Se der certo, o `resource\re6crashfix.log` mostra `HookD3D9Object succeeded`.

## Controles e configurações

O mod fixa a resolução na da tela onde o jogo abre, e o menu de gráficos não mostra outras opções. Para mudar:

1. Abra o jogo uma vez com o mod, ou crie o arquivo à mão.
2. Edite `resource\re6cfg.json` na pasta do jogo:
   ```json
   {
     "displayWidth": 1920,
     "displayHeight": 1080
   }
   ```
3. Use uma resolução que o seu monitor suporte.

## Fontes

- [README › Usage, Notes e Technical problem description](https://github.com/x0reaxeax/RE6CrashFix#readme)
- [Releases (1.0 e dxvk-compat-experimental)](https://github.com/x0reaxeax/RE6CrashFix/releases)

<!-- verificado: 2026-10-15 -->
