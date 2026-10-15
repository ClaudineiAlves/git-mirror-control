# git-mirror-control

Backup automático de repositórios do GitHub. Cada repositório listado no [`repos.txt`](repos.txt) ganha uma cópia **privada e independente** na conta de backup, atualizada pelo GitHub Actions (sem depender do seu computador ligado) e organizada em **GitHub Lists** por categoria.

Se o original for apagado, ficar privado ou sair do ar, o espelho **não é tocado**: a cópia fica como estava.

**Duas contas:** este repositório de controle fica na conta principal (`ClaudineiAlves`). Os espelhos, as Lists e as estrelas ficam na conta [`alves-r`](https://github.com/alves-r), que é a dona do token `MIRROR_TOKEN`. O `mirror.py` recusa token de qualquer outra conta (constante `ACCOUNT`), para que um token trocado não encha o perfil principal de espelhos.

## Como funciona

```
 Gatilhos: cron de hora em hora · push que altera o repos.txt · manual (Run workflow)
                                     │
                                     ▼
          GitHub Actions ──► python3 mirror.py sync   (para cada linha do repos.txt)
                                     │
   ① a origem responde? ─── não (404, 451, vazia, fora do ar) ──► 🛡️ espelho fica intacto
                                     │ sim
   ② o espelho existe?  ─── não ──► cria repo PRIVADO, desliga o Actions dele, cópia inicial
                                     │ sim
   ③ git ls-remote: origem = espelho? ─── sim ──► ✅ pula (nem clona)
                                     │ não
   ④ fetch só de branches/tags ──► push --force do que mudou ──► 🔄 atualizado
                                     │
   ⑤ ⭐ estrela + GitHub List da categoria + topics (mirror, <categoria>)

   github.com/owner/repo  ══ cópia ══►  github.com/alves-r/mirror-owner-repo (privado)
```

A cópia busca só `refs/heads/*` e `refs/tags/*` num repositório temporário e faz push forçado apenas do que mudou. Um `push --mirror` puro não serve, porque o GitHub rejeita os `refs/pull/*`. Baixar esses refs só gastaria banda.

**Regras de proteção do backup**

- Origem com 404, 451, desativada, vazia ou fora do ar: o espelho **não é tocado** e fica com status 🛡️ protegido, com um aviso no log. Vale também quando você perde acesso à origem.
- Branches e tags apagados na origem **continuam** no espelho. Só somem com `--prune`.
- Tirar uma linha do `repos.txt` só interrompe a sincronização. Nem o espelho nem as Lists são apagados; uma List que ficar vazia gera só um aviso.
- Um repositório seu com o nome do espelho e descrição diferente de `Mirror of <URL>` nunca é sobrescrito.
- Falha em um repo não interrompe os outros. Falha de categorização (Lists/topics) vira só um aviso.
- O token nunca vai em URL, argumento ou log. O git recebe o header de autenticação por variáveis de ambiente (`GIT_CONFIG_*`).

## Configuração (uma vez só)

### 1. Crie o token (PAT)

O `GITHUB_TOKEN` automático do Actions só enxerga o próprio repositório e não cria repos na sua conta. Por isso a automação usa um Personal Access Token, guardado no secret `MIRROR_TOKEN`.

**Recomendado: token classic.** Abra [o formulário já com os escopos marcados](https://github.com/settings/tokens/new?scopes=repo,workflow,user&description=git-mirror-control) **logado como `alves-r`**. A conta dona do token é a que recebe os espelhos.

| Escopo | Por que é necessário |
|---|---|
| `repo` | Criar os espelhos privados, fazer push, aplicar topics, desligar o Actions dos espelhos, definir o branch padrão e dar estrela. A API de estrelas aceita `public_repo` ou `repo`, mas repo privado exige `repo`. |
| `workflow` | Enviar repositórios que contêm `.github/workflows/`. Sem ele, o GitHub recusa o push com "refusing to allow a Personal Access Token to create or update workflow". |
| `user` | Criar Lists e mover espelhos entre elas (`createUserList`, `updateUserListsForItem`). |

> O GitHub não documenta o escopo exigido pelas mutations de Lists. `user` é o que ferramentas de terceiros relatam. Se ele faltar, o sync registra um aviso, continua espelhando e os topics seguem funcionando.

**Alternativa: fine-grained.** Serve porque todas as origens são públicas.

- *Resource owner*: sua conta. *Repository access*: **All repositories**, porque os espelhos são criados depois do token.
- *Repository permissions*: **Administration**, **Contents**, **Workflows** e **Repository creation** em *Read and write*; **Metadata** em *Read* (automático).
- *Account permissions*: **Starring** em *Read and write*.
- ⚠️ O GitHub não documenta Lists com fine-grained. Se não funcionar, aparece o aviso e só as Lists ficam de fora.

**Validade e renovação**

- Dê uma validade ao token (ex.: 1 ano). O GitHub manda e-mail antes de expirar.
- Se o token expirar ou for revogado, o workflow falha com `HTTP 401` e você recebe o e-mail de falha do Actions.
- Para renovar: logado como `alves-r`, vá em Settings → Developer settings → Personal access tokens → abra o token → **Regenerate token** (os escopos são mantidos). Depois atualize o secret com `gh secret set MIRROR_TOKEN -R ClaudineiAlves/git-mirror-control`.

### 2. Publique o repositório e cadastre o secret

```bash
cd ~/documents/data_programing/projects/git-mirror-control
git init -b main
git add .
git commit -m "feat: espelhamento automático de repositórios"
gh repo create git-mirror-control --public --source . --remote origin   # cria vazio, sem push
gh secret set MIRROR_TOKEN        # cole o token do alves-r quando pedir (não fica no histórico do shell)
git push -u origin main           # o push já dispara a 1ª execução, por isso o secret vem antes
```

Pelo site: repo → **Settings → Secrets and variables → Actions → New repository secret**, com o nome `MIRROR_TOKEN`. O nome não pode começar com `GITHUB_` (prefixo reservado). O workflow repassa o valor ao script como `GITHUB_TOKEN`.

### 3. Primeira execução

```bash
gh workflow run mirror.yml -f dry_run=true   # só simula
gh run watch                                 # acompanha
gh workflow run mirror.yml                   # pra valer
```

Ou em **Actions → Espelhar repositórios → Run workflow**. A aba **Summary** de cada execução mostra uma tabela por categoria.

## Usando o `repos.txt`

```ini
https://github.com/owner/sem-categoria        # antes de qualquer [cabeçalho]: fica fora das Lists

[IA e Machine Learning]                       # categoria = GitHub List com esse nome
https://github.com/owner/repo                 # espelho: mirror-owner-repo
https://github.com/owner/outro-repo meu-nome  # espelho com nome escolhido
# https://github.com/owner/pausado            # comentado = não sincroniza
```

- O nome padrão do espelho é `mirror-<owner>-<repo>` em minúsculas, derivado da URL (não há arquivo de estado). Nomes que passariam do limite de 100 caracteres do GitHub são encurtados com um hash.
- A URL pode ter `.git` e `/` no final. Comentários com `#` também podem ficar no fim da linha.
- Abortam o sync inteiro, com a linha apontada: URL duplicada, nome de espelho repetido e cabeçalho vazio (`[]`) ou malformado. Uma categoria sem nenhum repo ativo não é erro.
- Uma URL inválida faz falhar só a própria linha. As outras seguem.

| Quero… | Faço… |
|---|---|
| adicionar um repo | colo a URL embaixo da categoria |
| criar uma categoria | crio `[Nome]` com as URLs embaixo; a List nasce no próximo sync |
| mover de categoria | recorto a linha e colo na outra seção; o espelho troca de List e de topic |
| escolher o nome do espelho | `URL nome-do-espelho`, antes de criar (trocar depois cria **outro** espelho) |
| pausar | comento a linha com `#` |
| parar de sincronizar | apago a linha (o espelho continua lá, intacto) |
| congelar um espelho | arquivo o repo do espelho (Settings → Archive); ele vira 🧊 congelado |

**Pelo terminal**

```bash
git pull --rebase                 # o keepalive pode ter criado commits no GitHub
$EDITOR repos.txt
git commit -am "repos: adiciona owner/repo" && git push
```

**Pelo site** (no computador ou no navegador do celular): abra <https://github.com/ClaudineiAlves/git-mirror-control/edit/main/repos.txt>, edite e clique em **Commit changes**, opção *Commit directly to the main branch*.

**Pelo app GitHub Mobile**: repositório → **Browse code** → `repos.txt` → menu no canto superior direito → **Edit** → edite → **Commit** no `main`.

Todo commit no `main` que altera o `repos.txt` dispara o sync na hora. Acompanhe em **Actions**.

## Onde ver os espelhos

Logado como `alves-r`:

- **Lists**: aba Stars do perfil, seção *Lists*: <https://github.com/alves-r?tab=stars>. As listas são privadas, então só o `alves-r` as vê.
- **Topics**: <https://github.com/alves-r?tab=repositories&q=topic%3Amirror> mostra todos os espelhos. Para uma categoria só, use o topic dela, ex.: `topic:ia-e-machine-learning`. Na busca global, `user:alves-r topic:mirror`.
- **Status**: `python mirror.py list` localmente, ou o resumo de cada execução no Actions.

## Agendamento e execução manual

O agendamento está em `.github/workflows/mirror.yml`, sempre em **UTC**:

```yaml
- cron: "17 * * * *"   # minuto hora dia mês dia-da-semana (hoje: de hora em hora, no minuto 17)
```

| Frequência | cron |
|---|---|
| a cada 6 h | `0 */6 * * *` |
| 1×/dia às 06:00 de Brasília (09:00 UTC) | `0 9 * * *` |
| 1×/semana, domingo 00:00 UTC | `0 0 * * 0` |

O começo de cada hora é o horário mais congestionado do Actions. Um minuto "quebrado" (ex.: `17 */12 * * *`) atrasa menos. O intervalo mínimo é de 5 min.

Para rodar na mão: **Actions → Espelhar repositórios → Run workflow**, com estas opções:

- `dry_run`: só simula (`--dry-run`);
- `prune`: apaga do espelho os branches e tags que sumiram da origem (`--prune`);
- `only`: processa uma entrada só (`owner/repo` ou nome do espelho).

```bash
gh workflow run mirror.yml -f prune=true
gh workflow run mirror.yml -f only=owner/repo
```

## Uso local (opcional)

Precisa só de Python 3.12+ e git. Não há dependências. Use o token do `alves-r`: o do `gh` desta máquina é da conta principal e seria recusado.

```bash
read -rsp "Token do alves-r: " GITHUB_TOKEN && export GITHUB_TOKEN
python mirror.py list                             # status de cada entrada
python mirror.py sync --dry-run                   # o que seria feito
python mirror.py sync                             # aplica
python mirror.py sync --only owner/repo --prune
python mirror.py sync --skip-lists                # sem estrelas/Lists (topics continuam)
```

Códigos de saída: `0` tudo certo; `1` algum repo falhou; `2` erro de configuração (`repos.txt` inválido, token ausente ou recusado).

## O que fica público

O repositório de controle é **público**, então qualquer pessoa vê:

- o `repos.txt` (origens, categorias e nomes custom), o código e o workflow;
- a aba Actions, com histórico, logs e resumos: origem, categoria, status e mensagens de erro. O workflow roda com `--hide-names`, então os logs **não** mostram os nomes dos espelhos. Mesmo assim, o padrão `mirror-<owner>-<repo>` é dedutível e os nomes custom estão no `repos.txt`. Não trate os nomes como segredo (sem permissão, ninguém abre um repo privado);
- os commits de keepalive;
- o nome da conta dos espelhos (`alves-r`), citado neste README e no `mirror.py`.

Continuam privados o conteúdo dos espelhos, as Lists e o token. O secret aparece mascarado nos logs, forks e pull requests não têm acesso a ele, e o workflow não roda em PRs.

**Keepalive**: em repo público, o GitHub desativa agendamentos após 60 dias sem atividade. O job `keepalive` roda junto com o cron e faz um commit vazio quando o último commit tem 30 dias ou mais. Se mesmo assim o agendamento for desativado, reative em **Actions → Espelhar repositórios → Enable workflow**.

**Se um dia espelhar repositório privado**: o classic com `repo` cobre. Em organização com SSO, autorize o token em Settings → Developer settings → Personal access tokens → **Configure SSO**. Atenção: a URL do repo privado ficaria visível no `repos.txt` público, e espelhar código de empresa ou cliente numa conta pessoal pode violar contrato ou política interna.

## Limitações

- **Só branches e tags.** Issues, pull requests, wiki, releases (com seus arquivos), Discussions e configurações não são copiados.
- **Git LFS**: vão só os ponteiros, não os arquivos grandes.
- **O cron atrasa.** O `schedule` do Actions pode atrasar em horários de pico e, sob carga alta, uma execução pode ser descartada.
- **Falhas chegam por e-mail** (notificação padrão do Actions). Nos agendamentos, o aviso vai para quem editou o cron por último.
- **Estrelas**: as Lists só agrupam repos com estrela. Os espelhos categorizados aparecem com estrela no seu perfil e contam no total.
- **As Lists têm limites.** O GitHub limita a quantidade de Lists e o tamanho do nome (a comunidade relata 32 listas e 32 caracteres). Se a criação falhar, o log mostra o motivo e os topics continuam valendo.
- **Force push na origem é copiado.** O espelho acompanha o histórico reescrito; só a deleção de branches e tags depende de `--prune`.
- **Tamanho e tempo**: o GitHub limita cada push a 2 GB, então repositórios gigantes podem falhar na cópia inicial. O job tem 30 min. Passados 20 min, a execução não começa outro repo e o resto fica ⏭️ adiado (não conta como falha) para a próxima. Numa importação grande, rode de novo pelo *Run workflow* para não esperar o cron.
- **Criação em ritmo controlado**: o GitHub barra contas novas que criam muitos repos em pouco tempo (o `alves-r` foi barrado depois de 9 criações em ~1 min). Por isso cada execução cria no máximo 10 espelhos novos, com 60 s entre eles (`MAX_NEW_PER_RUN` e `CREATE_PAUSE` no `mirror.py`), e o resto fica ⏭️ adiado. O limite também mede o intervalo entre lotes (um lote começado 22 min depois do anterior foi barrado), então a execução só cria se o repo mais novo da conta tiver mais de 60 min (`CREATE_COOLDOWN`). A trava vale para qualquer disparo, seja cron, *Run workflow* ou o reforço local, e a mensagem de adiamento diz a hora em que a criação é liberada. Se mesmo assim o GitHub barrar as escritas, a execução para de escrever na hora e adia o que faltar. Insistir sob rate limit pode levar a banimento.
- **O Actions dos espelhos fica desligado** antes de qualquer push, para os workflows copiados da origem não rodarem nem gastarem minutos. Se não der para desligar, a cópia não acontece.
- **Os topics dos espelhos são gerenciados pela automação** (`mirror` mais o da categoria). Topics adicionados à mão são sobrescritos.

## Problemas comuns

| Sintoma | Causa / solução |
|---|---|
| `refusing to allow a Personal Access Token to create or update workflow` | Falta o escopo `workflow` no token. |
| `HTTP 401` ou "o token foi recusado" | O token expirou ou foi revogado. Renove e rode `gh secret set MIRROR_TOKEN`. |
| "o token é da conta …, mas os espelhos devem ficar em alves-r" | O secret recebeu o token da conta errada. Gere o PAT logado como `alves-r`. |
| Aviso "não foi possível ler suas Lists" ou `INSUFFICIENT_SCOPES` | Falta o escopo `user`. |
| "já existe um repositório com o nome deste espelho…" | O nome já é de outro repo seu. Use um nome custom na linha. |
| 🛡️ protegido | A origem sumiu ou está fora do ar e o espelho ficou intacto. É o backup funcionando. |
| O agendamento parou de rodar | Actions → Enable workflow (veja *Keepalive*). |
