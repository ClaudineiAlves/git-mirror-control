# Silent Hill 2 · SH2EE web installer (PC)

Repositório: https://github.com/nipkownix/SH2EE-web-installer · Espelho: https://github.com/alves-r/mirror-nipkownix-sh2ee-web-installer

> O README avisa que este código fica aqui **só como arquivo e referência**. Para instalar o SH2EE, baixe o instalador oficial no site do projeto (http://enhanced.townofsilenthill.com/SH2/).

Código-fonte, em Inno Setup, do instalador web do Silent Hill 2: Enhanced Edition. Começou como estudo e virou parte oficial do projeto. Ele baixa e instala os componentes do SH2EE ([guia do módulo](elishacloud-silent-hill-2-enhancements.md)).

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim, só Windows (1.1.2, de 04/04/2023: `SH2EEsetup.exe`), mas o README manda usar a versão do site oficial |
| Precisa de emulador | Não |
| Você precisa fornecer | O Silent Hill 2 original de PC, onde o SH2EE será instalado. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Não documentado no repositório |
| Windows | Nativo |
| Estado | Arquivo de referência. A versão de uso fica no site do SH2EE. |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

Não documentado no repositório. O instalador é um programa de Windows. Um caminho possível é rodá-lo pelo Proton, no mesmo prefixo do jogo (sugestão, não oficial; veja o [guia do módulo](elishacloud-silent-hill-2-enhancements.md)).

## Windows

1. Baixe o instalador oficial no site do SH2EE (http://enhanced.townofsilenthill.com/SH2/), como o README recomenda.
2. Abra o instalador. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Escolha a pasta do Silent Hill 2 e os componentes a instalar.

Para compilar o instalador, o README cita o Inno Setup e o Inno Download Plugin. O script principal é o `SH2EE-web-installer.iss`.

## Fontes

- [README](https://github.com/nipkownix/SH2EE-web-installer#readme)
- [Releases (1.1.2)](https://github.com/nipkownix/SH2EE-web-installer/releases)

<!-- verificado: 2026-10-15 -->
