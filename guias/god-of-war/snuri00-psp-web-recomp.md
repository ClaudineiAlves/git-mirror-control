# God of War: Chains of Olympus e Ghost of Sparta · psp-web-recomp (PSP)

Repositório: https://github.com/snuri00/psp-web-recomp · Espelho: https://github.com/alves-r/mirror-snuri00-psp-web-recomp

Ferramenta que transforma a ISO de um jogo de PSP seu numa página web (WebAssembly e WebGL2). Os dois God of War de PSP jogam a 55–60 fps, mas os vídeos ainda são pulados.

| Item | Detalhe |
|---|---|
| Tipo | Port / Recomp para compilar |
| Executável pronto | Não, precisa compilar |
| Precisa de emulador | Não |
| Você precisa fornecer | A ISO de um jogo de PSP seu (também serve um ZIP com ela ou a pasta extraída) e uma ferramenta que decripte o `EBOOT.BIN` (`PSP_DECRYPT`), como DecEboot, pspdecrypt ou o dump do executável feito pelo PPSSPP. Testados: God of War: Chains of Olympus e Ghost of Sparta. ⚠️ Você não soube dizer se consegue dumpar PSP. |
| Arch Linux | Nativo |
| Windows | Via WSL (só para compilar) |
| Estado | Dois jogos, do mesmo estúdio, funcionam: Chains of Olympus a 60 fps nas cenas medidas e Ghost of Sparta a 55–60 fps. Os vídeos ainda são pulados. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

O projeto foi testado em Linux. Reserve uns 2 GB por jogo.

1. Instale as ferramentas. O `mesa` e o `libglvnd` trazem os headers de EGL e GLES que o runner de teste usa (o README cita os nomes do Debian; conversão sugerida):
   `sudo pacman -S --needed git cmake ninja clang python mesa libglvnd`
2. Clone: `git clone https://github.com/snuri00/psp-web-recomp.git && cd psp-web-recomp`
3. Prepare o ambiente: `scripts/setup.sh`. Isso baixa o PSPRecomp, aplica os patches e instala o Emscripten SDK.
4. Gere o jogo: `PSP_DECRYPT=/caminho/para/decrypter scripts/port.sh gow "God of War.iso"`
   - O script extrai o disco, decripta o `EBOOT.BIN`, traduz para C++ e monta a página.
   - Leva uns 4 minutos num notebook de 8 núcleos.
   - Com `--native`, ele também gera um runner sem janela que salva quadros em imagem.
5. Sirva a página: `scripts/serve.sh gow` e abra http://localhost:8613/ no Chrome ou no Firefox.

## Windows

O projeto não documenta build no Windows. Compile no WSL2 e jogue no navegador do Windows:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu, instale as ferramentas (nomes do Ubuntu, citados no README para o runner):
   `sudo apt update && sudo apt install -y git cmake ninja-build clang python3 libegl-dev libgles-dev`
3. Siga os passos 2 a 5 da seção Arch Linux dentro do Ubuntu.
4. No Windows, abra http://localhost:8613/ no Chrome, no Edge ou no Firefox.

## Controles e configurações

- Os saves ficam em `PSP/SAVEDATA`, guardados no navegador.
- **Export saves** baixa tudo num ZIP; **Import saves** traz os saves de volta.
- Saves copiados de um PSP real ou do PPSSPP costumam estar criptografados e ainda não carregam.
- `?threads=0` força uma thread só, e `?profile` mostra o tempo de cada quadro.

## Problemas conhecidos

- Os vídeos do jogo são pulados.
- Os dois jogos testados usam a mesma engine. Outros jogos devem parar em chamadas de sistema não implementadas, que aparecem no log como `[hle] unimplemented ...`.
- Qualquer um com o endereço do servidor carrega o jogo. Mantenha-o só para você.

## Fontes

- [README › PSP Web Recomp, How it works e Port a game of your own](https://github.com/snuri00/psp-web-recomp#readme)
- [README › Saves e Hosting](https://github.com/snuri00/psp-web-recomp#saves)

<!-- verificado: 2026-10-15 -->
