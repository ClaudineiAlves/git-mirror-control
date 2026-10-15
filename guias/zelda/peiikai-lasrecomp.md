# The Legend of Zelda: Link's Awakening · LAS Recomp (Switch)

Repositório: https://github.com/peiikai/LASRecomp · Espelho: https://github.com/alves-r/mirror-peiikai-lasrecomp

Recompilação estática do Link's Awakening de Switch (2019) para Windows, Linux e macOS, com aspecto de tela livre e randomizer embutido. Está em beta.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (beta_4, de 15/10/2026: `LAS.Recomp-beta_4-linux-x86_64.AppImage`, `LAS.Recomp-beta_4-windows.zip`, macOS e Linux ARM experimental) |
| Precisa de emulador | Não |
| Você precisa fornecer | Os arquivos extraídos da sua cópia do Link's Awakening **v1.0.0** de Switch. O projeto não ensina a obtê-los. As fontes do sistema do Switch são opcionais e também têm de vir do seu console. ⚠️ Você indicou que não consegue dumpar Switch. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Beta. Há bugs e travamentos conhecidos, e algumas seeds do randomizer podem não ter solução. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal. O README avisa que o código foi escrito quase todo por IA (Claude), dirigida e testada por uma pessoa.

Requisitos: CPU x86-64 com AVX2 e placa de vídeo com Vulkan 1.3. No Linux, glibc 2.35 ou mais nova; no Windows, Windows 10 ou mais novo.

## Arch Linux

1. Baixe `LAS.Recomp-beta_4-linux-x86_64.AppImage` em https://github.com/peiikai/LASRecomp/releases.
2. Rode:
   ```bash
   chmod +x LAS.Recomp-beta_4-linux-x86_64.AppImage
   ./LAS.Recomp-beta_4-linux-x86_64.AppImage
   ```
3. Se der erro de FUSE, instale o `fuse3` (`sudo pacman -S --needed fuse3`) ou rode com `--appimage-extract-and-run`.
4. Na tela inicial, escolha a pasta com os arquivos do jogo. O programa prepara tudo, inclusive a recompilação local.
5. Tudo o que o programa grava fica em `~/.local/share/lasrecomp`: arquivos do jogo, saves, seeds, configurações e o log `lasrecomp.log`.

Vibração, LEDs e giroscópio dos controles PlayStation e Switch precisam de acesso a `/dev/hidraw*`, que as regras udev da Steam dão. Sem elas, o controle funciona pelo driver do kernel.

**Compilar, opcional** (`docs/linux.md`): o documento lista os pacotes do Ubuntu. No Arch, os equivalentes não estão documentados. Depois das dependências:
```bash
python3 -m venv tools/venv && tools/venv/bin/pip install lz4 capstone unicorn
make -j        # só a tela inicial: prepare os arquivos do jogo nela
make gen       # uma vez: recompila o jogo a partir dos seus arquivos
make -j        # gera build/lasrecomp
./build/lasrecomp
```

## Windows

1. Baixe `LAS.Recomp-beta_4-windows.zip` em https://github.com/peiikai/LASRecomp/releases.
2. Extraia a pasta `LAS Recomp` num lugar com permissão de escrita, fora de **Arquivos de Programas**. Saves e configurações ficam ao lado do `lasrecomp.exe`.
3. Abra o `lasrecomp.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. Na tela inicial, escolha a pasta com os arquivos do jogo.

**Compilar, opcional:** rode `powershell -ExecutionPolicy Bypass -File tools\setup_windows.ps1` na raiz do repositório. Ele instala o MSYS2 e o Python 3.12. Depois, num shell MSYS2 UCRT64, rode `make -j`, prepare os arquivos do jogo, rode `make gen` e `make -j` de novo. Detalhes em `docs/BUILD-windows.md`.

## Controles e configurações

- Teclado e controle, com todos os botões remapeáveis na aba **Controls** ou em **Settings → Controls** da tela inicial.
- **F1** (ou **Menos + Mais** no controle) abre o menu sobreposto.
- Na tela inicial, escolha entre o jogo normal e uma seed do randomizer.
- O idioma muda em **Settings → Controls**.

## Problemas conhecidos

- O controle não funciona na tela inicial.
- Examinar a cômoda no quarto da mãe do BowWow fecha o jogo.
- Clicar em **Title Screen** nas configurações próprias do LAS Recomp fecha o jogo.
- Às vezes aparecem caixas pretas nas salas das dungeons.
- Alguns efeitos de luz mostram linhas em dungeons, cavernas e casas.
- No randomizer da beta_4, recargas de bomba aparecem como **Bomb Bag**. Uma delas é a de verdade.

## Fontes

- [README › Status, Known issues, Features, Windows e Linux](https://github.com/peiikai/LASRecomp#readme)
- [docs/linux.md](https://github.com/peiikai/LASRecomp/blob/main/docs/linux.md)
- [docs/BUILD-windows.md](https://github.com/peiikai/LASRecomp/blob/main/docs/BUILD-windows.md)
- [Releases (beta_4)](https://github.com/peiikai/LASRecomp/releases)

<!-- verificado: 2026-10-15 -->
