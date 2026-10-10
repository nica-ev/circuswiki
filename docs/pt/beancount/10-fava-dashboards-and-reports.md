---
lang: pt
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Dashboards e Relatórios Fava
description: Visão geral dos relatórios Fava e dashboards personalizados usados para revisão de contabilidade.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:31+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:31+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 - Dashboards e Relatórios Fava

O Fava oferece relatórios contábeis padrão. O sistema também utiliza `fava-dashboards` para páginas de visão geral personalizadas.

## Visualizações Padrão do Fava

| Visualização | Uso para |
| --- | --- |
| Balanço Patrimonial | Verificar ativos, passivos, fundos livres, PayPal, dinheiro em espécie e saldos de projetos. |
| Demonstração de Resultados | Visualizar receitas e despesas ao longo do tempo. |
| Página de Conta | Inspecionar todas as transações de uma conta específica. |
| Diário | Pesquisar histórico cronológico de transações. |
| Consulta | Executar consultas Beancount personalizadas quando necessário. |
| Documentos | Encontrar recibos e arquivos vinculados. |

## Extensão de Dashboard

Os ledgers incluem esta diretiva:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Isso ativa a extensão de dashboard se `fava-dashboards` estiver instalado.

## Arquivos de Configuração do Dashboard

Os arquivos de dashboard são nomeados `dashboards.yaml`. Eles são armazenados perto dos arquivos do ledger e no nível compartilhado de contabilidade.

## Seções Principais do Dashboard

| Dashboard | Propósito |
| --- | --- |
| `Vorstand-Cockpit` | Visão geral da gestão: dinheiro livre, saldo total Sparkasse, PayPal, dinheiro em espécie, tendência de liquidez, resultado mensal, saldos de projetos ativos. |
| `Details & Daten` | Gráficos detalhados: despesas por categoria, receitas por categoria, fluxo de caixa, rede de projetos/pessoas. |

## Indicadores Importantes do Dashboard

### Freies Geld (Dinheiro Livre)

Mostra o dinheiro disponível fora dos fundos restritos de projetos. Contas típicas são `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` e `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt (Total Sparkasse)

Mostra o saldo total da Sparkasse entre a conta bancária principal e subcontas internas.

### PayPal

Mostra o saldo do PayPal. Um saldo negativo no PayPal indica que algo precisa ser verificado.

### Barkasse (Caixa)

Mostra o saldo da caixa de dinheiro.

### Saldo Aktiver Projekte (Saldo de Projetos Ativos)

Mostra saldos de projetos diferentes de zero. Isso é útil para ver quais projetos ainda possuem dinheiro ou estão com gastos excessivos.

### Monatlicher Ueberschuss / Fehlbetrag (Excedente / Déficit Mensal)

Mostra o excedente ou déficit operacional mensal, excluindo contas de projetos na consulta do dashboard.

## Como Usar Dashboards com Responsabilidade

Dashboards são resumos. Se um número parecer surpreendente:

1. Clique na conta ou relatório Fava vinculado.
2. Inspecione as transações subjacentes.
3. Verifique se uma transação ainda está em `Sonstiges` (Outros) ou `Bank Dump` (Despejo Bancário).
4. Verifique se o nome da conta corresponde ao padrão da consulta do dashboard.
5. Confirme as verificações de saldo antes de confiar nos números da gestão.

## Quando os Números do Dashboard Parecem Errados

Causas comuns:

- Uma transação foi registrada na conta bancária principal em vez da subconta do projeto.
- Uma conta de projeto foi fechada, mas ainda possui um saldo diferente de zero.
- Um novo projeto usa um padrão de nomenclatura não incluído na consulta do dashboard.
- Uma transação ainda está em uma categoria de fallback ampla.
- O arquivo do dashboard pertence a um ledger diferente do que está aberto no momento.
