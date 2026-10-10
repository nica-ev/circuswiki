---
lang: el
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Άνοιγμα Fava
description: Πώς να ξεκινήσετε και να ανοίξετε την τοπική διεπαφή λογιστικής Fava.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:09+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:09+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Άνοιγμα Fava

Το Fava είναι η διαδικτυακή διεπαφή που χρησιμοποιείται για την επιθεώρηση της λογιστικής. Εκτελείται τοπικά στον υπολογιστή και ανοίγει σε ένα πρόγραμμα περιήγησης ή στην προβολή web του Obsidian.

## Απαιτήσεις

Ο υπολογιστής πρέπει να έχει εγκατεστημένα και διαθέσιμα τα ακόλουθα προγράμματα:

- Python
- Beancount
- Fava
- `fava-dashboards` εάν η επέκταση των ταμπλό πρέπει να είναι ορατή
- Obsidian, εάν χρησιμοποιείτε τα κουμπιά του Obsidian

## Άνοιγμα από το Obsidian

Η σημείωση `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` περιέχει κουμπιά για το άνοιγμα της λογιστικής. Τα κουμπιά ξεκινούν το Fava μέσω των Εντολών Κελύφους του Obsidian και στη συνέχεια ανοίγουν την τοπική διεύθυνση URL του Fava.

| Κουμπί | Ανοίγει |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava στη θύρα `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava στη θύρα `4999` |

Μην κλείσετε το παράθυρο του τερματικού που ξεκινά το Fava. Εάν κλείσει το τερματικό, το Fava σταματά.

## Χειροκίνητο άνοιγμα

### NICA e.V.

Ανοίξτε ένα τερματικό στο:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Εκτελέστε:

```powershell
fava nica.beancount --port 4998
```

Στη συνέχεια, ανοίξτε τη διεύθυνση `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Ανοίξτε ένα τερματικό στο:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Εκτελέστε:

```powershell
fava 2023.beancount --port 4999
```

Στη συνέχεια, ανοίξτε τη διεύθυνση `http://127.0.0.1:4999/`.

## Αρχεία δέσμης εκκίνησης

| Αρχείο | Σκοπός |
| --- | --- |
| `startup-nica.bat` | Ξεκινά το NICA Fava στη θύρα `4998`. |
| `startup-tohu.bat` | Ξεκινά το Tohuwabohu Fava στη θύρα `4999`. |
| `startup-all.bat` | Ξεκινά το Obsidian, διάφορα εργαλεία και τις δύο παρουσίες Fava. |

## Σημαντικές διευθύνσεις URL

| Προβολή | NICA | Tohuwabohu |
| --- | --- | --- |
| Αρχική | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Ταμπλό | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Κατάσταση Εσόδων | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Όταν το Fava εκτελείται ήδη

Εάν το Fava εκτελείται ήδη, αρκεί το άνοιγμα της διεύθυνσης URL. Εάν η θύρα είναι ήδη κατειλημμένη και το Fava αρνείται να ξεκινήσει, ενδέχεται να υπάρχει ήδη ανοιχτή μια άλλη παρουσία Fava. Χρησιμοποιήστε την υπάρχουσα σελίδα του προγράμματος περιήγησης ή κλείστε το παλιό παράθυρο του τερματικού και ξεκινήστε ξανά.
