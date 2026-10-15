# Bloodborne · BloodBorneButPc (PS4)

Repositório: https://github.com/Awakenchan/BloodBorneButPc · Espelho: https://github.com/alves-r/mirror-awakenchan-bloodbornebutpc

Pacote para Windows, com launcher e engine própria derivada do bbport, que roda o Bloodborne a partir do seu dump de PS4. O README não diz se o jogo já foi zerado nele.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (`BloodbornePC-v0.9.31-win64.zip` e `Bloodborne.Launcher.exe`, Windows x64) |
| Precisa de emulador | Não |
| Você precisa fornecer | Dump decriptado do Bloodborne (CUSA03173 ou outra região) com a atualização 1.09: a pasta que contém `eboot.bin`. ⚠️ Você não soube dizer se consegue dumpar PS4, e sem esse dump não há como jogar. |
| Arch Linux | Via Proton ou Wine (não oficial) |
| Windows | Nativo |
| Estado | Beta ativa: v0.9.31 (estável) e v0.9.32-beta.1, ambas de 15/10/2026. O README não diz se dá para zerar. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com `.exe` não assinado e sem checksum no release. Baixe só pela página de Releases do repositório e passe o arquivo no VirusTotal antes de abrir.

## Arch Linux

O projeto só publica build para Windows. No Arch, o caminho indicado é o **bbport** ([guia](deadinside28-bloodborne_pc.md)): o port nativo para Linux de onde esta engine saiu.

Se mesmo assim quiser este pacote, dá para tentar pelo Proton. Não é suportado oficialmente.

1. Habilite o repositório multilib, que está desligado na sua máquina: em `/etc/pacman.conf`, descomente as linhas `[multilib]` e `Include = /etc/pacman.d/mirrorlist` (sugestão).
2. Instale a Steam: `sudo pacman -Syu steam`
3. Baixe `BloodbornePC-v0.9.31-win64.zip` em https://github.com/Awakenchan/BloodBorneButPc/releases e extraia em uma pasta.
4. Na Steam, vá em **Adicionar jogo → Adicionar jogo não Steam → Procurar** e escolha `Bloodborne Launcher.exe`.
5. Em **Propriedades → Compatibilidade**, marque "Forçar o uso de uma ferramenta de compatibilidade" e escolha o **Proton Experimental**.
6. Abra pela Steam, escolha a pasta do jogo (a que tem `eboot.bin`) e clique em **Play**.

## Windows

1. Baixe `BloodbornePC-v0.9.31-win64.zip` em https://github.com/Awakenchan/BloodBorneButPc/releases. A `v0.9.32-beta.1` é a versão beta.
2. Extraia o zip em qualquer pasta.
3. Abra `Bloodborne Launcher.exe` (no release avulso, o arquivo aparece como `Bloodborne.Launcher.exe`). Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. Escolha a pasta do jogo (a que tem `eboot.bin`).
5. Clique em **Play**.
6. Opcional: `Bloodborne.exe` abre o jogo direto com as suas configurações, útil para criar atalho ou adicionar na Steam.

O launcher se atualiza sozinho pela página de Releases e deixa escolher entre o canal estável e o beta.

Para compilar o launcher, opcional: instale o .NET 8 SDK e rode `dotnet build launcher/windows/BloodborneLauncher.sln -c Release`. Os passos de build da engine ficam na pasta `engine/` do repositório.

## Controles e configurações

- Teclado e mouse funcionam em todas as ações. Os ícones de botão do jogo passam a mostrar suas teclas ou botões de Xbox.
- O remapeamento usa perfis JSON (`"format": "bbport-controls"`). Cada ação aceita uma tecla e uma entrada de mouse.
- Teclas usam os nomes do SDL (`Space`, `Left Shift`, `Return`, `F`).
- Entradas de mouse: `Mouse1` (esquerdo), `Mouse2` (meio), `Mouse3` (direito), `Mouse4`, `Mouse5`, `WheelUp` e `WheelDown`.
- Ações disponíveis: `move_forward`, `move_back`, `move_left`, `move_right`, `walk`, `roll`, `attack`, `strong_attack`, `transform`, `firearm`, `lock_on`, `blood_vial`, `use_item`, `interact`, `menu`, entre outras listadas no README.

## Fontes

- [README › Install](https://github.com/Awakenchan/BloodBorneButPc#install)
- [README › Features](https://github.com/Awakenchan/BloodBorneButPc#features)
- [README › Control profile format](https://github.com/Awakenchan/BloodBorneButPc#control-profile-format)
- [README › Building the launcher](https://github.com/Awakenchan/BloodBorneButPc#building-the-launcher)
- [README › Engine](https://github.com/Awakenchan/BloodBorneButPc#engine)
- [Releases](https://github.com/Awakenchan/BloodBorneButPc/releases)

<!-- verificado: 2026-10-15 -->
