---
lang: sk
translation_id: vault-file-system
created: 2025-01-21 18:09:55
update: 2025-01-25 02:06:00
publish: true
tags: 
title: Vault File System
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Vault File System.md
translation_source_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:14:10+00:00
translation_source_body_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_source_metadata_hash: e5706bd684a1a5f866fffe140d52f56035ed28ea15fe48118eff23e9efad70ed
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:25:29+00:00
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

Každý priečinok s predponou _ je systémový priečinok.

# ```_attachments```
Všetky obrázky, PDF súbory a iné prílohy.

- hlavne na udržanie poriadku
- na oddelenie obrazových a textových dát
- na zjednodušenie neskoršej organizácie pri veľkom objeme dát
- na zjednodušenie neskorších automatizácií

❗V súčasnosti tento priečinok Git ignoruje, ešte je potrebné zvážiť, ako budeme pracovať s obrazovými dátami. To znamená, že obrazové dáta sú momentálne dostupné iba lokálne (a samozrejme na výslednej webovej stránke), ale momentálne nie sú súčasťou úložiska. #todo

# ```_canvas```
Canvas je funkcia Obsidianu, ktorá je vhodná na myšlienkové mapy a podobné veci.
Keďže toto používame iba v rámci Obsidianu, dáta sú oddelené.
