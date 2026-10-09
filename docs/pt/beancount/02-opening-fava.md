---
lang: pt
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Abertura Fava
description: Como iniciar e abrir a interface local de contabilidade Fava.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:34:16+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:34:16+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Abrir o Fava

Fava é a interface web utilizada para inspecionar a contabilidade. Ela é executada localmente no computador e aberta num navegador ou na visualização web do Obsidian.

## Requisitos

O computador deve ter os seguintes programas instalados e disponíveis:

- Python
- Beancount
- Fava
- `fava-dashboards` se a extensão de dashboards deve ser visível
- Obsidian, se estiver a usar os botões do Obsidian

## Abrir a partir do Obsidian

A nota `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` contém botões para abrir a contabilidade. Os botões iniciam o Fava através dos Comandos de Shell do Obsidian e depois abrem o URL local do Fava.

| Botão | Abre |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava na porta `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava na porta `4999` |

Não feche a janela do terminal que inicia o Fava. Se o terminal for fechado, o Fava para.

## Abrir manualmente

### NICA e.V.

Abra um terminal em:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Execute:

```powershell
fava nica.beancount --port 4998
```

Depois abra `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Abra um terminal em:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Execute:

```powershell
fava 2023.beancount --port 4999
```

Depois abra `http://127.0.0.1:4999/`.

## Ficheiros batch de inicialização

| Ficheiro | Propósito |
| --- | --- |
| `startup-nica.bat` | Inicia o NICA Fava na porta `4998`. |
| `startup-tohu.bat` | Inicia o Tohuwabohu Fava na porta `4999`. |
| `startup-all.bat` | Inicia o Obsidian, várias ferramentas e ambas as instâncias do Fava. |

## URLs importantes

| Visualização | NICA | Tohuwabohu |
| --- | --- | --- |
| Início | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Dashboards | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Demonstração de Resultados | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Quando o Fava já está a correr

Se o Fava já estiver a correr, basta abrir o URL. Se a porta já estiver ocupada e o Fava se recusar a iniciar, é possível que outra instância do Fava já esteja aberta. Utilize a página do navegador existente ou feche a janela do terminal antiga e recomece.
