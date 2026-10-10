---
lang: pt
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Rotina Regular de Contabilidade
description: Um checklist prático e recorrente para manter os livros atualizados.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:08+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:08+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 - Rotina Regular de Contabilidade

Esta página descreve uma rotina prática para manter os livros contábeis atualizados.

## Rotina Semanal ou Quinzenal

Use esta rotina quando houver movimentos bancários regulares.

1. Abra a instância correta do Fava.
2. Verifique se o Fava exibe erros.
3. Encontre a última verificação de saldo.
4. Exporte os novos dados CSV do Sparkasse.
5. Converta o CSV com `csv2bean.py`.
6. Cole as novas entradas em `Bank Dump`.
7. Classifique as entradas nas contas corretas.
8. Anexe ou referencie recibos onde necessário.
9. Adicione uma nova verificação de saldo.
10. Recarregue o Fava e resolva os erros.
11. Revise `Ausgaben:Sonstiges` (Despesas:Outros) e `Einnahmen:Sonstiges` (Receitas:Outros) para entradas que deveriam ser mais específicas.

## Rotina Mensal

No final do mês:

1. Concilie o Sparkasse.
2. Concilie o PayPal, se utilizado.
3. Concilie a caixa de dinheiro, se dinheiro foi utilizado.
4. Verifique os passivos pendentes com pessoas.
5. Verifique os saldos dos projetos ativos.
6. Revise as entradas não classificadas em `Sonstiges` (Outros).
7. Verifique recibos em falta.
8. Verifique se algum projeto concluído deve ser preparado para encerramento.

## Rotina de Relatório de Projetos

Antes de preparar um relatório de projeto ou Verwendungsnachweis (comprovação de uso):

1. Abra as páginas da conta do projeto no Fava.
2. Exporte ou revise todas as receitas e despesas do projeto.
3. Confirme se as categorias correspondem às linhas orçamentárias do financiador.
4. Confirme se todos os recibos e documentos de honorários existem.
5. Verifique se reembolsos, cancelamentos e ressarcimentos foram registrados como correções e não como receitas falsas.
6. Confirme se o saldo de ativos do projeto é explicável.
7. Se o projeto estiver concluído, mova o dinheiro restante corretamente e encerre as contas do projeto.

## Rotina de Fim de Ano

No final do ano:

1. Concilie todas as contas bancárias.
2. Concilie o PayPal.
3. Concilie as caixas de dinheiro.
4. Verifique os passivos.
5. Verifique os saldos pendentes dos projetos.
6. Garanta que todos os recibos estejam armazenados e vinculados ou localizáveis.
7. Revise as categorias de receitas e despesas.
8. Adicione verificações de saldo finais.
9. Prepare relatórios a partir do Fava.
10. Arquive os CSVs exportados e os documentos de suporte.

## Verificações de Qualidade

Um livro contábil está em bom estado quando:

- O Fava abre sem erros.
- A última verificação de saldo do Sparkasse corresponde ao banco.
- Os saldos do PayPal e de dinheiro são verificados onde relevante.
- Os saldos dos projetos são intencionais e explicáveis.
- Projetos encerrados têm saldo de ativos zero.
- As contas `Sonstiges` (Outros) não contêm entradas não categorizadas evitáveis.
- Recibos de despesas podem ser encontrados.
- Comentários explicam correções ou suposições incomuns.

## Lista de Verificação para Transição para Outra Pessoa

Antes de entregar a contabilidade a outra pessoa:

- Mostre a ela o arquivo de contabilidade correto para cada associação.
- Mostre como iniciar o Fava.
- Mostre a ela a última verificação de saldo.
- Mostre como as importações de CSV são organizadas em `Bank Dump`.
- Mostre onde os recibos são armazenados.
- Mostre um exemplo de projeto, desde a receita do financiamento até o encerramento final.
- Indique a ela esta pasta de documentação.
