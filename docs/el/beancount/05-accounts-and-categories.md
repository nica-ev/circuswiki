---
lang: el
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Λογαριασμοί και Κατηγορίες
description: Εξηγεί τη γερμανική δομή λογαριασμών και τις συμβάσεις κατηγοριών που χρησιμοποιούνται στα λογιστικά βιβλία.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:37:17+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:37:17+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Λογαριασμοί και Κατηγορίες

Αυτή η σελίδα εξηγεί τη δομή των λογαριασμών που χρησιμοποιούνται στα λογιστικά βιβλία.

## Γλώσσα ονομασίας

Τα ονόματα των λογαριασμών είναι στα Γερμανικά. Συνεχίστε να χρησιμοποιείτε τα υπάρχοντα ονόματα λογαριασμών για να διατηρήσετε τη συνέπεια στις αναφορές.

| Γερμανικά | Αγγλική σημασία |
| --- | --- |
| `Vermoegen` | Περιουσιακά στοιχεία |
| `Verbindlichkeiten` | Υποχρεώσεις |
| `Einnahmen` | Έσοδα |
| `Ausgaben` | Έξοδα |
| `Buero` | Γραφείο |
| `Verein` | Σύλλογος/γενική δραστηριότητα συλλόγου |
| `Projekt` | Έργο |
| `Barkasse` | Ταμειακή μηχανή |
| `Freies-Geld` | Ελεύθερα/μη δεσμευμένα κεφάλαια |

## Λογαριασμοί περιουσιακών στοιχείων

Παραδείγματα NICA:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Παραδείγματα Tohuwabohu:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Γενικοί λογαριασμοί εσόδων

| Λογαριασμός | Χρήση για |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Συνδρομές μέλους. |
| `Einnahmen:Spende` | Δωρεές. |
| `Einnahmen:Verleih` | Έσοδα από ενοικίαση ή δανεισμό. |
| `Einnahmen:Sonstiges` | Άλλα έσοδα που δεν ταιριάζουν αλλού. |

## Γενικοί λογαριασμοί εξόδων

| Λογαριασμός | Χρήση για |
| --- | --- |
| `Ausgaben:Buero:Miete` | Ενοίκιο γραφείου ή χώρου. |
| `Ausgaben:Buero:Internet` | Internet και ψηφιακές υπηρεσίες. |
| `Ausgaben:Buero:Sonstiges` | Άλλα έξοδα γραφείου. |
| `Ausgaben:Verein:Versicherung` | Ασφάλιση συλλόγου. |
| `Ausgaben:Verein:Ehrenamt` | Επιδόματα εθελοντών ή έξοδα εθελοντών συλλόγου. |
| `Ausgaben:Essen` | Έξοδα φαγητού εκτός συγκεκριμένου έργου. |
| `Ausgaben:Sonstiges` | Προσωρινή λύση για ασαφή έξοδα. |

Οι λογαριασμοί `Ausgaben:Sonstiges` και `Einnahmen:Sonstiges` είναι χρήσιμοι κατά την εισαγωγή δεδομένων, αλλά δεν πρέπει να γίνονται η τελική κατηγορία εάν υπάρχει πιο ακριβής κατηγορία.

## Λογαριασμοί έργων

Οι λογαριασμοί έργων ακολουθούν αυτό το μοτίβο:

```text
Vermoegen:Bank:Sparkasse-ASSOCIATION:PROJECT
Ausgaben:Projekt:PROJECT
Einnahmen:Projekt:PROJECT
```

Παραδείγματα:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Τυπικές υποκατηγορίες έργων

| Υποκατηγορία | Σημασία |
| --- | --- |
| `Honorar` | Αμοιβές που καταβάλλονται σε άτομα ή λαμβάνονται για εργασία. |
| `Aufwand` | Έξοδα ή επίδομα εξόδων. |
| `Sachmittel` | Υλικά και προμήθειες. |
| `Sonstiges` | Άλλα έξοδα ή έσοδα έργου. |
| `Pauschale` / `Pauschalen` | Συνολικός προϋπολογισμός έργου ή κατ' αποκοπήν. |

## Υποχρεώσεις προς άτομα

Οι λογαριασμοί υποχρεώσεων παρακολουθούν χρήματα που οφείλονται σε άτομα ή επιστρέφονται σε άτομα. Παραδείγματα περιλαμβάνουν `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` και `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Επιλογή του σωστού λογαριασμού

1. Αφορά το επίπεδο του συλλόγου ή το επίπεδο του έργου;
2. Εάν αφορά το επίπεδο του έργου, ποιο έργο κατέχει τα χρήματα;
3. Είναι έσοδο, έξοδο, κίνηση περιουσιακών στοιχείων ή αποπληρωμή υποχρέωσης;
4. Υπάρχει ήδη ανοιχτή ακριβής κατηγορία;
5. Εάν δεν υπάρχει καλή κατηγορία, χρησιμοποιήστε προσωρινά το `Sonstiges` και προσθέστε ένα σχόλιο.
