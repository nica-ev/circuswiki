---
lang: el
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Διαδραστικό πρωτότυπο για αναζήτηση και εξερεύνηση χώρων και δικτύων τσίρκου από δεδομένα του CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:36+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:36+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">Φόρτωση CircusFinder...</p>
</div>

> [!info] Ακριβείς τοποθεσίες και κατά προσέγγιση θέσεις δικτύου
> Οι μπλε δείκτες βασίζονται σε δημοσιευμένες διευθύνσεις. Οι πορτοκαλί δείκτες των εισαγόμενων επαφών δικτύου, αντίθετα, δείχνουν μόνο κέντρα πόλεων ή περιοχών. Παρακαλούμε ελέγξτε τις χρονικά εξαρτώμενες πληροφορίες, όπως ώρες μαθημάτων και προπονήσεων, στον συνδεδεμένο ιστότοπο πριν από την επίσκεψή σας.

<noscript>
Το CircusFinder απαιτεί JavaScript για τον χάρτη και τα φίλτρα. Οι μεμονωμένες καταχωρήσεις παραμένουν προσβάσιμες ως κανονικές σελίδες Wiki.
</noscript>

## Τι δοκιμάζει αυτό το πρωτότυπο

Τα δεδομένα προέρχονται από αρχεία Markdown με μεταδεδομένα YAML. Κατά τη δημιουργία του Zensical, ελέγχονται και εξάγονται ως JSON. Αυτή η σελίδα φορτώνει αποκλειστικά αυτήν την εξαγωγή και δεν γνωρίζει τα αρχικά αρχεία Markdown.

- Αναζήτηση ελεύθερου κειμένου σε ονόματα, περιγραφές, τοποθεσίες και προσφορές
- Φίλτρο κατά τύπο καταχώρησης
- Δείκτες χάρτη με πληροφορίες σε αναδυόμενο παράθυρο
- Μπλε δείκτες για δημοσιευμένες, ακριβείς διευθύνσεις
- Πορτοκαλί δείκτες για κατά προσέγγιση θέσεις πόλεων ή περιοχών
- Εθελοντική αναζήτηση σε ακτίνα μέσω της γεωεντοπισμού του προγράμματος περιήγησης
- Καταχωρήσεις χωρίς γεωγραφικό σημείο, π.χ. διεθνή δίκτυα
