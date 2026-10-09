---
lang: pt
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Documentação do Sistema de Contabilidade
description: Visão geral e ponto de partida para a documentação de contabilidade Beancount da NICA e.V. e Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:31:53+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:31:53+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Documentação do Sistema de Contabilidade

Esta documentação explica como funciona o sistema de contabilidade da NICA e.V. e da Tohuwabohu Halle e.V. do ponto de vista de um utilizador normal.

O sistema utiliza ficheiros de contabilidade em texto simples no formato Beancount e uma interface de navegador chamada Fava. Não precisa de compreender programação para o utilizar, mas precisa de seguir cuidadosamente o fluxo de trabalho de contabilidade: importar dados bancários, classificar transações, anexar recibos quando necessário e verificar saldos.

## Comece aqui

- [01 - Visão Geral do Sistema](01-system-overview.md)
- [02 - Abrir o Fava](02-opening-fava.md)
- [03 - Mapa de Pastas e Ficheiros](03-folder-and-file-map.md)
- [04 - Noções Básicas de Beancount para Utilizadores](04-beancount-basics-for-users.md)
- [05 - Contas e Categorias](05-accounts-and-categories.md)
- [06 - Inserir e Editar Transações](06-entering-and-editing-transactions.md)
- [07 - Importação e Conciliação de CSV Bancário](07-bank-csv-import-and-reconciliation.md)
- [08 - Projetos e Fundos Restritos](08-projects-and-restricted-funds.md)
- [09 - Recibos e Documentos](09-receipts-and-documents.md)
- [10 - Dashboards e Relatórios do Fava](10-fava-dashboards-and-reports.md)
- [11 - Rotina Regular de Contabilidade](11-regular-bookkeeping-routine.md)
- [12 - Resolução de Problemas](12-troubleshooting.md)
- [13 - Glossário](13-glossary.md)

## A regra mais importante

O ficheiro de contabilidade é a fonte da verdade. O Fava apenas exibe o que está escrito nos ficheiros `.beancount`. Se algo parecer incorreto no Fava, corrija a entrada no Beancount e recarregue o Fava.

## Livros de contas atuais

| Organização | Ficheiro principal | Endereço Fava | Porta |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## O que esta documentação não é

Isto não é aconselhamento legal ou fiscal. Descreve como este sistema de contabilidade local específico está organizado e como os utilizadores devem trabalhar com ele de forma consistente.
