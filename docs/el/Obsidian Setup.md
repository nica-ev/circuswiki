---
lang: el
translation_id: obsidian-setup
publish: true
tags: 
title: Ρύθμιση Obsidian
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T13:50:23+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:22+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Το Obsidian είναι εξαιρετικά προσαρμόσιμο, κάτι που μπορεί να αποτελέσει πρόβλημα για τους νεοεισερχόμενους.
Παρέχουμε μια βασική ρύθμιση που μπορεί να χρησιμοποιηθεί ως έχει, συμπεριλαμβανομένων plugins και θεμάτων, καθώς και τις ρυθμίσεις τους.
Αυτή είναι μια βασική ρύθμιση και μπορεί να προσαρμοστεί περαιτέρω στις προσωπικές προτιμήσεις του καθενός.
Παρέχουμε απλώς μια λειτουργική λύση – την οποία θα τεκμηριώσουμε και θα εξηγήσουμε εδώ.

## Χρησιμοποιούμενοι Όροι
**Vault** – μια συλλογή από αρχεία markdown και εικόνες που σχηματίζουν τη βάση γνώσεων

## Plugins

- Advanced Canvas
- BRAT
- Better Wordcount
- Clear unused Images
- Dataview
- Dataview Serializer
- Emoji Toolbar
- Linter
- Note Toolbar
- Tag Wrangler
- Templater
- Beautitab
- Omnisearch
- Status Bar Organizer
- Workspaces Plus
- Sortable

### Advanced Canvas
Παρέχει πρόσβαση σε πολλές νέες λειτουργίες και επιλογές στυλ για το Canvas

### BRAT
Απαραίτητο για την εγκατάσταση ανεπίσημων plugins / plugins που δεν είναι εγγεγραμμένα στο Οικοσύστημα του Obsidian, συγκεκριμένα:
- Dataview Serializer
- Sortable

### Better Word Count
Χρησιμοποιείται κυρίως για την ικανότητά του να εμφανίζει τον αριθμό λέξεων/χαρακτήρων σε επισημασμένο κείμενο.
Είναι ορατό στη γραμμή κατάστασης

### Beautitab
Καθαρά κοσμητικό, παρέχει μια προσαρμόσιμη σελίδα "κενής νέας καρτέλας"

### Clear unused Images
Όπως λέει και το όνομα, βοηθά στην οργάνωση του vault εντοπίζοντας αχρησιμοποίητες εικόνες

❗Έχω εξαιρέσει τον υποφάκελο ```/site/``` ώστε να μην διαγράφει πάντα τις εικόνες από τον ιστότοπο που δημιουργείται (κάτι που δεν είναι πρόβλημα, περισσότερο ενόχληση)

❗Προσοχή στη χρήση της εντολής clear attachments – καθώς αυτή θα διαγράφει πάντα το ```mkdocs.yml``` και το ```license.``` --> αν συμβεί αυτό, τα αρχεία βρίσκονται στον φάκελο .trash και μπορούν να ανακτηθούν. Αλλά είναι εύκολο να το χάσετε.

### Dataview
Ενεργοποιεί ερωτήματα τύπου SQL στο vault

### Dataview Serializer
Μετατρέπει τα αποτελέσματα του Dataview σε markdown
Βοηθά στην επαναχρησιμοποίηση των αποτελεσμάτων των ερωτημάτων dataview στις πραγματικές σημειώσεις

### Emoji Toolbar
Λοιπόν, παρέχει εύκολη πρόσβαση σε emojis
**Συντόμευση ορισμένη σε: ALT-E**
😍

### Linter
Καθαρίζει αρχεία markdown και δεδομένα frontmatter
Βοηθά στη διατήρηση μιας συνεπής μορφής

### Note Toolbar
Ενεργοποιεί προσαρμόσιμες γραμμές εργαλείων στην κορυφή μιας σημείωσης που μπορούν να οριστούν σε επίπεδο φακέλου/αρχείου

### Tag Wrangler
Παρέχει πρόσθετες επιλογές για εργασία με ετικέτες
- Μετονομασία ετικετών
Βοηθά στην οργάνωση του vault

### Templater
Επιτρέπει προσαρμόσιμα πρότυπα που μπορούν να εισαχθούν χειροκίνητα ή βάσει συνθηκών (όπως η δημιουργία μιας σημείωσης)

### Status Bar Organizer
Επιτρέπει την απόκρυψη στοιχείων από τη γραμμή κατάστασης

### Sortable
Επιτρέπει την ταξινόμηση πινάκων (τόσο markdown όσο και dataview) κάνοντας κλικ στις κεφαλίδες τους.

### Workspaces Plus
Επιτρέπει μια εύκολη γρήγορη εναλλαγή από τη γραμμή κατάστασης

## Σύστημα Αρχείων του Vault

[Σύστημα Αρχείων του Vault](Vault%20File%20System.md){ .md-button }
