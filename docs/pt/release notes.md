---
lang: pt
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Notas de Lançamento
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:14:13+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:04+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
[!info]
Estas notas de lançamento fornecem apenas uma visão geral aproximada; pequenas alterações (como páginas individuais novas ou modificações de conteúdo existente) não são todas listadas. No entanto, estas podem ser rastreadas em detalhe no histórico do repositório.

[!info]- **Versão:** v0.04 - **Data de Lançamento**: 9 de junho de 2026
>**Conteúdo**
>- Conteúdo multilíngue amplamente expandido: o conteúdo agora está estruturado em `docs/<idioma>`.
>- Adicionadas novas e atualizadas traduções para muitas descrições de jogos e páginas de projetos.
>- Materiais de workshop em polonês importados e integrados à estrutura de conteúdo multilíngue.
>- Estrutura de conteúdo e metadados para jogos ainda mais unificada.
>
>**Técnico**
>- Gerador de site alterado de MkDocs/MkDocs Material para Zensical.
>- Nova estrutura multilíngue de build e staging introduzida.
>- O alemão continua sendo o idioma padrão sem prefixo de idioma; outros idiomas serão publicados sob códigos de idioma, por exemplo, `/en/`, `/pl/`, `/es/`.
>- Configuração central de idioma introduzida através de `tools/config/languages.json`.
>- Implantação do GitHub Pages atualizada para a nova estrutura Zensical.
>- Ferramentas de tradução local e console de desenvolvimento amplamente expandidos: verificações de integridade, agendamento em lote, status de tradução, visualizações de gráfico, ferramentas de navegação, reparo de links e fluxos de trabalho de limpeza.
>- Adicionado seletor de idioma, indicadores de status de tradução e páginas de fallback para traduções ausentes.
>- Tabelas na saída final do site aprimoradas: tabelas classificáveis, melhor exibição de tabelas densas e seções de página opcionalmente recolhíveis.
>
>**Corrigido**
>- Links internos e links Markdown em páginas traduzidas são mantidos e reparados de forma mais confiável.
>- Navegação multilíngue e estrutura de URL foram estabilizadas.
>- O comportamento responsivo da navegação foi aprimorado, especialmente em conjunto com o menu hambúrguer móvel do Zensical.

[!info]- **Versão:** v0.03 - **Data de Lançamento**: 11 de março de 2025
>**Conteúdo**
>- Descrições de jogos ausentes adicionadas
>
>**Técnico**
>- Favicon + logotipo adicionados
>- Redesign da UI
>- A navegação de primeiro nível agora está no cabeçalho da página, enquanto a barra de navegação direita é ajustada contextualmente
>- Tabelas podem ser classificadas clicando nos cabeçalhos
>
>**Corrigido**
>- Tags funcionando novamente

[!info]- **Versão:** v0.02 - **Data de Lançamento**: 26 de fevereiro de 2025
>**Técnico**
>- Função de Blog
>- Analytics (Google)
>- Banner de Cookies
>- Widget de Feedback (na parte inferior de cada página)

[!info]- **Versão:** v0.01 - **Data de Lançamento** 15 de janeiro de 2025
>**Conteúdo**
>- 150 descrições de jogos adicionadas
>- Descrição básica da documentação
>
>**Técnico**
>- Configuração base para Mkdocs e Mkdocs-materials
>- Suporte Obsidian com Mkdocs-publisher (permite o uso de Markdown do Obsidian, como links Markdown, caixas de chamada)
