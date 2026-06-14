---
lang: pt
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki e Além
description: 
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Zettelkasten, Wiki, and Beyond.md
translation_source_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:30:32+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:14+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki e Além**  
**Por que comecei este projeto, as ideias por trás dele e para onde ele pode levar.**

Em 2013, trabalhei como gestor de projetos para um circo jovem. Os formadores frequentemente me perguntavam se eu conhecia outros jogos, métodos ou truques. Na época, eu tinha muitos recursos — livros, revistas, anotações de workshops — mas tudo estava desorganizado e mal digitalizado.  
<!-- more -->
Minha primeira tentativa de tornar esses recursos acessíveis aos formadores foi um wiki clássico. Muitas das descrições de jogos que vocês veem hoje se originaram desse período. Simultaneamente, comecei a digitalizar minhas fontes. Descobri o método *Zettelkasten* (caixa de fichas) de Niklas Luhmann e comecei a organizar meus dados usando seus princípios.  

O wiki foi um fracasso. Houve pouca interação; os formadores o usaram algumas vezes e ele foi rapidamente esquecido. Meu Zettelkasten pessoal, no entanto, começou a crescer. Embora eu tenha começado usando software especializado, logo comecei a pensar em como tornar essa coleção cada vez mais valiosa à prova de futuro.  

O que isso significa? O primeiro alerta veio quando percebi que o software que eu estava usando não estava mais em desenvolvimento. Tive que encontrar um novo software — e descobrir como migrar meus dados para ele. Foi quando descobri o Markdown.  

Markdown é um formato de arquivo simples — essencialmente um arquivo de texto puro — projetado para funcionar independentemente de qualquer software específico. Em outras palavras, é um padrão amplamente adotado que pode ser lido e editado com as ferramentas mais básicas.  

O formato suportava tudo o que eu precisava: formatação básica de texto, links, tags e metadados (por exemplo, título, autor, descrição, etc.). Encontrei um novo software que usava Markdown e continuei a construir meu Zettelkasten. Naquele ponto, eu tinha cerca de 600 notas (ou arquivos/páginas). Mais tarde, troquei de software novamente, e a transição foi perfeita.  

>[!info]  Ponto Chave
>Tornar seus dados à prova de futuro significa usar um formato simples, amplamente adotado e independente de software específico.  

## Colaboração e Compartilhamento  

Minha primeira tentativa de wiki não funcionou — em parte porque falhei em inspirar outros a contribuir. Ao longo dos anos, meu Zettelkasten pessoal cresceu para mais de 3.000 notas, muitas delas sobre tópicos como pedagogia circense, jogos, malabarismo e muito mais.  

Por um tempo, simplesmente o disponibilizei online, mas, além de algumas pessoas que sabiam sobre ele e ocasionalmente consultavam descrições de jogos, não houve colaboração real ou compartilhamento mais amplo.  

Agora, cerca de 12 anos após iniciar meu Zettelkasten, estou tentando novamente. O objetivo é criar uma base de conhecimento compartilhada para tópicos como pedagogia circense e de movimento, artes circenses e além.  

### Considerações e Perguntas Chave  
- **Independência de sistemas específicos**  
- **Formato de dados simples e fácil de entender**  
- **Utilidade e público-alvo**  
- **Dados estruturados**  

Software de wiki tradicional (ou plataformas como WordPress) estavam fora de questão porque criam dependência de um único sistema. Embora isso possa funcionar a curto ou médio prazo, é uma fraqueza clara a longo prazo.  

Em vez disso, estou gerenciando os dados (como arquivos Markdown e de imagem) independentemente de como eles são apresentados. Isso garante que, mesmo daqui a 20 anos, os dados permaneçam utilizáveis. A forma como são exibidos ou editados pode mudar drasticamente, mas os dados subjacentes permanecem os mesmos.  

Existem inúmeras maneiras de apresentar os dados: como um site, um eBook, um PDF ou até mesmo um aplicativo. Pode ser compactado em um arquivo e lido ou editado offline com um editor de texto simples. Se você quiser exibi-lo como um site WordPress ou wiki, isso é apenas uma questão de importar os dados — como eles são estruturados e fáceis de ler, é relativamente simples de implementar (com o conhecimento certo).  

## Minha Solução Atual para o Website  

Estou usando MkDocs e o tema MkDocs-Material para gerar um site estático. Existem muitos programas que criam arquivos HTML estáticos a partir de Markdown, mas o MkDocs é projetado especificamente para documentação. Muitos dos recursos que ele gera — como busca em texto completo e navegação — são incrivelmente úteis.  

O MkDocs também é uma solução de código aberto amplamente utilizada e apoiada por grandes empresas, o que garante que ele permanecerá funcional pelo menos a médio prazo.  

## Colaboração  

O próximo passo é tornar isso um esforço colaborativo. Estou explorando maneiras de convidar outros a contribuir, seja adicionando novo conteúdo, refinando entradas existentes ou sugerindo melhorias. O objetivo é criar um recurso vivo e em evolução que se beneficie do conhecimento e da experiência coletivos.
