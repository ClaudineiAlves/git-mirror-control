# Call of Duty 4: Modern Warfare · iw3xo (PC)

Repositório: https://github.com/xoxor4d/iw3xo-dev · Espelho: https://github.com/alves-r/mirror-xoxor4d-iw3xo-dev

Mod de cliente para o Call of Duty 4 que acrescenta recursos ao jogo e o deixa compatível com o RTX Remix da NVIDIA. Tem exportação de mapas, ligação ao vivo com o editor Radiant, ciclo de dia e noite e opções de movimento.

| Item | Detalhe |
|---|---|
| Tipo | Mod / fix / cliente |
| Executável pronto | Sim (3550-remix-comp, de 13/07/2025: `cod4_iw3xo_rtx.7z`, `cod4_rtxcomp_mod.7z` e o RTX Remix; 3537, de 14/06/2024: `iw3xo_b3537.zip` e `iw3xo_b3537_rtx.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | O Call of Duty 4 de PC, versão 1.7, em inglês. Outros idiomas funcionam se forem renomeados. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Via Proton ou Wine (não documentado) |
| Windows | Nativo |
| Estado | Última versão em 07/2025. O próprio mod só deixa o jogo compatível com o Remix; materiais e modelos melhorados ficam num mod separado, no ModDB. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

## Arch Linux

Não documentado no repositório. O mod é para Windows. O jogo pode rodar pelo Proton (sugestão, não oficial):

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam (`sudo pacman -Syu steam`) e o Call of Duty 4.
3. Faça a instalação da seção Windows na pasta do jogo.
4. Na Steam, adicione o `iw3xo.exe` como **jogo não Steam** e force o **Proton Experimental** em **Propriedades → Compatibilidade**.

O RTX Remix exige placa NVIDIA RTX, e o README não fala de Linux.

## Windows

1. Deixe o jogo em inglês, se ainda não estiver:
   - na primeira linha de `localization.txt`, escreva `english`;
   - em `main/`, renomeie os `localized_<idioma>_iw**.iwd` para `localized_english_iw**.iwd`;
   - em `zone/`, renomeie a pasta do idioma para `english`.
2. Baixe a versão mais recente em https://github.com/xoxor4d/iw3xo-dev/releases. A variante `_rtx` traz tudo o que o RTX Remix precisa.
3. Extraia o conteúdo na pasta raiz do CoD4.
4. Para usar o RTX Remix, rode `run_remix.bat`. Sem ele, abra direto o `iw3xo.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.

Também há builds noturnos (link "Nightly" no README). Para eles, troque o `iw3x.dll` e, no caso do RTX, copie o conteúdo da pasta `assets-remix` para a raiz do jogo.

**Compilar, opcional:**
1. Clone o repositório. O zip do GitHub não traz as dependências.
2. Opcional: crie a variável de ambiente `COD4_ROOT` com a pasta do jogo.
3. Rode `generate-buildfiles_vs22.bat`.
4. Abra `build/iw3xo-dev.sln` no Visual Studio e compile.

## Controles e configurações

- `/devgui` no console abre a interface de desenvolvedor, com a aba **RTX**. Sugestão do README: `/bind F5 devgui`.
- Opções de linha de comando:
  - `-rtx`: obrigatória para o RTX Remix;
  - `-no_default_sky`, `-no_sun` e `-no_fog`: desligam céu, sol e neblina;
  - `-stock_effects`: desenha os efeitos com shaders.
- Exemplo: `iw3xo.exe -rtx -no_default_sky -stock_effects`

## Problemas conhecidos

- Mudanças bruscas de geometria, como teletransporte, podem fechar o jogo. Aumente o culling ou ajuste `r_lodScaleRigid`.
- O Remix pode tentar usar a placa de vídeo integrada. Desative-a na BIOS ou no Gerenciador de Dispositivos.
- Alguns efeitos deixam o jogo lento.

## Fontes

- [README › Usage, Remix section, Current Issues, Requirements e How to build](https://github.com/xoxor4d/iw3xo-dev#readme)
- [Releases](https://github.com/xoxor4d/iw3xo-dev/releases)

<!-- verificado: 2026-10-15 -->
