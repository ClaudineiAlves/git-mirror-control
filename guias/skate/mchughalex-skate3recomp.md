# Skate 3 · skate3recomp (Xbox 360)

Repositório: https://github.com/mchughalex/skate3recomp · Espelho: https://github.com/alves-r/mirror-mchughalex-skate3recomp

Recompilação nativa e não oficial do Skate 3 de Xbox 360 para Windows, Linux e macOS. Desde a v2.0.0 tem renderizador próprio, em Direct3D 12 ou Vulkan, com mais que o dobro de FPS do renderizador emulado.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v2.0.2, de 24/07/2026: `Skate3Recomp-Windows.zip`, `Skate3Recomp-Linux.zip` e `Skate3Recomp-macOS.zip`) |
| Precisa de emulador | Não |
| Você precisa fornecer | A ISO da sua cópia do Skate 3 de Xbox 360. Para DLCs, opcionais, os pacotes da sua cópia. ⚠️ Você não soube dizer se consegue dumpar Xbox 360. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Ativo. O renderizador nativo é novo e ainda não foi testado do começo ao fim do jogo. A versão de Windows é a mais testada, depois a de Linux. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor, com executável não assinado e sem checksum publicado. Baixe só pela página de Releases e passe o arquivo no VirusTotal.

## Arch Linux

1. Baixe `Skate3Recomp-Linux.zip` em https://github.com/mchughalex/skate3recomp/releases.
2. Extraia numa pasta sua: `bsdtar -xf Skate3Recomp-Linux.zip` (sugestão).
3. Rode o `skate3`. Se precisar, antes rode `chmod +x skate3`.
4. Clique em **Select ISO** e escolha a sua cópia.
5. Espere o instalador extrair os arquivos do jogo e clique em **Start Game**.

O README avisa que, em alguns hardwares, a versão de Windows pelo Proton pode funcionar melhor que a nativa de Linux. No Linux, o renderizador usa Vulkan.

**Compilar, opcional** (README, seções Building from Source e Ubuntu/Linux Build). É preciso CMake, Ninja, Clang 20 ou mais novo, headers de Vulkan e GTK 3 e bibliotecas de áudio e entrada.
1. Clone com submódulos.
2. Coloque o dump extraído do jogo, com `default.xex` e `data/webkit/EAWebkit.xex`, em `game/`.
3. Coloque o pacote da Title Update 3 (`TU_12K2276_000000C000000.00000000000O3`) na raiz.
4. Gere o código, reconfigure e compile:
   ```bash
   cmake --preset linux-release -DSKATE3_GAME_DATA_ROOT="$PWD/game"
   cmake --build --preset linux-release --target generate-all --parallel
   cmake --preset linux-release -DSKATE3_GAME_DATA_ROOT="$PWD/game"
   cmake --build --preset linux-release --parallel
   ```
5. O resultado fica em `out/build/linux-release/skate3`.

## Windows

1. Baixe `Skate3Recomp-Windows.zip` em https://github.com/mchughalex/skate3recomp/releases.
2. Extraia numa pasta sua.
3. Abra o `skate3.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. Clique em **Select ISO**, escolha a sua cópia e espere a extração.
5. Clique em **Start Game**.

## Controles e configurações

- **Controle de Xbox:** é o método principal.
- **PlayStation, Switch e controles genéricos:** em **Settings → Controls → Controller Backend**, escolha **SDL** e reinicie o jogo.
- **Teclado:** ligue nas configurações do jogo.
  | Controle | Teclado |
  |---|---|
  | Analógico esquerdo | W A S D |
  | Analógico direito | Mouse |
  | A / B / X / Y | Espaço / C / E / F |
  | LT / RT | Botão direito / esquerdo do mouse |
  | LB / RB | Q / R |
  | Back / Start | Tab / Enter |
- **Esc** (ou **RB + Start** no controle) abre as configurações.
- **Renderizador:** **Settings → Video → Renderer** troca entre Nativo e Emulado, e **F5** alterna na hora. No Windows, **Graphics API** escolhe entre DirectX 12 e Vulkan.
- **DLC:** crie uma pasta `dlc` ao lado do executável e coloque os pacotes lá.
- **Saves:** ficam em `%APPDATA%\skate3` no Windows.
  - Uma pasta `saves` criada ao lado do executável, antes de abrir o jogo, passa a guardar os saves.
  - Um arquivo vazio `portable.txt` guarda tudo na pasta do jogo.

## Problemas conhecidos

- Texturas e objetos podem aparecer de repente ou piscar quando você anda rápido pelo mapa.
- O editor de skatista não mostra direito pele, cabelo e roupas.
- O Hall of Meat não aparece corretamente.
- As pistas e o editor de pistas têm falhas visuais.

## Fontes

- [README › How Do I Play?, Native Renderer, Installing DLC, Saves, Controls e Building from Source](https://github.com/mchughalex/skate3recomp#readme)
- [Releases (v2.0.2)](https://github.com/mchughalex/skate3recomp/releases)

<!-- verificado: 2026-10-15 -->
