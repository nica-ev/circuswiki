---
lang: el
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Έργα και Αποθεματικά Κεφάλαια
description: Εξηγεί πώς αναπαρίστανται και ελέγχονται τα χρήματα έργων και τα αποθεματικά κεφάλαια.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:11+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:11+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Έργα και Περιορισμένα Κεφάλαια

Τα έργα αποτελούν κεντρικό στοιχείο αυτού του συστήματος τήρησης λογιστικών βιβλίων. Πολλές επιχορηγήσεις και δραστηριότητες πρέπει να παρακολουθούνται ξεχωριστά από τα χρήματα ελεύθερης διάθεσης.

## Τι σημαίνει ένα έργο στο λογιστικό βιβλίο

| Τύπος λογαριασμού | Παράδειγμα | Σκοπός |
| --- | --- | --- |
| Περιουσιακό στοιχείο έργου | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Εσωτερικό υπόλοιπο χρημάτων έργου. |
| Έσοδα έργου | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Χρηματοδότηση έργου ή έσοδα έργου. |
| Έξοδα έργου | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Δαπάνες έργου. |

Ο πραγματικός τραπεζικός λογαριασμός μπορεί να είναι ένας λογαριασμός της Sparkasse, αλλά το λογιστικό βιβλίο διαχωρίζει τα εσωτερικά υπόλοιπα των έργων, ώστε η ομάδα να μπορεί να βλέπει τι ανήκει σε κάθε έργο.

## Ενεργά και κλειστά έργα

Τα ενεργά έργα έχουν ανοιχτούς λογαριασμούς και σχετικά υπόλοιπα. Τα κλειστά έργα συνήθως έχουν έναν τελικό έλεγχο υπολοίπου `0.00 EUR` και οδηγίες `close` για τους λογαριασμούς περιουσιακών στοιχείων, εσόδων και εξόδων του έργου.

Μην καταχωρείτε νέες συναλλαγές σε κλειστά έργα, εκτός εάν σκοπίμως τα επανενεργοποιήσετε ή διορθώσετε ιστορικά δεδομένα.

## Τρέχοντα παραδείγματα στη NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- κλειστά έργα του 2024 όπως `24-AWO`, `24-HONY`, `24-Peter`

## Τρέχοντα παραδείγματα στο Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- κλειστά έργα όπως `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Δημιουργία νέου έργου

Ένα νέο έργο συνήθως χρειάζεται να ανοίξουν οι λογαριασμοί του πριν από την καταχώρηση συναλλαγών.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Ανοίξτε μόνο κατηγορίες που είναι πραγματικά χρήσιμες για το έργο.

## Καταχώρηση χρηματοδότησης έργου

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Καταχώρηση εξόδων έργου

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Κατανόηση υπολοίπων έργου

Ένα θετικό υπόλοιπο περιουσιακού στοιχείου έργου σημαίνει ότι χρήματα εξακολουθούν να έχουν εκχωρηθεί σε αυτό το έργο. Ένα υπόλοιπο μηδέν στο περιουσιακό στοιχείο του έργου σημαίνει ότι το έργο δεν έχει εναπομείναν εσωτερικό τραπεζικό υπόλοιπο. Ένα αρνητικό υπόλοιπο περιουσιακού στοιχείου έργου συνήθως σημαίνει ότι το έργο έχει δαπανήσει περισσότερα από τα εκχωρημένα κεφάλαιά του ή ότι λείπει μια εκχώρηση.

## Κλείσιμο έργου

Πριν από το κλείσιμο ενός έργου, πρέπει να έχουν καταχωρηθεί όλα τα έσοδα και τα έξοδα, τα αποδεικτικά πρέπει να είναι διαθέσιμα, ο λογαριασμός περιουσιακού στοιχείου του έργου πρέπει να είναι ακριβώς μηδέν και τυχόν εναπομείναντα χρήματα πρέπει να έχουν μεταφερθεί ή επιστραφεί σωστά.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Κλείστε και τους υπολογαριασμούς εάν είχαν ανοιχτεί ξεχωριστά.
