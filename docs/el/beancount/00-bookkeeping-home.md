---
lang: el
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Τεκμηρίωση Συστήματος Τήρησης Βιβλίων
description: Επισκόπηση και σημείο εκκίνησης για την τεκμηρίωση τήρησης βιβλίων Beancount των NICA e.V. και Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:03:47+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:03:47+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Τεκμηρίωση Συστήματος Τήρησης Βιβλίων

Αυτή η τεκμηρίωση εξηγεί πώς λειτουργεί το σύστημα τήρησης βιβλίων για τους NICA e.V. και Tohuwabohu Halle e.V. από την οπτική γωνία ενός απλού χρήστη.

Το σύστημα χρησιμοποιεί αρχεία λογιστικής απλού κειμένου σε Beancount και μια διεπαφή περιηγητή που ονομάζεται Fava. Δεν χρειάζεται να κατανοείτε προγραμματισμό για να το χρησιμοποιήσετε, αλλά πρέπει να ακολουθείτε προσεκτικά τη ροή εργασίας της τήρησης βιβλίων: εισαγωγή τραπεζικών δεδομένων, ταξινόμηση συναλλαγών, επισύναψη αποδείξεων όπου χρειάζεται και έλεγχος υπολοίπων.

## Ξεκινήστε από εδώ

- [01 - Επισκόπηση Συστήματος](01-system-overview.md)
- [02 - Άνοιγμα Fava](02-opening-fava.md)
- [03 - Χάρτης Φακέλων και Αρχείων](03-folder-and-file-map.md)
- [04 - Βασικές Αρχές Beancount για Χρήστες](04-beancount-basics-for-users.md)
- [05 - Λογαριασμοί και Κατηγορίες](05-accounts-and-categories.md)
- [06 - Εισαγωγή και Επεξεργασία Συναλλαγών](06-entering-and-editing-transactions.md)
- [07 - Εισαγωγή Τραπεζικών CSV και Συμφωνία](07-bank-csv-import-and-reconciliation.md)
- [08 - Έργα και Δεσμευμένα Κεφάλαια](08-projects-and-restricted-funds.md)
- [09 - Αποδείξεις και Έγγραφα](09-receipts-and-documents.md)
- [10 - Πίνακες Ελέγχου και Αναφορές Fava](10-fava-dashboards-and-reports.md)
- [11 - Τακτική Ρουτίνα Τήρησης Βιβλίων](11-regular-bookkeeping-routine.md)
- [12 - Αντιμετώπιση Προβλημάτων](12-troubleshooting.md)
- [13 - Γλωσσάρι](13-glossary.md)

## Ο πιο σημαντικός κανόνας

Το αρχείο λογιστικής είναι η πηγή της αλήθειας. Το Fava εμφανίζει μόνο ό,τι είναι γραμμένο στα αρχεία `.beancount`. Αν κάτι φαίνεται λάθος στο Fava, διορθώστε την καταχώρηση στο Beancount και ανανεώστε το Fava.

## Τρέχοντα Καθολικά

| Οργανισμός | Κύριο αρχείο | Διεύθυνση Fava | Θύρα |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Τι δεν είναι αυτή η τεκμηρίωση

Αυτές δεν είναι νομικές ή φορολογικές συμβουλές. Περιγράφει πώς είναι οργανωμένο αυτό το συγκεκριμένο τοπικό σύστημα τήρησης βιβλίων και πώς οι χρήστες θα πρέπει να εργάζονται με αυτό με συνέπεια.
