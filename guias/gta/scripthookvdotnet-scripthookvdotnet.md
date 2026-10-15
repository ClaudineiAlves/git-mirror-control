# Grand Theft Auto V · Script Hook V .NET (PC)

Repositório: https://github.com/scripthookvdotnet/scripthookvdotnet · Espelho: https://github.com/alves-r/mirror-scripthookvdotnet-scripthookvdotnet

Plugin ASI para o GTA V que roda dentro do jogo scripts escritos em qualquer linguagem .NET. É a base de muitos mods do modo história.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (v3.6.0, de 29/12/2022: `ScriptHookVDotNet.zip`). Para o jogo v1.0.3258.0 ou mais novo, use um build noturno v3.6.0-nightly.89 ou mais novo. |
| Precisa de emulador | Não |
| Você precisa fornecer | O GTA V de PC. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton (não documentado) |
| Windows | Nativo |
| Estado | Ativo. A versão estável é de 2022, e as novidades saem nos builds noturnos. |
| Dificuldade | Fácil (baixar e rodar) |

**Requisitos de fora do repositório:** o Script Hook V em C++, de Alexander Blade (http://www.dev-c.com/gtav/scripthookv/), o .NET Framework 4.8 ou mais novo e o Microsoft Visual C++ Redistributable v14 mais recente.

## Arch Linux

Não documentado no repositório. O GTA V roda pelo Proton, e o Script Hook V carrega os plugins por um `dinput8.dll` (sugestão, não oficial):

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o GTA V.
3. Faça a instalação da seção Windows na pasta do jogo, dentro de `~/.local/share/Steam/steamapps/common/`.
4. Nas **Propriedades** do jogo, em **Opções de inicialização**, coloque `WINEDLLOVERRIDES="dinput8=n,b" %command%`.

## Windows

1. Instale o Script Hook V, o .NET Framework 4.8 e o Visual C++ Redistributable.
2. Baixe o `ScriptHookVDotNet.zip` em https://github.com/scripthookvdotnet/scripthookvdotnet/releases. Para o jogo v1.0.3258.0 ou mais novo, baixe um build noturno em https://github.com/scripthookvdotnet/scripthookvdotnet-nightly/releases, ou faça downgrade do jogo para a v1.0.3179.0 ou anterior.
3. Extraia na pasta do jogo, onde fica o `GTA5.exe`, todos os arquivos da raiz do zip, menos o `README.txt` e as duas pastas.
4. Ao atualizar, troque **sempre juntos** o `ScriptHookVDotNet.asi`, o `ScriptHookVDotNet2.dll` e o `ScriptHookVDotNet3.dll`.

## Problemas conhecidos

- As versões v3.6.0 e v3.5.1 não funcionam com o jogo v1.0.3258.0 ou mais novo.
- Nos builds noturnos:
  - a API padrão dos scripts `.cs` e `.vb` passou da v2 para a v3. Indique a versão no nome do arquivo, como o README explica;
  - o `.ini` mudou. Use o que vem no build noturno, porque as opções que faltam não são acrescentadas sozinhas.

## Fontes

- [README › Requirements, Downloads e Installation](https://github.com/scripthookvdotnet/scripthookvdotnet#readme)
- [Releases (v3.6.0)](https://github.com/scripthookvdotnet/scripthookvdotnet/releases)

<!-- verificado: 2026-10-15 -->
