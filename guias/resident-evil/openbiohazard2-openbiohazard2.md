# Resident Evil 2 · OpenBiohazard2 (PC)

Repositório: https://github.com/OpenBiohazard2/OpenBiohazard2 · Espelho: https://github.com/alves-r/mirror-openbiohazard2-openbiohazard2

Reimplementação aberta do motor do Resident Evil 2 original, escrita em Go com OpenGL. Usa os arquivos da sua cópia do jogo de PC e ainda está incompleta.

| Item | Detalhe |
|---|---|
| Tipo | Port / Recomp para compilar |
| Executável pronto | Não, precisa compilar. Há uma pré-release antiga para Windows (0.1.0, de 17/05/2024: `OpenBiohazard2-win64-0.1.0.zip`), sem instruções de uso. |
| Precisa de emulador | Não |
| Você precisa fornecer | Os arquivos do Resident Evil 2 original de PC, copiados da pasta de instalação para `data/`. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Incompleto. Já há colisão, gatilhos de eventos, animação e cenários pré-renderizados. Faltam áudio, inventário, IA dos inimigos, quebra-cabeças, transições de porta, sprites e sombras. |
| Dificuldade | Média (compilar com script) |

O README não lista dependências além do Go.

## Arch Linux

1. Instale: `sudo pacman -S --needed git go`
2. Clone: `git clone https://github.com/OpenBiohazard2/OpenBiohazard2 && cd OpenBiohazard2`
3. Copie todos os arquivos da sua instalação do jogo para a pasta `data/`.
4. Compile: `go build`
5. Rode o programa gerado na pasta: `./OpenBiohazard2`

## Windows

1. Instale o Go (go.dev) e o Git.
2. Clone o repositório e copie os arquivos da sua instalação do jogo para `data\`.
3. No terminal, dentro da pasta, rode `go build` e abra o `OpenBiohazard2.exe` gerado.

## Controles e configurações

- **W / S:** anda para frente / para trás.
- **A / D:** vira para a esquerda / direita.
- **Tab:** inventário.
- **Enter:** ação.

## Fontes

- [README › Installation, Task list e Controls](https://github.com/OpenBiohazard2/OpenBiohazard2#readme)
- [Releases (pré-release 0.1.0)](https://github.com/OpenBiohazard2/OpenBiohazard2/releases)

<!-- verificado: 2026-10-15 -->
