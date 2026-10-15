# Shadow of the Colossus (remake) · ShadowOfTheColossus-PC (PS4)

Repositório: https://github.com/AjncSystem/ShadowOfTheColossus-PC · Espelho: https://github.com/alves-r/mirror-ajncsystem-shadowofthecolossus-pc

Port nativo para Windows do remake de Shadow of the Colossus de PS4 (CUSA08809), com launcher próprio. O README não diz se o jogo foi zerado nele.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (`SotC-PC.zip` da v0.57, de 14/10/2026, para Windows 10/11 64 bits) |
| Precisa de emulador | Não |
| Você precisa fornecer | O dump CUSA08809 (de preferência EU 1.01), com `eboot.bin`, `sce_module` e `sce_sys`. Também os módulos de som decriptados `libSceNgs2.sprx` e `libSceUlt.sprx`, do seu PS4 ou da pasta `user/sys_modules` de um shadPS4 que você já tenha; sem eles o jogo fica mudo. ⚠️ Você não soube dizer se consegue dumpar PS4. |
| Arch Linux | Via Proton ou Wine (não oficial) |
| Windows | Nativo |
| Estado | Ativo (v0.57, de 14/10/2026). Os modos 60 FPS e filtro 16x só valem para a EU 1.01; as outras versões rodam a 30 FPS. O README não diz se dá para zerar. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com `.exe` não assinado e sem checksum no release. Baixe só pela página de Releases do repositório e passe o arquivo no VirusTotal.

O projeto pede placa de vídeo com Vulkan 1.3 (NVIDIA, AMD ou Intel com driver recente).

## Arch Linux

O projeto só publica build para Windows. Dá para tentar pelo Proton, mas não é suportado oficialmente:

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente `[multilib]` e a linha `Include` logo abaixo (sugestão).
2. Instale a Steam: `sudo pacman -Syu steam`
3. Baixe `SotC-PC.zip` em https://github.com/AjncSystem/ShadowOfTheColossus-PC/releases e extraia numa pasta.
4. Na Steam, vá em **Adicionar jogo → Adicionar jogo não Steam** e escolha `SotC.exe`.
5. Em **Propriedades → Compatibilidade**, force o **Proton Experimental**.
6. Abra pela Steam e siga os passos 3 e 4 da seção Windows.

## Windows

1. Baixe `SotC-PC.zip` em https://github.com/AjncSystem/ShadowOfTheColossus-PC/releases e descompacte numa pasta.
2. Abra **`SotC.exe`**. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**. Na primeira vez, o launcher procura sozinho nos discos do PC:
   - a pasta do jogo (o dump CUSA08809);
   - os módulos de som de um shadPS4 instalado, que ele copia para a pasta de dados do port;
   - um save do jogo no shadPS4, que ele oferece importar;
   - as DLCs, se houver.
3. Confira a página **Jogo e saves**. A biblioteca funciona como a do shadPS4: adicione a pasta dos seus jogos e escolha o jogo na lista.
4. Clique em **JOGAR**.

Não é preciso instalar Python.

**Compilar, opcional:** no MSYS2 (terminal CLANG64), com os pacotes listados em `packaging/windows/README.md`:

```bash
bash build.sh                              # gera out/bb-probe.exe
bash packaging/windows/package_sotc.sh     # gera dist/SotC-PC.zip
```

Para montar o `SotC.exe`, é preciso um Python do Windows com PyInstaller e Pillow (variável `WINPYTHON`).

## Controles e configurações

- Funcionam DualShock 4, DualSense e Xbox, com câmera no mouse e teclas remapeáveis.
- O launcher oferece saída de 720p a 4K. O jogo renderiza em 1080p, com upscale por FSR 1 e RCAS.
- Também há modo PS4 Pro, 60 FPS e filtro 16x, variáveis da engine Bluepoint e atalho na área de trabalho.
- O log da sessão fica em `user/last_run.log`.

## Problemas conhecidos

- **Depois de atualizar:** a primeira abertura recompila os shaders, então o primeiro carregamento é lento e engasga.
- **Placas AMD:** a v0.57 traz a correção do tom verde/rosa, mas ela ainda não foi testada numa placa AMD.
- **8 GB de memória de vídeo:** o uso chega perto do limite nas áreas grandes.

## Fontes

- [README › Download e uso, Os arquivos que você precisa ter e O lançador](https://github.com/AjncSystem/ShadowOfTheColossus-PC#readme)
- [README › Known issues, Launcher features e Compilar / Building](https://github.com/AjncSystem/ShadowOfTheColossus-PC#known-issues)
- [Releases](https://github.com/AjncSystem/ShadowOfTheColossus-PC/releases)

<!-- verificado: 2026-10-15 -->
