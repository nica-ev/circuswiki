---
lang: pt
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Recibos e Documentos
description: Explica onde os documentos de suporte são armazenados e como as transações fazem referência a recibos.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:56+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:56+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Recibos e Documentos

Recibos, faturas, contratos e outros documentos de suporte tornam as transações auditáveis. O livro-razão deve permitir encontrar o documento por trás de uma despesa.

## Onde os documentos são armazenados

O Tohuwabohu tem atualmente uma pasta clara para recibos:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Recibos já inseridos no livro-razão estão frequentemente em:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

O NICA usa arquivos de suporte na sua pasta de contabilidade e nas pastas de projetos. Se uma pasta de recibos consistente para o NICA for introduzida mais tarde, documente-a aqui e use-a de forma consistente.

## Entradas `document`

Uma entrada `document` liga um arquivo a uma conta e data:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

O caminho do arquivo é relativo à pasta que contém o arquivo do livro-razão.

## Links de documentos com tags

Algumas entradas mais antigas incluem tags de documento como:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

A parte `^2023_001` é um link do Beancount. Ele pode conectar um recibo à transação relacionada se o mesmo link for usado lá.

## Significado de `scanned`

Comentários nos livros-razão definem a convenção para recibos digitalizados. Quando a tag `scanned` é usada, significa:

- O recibo foi digitalizado ou transformado em formato digital.
- A imagem foi reduzida e otimizada, por exemplo, com TinyPNG.
- O arquivo foi salvo usando um padrão de ano e número, por exemplo, `2023_002.jpg`.
- O número é referenciado na entrada do livro-razão relacionada.

## Bons nomes de arquivos

Bons nomes de arquivos de recibos são estáveis e legíveis:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Evite nomes como `scan.jpg`, `image1.jpg` ou `download.pdf`.

## Fluxo de trabalho para um novo recibo

1. Salve o recibo na pasta de recibos correta.
2. Renomeie-o para que possa ser reconhecido mais tarde.
3. Insira ou encontre a transação relacionada.
4. Adicione uma linha `document` ou metadados de link, se for útil.
5. Se o recibo foi processado, mova-o para `Eingetragen`, se essa for a convenção da pasta.
6. Recarregue o Fava e verifique se o link do documento funciona.

## Quando um recibo está em falta

Se um recibo estiver em falta, adicione um comentário perto da transação:

```beancount
; Receipt missing. Ask responsible person.
```

Não finja que existe um documento se ele não estiver disponível.

## Contratos e documentos de honorários

Contratos e faturas de honorários devem ser armazenados perto do projeto relacionado ou da pasta de contabilidade e referenciados claramente. Para auditorias de projetos, a pergunta importante não é apenas se a transação existe, mas se o documento que comprova a despesa pode ser encontrado rapidamente.
