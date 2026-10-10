---
lang: pt
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Visão Geral do Sistema
description: Explica o propósito, os componentes e o fluxo de trabalho normal do usuário do sistema de contabilidade.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:03:59+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:03:59+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Visão Geral do Sistema

## Propósito

O sistema de contabilidade registra toda a atividade financeira das associações de forma estruturada e verificável. Ele foi projetado para responder às perguntas normais de contabilidade:

- Quanto dinheiro está disponível no momento?
- Quais receitas e despesas pertencem à própria associação?
- Quais receitas e despesas pertencem a um projeto específico?
- Os saldos da Sparkasse, PayPal e dinheiro estão corretos?
- Quais comprovantes e documentos pertencem a quais transações?
- Quais projetos estão ativos, concluídos ou já encerrados?

## Componentes Principais

| Componente | O que faz |
| --- | --- |
| Beancount | O formato dos dados contábeis. As transações são escritas em arquivos de texto simples. |
| Fava | A interface do navegador para visualizar e filtrar os dados do Beancount. |
| Fava Dashboards | Páginas de painel personalizadas dentro do Fava para visão geral da gestão e visualizações de projetos. |
| Obsidian | O sistema de notas a partir do qual a contabilidade pode ser aberta através de botões. |
| Scripts de importação CSV | Scripts auxiliares que convertem exportações CSV da Sparkasse em entradas Beancount. |

## Como as partes se encaixam

1. Os dados do banco ou PayPal são exportados como CSV.
2. O CSV é convertido em entradas temporárias do Beancount.
3. As novas entradas são copiadas para o arquivo de razão correto.
4. O usuário verifica, classifica e corrige as entradas.
5. Verificações de saldo confirmam que a razão corresponde ao saldo do banco ou PayPal.
6. O Fava exibe relatórios, páginas de contas, demonstrações de resultados, balanços e painéis.

## Duas associações separadas

| Associação | Razão | Prefixo de conta típico |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Existe também um arquivo combinado experimental: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. O trabalho normal do dia a dia deve ser feito na razão individual da associação relevante.

## Fluxo de trabalho básico

1. Abra a instância correta do Fava.
2. Encontre a última verificação de saldo concluída.
3. Exporte as novas transações bancárias da Sparkasse a partir da última data verificada.
4. Converta o CSV para o formato Beancount.
5. Cole as entradas geradas primeiro na seção `Bank Dump`.
6. Mova ou classifique as entradas para as seções corretas da associação ou projeto.
7. Adicione comprovantes, links, comentários ou tags quando necessário.
8. Adicione uma nova verificação de saldo.
9. Recarregue o Fava e verifique se não há erros.

## O que um novo usuário deve aprender primeiro

1. [Abrindo o Fava](02-opening-fava.md)
2. [Noções básicas de Beancount para usuários](04-beancount-basics-for-users.md)
3. [Importação e Conciliação de CSV Bancário](07-bank-csv-import-and-reconciliation.md)
4. [Contas e Categorias](05-accounts-and-categories.md)
5. [Projetos e Fundos Restritos](08-projects-and-restricted-funds.md)
