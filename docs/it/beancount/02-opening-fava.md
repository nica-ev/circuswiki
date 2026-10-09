---
lang: it
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Apertura Fava
description: Come avviare e aprire l'interfaccia locale di contabilità Fava.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:33:33+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:33:33+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Avvio di Fava

Fava è l'interfaccia web utilizzata per ispezionare la contabilità. Viene eseguita localmente sul computer e si apre in un browser o nella vista web di Obsidian.

## Requisiti

Il computer deve avere installati e disponibili i seguenti programmi:

- Python
- Beancount
- Fava
- `fava-dashboards` se l'estensione dashboard deve essere visibile
- Obsidian, se si utilizzano i pulsanti di Obsidian

## Apertura da Obsidian

La nota `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` contiene pulsanti per aprire la contabilità. I pulsanti avviano Fava tramite Obsidian Shell Commands e quindi aprono l'URL locale di Fava.

| Pulsante | Apre |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava sulla porta `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava sulla porta `4999` |

Non chiudere la finestra del terminale che avvia Fava. Se il terminale viene chiuso, Fava si interrompe.

## Apertura manuale

### NICA e.V.

Aprire un terminale in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Eseguire:

```powershell
fava nica.beancount --port 4998
```

Quindi aprire `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Aprire un terminale in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Eseguire:

```powershell
fava 2023.beancount --port 4999
```

Quindi aprire `http://127.0.0.1:4999/`.

## File batch di avvio

| File | Scopo |
| --- | --- |
| `startup-nica.bat` | Avvia NICA Fava sulla porta `4998`. |
| `startup-tohu.bat` | Avvia Tohuwabohu Fava sulla porta `4999`. |
| `startup-all.bat` | Avvia Obsidian, diversi strumenti e entrambe le istanze di Fava. |

## URL importanti

| Vista | NICA | Tohuwabohu |
| --- | --- | --- |
| Home | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Dashboards | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Conto Economico | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Quando Fava è già in esecuzione

Se Fava è già in esecuzione, è sufficiente aprire l'URL. Se la porta è già occupata e Fava non si avvia, un'altra istanza di Fava potrebbe essere già aperta. Utilizzare la pagina del browser esistente o chiudere la vecchia finestra del terminale e riavviare.
