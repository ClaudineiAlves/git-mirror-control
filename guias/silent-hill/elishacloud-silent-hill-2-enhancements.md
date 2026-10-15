# Silent Hill 2 · Silent Hill 2: Enhanced Edition (PC)

Repositório: https://github.com/elishacloud/Silent-Hill-2-Enhancements · Espelho: https://github.com/alves-r/mirror-elishacloud-silent-hill-2-enhancements

Módulo que melhora os gráficos e o áudio do Silent Hill 2 de PC, com modo de 60 FPS, dezenas de correções de cenas e iluminação e carregador de ASI. É a base do projeto Silent Hill 2: Enhanced Edition (SH2EE).

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (v3.0.2218.0, de 07/10/2024: `d3d8.zip`, `d3dx.zip` e `SH2EEconfig.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Silent Hill 2 original de PC. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton ou Wine (não documentado) |
| Windows | Nativo |
| Estado | Ativo no código. O módulo tem atualização automática. |
| Dificuldade | Fácil (baixar e rodar) |

O passo a passo de instalação **não está no repositório**: o README manda para o guia do site oficial (http://www.enhanced.townofsilenthill.com/SH2/), que usa o instalador do SH2EE ([guia do instalador](nipkownix-sh2ee-web-installer.md)).

## Arch Linux

Não documentado no repositório. O README cita uma correção para o WineD3D ("Reset Screen Res"), o que indica uso com Wine. Um caminho possível é o Proton (sugestão, não oficial):

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e adicione o jogo como **jogo não Steam**, forçando o **Proton Experimental** em **Propriedades → Compatibilidade**.
3. Instale o SH2EE pelo instalador oficial, rodando-o no mesmo prefixo do Proton.
4. Para o Proton carregar o módulo, coloque nas **Opções de inicialização**: `WINEDLLOVERRIDES="d3d8=n,b" %command%` (sugestão).

## Windows

1. Siga o guia de instalação do site oficial (http://www.enhanced.townofsilenthill.com/SH2/), que usa o instalador do SH2EE.
2. Os arquivos do módulo também estão em https://github.com/elishacloud/Silent-Hill-2-Enhancements/releases (`d3d8.zip`, `d3dx.zip` e o configurador `SH2EEconfig.zip`). O README não explica a instalação manual.

## Controles e configurações

- As opções ficam num arquivo `.ini`. O exemplo completo está em [`Common/Settings.ini`](https://github.com/elishacloud/Silent-Hill-2-Enhancements/blob/master/Common/Settings.ini).
- Os detalhes de cada opção estão na página "Configuration Details" do site oficial.
- **Alt+Enter:** alterna entre tela cheia e janela.

## Fontes

- [README › Introduction, Features, Installation Guide e Configuration](https://github.com/elishacloud/Silent-Hill-2-Enhancements#readme)
- [Releases (v3.0.2218.0)](https://github.com/elishacloud/Silent-Hill-2-Enhancements/releases)

<!-- verificado: 2026-10-15 -->
