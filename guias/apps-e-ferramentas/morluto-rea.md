# REA: Reverse Engineer Anything · rea (PC)

Repositório: https://github.com/morluto/rea · Espelho: https://github.com/alves-r/mirror-morluto-rea

Servidor MCP e linha de comando para engenharia reversa com agentes de IA. Ele analisa binários nativos, apps JavaScript/Electron, APKs de Android, .NET, WASM, firmware, capturas de rede e mais, e devolve as descobertas com as evidências para o seu agente, como o Claude Code.

| Item | Detalhe |
|---|---|
| Tipo | Servidor / ferramenta |
| Executável pronto | Sim, pelo npm (pacote `rea-agents`, versão 6.5.0, de 14/10/2026). Os Releases do GitHub não têm arquivos. |
| Precisa de emulador | Não |
| Você precisa fornecer | Node.js 22.x (≥22.19), 24.x (≥24.11) ou 26+, com npm, e um agente com suporte a MCP. Para a análise profunda de binários nativos, também o Hopper, o Ghidra ou o IDA. |
| Arch Linux | Nativo |
| Windows | Nativo (o Ghidra no Windows é experimental) |
| Estado | Ativo, com versões frequentes |
| Dificuldade | Fácil (baixar e rodar) |

> **Cuidado com cópias.** O próprio README manda obter o REA só pelo `morluto/rea`, pelo site https://rea.tools ou pelo pacote npm `rea-agents`. Um nome de repositório parecido ou um README copiado não tornam um download oficial. A entrada antiga do `repos.txt`, `rea-githu/REA`, era uma dessas cópias-isca e foi removida do GitHub.

O REA é para uso legal: pesquisa, educação, interoperabilidade, preservação de software e análise de software que você possui ou tem autorização para examinar. Detalhes em `DISCLAIMER.md`.

## Arch Linux

1. Instale o Node.js, o npm e um `ps` compatível com procps, que o REA exige no Linux para o Ghidra, o JADX, ferramentas de firmware e a análise de JavaScript/Electron.
   - Na sua máquina já há o `nodejs-lts-jod` 22.23.2, que atende ao mínimo, e o `procps-ng`. Falta só o npm: `sudo pacman -S --needed npm`
   - Em outro Arch (sugestão): `sudo pacman -S --needed nodejs npm procps-ng`
2. Configure o seu agente: `npx rea-agents setup`
   1. Escolha os agentes, como Claude Code, Codex, Cursor, Gemini CLI ou Windsurf.
   2. Revise as mudanças propostas e aprove. O setup faz backup das configurações existentes.
   3. Reinicie o agente.
3. Peça ao agente, por exemplo: "Entenda como a busca funciona no app X, mostre as evidências e implemente algo parecido no meu projeto."
4. Para a análise de binários nativos, instale um motor. O Ghidra está nos repositórios oficiais (sugestão): `sudo pacman -S ghidra`. O setup também pode instalar o Hopper, com a sua aprovação.
5. Para conferir se está tudo pronto: `npx rea-agents@latest doctor --json`. Ele só lê, não altera nada.

**Comando `rea` permanente, opcional:** `npm install --global rea-agents` e depois `rea --help`. No Arch, a instalação global do npm vai para o sistema e pede `sudo`, a menos que você configure um prefixo no seu home (sugestão). Para comandos avulsos, `npx rea-agents@latest <comando>` dispensa a instalação.

## Windows

1. Instale o Node.js 22.19+ ou 24.11+, que já vem com o npm.
2. No PowerShell, rode `npx rea-agents setup`, escolha os agentes, aprove as mudanças e reinicie o agente.
3. Se usar o Claude Desktop, feche-o por completo antes de aprovar o setup, senão o app em execução pode sobrescrever o registro.
4. O suporte ao Ghidra no Windows é experimental (`docs/windows-ghidra-p0.md`).

## Controles e configurações

- **Atualizar:**
  - instalação pelo `npx`: rode `npx rea-agents@latest setup` de novo e reinicie o agente;
  - instalação global: `rea update`.
- **Remover:**
  - `rea uninstall` mantém o Hopper, o Node.js e os seus arquivos de evidência;
  - `rea uninstall --purge-data` apaga também o cache e o estado em `~/.rea`.
- **Linha de comando, sem agente:** `npx -y rea-agents@latest analyze-javascript-application /caminho/do/app --json` lista os módulos, imports e pontes do Electron de um app extraído ou de um ASAR.
- **Binários grandes:** aumente o tempo de inicialização do motor com `REA_GHIDRA_STARTUP_TIMEOUT_MS` ou `REA_HOPPER_STARTUP_TIMEOUT_MS`.
- **Privacidade:** a análise é local. O seu agente recebe os resultados, e o provedor do modelo segue a própria política de dados.

## Fontes

- [README › Quick start, What you can analyze, FAQ e Disclaimer](https://github.com/morluto/rea#readme)
- [docs/installation.md](https://github.com/morluto/rea/blob/main/docs/installation.md)
- [Pacote npm rea-agents](https://www.npmjs.com/package/rea-agents)

<!-- verificado: 2026-10-15 -->
