# God of War · god-of-war-recomp (PS2)

Repositório: https://github.com/KIexster/god-of-war-recomp · Espelho: https://github.com/alves-r/mirror-kiexster-god-of-war-recomp

Port nativo experimental para Windows do God of War de PS2 (NTSC-U, `SCUS-97399`), feito por recompilação estática com o PS2Recomp. Já chega ao gameplay, mas roda a uns 12 fps por padrão.

| Item | Detalhe |
|---|---|
| Tipo | Port / Recomp para compilar |
| Executável pronto | Não, precisa compilar |
| Precisa de emulador | Não |
| Você precisa fornecer | Sua cópia de God of War (PS2, NTSC-U, `SCUS-97399`): o executável `SCUS_973.99` (em `game\`), os módulos `.IRX` do disco (`SMPD_IOP.IRX`, `989NOMID.IRX`, `LIBSD.IRX`…) ao lado dele e a ISO original com o nome `God of War.iso`, na pasta acima. ⚠️ Você indicou que não consegue dumpar PS2. |
| Arch Linux | Não suportado |
| Windows | Nativo |
| Estado | Experimental. Abre, carrega do ISO e chega aos menus e ao gameplay. Nas docas de Atenas roda a ~12 fps (~25 com as threads opcionais; a meta é 30). O vídeo de abertura funciona; o áudio engasga e a renderização ainda está em ajuste. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

Não disponível no Linux: o projeto só documenta o build para Windows 10/11 com MSVC.

Como alternativa, o God of War original de PS2 roda no emulador PCSX2 ([guia](../recomp-e-emulacao/pcsx2-pcsx2.md)), que também exige o seu dump.

## Windows

Requisitos do projeto: Windows 10/11 x64, cerca de 10 GB livres e 16 GB de RAM recomendados (o build usa todos os núcleos).

1. **Arquivos do jogo:** copie o executável do seu disco ou ISO para `game\SCUS_973.99` (ou aponte a variável `GOW_ELF` para ele).
2. Ponha os módulos `.IRX` do disco ao lado do executável.
3. Coloque a ISO original com o nome `God of War.iso` na pasta acima da pasta do executável (ou defina a variável `GOW_ISO` com o caminho).
4. Opcional, para extrair também os dados da segunda camada do DVD:
   ```powershell
   powershell -ExecutionPolicy Bypass -File tools\extraer_capa2.ps1 -Iso "D:\God of War.iso" -Salida "D:\GOW ISO extraida"
   ```
5. **Ferramentas, só na primeira vez:** `scripts\1_instalar_herramientas.cmd`. Ele instala o Git e o Visual Studio 2022 Build Tools (com C++, CMake e Ninja) pelo `winget`.
6. **Compile:** `scripts\2_compilar.cmd`. Na primeira vez leva de 20 a 40 minutos. O script clona o PS2Recomp em `<drive>:\gowport` (caminho curto, para fugir do limite de 260 caracteres; configurável com `GOW_WORK`), aplica os patches, gera o C++ e compila `ps2EntryRunner.exe`. O log fica em `logs\2_compilar.log`.
7. **Rode:**
   - `scripts\3_ejecutar.cmd` roda por 60 segundos e salva a saída em `logs\`;
   - `scripts\3_ejecutar_manual.cmd` roda sem limite de tempo.

Para chegar a ~25 fps, ative as threads opcionais antes de rodar: `PS2X_VU1_HILO=1`, `PS2X_GS_FRENTE=1` e `GOW_GS_FINISH_ASINCRONO=1`.

## Problemas conhecidos

- O desempenho ainda está abaixo do jogável: ~12 fps por padrão.
- O áudio engasga na velocidade atual.
- Só o vídeo de abertura foi verificado. Formatar o memory card ainda não foi testado.

## Fontes

- [README › Current status, Requirements e Building and running](https://github.com/KIexster/god-of-war-recomp#readme)
- [docs/estado/detalle.en.md](https://github.com/KIexster/god-of-war-recomp/blob/main/docs/estado/detalle.en.md)

<!-- verificado: 2026-10-15 -->
