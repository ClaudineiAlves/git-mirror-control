# Resident Evil 3: Nemesis · resident-evil-3-recomp (PS1)

Repositório: https://github.com/alexbeavs-ps1-ports/resident-evil-3-recomp · Espelho: https://github.com/alves-r/mirror-alexbeavs-ps1-ports-resident-evil-3-recomp

Recompilação estática do Resident Evil 3 de PS1, feita com o PSXRecomp. O pacote traz um assistente que gera o código do jogo a partir do seu disco e o compila na sua máquina. É um candidato a versão final.

| Item | Detalhe |
|---|---|
| Tipo | Port nativo / Recomp com binário |
| Executável pronto | Sim (v0.1.1, de 30/09/2026: zips para Linux x64, Windows x64 e macOS, com `SHA256SUMS.txt`). O jogo em si é gerado e compilado na primeira execução. |
| Precisa de emulador | Não |
| Você precisa fornecer | O disco europeu `SLES-02529` em `.cue`/`.bin` no padrão Redump (`.chd` e outros formatos não passam na verificação) e o arquivo `.sbi` com o mesmo nome, ao lado do `.cue`. Também a BIOS europeia SCPH-5502/5552 (524288 bytes, SHA-256 `1faaa18fa820a0225e488d9f086296b8e6c46df739666093987ff7d8fd352c09`). ⚠️ Você indicou que não consegue dumpar PS1, e a BIOS também tem de sair do seu próprio console. |
| Arch Linux | Nativo |
| Windows | Nativo |
| Estado | Candidato a versão final, sem promessa de jogo completo. A configuração inicial, o gameplay, os saves e o suporte nativo a Linux e macOS ainda passam por testes separados. |
| Dificuldade | Média (compilar com script) |

> Projeto de um único autor, com executável não assinado. Baixe só pela página de Releases, confira com o `SHA256SUMS.txt` e passe o arquivo no VirusTotal.

## Arch Linux

1. O README pede CMake, Ninja, Python 3 e um compilador C/C++: `sudo pacman -S --needed cmake ninja python gcc`
2. Baixe `resident-evil-3-0.1.1-linux-x64.zip` e `SHA256SUMS.txt` em https://github.com/alexbeavs-ps1-ports/resident-evil-3-recomp/releases.
3. Confira: `sha256sum -c SHA256SUMS.txt --ignore-missing`
4. Extraia o zip inteiro numa pasta com permissão de escrita: `bsdtar -xf resident-evil-3-0.1.1-linux-x64.zip` (sugestão).
5. Rode o `Resident_Evil_3__Nemesis_Recompiled`.
6. No assistente, escolha o seu `.cue` e a BIOS. Mantenha o `.cue`, os `.bin` e o `.sbi` juntos.
7. Clique em **Generate & rebuild** e espere o jogo abrir.

## Windows

1. Baixe `resident-evil-3-0.1.1-windows-x64.zip` e `SHA256SUMS.txt` em https://github.com/alexbeavs-ps1-ports/resident-evil-3-recomp/releases.
2. Confira o hash no PowerShell: `Get-FileHash .\resident-evil-3-0.1.1-windows-x64.zip` e compare com o `SHA256SUMS.txt`.
3. Extraia o zip inteiro numa pasta com permissão de escrita.
4. Abra o `Resident_Evil_3__Nemesis_Recompiled.exe`. Se o SmartScreen avisar, clique em **Mais informações → Executar assim mesmo**.
5. No assistente, escolha o `.cue` e a BIOS e clique em **Generate & rebuild**. No Windows, o assistente pode baixar sozinho as ferramentas de build portáteis.

## Problemas conhecidos

- A v0.1.0 voltava à tela de configuração depois do build e pedia a BIOS errada. A v0.1.1 corrige os dois problemas.

## Fontes

- [README › Setup e Candidate status](https://github.com/alexbeavs-ps1-ports/resident-evil-3-recomp#readme)
- [docs/FEASIBILITY.md](https://github.com/alexbeavs-ps1-ports/resident-evil-3-recomp/blob/main/docs/FEASIBILITY.md)
- [Releases (v0.1.1)](https://github.com/alexbeavs-ps1-ports/resident-evil-3-recomp/releases)

<!-- verificado: 2026-10-15 -->
