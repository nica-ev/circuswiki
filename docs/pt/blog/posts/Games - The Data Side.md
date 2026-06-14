---
lang: pt
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Jogos - O Lado dos Dados
description: Como as descrições de jogos foram padronizadas e tornadas mais dinâmicas usando metadados e plugins do Obsidian.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:01:12+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:58+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Jogos - O Lado dos Dados**
**Como as descrições de jogos foram padronizadas e tornadas mais dinâmicas usando metadados e plugins do Obsidian.**

Quando se trata de gerir conteúdo, a consistência é fundamental. Para a primeira grande secção deste projeto, o meu foco foram os jogos — cerca de 170 deles, cada um com o seu formato, estilo e acessibilidade únicos. O problema? Muitas destas descrições dependiam de links codificados e estáticos, o que tornava um pesadelo adicionar novos jogos ou ajustar a estrutura.

Então, arregacei as mangas e pus-me a trabalhar.
<!-- more -->
## Passo 1: Um Formato Unificado
A primeira ordem de trabalhos foi estabelecer um formato consistente para todas as descrições de jogos. Inspirei-me no "Tasifan Spielebuch" (Livro de Jogos Tasifan), um recurso bem organizado para descrições de jogos. Para tornar as coisas ainda mais fáceis de usar, adicionei resumos curtos para que todos os detalhes essenciais fiquem visíveis num relance — mesmo numa pré-visualização.

Mas a verdadeira revolução? Metadados.

## Passo 2: Magia dos Metadados
Agora, toda a informação chave — tamanho do grupo, materiais, duração e mais — é armazenada como metadados no topo de cada ficheiro Markdown num formato chamado YAML (ou frontmatter). Isto não só mantém as coisas organizadas, como também torna os dados reutilizáveis em todo o sistema.

Para facilitar a procura do jogo certo, implementei uma lógica simples mas eficaz:
1. **Escolha uma categoria**: Que tipo de jogo procura? Um jogo de relaxamento? Um jogo de apanhada? Algo para construir equipas? Criei um conjunto de categorias para começar, mas estas podem ser ajustadas ou expandidas conforme necessário.
2. **Navegue pela tabela**: Assim que escolher uma categoria, verá uma tabela a listar todos os jogos que se encaixam. A tabela é ordenável — basta clicar nos cabeçalhos para organizar por duração, dificuldade ou outros critérios.

E aqui está o pormenor: muitos jogos aparecem em várias categorias, pelo que nunca está limitado a apenas uma forma de encontrar o que precisa.

## Tabelas Não Totalmente Dinâmicas
A verdadeira magia acontece com dois plugins do Obsidian: **Dataview** e **Dataview Serializer**.

O Dataview permite-me criar listas e tabelas dinâmicas usando consultas semelhantes a bases de dados. A contrapartida? Estas tabelas só funcionam dentro do Obsidian porque os ficheiros Markdown subjacentes não são modificados.

Entra o Dataview Serializer. Este plugin converte essas tabelas dinâmicas em formato Markdown estático e escreve-as diretamente no ficheiro. Quando o site é construído usando MkDocs, as tabelas são estáticas, mas foram essencialmente geradas dinamicamente offline.

Estas consultas podem tornar-se bastante complexas, permitindo-me pesquisar ou exibir partes específicas do wiki — como todas as descrições de jogos ou artigos escritos por um autor específico. E como se atualizam automaticamente (através do passo do serializador), adicionar nova informação e construir uma estrutura navegável é uma brisa.

Mas nem tudo são rosas. O processo não é totalmente automático. O Dataview Serializer só pode reescrever um ficheiro se este estiver aberto no Obsidian. Por agora, isto é gerível — marquei cada página com uma tabela ou lista dinâmica, tornando fácil percorrer as mesmas. Mas se o número destas páginas crescer significativamente, pode ser necessário repensar a abordagem.

## Ferramentas e Modelos de Linguagem
As descrições originais dos jogos eram uma mistura em termos de formatação e qualidade. Para otimizar o processo, recorri a modelos de linguagem (LLMs). Criei um prompt específico, completo com exemplos de formatação, para garantir que o conteúdo em si não era alterado (sem reescritas desnecessárias). Ainda assim, revistei manualmente cada resultado e fiz pequenos ajustes onde necessário.

Aqui está a conclusão: quando usadas corretamente, estas ferramentas são *incrivelmente* poderosas. A chave é ser preciso e intencional na forma como formula as suas tarefas.

As alterações finais são maioritariamente de formatação — como a informação e as descrições dos jogos são apresentadas. Os metadados, no entanto, foram todos inseridos manualmente. Como tive de verificar tudo de qualquer forma, fazê-lo à mão foi mais rápido neste caso.

É um processo lento, no entanto. Trabalhando a tempo parcial, consigo gerir cerca de 10-15 jogos por dia. O progresso é constante, mas vai demorar algum tempo.

## Desafios Futuros
Um obstáculo potencial são as traduções. As consultas de pesquisa teriam de ser adaptadas para encontrar versões específicas de jogos ou etiquetas em diferentes idiomas. Por agora, isto pode ser tratado manualmente, mas se o sistema crescer, a automação pode ser necessária.

A tradução é um tópico complexo, e irei aprofundar mais sobre isso noutra altura.

## Porquê o Esforço?
A resposta curta? Escalabilidade.

Este sistema foi concebido para crescer. Ao padronizar o formato, alavancar metadados e usar ferramentas dinâmicas, criei uma base que pode lidar com mais conteúdo sem se tornar incontrolável.

## O Que Mais Há de Novo?
A função de pesquisa recebeu algumas atualizações:
- **Autocompletar**: À medida que digita, a pesquisa sugere consultas que produzem mais resultados. Isto não se baseia no comportamento do utilizador — não rastreamos pesquisas — mas sim no índice de pesquisa estático gerado quando o site é construído.
- **Pesquisas guardadas**: Clique num pequeno ícone ao lado da barra de pesquisa, e a sua consulta (e resultados) são guardados no URL. Marque-o como favorito e obterá os mesmos resultados sempre.

É uma funcionalidade pequena, mas que pode tornar-se incrivelmente útil à medida que o wiki cresce e abrange tópicos mais diversos.
