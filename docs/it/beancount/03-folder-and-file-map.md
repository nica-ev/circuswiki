---
lang: it
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Mappa Cartelle e File
description: Mappa le cartelle contabili importanti, i file di registro, le dashboard e i file di supporto.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:03+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Mappa Cartelle e File

Questa pagina spiega dove sono archiviati i file contabili importanti.

## Cartella principale di contabilità

```text
1. Vereinsverwaltung/Buchhaltung
```

Questa cartella contiene i registri, i file di dashboard, i documenti di supporto e le cartelle di aiuto.

## File importanti di primo livello

| File | Scopo |
| --- | --- |
| `Buchhaltung Home.md` | Pagina di ingresso di Obsidian con pulsanti e una breve nota sul flusso di lavoro. |
| `all.beancount` | Registro combinato sperimentale che include sia NICA che Tohuwabohu. |
| `dashboards.yaml` | Definizione del dashboard per i dashboard di Fava a livello condiviso. |

## Struttura NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Percorso | Scopo |
| --- | --- |
| `2023/nica.beancount` | Registro principale NICA. Questo è il file normalmente modificato. |
| `2023/dashboards.yaml` | Configurazione del dashboard per il registro NICA. |
| `2023/Buchhaltung NICA eV.md` | Nota di aiuto di Obsidian per l'apertura della contabilità NICA. |
| `2023/CSV/` | Esportazioni CSV archiviate. |
| `test/csv2bean.py` | Converte CSV Sparkasse in voci Beancount temporanee. |
| `test/beancount_file.beancount` | Output generato dalla conversione CSV. |
| `test/paypal2bean.py` | Aiuto per le importazioni CSV di PayPal. |
| `test/output_file_paypal.beancount` | File di output PayPal generato. |
| `test/old files/` | CSV più vecchi e file generati. |

## Struttura Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Percorso | Scopo |
| --- | --- |
| `2023/2023.beancount` | Registro principale Tohuwabohu. Questo è il file normalmente modificato. |
| `2021/2021.beancount` | Dati di registro più vecchi inclusi tramite `all.beancount`. |
| `all.beancount` | File combinato Tohuwabohu che include i file di registro 2021 e 2023. |
| `2023/dashboards.yaml` | Configurazione del dashboard per il registro Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Nota di aiuto di Obsidian. |
| `2023/Belege Ausgaben/` | Ricevute e documenti di supporto per le spese. |
| `2023/Belege Ausgaben/Eingetragen/` | Ricevute già inserite nel registro. |
| `test/csv2bean.py` | Converte CSV Sparkasse in voci Beancount temporanee. |
| `test/beancount_file.beancount` | Output generato dalla conversione CSV. |
| `test/paypal2bean.py` | Aiuto per le importazioni CSV di PayPal. |
| `test/output_file_paypal.beancount` | File di output PayPal generato. |
| `test/CSV - old files/` | CSV più vecchi e file generati. |

## Principio di denominazione dei file

Le cartelle contengono ancora nomi storici come `2023`, anche quando contengono attività successive dal 2024, 2025 e 2026. Tratta i file di registro principali attualmente referenziati come i registri attivi a meno che la struttura non venga modificata intenzionalmente.

## Dove modificare

| Associazione | Modifica questo file |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Non modificare i file di output generati come record permanente. Sono file temporanei di staging.
