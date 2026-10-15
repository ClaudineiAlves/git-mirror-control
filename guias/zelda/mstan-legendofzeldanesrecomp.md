# The Legend of Zelda · LegendOfZeldaNESRecomp (NES)

Repositório: https://github.com/mstan/LegendOfZeldaNESRecomp · Espelho: https://github.com/alves-r/mirror-mstan-legendofzeldanesrecomp

Recompilação estática do primeiro The Legend of Zelda de NES, com launcher, mods opcionais (HD remasterizado e visão Voxel 3D) e binário pronto para Windows.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim, só Windows (v1.9.1, de 07/10/2026: `LegendOfZeldaNESRecomp-windows-x64.zip`, com `SHA256SUMS.txt`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM The Legend of Zelda (EUA), revisão PRG0. ⚠️ Você indicou que não consegue dumpar NES. |
| Arch Linux | Via Proton (não oficial) |
| Windows | Nativo |
| Estado | Ativo. O Voxel 3D é experimental. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado. Baixe só pela página de Releases, confira com o `SHA256SUMS.txt` e passe o arquivo no VirusTotal.

## Arch Linux

O README não documenta o build no Linux além do `setup.sh`, e só há binário para Windows. Dá para tentar pelo Proton, mas não é suportado oficialmente:

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam: `sudo pacman -Syu steam`
3. Baixe `LegendOfZeldaNESRecomp-windows-x64.zip` e `SHA256SUMS.txt` em https://github.com/mstan/LegendOfZeldaNESRecomp/releases. Confira com `sha256sum -c SHA256SUMS.txt --ignore-missing` e extraia.
4. Na Steam, vá em **Adicionar jogo → Adicionar jogo não Steam** e escolha `LegendOfZeldaNESRecomp.exe`.
5. Em **Propriedades → Compatibilidade**, force o **Proton Experimental**.
6. Abra pela Steam e escolha a sua ROM quando pedir.

O repositório tem um script `tools/build-linux.sh` com as opções explicadas no cabeçalho, como `--rom` e `--no-package`. O README, porém, não ensina a usá-lo.

## Windows

1. Baixe `LegendOfZeldaNESRecomp-windows-x64.zip` e `SHA256SUMS.txt` em https://github.com/mstan/LegendOfZeldaNESRecomp/releases.
2. Confira o hash no PowerShell: `Get-FileHash .\LegendOfZeldaNESRecomp-windows-x64.zip` e compare com o `SHA256SUMS.txt`.
3. Extraia e abra `LegendOfZeldaNESRecomp.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. Escolha a sua ROM dos EUA quando pedir. O caminho fica salvo.

**Compilar, opcional:**
1. Instale o Visual Studio 2022 e o CMake 3.20+.
2. Rode `setup.bat`.
3. Gere e compile o projeto:
   ```bash
   cmake -S . -B build-cycle -G "Visual Studio 17 2022" -A x64 -DNESRECOMP_ROM="C:/Jogos/Legend of Zelda.NES"
   cmake --build build-cycle --config Release
   ```
4. Ao jogar, escolha a mesma ROM PRG0 dos EUA.

## Controles e configurações

| NES | Tecla |
|---|---|
| Direcional | Setas |
| A / B | Z / X |
| Start / Select | Enter / Barra invertida |

- **Esc:** menu e configurações.
- **Tab:** segure para acelerar.
- **F8 / F9:** salva e carrega o estado.
- **F11:** tela cheia.
- **F12:** captura de tela.
- **Num 0:** liga ou desliga o Voxel 3D.

Os mods ficam na página **Mods** do launcher:
- **Zelda Remastered HD:** você gera um pacote local a partir do seu pack HD do Mesen, com `python tools/import_hdpack.py`. Ele não pode ficar ligado junto com as visões voxel.
- **Startup and Crash Diagnostics:** se o jogo não abrir e não mostrar erro, ligue antes de clicar em PLAY. Ele gera logs na pasta `diagnostics`.

## Problemas conhecidos

- Os save states antigos não funcionam no backend novo ("cycle"). O progresso da bateria continua valendo.
- O Remastered HD não troca músicas nem efeitos sonoros.
- As visões Voxel têm limitações de câmera e geometria.

## Fontes

- [README › Quick Start, Controls, Zelda Remastered HD Mod, Building from Source e Known Limitations](https://github.com/mstan/LegendOfZeldaNESRecomp#readme)
- [Releases (v1.9.1)](https://github.com/mstan/LegendOfZeldaNESRecomp/releases)

<!-- verificado: 2026-10-15 -->
