---
lang: pt
translation_id: obsidian-setup
publish: true
tags: 
title: Configuração do Obsidian
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:07:03+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:23+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
O Obsidian é extremamente personalizável, o que pode ser um problema para iniciantes.
Fornecemos uma configuração base que pode ser usada como está, incluindo plugins e temas, bem como as suas configurações ajustadas.
Esta é uma configuração base e pode ser ainda mais adaptada às preferências pessoais de cada um.
Fornecemos apenas uma solução funcional – que documentaremos e explicaremos aqui.

## Termos utilizados
**Vault** – uma coleção de ficheiros markdown e imagens que formam a base de conhecimento

## Plugins

- Advanced Canvas
- BRAT
- Better Wordcount
- Clear unused Images
- Dataview
- Dataview Serializer
- Emoji Toolbar
- Linter
- Note Toolbar
- Tag Wrangler
- Templater
- Beautitab
- Omnisearch
- Status Bar Organizer
- Workspaces Plus
- Sortable

### Advanced Canvas
Dá acesso a muitas novas funcionalidades e opções de estilo para o Canvas

### BRAT
necessário para instalar plugins não oficiais / plugins não registados no Ecossistema do Obsidian, nomeadamente:
- Dataview Serializer
- Sortable

### Better Word Count
Usado principalmente pela sua capacidade de mostrar o número de palavras/caracteres no texto destacado.
É visível na barra de estado

### Beautitab
Puramente cosmético, fornece uma página personalizável de "novo separador vazio"

### Clear unused Images
como o nome diz, ajuda a organizar o vault identificando imagens não utilizadas

❗Excluí a subpasta ```/site/``` para não apagar sempre as imagens do site compilado (o que não é um problema, mais um incómodo)

❗Cuidado ao usar o comando clear attachments – pois isto apagará sempre ```mkdocs.yml``` e a ```license.``` --> se isto acontecer, os ficheiros estão na pasta .trash e podem ser recuperados. Mas é fácil de se esquecer.

### Dataview
permite consultas semelhantes a SQL no vault

### Dataview Serializer
transforma os resultados do Dataview em markdown
ajuda a reutilizar os resultados das consultas do dataview nas notas atuais

### Emoji Toolbar
bem, dá acesso fácil a emojis
**Atalho definido para: ALT-E**
😍

### Linter
limpa ficheiros markdown e dados de frontmatter
ajuda a manter uma forma consistente

### Note Toolbar
permite barras de ferramentas personalizáveis no topo de uma nota que podem ser definidas a nível de pasta/ficheiro

### Tag Wrangler
dá opções adicionais para trabalhar com tags
- renomear tags
ajuda a organizar o vault

### Templater
permite modelos personalizáveis que podem ser inseridos manualmente ou com base em condições (como a criação de uma nota)

### Status Bar Organizer
Permite ocultar itens da barra de estado

### Sortable
Permite a ordenação de tabelas (tanto markdown como tabelas dataview) clicando nos seus cabeçalhos.

### Workspaces Plus
Permite uma troca rápida e fácil a partir da barra de estado

## Sistema de Ficheiros do Vault

[Sistema de Ficheiros do Vault](Vault%20File%20System.md){ .md-button }
