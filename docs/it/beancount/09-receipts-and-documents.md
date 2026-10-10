---
lang: it
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Ricevute e Documenti
description: Spiega dove sono archiviati i documenti di supporto e come le transazioni fanno riferimento alle ricevute.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:40+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:40+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Ricevute e Documenti

Ricevute, fatture, contratti e altri documenti di supporto rendono le transazioni verificabili. Il libro mastro dovrebbe permettere di trovare il documento dietro una spesa.

## Dove vengono archiviati i documenti

Tohuwabohu dispone attualmente di una cartella chiara per le ricevute:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Le ricevute già inserite nel libro mastro si trovano spesso in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA utilizza file di supporto nella sua cartella di contabilità e nelle cartelle di progetto. Se in futuro verrà introdotta una cartella coerente per le ricevute NICA, documentarla qui e utilizzarla in modo uniforme.

## Voci `document`

Una voce `document` collega un file a un conto e a una data:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

Il percorso del file è relativo alla cartella che contiene il file del libro mastro.

## Collegamenti ai documenti con tag

Alcune voci più vecchie includono tag di documento come:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

La parte `^2023_001` è un collegamento Beancount. Può collegare una ricevuta alla transazione correlata se lo stesso collegamento viene utilizzato lì.

## Significato di `scanned`

I commenti nei libri mastri definiscono la convenzione per le ricevute scansionate. Quando viene utilizzato il tag `scanned`, significa:

- La ricevuta è stata scansionata o digitalizzata.
- L'immagine è stata ridotta e ottimizzata, ad esempio con TinyPNG.
- Il file è stato salvato utilizzando uno schema anno e numero, ad esempio `2023_002.jpg`.
- Il numero è referenziato nella voce di libro mastro correlata.

## Nomi di file corretti

Nomi di file di ricevute corretti sono stabili e leggibili:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Evitare nomi come `scan.jpg`, `image1.jpg` o `download.pdf`.

## Flusso di lavoro per una nuova ricevuta

1. Salvare la ricevuta nella cartella corretta per le ricevute.
2. Rinominarla in modo che possa essere riconosciuta in seguito.
3. Inserire o trovare la transazione correlata.
4. Aggiungere una riga `document` o collegare metadati se utile.
5. Se la ricevuta è stata elaborata, spostarla in `Eingetragen` se questa è la convenzione della cartella.
6. Ricaricare Fava e verificare che il collegamento al documento funzioni.

## Quando manca una ricevuta

Se una ricevuta manca, aggiungere un commento vicino alla transazione:

```beancount
; Receipt missing. Ask responsible person.
```

Non fingere che esista un documento se non è disponibile.

## Contratti e documenti di onorario

I contratti e le fatture di onorario dovrebbero essere archiviati vicino al progetto correlato o alla cartella di contabilità e referenziati chiaramente. Per le verifiche di progetto, la domanda importante non è solo che la transazione esista, ma che il documento che prova la spesa possa essere trovato rapidamente.
