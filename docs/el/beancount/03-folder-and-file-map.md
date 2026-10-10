---
lang: el
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Χάρτης Φακέλων και Αρχείων
description: Χαρτογραφεί τους σημαντικούς φακέλους λογιστικής, αρχεία καθολικών, πίνακες ελέγχου και βοηθητικά αρχεία.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:23+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:23+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Δομή Φακέλων και Αρχείων

Αυτή η σελίδα εξηγεί πού αποθηκεύονται τα σημαντικά αρχεία τήρησης βιβλίων.

## Κύριος φάκελος τήρησης βιβλίων

```text
1. Vereinsverwaltung/Buchhaltung
```

Αυτός ο φάκελος περιέχει τα λογιστικά βιβλία, τα αρχεία πίνακα ελέγχου, τα υποστηρικτικά έγγραφα και τους βοηθητικούς φακέλους.

## Σημαντικά αρχεία ανώτερου επιπέδου

| Αρχείο | Σκοπός |
| --- | --- |
| `Buchhaltung Home.md` | Σελίδα εισόδου στο Obsidian με κουμπιά και μια σύντομη σημείωση ροής εργασιών. |
| `all.beancount` | Πειραματικό συνδυασμένο λογιστικό βιβλίο που περιλαμβάνει τόσο το NICA όσο και το Tohuwabohu. |
| `dashboards.yaml` | Ορισμός πίνακα ελέγχου για τους πίνακες ελέγχου του Fava στο κοινόχρηστο επίπεδο. |

## Δομή NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Διαδρομή | Σκοπός |
| --- | --- |
| `2023/nica.beancount` | Κύριο λογιστικό βιβλίο NICA. Αυτό είναι το αρχείο που συνήθως επεξεργάζεται. |
| `2023/dashboards.yaml` | Ρύθμιση πίνακα ελέγχου για το λογιστικό βιβλίο NICA. |
| `2023/Buchhaltung NICA eV.md` | Βοηθητική σημείωση Obsidian για το άνοιγμα της τήρησης βιβλίων NICA. |
| `2023/CSV/` | Αποθηκευμένες εξαγωγές CSV. |
| `test/csv2bean.py` | Μετατρέπει CSV της Sparkasse σε προσωρινές εγγραφές Beancount. |
| `test/beancount_file.beancount` | Παραγόμενη έξοδος από τη μετατροπή CSV. |
| `test/paypal2bean.py` | Βοηθητικό πρόγραμμα για εισαγωγές CSV του PayPal. |
| `test/output_file_paypal.beancount` | Παραγόμενο αρχείο εξόδου PayPal. |
| `test/old files/` | Παλαιότερα CSV και παραγόμενα αρχεία. |

## Δομή Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Διαδρομή | Σκοπός |
| --- | --- |
| `2023/2023.beancount` | Κύριο λογιστικό βιβλίο Tohuwabohu. Αυτό είναι το αρχείο που συνήθως επεξεργάζεται. |
| `2021/2021.beancount` | Παλαιότερα δεδομένα λογιστικού βιβλίου που περιλαμβάνονται μέσω του `all.beancount`. |
| `all.beancount` | Συνδυασμένο αρχείο Tohuwabohu που περιλαμβάνει τα αρχεία λογιστικών βιβλίων του 2021 και του 2023. |
| `2023/dashboards.yaml` | Ρύθμιση πίνακα ελέγχου για το λογιστικό βιβλίο Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Βοηθητική σημείωση Obsidian. |
| `2023/Belege Ausgaben/` | Αποδείξεις και υποστηρικτικά έγγραφα για δαπάνες. |
| `2023/Belege Ausgaben/Eingetragen/` | Αποδείξεις που έχουν ήδη καταχωρηθεί στο λογιστικό βιβλίο. |
| `test/csv2bean.py` | Μετατρέπει CSV της Sparkasse σε προσωρινές εγγραφές Beancount. |
| `test/beancount_file.beancount` | Παραγόμενη έξοδος από τη μετατροπή CSV. |
| `test/paypal2bean.py` | Βοηθητικό πρόγραμμα για εισαγωγές CSV του PayPal. |
| `test/output_file_paypal.beancount` | Παραγόμενο αρχείο εξόδου PayPal. |
| `test/CSV - old files/` | Παλαιότερα CSV και παραγόμενα αρχεία. |

## Αρχή ονομασίας αρχείων

Οι φάκελοι εξακολουθούν να περιέχουν ιστορικά ονόματα όπως `2023`, ακόμη και όταν περιέχουν μεταγενέστερη δραστηριότητα από το 2024, 2025 και 2026. Αντιμετωπίστε τα κύρια αρχεία λογιστικών βιβλίων που αναφέρονται επί του παρόντος ως τα ενεργά λογιστικά βιβλία, εκτός αν η δομή αλλάξει σκόπιμα.

## Πού να επεξεργαστείτε

| Σύλλογος | Επεξεργαστείτε αυτό το αρχείο |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Μην επεξεργάζεστε αρχεία παραγόμενης εξόδου ως μόνιμη καταγραφή. Είναι προσωρινά αρχεία προετοιμασίας.
