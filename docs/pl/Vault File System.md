---
lang: pl
translation_id: vault-file-system
created: 2025-01-21 18:09:55
update: 2025-01-25 02:06:00
publish: true
tags: 
title: System plików Vault
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Vault File System.md
translation_source_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T20:24:44+00:00
translation_source_body_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_source_metadata_hash: e5706bd684a1a5f866fffe140d52f56035ed28ea15fe48118eff23e9efad70ed
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:25:22+00:00
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

Każdy folder z prefiksem _ jest folderem systemowym

# ```_attachments```  
Wszystkie obrazy, pliki PDF i inne załączniki

- głównie w celu utrzymania porządku
- oddzielenia danych graficznych od tekstowych
- ułatwienia późniejszej organizacji przy dużych ilościach danych
- uproszczenia późniejszych automatyzacji

❗Obecnie ten folder jest ignorowany przez Git. Wymaga to dalszych przemyśleń, jak będziemy postępować z danymi graficznymi. Oznacza to, że dane graficzne są obecnie dostępne tylko lokalnie (i oczywiście na stronie internetowej), ale nie są częścią repozytorium. #todo

# ```_canvas```
Canvas to funkcja Obsidian, która dobrze nadaje się do tworzenia map myśli i podobnych struktur.
Ponieważ korzystamy z niej tylko w obrębie Obsidian, dane są odseparowane.
