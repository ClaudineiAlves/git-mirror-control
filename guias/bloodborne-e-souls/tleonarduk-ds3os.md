# Dark Souls III e II · ds3os (PC)

Repositório: https://github.com/TLeonardUK/ds3os · Espelho: https://github.com/alves-r/mirror-tleonarduk-ds3os

Servidor aberto, não oficial, para Dark Souls III e Dark Souls II: Scholar of the First Sin no PC. Serve para jogar online com mods ou só com amigos, sem risco de ban. O DS3 está estável e o DS2 ainda é experimental.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim (v0.42.0.0, de 14/08/2024: `windows.zip` traz `Loader/Loader.exe` e `Server/Server.exe`; `linux.zip` traz só o servidor, em `Server/Server`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Dark Souls III ou Dark Souls II: Scholar of the First Sin, originais na Steam. O servidor valida tickets da Steam e não funciona com jogo pirata. ⚠️ Você não soube dizer se tem os jogos de PC. |
| Arch Linux | Nativo (só o servidor; o README não documenta como conectar o jogo no Linux) |
| Windows | Nativo |
| Estado | DS3 estável o bastante para uso; DS2 SOTFS experimental. A última release é de 14/08/2024. |
| Dificuldade | Fácil (baixar e rodar) |

## Arch Linux

No Arch dá para **hospedar** o servidor. O Loader, que conecta o jogo ao servidor, é um programa de Windows, e o README não documenta como usá-lo com o jogo rodando no Proton.

**Opção 1: release pronta**

1. Baixe `linux.zip` em https://github.com/TLeonardUK/ds3os/releases.
2. Extraia: `bsdtar -xf linux.zip` (sugestão; o `unzip` não vem instalado na sua máquina).
3. Rode o servidor: `cd Server && chmod +x Server && ./Server`
4. Na primeira execução ele cria `Saved/default/config.json`. Ajuste e reinicie o servidor:
   - `ServerHostname`: o seu IP externo (WAN)
   - `ServerPrivateHostname`: o seu IP da rede local (LAN)
   - uma senha, se quiser um servidor fechado
5. Libere no roteador as portas **50000, 50010, 50050 e 50020**, em TCP e UDP.
6. Para hospedar Dark Souls II, troque `GameType` de `DarkSouls3` para `DarkSouls2` no `config.json`.

**Opção 2: Docker**

1. Instale e ative o Docker (sugestão): `sudo pacman -S --needed docker && sudo systemctl enable --now docker`
2. Rode o comando do README:
   ```bash
   sudo mkdir -p /opt/ds3os/Saved && sudo chown 1000:1000 /opt/ds3os/Saved && sudo docker run -d -m 2G --restart always --net host --mount type=bind,source=/opt/ds3os/Saved,target=/opt/ds3os/Saved timleonarduk/ds3os:latest
   ```
3. A configuração fica em `/opt/ds3os/Saved`.

**Opção 3: Nix:** `nix run github:TLeonardUK/ds3os`. Nesse caso a configuração fica em `~/.config/ds3os`.

## Windows

1. Baixe `windows.zip` em https://github.com/TLeonardUK/ds3os/releases e extraia.
2. O pacote traz `Prerequisites/VC_redist.x64.exe`. Instale-o se algum programa reclamar de DLL faltando.
3. **Para jogar:** abra `Loader/Loader.exe` como administrador, porque ele precisa alterar a memória do jogo para conectá-lo. Escolha entrar num servidor existente ou criar um. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
4. **Para hospedar:**
   1. Instale o cliente da Steam. Ele precisa estar instalado, mas não precisa estar logado, senão o `Server.exe` não inicia.
   2. Rode `Server/Server.exe`. Na primeira vez ele cria `Saved\default\config.json`.
   3. Ajuste `ServerHostname` (IP externo), `ServerPrivateHostname` (IP local), a senha e o `GameType`, e reinicie o servidor.
   4. Libere as portas 50000, 50010, 50050 e 50020 (TCP e UDP) no roteador e no Windows Defender Firewall.
5. **Saves:** o ds3os usa saves próprios. Para levar os seus, clique na engrenagem do Loader e em "copy retail saves".

**Compilar, opcional:** o projeto usa Visual Studio 2022 e C++17. Gere os arquivos de projeto com o CMake ou com um dos scripts `generate_*` da pasta `Tools` e compile a solução gerada na pasta intermediate.

## Problemas conhecidos

- **O jogo não conecta:** confira se o Loader está rodando como administrador e se as portas estão liberadas. Com várias placas de rede (ou Hamachi), os IPs detectados no `config.json` podem sair errados (Windows).
- **Server.exe não inicia:** acontece quando o cliente da Steam não está instalado (Windows).
- **Dark Souls II é experimental:** o README avisa que há grande chance de algo não funcionar direito.

## Fontes

- [README](https://github.com/TLeonardUK/ds3os#readme) (seções What is this project?, How do I use it?, What currently works?, FAQ e How do I build it?)
- [Releases](https://github.com/TLeonardUK/ds3os/releases)

<!-- verificado: 2026-10-15 -->
