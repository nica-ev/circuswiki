---
lang: pt
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: GitHub - Colaborar diretamente no repositório
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:47+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:20+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] Em resumo
> Esta página destina-se a pessoas que desejam trabalhar diretamente nos ficheiros Markdown do CircusWiki. Para contribuições normais, não precisa deste caminho: pode simplesmente enviar material por e-mail.

A colaboração direta através do GitHub é prática se quiser corrigir páginas regularmente, criar novos ficheiros Markdown ou trabalhar com o cofre do CircusWiki num editor como o Obsidian.

Se quiser apenas contribuir com um jogo, um método, um PDF, um link ou uma correção, o caminho mais simples é geralmente o melhor:

[Voltar a Contribuir](mitmachen.md){ .md-button }

## O que precisa

- Uma conta gratuita no GitHub: [https://github.com/join](https://github.com/join)
- Opcionalmente, GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- Um editor de texto para ficheiros Markdown, por exemplo, Obsidian, VS Code ou um editor simples

O GitHub Desktop não é obrigatório, mas é mais fácil para muitas pessoas do que a linha de comando.

## Encontrar o repositório

O repositório público encontra-se aqui:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Lá estão os ficheiros Markdown reais, imagens, traduções e ferramentas a partir dos quais o website é construído.

## Fluxo de trabalho em resumo

O processo típico é:

1. Fazer um fork do repositório no GitHub.
2. Clonar a sua cópia para o seu próprio computador.
3. Fazer alterações num novo branch.
4. Editar ficheiros ou criar novos ficheiros Markdown.
5. Fazer commit das alterações.
6. Carregar o branch para o GitHub.
7. Abrir um Pull Request para que a alteração possa ser revista e aceite.

## Passo a passo com GitHub Desktop

### 1. Fazer um fork do repositório

Abra o repositório CircusWiki no GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Clique em `Fork`. Isto cria uma cópia própria do repositório na sua conta GitHub. Nesta cópia, pode trabalhar sem alterar diretamente o projeto principal.

### 2. Clonar o repositório

Abra o GitHub Desktop e selecione:

```text
File -> Clone repository...
```

Selecione o seu fork de `nica-ev/circuswiki` e escolha uma pasta no seu computador.

Depois disto, terá uma cópia local dos ficheiros.

### 3. Criar um branch

É melhor criar um branch próprio para a sua alteração, por exemplo:

```text
adicionar-descricao-jogo
corrigir-link
novo-metodo-equilibrismo
```

Um branch mantém o seu trabalho separado do estado principal. Isto facilita a revisão posterior.

### 4. Editar ficheiros

Os conteúdos públicos encontram-se principalmente nas pastas de idiomas em `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Todas as línguas são equivalentes. Não existe uma língua principal em que novos conteúdos devam ser criados fundamentalmente.

Se criar uma nova página original, coloque-a na pasta de idioma na qual o texto está escrito. Um texto original em espanhol, por exemplo, deve ir para `docs/es/`, um em alemão para `docs/de/`, um em inglês para `docs/en/`.

O "frontmatter" no início do ficheiro é importante. Deve ser reconhecível que a página é um original, por exemplo:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` corresponde à língua do texto original. A partir deste original, as traduções podem ser geradas automaticamente em todas as línguas suportadas mais tarde.

Ao editar, preste atenção ao seguinte:

- Não apague o "frontmatter" no início do ficheiro.
- Para novas páginas originais, defina `translation_status: original` e a `translation_source_lang` apropriada.
- Mantenha os links existentes sempre que possível.
- Não publique dados privados, chaves de API ou notas internas.
- Use imagens apenas se os direitos de uso forem claros.
- Prefira fazer alterações pequenas e claras em vez de alterações mistas muito grandes.

### 5. Fazer commit das alterações

No GitHub Desktop, verá os seus ficheiros alterados na secção `Changes`.

Escreva um breve resumo, por exemplo:

```text
Corrigir lista de materiais no jogo de movimento
Adicionar aviso de segurança para Beigoma
Adicionar nova descrição de jogo
```

Em seguida, clique em `Commit to <branch-name>`.

### 6. Carregar as alterações

Clique em `Push origin` para carregar o seu branch para o GitHub.

### 7. Abrir um Pull Request

O GitHub Desktop ou o GitHub no navegador oferecerão então a opção de criar um Pull Request.

Um Pull Request significa: você propõe a sua alteração para o repositório principal. A alteração será revista, comentada se necessário e depois aceite ou trabalhada posteriormente.

## Fundamentos do Markdown

Markdown é um formato de texto simples. Os caracteres mais importantes são suficientes para a maioria das contribuições:

```markdown
# Título grande
## Título de secção

Texto normal com **parte em negrito** e *parte em itálico*.

- Ponto de lista
- Outro ponto de lista

[Texto do link](https://www.example.com)
```

## Se algo não estiver claro

Não é preciso dominar imediatamente a colaboração direta através do GitHub. Se abrir um Pull Request e algo ainda não estiver correto, isso pode ser esclarecido na revisão.

Se quiser apenas contribuir com conteúdo e o caminho técnico parecer demasiado complicado, utilize simplesmente o e-mail na [página de Contribuição](mitmachen.md).
