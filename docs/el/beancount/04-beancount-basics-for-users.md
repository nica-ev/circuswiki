---
lang: el
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Βασικές αρχές του Beancount για χρήστες
description: Εισάγει τη μορφή κειμένου Beancount και τα μοτίβα συναλλαγών που χρησιμοποιούνται στα λογιστικά βιβλία.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:33+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:33+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Βασικές αρχές του Beancount για χρήστες

Το Beancount αποθηκεύει λογιστικές εγγραφές ως αναγνώσιμο κείμενο. Κάθε συναλλαγή δηλώνει τι συνέβη, σε ποια ημερομηνία, ποιοι εμπλέκονταν και ποιοι λογαριασμοί άλλαξαν.

## Βασική μορφή συναλλαγής

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Μέρος | Σημασία |
| --- | --- |
| `2026-01-13` | Ημερομηνία της συναλλαγής. |
| `!` | Δείκτης κατάστασης. Σε αυτό το σύστημα χρησιμοποιείται συνήθως για εισαγόμενες ή μη οριστικά ελεγμένες εγγραφές. |
| Πρώτο κείμενο σε εισαγωγικά | Πληρωτής ή αποστολέας. |
| Δεύτερο κείμενο σε εισαγωγικά | Περιγραφή ή κείμενο κράτησης από την τράπεζα. |
| Πρώτη γραμμή λογαριασμού | Από πού πήγαν ή ήρθαν τα χρήματα. |
| Δεύτερη γραμμή λογαριασμού | Η αντίθετη κατηγορία. Εάν δεν υπάρχει ποσό, το Beancount το υπολογίζει αυτόματα. |

## Ονόματα λογαριασμών

Τα ονόματα λογαριασμών χωρίζονται με άνω και κάτω τελείες:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Διαβάστε το από αριστερά προς τα δεξιά: περιουσιακό στοιχείο, τραπεζικός λογαριασμός, Sparkasse NICA, ελεύθερα διαθέσιμα κεφάλαια.

## Οι πέντε οικογένειες λογαριασμών

| Οικογένεια | Σημασία | Παράδειγμα |
| --- | --- | --- |
| `Vermoegen` | Περιουσιακά στοιχεία: τράπεζα, PayPal, μετρητά, απόθεμα. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Υποχρεώσεις: χρήματα που οφείλονται σε άτομα ή άλλους. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Αρχικά υπόλοιπα και εγγραφές εξισορρόπησης. | `Equity:Opening-Balances` |
| `Einnahmen` | Έσοδα. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Έξοδα. | `Ausgaben:Buero:Miete` |

## Πρόσημα εσόδων και εξόδων

Στις αναφορές του Beancount, τα έσοδα εμφανίζονται συχνά με αρνητικό πρόσημο εσωτερικά και τα έξοδα με θετικό πρόσημο. Το Fava και τα dashboards παρουσιάζουν συχνά αυτές τις τιμές με πιο φιλικό προς τον χρήστη τρόπο. Μην αλλάζετε συναλλαγές μόνο επειδή ένας αριθμός εσόδων φαίνεται αρνητικός σε ένα ακατέργαστο ερώτημα.

## Έλεγχοι υπολοίπου

Ένας έλεγχος υπολοίπου δηλώνει ότι ένας λογαριασμός πρέπει να έχει συγκεκριμένο υπόλοιπο σε μια ημερομηνία:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Εάν το Beancount δεν μπορεί να αντιστοιχίσει αυτό το υπόλοιπο από τις συναλλαγές πριν από αυτήν την ημερομηνία, το Fava εμφανίζει σφάλμα. Οι έλεγχοι υπολοίπου είναι ο κύριος μηχανισμός ποιοτικού ελέγχου.

## Άνοιγμα και κλείσιμο λογαριασμών

Πριν χρησιμοποιηθεί ένας λογαριασμός, ανοίγει:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Όταν ένα έργο ολοκληρωθεί και ο λογαριασμός του έργου είναι μηδέν, μπορεί να κλείσει:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Οι κλειστοί λογαριασμοί κανονικά δεν πρέπει να λαμβάνουν νέες συναλλαγές.

## Σχόλια και έγγραφα

Γραμμές που ξεκινούν με `;` είναι σχόλια. Εξηγούν αποφάσεις ή αβέβαιες καταστάσεις και δεν επηρεάζουν τους αριθμούς.

Οι αποδείξεις μπορούν να συνδεθούν με γραμμές `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
