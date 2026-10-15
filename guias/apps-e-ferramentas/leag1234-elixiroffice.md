# ElixirOffice · elixiroffice (PC)

Repositório: https://github.com/leag1234/elixiroffice · Espelho: https://github.com/alves-r/mirror-leag1234-elixiroffice

Suíte de escritório de código aberto (AGPLv3), derivada do Euro-Office e do ONLYOFFICE, para quem está acostumado ao Microsoft Office: textos, planilhas e apresentações com faixa de opções, menus e atalhos do Office. Tem um app de desktop 100% local e uma versão de servidor para equipes.

| Item | Detalhe |
|---|---|
| Tipo | App (não é jogo) |
| Executável pronto | Sim (desktop v0.2.0 beta, de 15/10/2026: `ElixirOffice-0.2.0-x86_64.AppImage`, `ElixirOffice-0.2.0-linux-amd64.deb`, `ElixirOffice-0.2.0-win-x64.exe` e `ElixirOffice-0.2.0-mac-arm64.dmg`, com `SHA256SUMS`) |
| Precisa de emulador | Não |
| Você precisa fornecer | Nada |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Beta. O app avisa: guarde backup dos arquivos importantes e confira os documentos e PDFs salvos antes de compartilhar. |
| Dificuldade | Fácil (baixar e rodar) |

> Projeto de um único autor. O instalador de Windows não é assinado, e o app de macOS não é notarizado, como o próprio README avisa. Baixe só pela página de Releases, confira com o `SHA256SUMS` e passe o arquivo no VirusTotal.

O app de desktop abre e converte os documentos no próprio computador. Ele não usa servidor de documentos, não tem telemetria nem atualização automática.

## Arch Linux

1. Baixe `ElixirOffice-0.2.0-x86_64.AppImage` e `SHA256SUMS` em https://github.com/leag1234/elixiroffice/releases/tag/v0.2.0.
2. Confira: `sha256sum -c SHA256SUMS --ignore-missing`
3. Rode: `chmod +x ElixirOffice-0.2.0-x86_64.AppImage && ./ElixirOffice-0.2.0-x86_64.AppImage`
4. Sem suporte a FUSE, extraia com `./ElixirOffice-0.2.0-x86_64.AppImage --appimage-extract`, numa pasta com permissão de escrita, e rode `squashfs-root/AppRun`. Instalar o FUSE 2 também resolve (sugestão): `sudo pacman -S --needed fuse2`.

Sem user namespaces no sistema, o AppImage roda sem o sandbox do Chromium e mostra um aviso. O `.deb` é para Debian e Ubuntu.

## Windows

1. Baixe `ElixirOffice-0.2.0-win-x64.exe` e `SHA256SUMS` em https://github.com/leag1234/elixiroffice/releases/tag/v0.2.0.
2. Confira o hash no PowerShell: `Get-FileHash .\ElixirOffice-0.2.0-win-x64.exe` e compare com o `SHA256SUMS`.
3. Rode o instalador. O SmartScreen vai avisar, porque ele não é assinado: clique em **Mais informações → Executar assim mesmo**.

**Versão de servidor (para equipes):** roda num host Linux com Docker e um nome DNS público, com edição no navegador e coedição em tempo real. O passo a passo está em `docs/install-server.md`. O próprio documento diz que ainda é um candidato a versão, não uma distribuição publicada.

## Controles e configurações

- Abre e salva `.docx`, `.xlsx`, `.pptx`, `.odt`, `.ods` e `.odp`, sempre no seu computador.
- **Salvar como:**
  - textos: DOCX, ODT, RTF, TXT ou PDF;
  - planilhas: XLSX, ODS ou CSV;
  - apresentações: PPTX, ODP ou PDF.
- **PDF (v0.2.0):** abrir, anotar, preencher formulários e salvar.
- Abre arquivos protegidos por senha.

## Fontes

- [README › Get ElixirOffice, Two ways to use it e Try it](https://github.com/leag1234/elixiroffice#readme)
- [docs/desktop.md](https://github.com/leag1234/elixiroffice/blob/main/docs/desktop.md)
- [docs/install-server.md](https://github.com/leag1234/elixiroffice/blob/main/docs/install-server.md)
- [Release v0.2.0 (notas e tabela de downloads)](https://github.com/leag1234/elixiroffice/releases/tag/v0.2.0)

<!-- verificado: 2026-10-15 -->
