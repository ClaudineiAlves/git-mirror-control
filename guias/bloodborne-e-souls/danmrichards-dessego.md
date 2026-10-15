# Demon's Souls · dessego (PS3)

Repositório: https://github.com/danmrichards/dessego · Espelho: https://github.com/alves-r/mirror-danmrichards-dessego

Servidor online alternativo para o Demon's Souls de PS3, escrito em Go. Cobre login, mensagens, manchas de sangue, fantasmas e invocações, mas o multiplayer completo ainda depende da PSN.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Não, precisa compilar |
| Precisa de emulador | Sim, para jogar sem PS3: RPCS3 no Linux e no Windows ([guia](../recomp-e-emulacao/rpcs3-rpcs3.md)) |
| Você precisa fornecer | Demon's Souls (PS3) rodando no seu PS3 ou no RPCS3. ⚠️ Você indicou que não consegue dumpar PS3. O servidor em si não usa arquivos do jogo. |
| Arch Linux | Nativo |
| Windows | Via WSL (o projeto só documenta Linux) |
| Estado | Sem atualizações desde 07/04/2021. O README avisa que o fluxo completo de invocação e multiplayer depende do matchmaking da PSN. |
| Dificuldade | Média (compilar com script) |

## Arch Linux

1. Instale as ferramentas: `sudo pacman -S --needed go git make`
2. Clone: `git clone https://github.com/danmrichards/dessego.git && cd dessego`
3. Compile: `make build`. Isso gera `bin/dessego-linux-amd64`.
4. Rode o servidor: `./bin/dessego-linux-amd64`. A opção `-seed` popula o banco com os dados legados.
5. Conecte o jogo pelo RPCS3:
   1. Crie uma configuração personalizada para o Demon's Souls e, em **Network**, defina:
      - **Network Status:** Connected
      - **PSN Status:** RPCN
      - **DNS:** `8.8.8.8`
      - **IP/Host Switch:** `ds-eu-c.scej-online.jp=<IP>&&ds-eu-g.scej-online.jp=<IP>&&c.demons-souls.com=<IP>&&g.demons-souls.com=<IP>&&cmnap.scej-online.jp=<IP>&&demons-souls.scej-online.jp=<IP>`, trocando `<IP>` pelo endereço da máquina que roda o dessego.
   2. Salve a configuração.
   3. Em **Configuration → RPCN**, use o host `np.rpcs3.net`, escolha um NPID e uma senha e clique em **Create Account**.
   4. Informe seu e-mail e cole no campo Token o código que chegar por e-mail.
   5. Salve e abra o jogo.

Num PS3 de verdade, você precisa de um proxy DNS que aponte os seis domínios acima para o servidor. No PS3, configure o DNS manual apontando para esse proxy: **Settings → Network → Internet Connection Settings → Custom → Enter Manually**, depois DNS em **Manual**.

As portas que o servidor usa não estão documentadas no repositório.

## Windows

O projeto só documenta Linux. No Windows, rode-o dentro do WSL2:

1. No PowerShell como administrador, rode `wsl --install -d Ubuntu` e reinicie.
2. No Ubuntu: `sudo apt update && sudo apt install -y golang-go git make`. O README pede Go 1.13 ou mais novo.
3. Clone e compile: `git clone https://github.com/danmrichards/dessego.git && cd dessego && make build`
4. Rode: `./bin/dessego-linux-amd64`
5. Configure o RPCS3 do Windows como no passo 5 da seção Arch Linux. Como `<IP>`, use o endereço do WSL, que aparece com `hostname -I` dentro do Ubuntu (sugestão).

## Fontes

- [README › Features, Requirements, Building From Source e Usage](https://github.com/danmrichards/dessego#readme)
- [README › Connecting from Demon's Souls (Native PS3 e RPCS3)](https://github.com/danmrichards/dessego#connecting-from-demons-souls)

<!-- verificado: 2026-10-15 -->
