---
lang: pt
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Mapa de Pastas e Arquivos
description: Mapeia as pastas importantes de contabilidade, arquivos de lançamentos, painéis e arquivos auxiliares.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:28+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:28+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Mapa de Pastas e Arquivos

Esta página explica onde os arquivos importantes de contabilidade estão armazenados.

## Pasta principal de contabilidade

```text
1. Vereinsverwaltung/Buchhaltung
```

Esta pasta contém os livros-razão, arquivos de painel, documentos de suporte e pastas auxiliares.

## Arquivos importantes de nível superior

| Arquivo | Propósito |
| --- | --- |
| `Buchhaltung Home.md` | Página de entrada do Obsidian com botões e uma breve nota de fluxo de trabalho. |
| `all.beancount` | Livro-razão combinado experimental incluindo NICA e Tohuwabohu. |
| `dashboards.yaml` | Definição do painel para os painéis Fava no nível compartilhado. |

## Estrutura NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Caminho | Propósito |
| --- | --- |
| `2023/nica.beancount` | Livro-razão principal da NICA. Este é o arquivo normalmente editado. |
| `2023/dashboards.yaml` | Configuração do painel para o livro-razão da NICA. |
| `2023/Buchhaltung NICA eV.md` | Nota auxiliar do Obsidian para abrir a contabilidade da NICA. |
| `2023/CSV/` | Exportações CSV armazenadas. |
| `test/csv2bean.py` | Converte CSV da Sparkasse em entradas temporárias do Beancount. |
| `test/beancount_file.beancount` | Saída gerada da conversão CSV. |
| `test/paypal2bean.py` | Auxiliar para importações CSV do PayPal. |
| `test/output_file_paypal.beancount` | Arquivo de saída do PayPal gerado. |
| `test/old files/` | CSVs mais antigos e arquivos gerados. |

## Estrutura Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Caminho | Propósito |
| --- | --- |
| `2023/2023.beancount` | Livro-razão principal do Tohuwabohu. Este é o arquivo normalmente editado. |
| `2021/2021.beancount` | Dados de livro-razão mais antigos incluídos através de `all.beancount`. |
| `all.beancount` | Arquivo combinado do Tohuwabohu incluindo os arquivos de livro-razão de 2021 e 2023. |
| `2023/dashboards.yaml` | Configuração do painel para o livro-razão do Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Nota auxiliar do Obsidian. |
| `2023/Belege Ausgaben/` | Recibos e documentos de suporte para despesas. |
| `2023/Belege Ausgaben/Eingetragen/` | Recibos já registrados no livro-razão. |
| `test/csv2bean.py` | Converte CSV da Sparkasse em entradas temporárias do Beancount. |
| `test/beancount_file.beancount` | Saída gerada da conversão CSV. |
| `test/paypal2bean.py` | Auxiliar para importações CSV do PayPal. |
| `test/output_file_paypal.beancount` | Arquivo de saída do PayPal gerado. |
| `test/CSV - old files/` | CSVs mais antigos e arquivos gerados. |

## Princípio de nomenclatura de arquivos

As pastas ainda contêm nomes históricos como `2023`, mesmo quando também contêm atividades posteriores de 2024, 2025 e 2026. Trate os arquivos de livro-razão principais atualmente referenciados como os livros-razão ativos, a menos que a estrutura seja alterada intencionalmente.

## Onde editar

| Associação | Edite este arquivo |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Não edite arquivos de saída gerados como registro permanente. Eles são arquivos temporários de preparação.
