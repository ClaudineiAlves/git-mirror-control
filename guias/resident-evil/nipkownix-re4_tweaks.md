# Resident Evil 4 (UHD) · re4_tweaks (PC)

Repositório: https://github.com/nipkownix/re4_tweaks · Espelho: https://github.com/alves-r/mirror-nipkownix-re4_tweaks

Correções e ajustes para o port "UHD" do Resident Evil 4 na Steam. Traz FOV maior, ultrawide, desligar o V-Sync, imagem mais nítida e efeitos da versão de GameCube restaurados.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (1.9.1, de 22/03/2023: `re4_tweaks1.9.1.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Resident Evil 4 "UHD" da Steam (app 254700). ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton (suporte documentado) |
| Windows | Nativo |
| Estado | Ativo no código; a última versão publicada é de 2023. |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o Resident Evil 4.
3. Baixe `re4_tweaks1.9.1.zip` em https://github.com/nipkownix/re4_tweaks/releases.
4. Extraia a pasta `re4_tweaks`, o `dinput8.dll` e o `dinput8.ini` em `Resident Evil 4/Bin32`, dentro de `~/.local/share/Steam/steamapps/common/`.
5. Nas **Propriedades** do jogo, em **Opções de inicialização**, coloque `WINEDLLOVERRIDES="dinput8=n,b" %command%`, como o README pede.

## Windows

1. Baixe `re4_tweaks1.9.1.zip` em https://github.com/nipkownix/re4_tweaks/releases.
2. Extraia a pasta `re4_tweaks`, o `dinput8.dll` e o `dinput8.ini` em `Steam\steamapps\common\Resident Evil 4\Bin32`.
3. Abra o jogo normalmente.

## Controles e configurações

- **F1** abre o menu de configuração dentro do jogo. Também dá para editar o `dinput8.ini` à mão.
- Alguns ajustes:
  - FOV maior e correção do aspecto ultrawide (21:9 e 32:9);
  - remoção das faixas pretas em 16:10 e correção da escala de DPI;
  - V-Sync desligável e taxas de atualização diferentes de 60 Hz em tela cheia, o que corrige a tela preta ao abrir;
  - imagem sem o borrão do vertex buffer e sem granulação;
  - desfoque de profundidade e da mira da versão de GameCube;
  - janela sem bordas e volumes separados.

## Problemas conhecidos

- **Conflito com o "Ultimate Trainer Companion" do Raz0r**, que também usa o nome `dinput8`: renomeie os arquivos do re4_tweaks para `winmm` ou `xinput1_3`.
- **O jogo fecha ou não carrega:** confira os arquivos do jogo pela página de problemas conhecidos do RE4HD (link no README). Se não resolver, abra uma issue no GitHub. Para travamentos, crie uma pasta `CrashDumps` dentro de `Bin32` antes de reproduzir o erro.

## Fontes

- [README › Description, Current features, Installation e Support/Problems](https://github.com/nipkownix/re4_tweaks#readme)
- [Releases (1.9.1)](https://github.com/nipkownix/re4_tweaks/releases)

<!-- verificado: 2026-10-15 -->
