# Super Mario World · SuperMarioWorldRecomp (SNES)

Repositório: https://github.com/mstan/SuperMarioWorldRecomp · Espelho: https://github.com/alves-r/mirror-mstan-supermarioworldrecomp

Recompilação estática do Super Mario World, com binário pronto para Windows e Linux. O autor acredita que dá para jogar do início ao fim: os mundos 1 e 2 foram verificados à mão.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v0.14.2, de 22/09/2026: `SuperMarioWorldRecomp-windows-x64-v0.14.2.zip` e `SuperMarioWorldRecomp-linux-0.14.2-x86_64.AppImage`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ROM do Super Mario World (EUA), em `.sfc` ou `.smc`. ⚠️ Você indicou que não consegue dumpar SNES. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | "Believed fully playable": Yoshi's Island e Donut Plains foram verificados de ponta a ponta, Vanilla Dome está em andamento e os mundos 4 a 7 ainda não foram verificados. Desenvolvimento ativo; só o branch `main` tem build garantido. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado. A v0.14.2 não traz checksum (a v0.14.1 trazia `SHA256SUMS.txt`). Baixe só pela página de Releases e passe o arquivo no VirusTotal.

## Arch Linux

1. Baixe `SuperMarioWorldRecomp-linux-0.14.2-x86_64.AppImage` em https://github.com/mstan/SuperMarioWorldRecomp/releases.
2. Instale o FUSE 2, que os AppImages usam no Arch (sugestão): `sudo pacman -S --needed fuse2`
3. Dê permissão e abra: `chmod +x SuperMarioWorldRecomp-linux-0.14.2-x86_64.AppImage && ./SuperMarioWorldRecomp-linux-0.14.2-x86_64.AppImage`
4. Na primeira vez, escolha a sua ROM do Super Mario World (EUA). O caminho fica salvo em `rom.cfg`.

O README só documenta compilação no Windows.

## Windows

1. Baixe `SuperMarioWorldRecomp-windows-x64-v0.14.2.zip` em https://github.com/mstan/SuperMarioWorldRecomp/releases e extraia.
2. Abra `SuperMarioWorldSNESRecomp.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
3. Na primeira vez, escolha a sua ROM (EUA). O caminho fica salvo em `rom.cfg`, ao lado do executável.

**Compilar, opcional:** precisa de Windows 10 ou mais novo, Visual Studio 2022 (carga de C++ para desktop), Python 3.9+ no PATH e `rustup`.

```bash
git clone --recurse-submodules https://github.com/mstan/SuperMarioWorldRecomp
cd SuperMarioWorldRecomp
bash tools/regen.sh --stock
msbuild smw.sln /p:Configuration=Production /p:Platform=x64 /m
```

O `regen.sh` gera o código C a partir da sua ROM, que fica fora do repositório.

## Controles e configurações

Teclado padrão (o `keybinds.ini` é criado ao lado do executável na primeira execução; edite e reinicie):

| SNES | Tecla |
|---|---|
| Direcional | Setas |
| A / B / X / Y | X / Z / S / A |
| L / R | C / V |
| Start / Select | Enter / Shift direito |

Controles de Xbox, PlayStation e Switch Pro são detectados sozinhos. O mapeamento segue a posição física (o botão de baixo é o B do SNES) e muda na seção `[GamepadMap]` do `config.ini`.

| Ação | Tecla |
|---|---|
| Salvar / carregar estado 1–10 | Shift+F1..F10 / F1..F10 |
| Pausa | P |
| Reiniciar | Ctrl+R |
| Tela cheia | Alt+Enter |
| Turbo | Tab |

Há também uma build de co-op simultâneo (`SuperMarioWorldCoopSNESRecomp`), que aplica um patch IPS sobre a sua ROM, e um modo widescreen experimental.

## Problemas conhecidos

- Os mundos 4 a 7, a Star Road e o Special World ainda não foram verificados.
- Na build de co-op, o widescreen fica desligado e a imagem é sempre 4:3.

## Fontes

- [README › Current status, Quick start, Simultaneous co-op build, Controls e Building](https://github.com/mstan/SuperMarioWorldRecomp#readme)
- [Releases](https://github.com/mstan/SuperMarioWorldRecomp/releases)

<!-- verificado: 2026-10-15 -->
