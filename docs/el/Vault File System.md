---
lang: el
translation_id: vault-file-system
created: 2025-01-21 18:09:55
update: 2025-01-25 02:06:00
publish: true
tags: 
title: Σύστημα Αρχείων Vault
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Vault File System.md
translation_source_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T13:55:54+00:00
translation_source_body_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_source_metadata_hash: e5706bd684a1a5f866fffe140d52f56035ed28ea15fe48118eff23e9efad70ed
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:25:25+00:00
translation_source_localized_metadata_hash: e5706bd684a1a5f866fffe140d52f56035ed28ea15fe48118eff23e9efad70ed
translation_source_structural_metadata_hash: 7117b80962cd904a4681c4da9fa10219d16d910b6eb351ac67097e8855fb830b
---
```code
/_attachments/        
/_canvas/             
/_dataview/           
/_inbox/
/_sonstiges/
/_templates/
/docs/
/site/
license
mkdocs.yml
readme.md
```

Κάθε φάκελος με το πρόθεμα _ είναι φάκελος συστήματος

# ```_attachments```  
Όλες οι εικόνες, τα PDF και άλλα συνημμένα αρχεία

- κυρίως για να διατηρείται η τάξη
- για να διαχωρίζονται τα δεδομένα εικόνας και κειμένου
- για να απλοποιηθεί η μελλοντική οργάνωση σε μεγάλες ποσότητες δεδομένων
- για να απλοποιηθούν οι μελλοντικές αυτοματοποιήσεις

❗Αυτή τη στιγμή, αυτός ο φάκελος αγνοείται από το Git. Χρειάζεται περαιτέρω σκέψη για το πώς θα διαχειριστούμε τα δεδομένα εικόνας. Αυτό σημαίνει ότι τα δεδομένα εικόνας είναι προς το παρόν διαθέσιμα μόνο τοπικά (και φυσικά στην τελική ιστοσελίδα), αλλά δεν αποτελούν μέρος του αποθετηρίου αυτή τη στιγμή. #todo

# ```_canvas```
Το Canvas είναι ένα χαρακτηριστικό του Obsidian, το οποίο είναι κατάλληλο για mind maps και παρόμοια. 
Δεδομένου ότι το χρησιμοποιούμε μόνο εντός του Obsidian, τα δεδομένα είναι διαχωρισμένα
