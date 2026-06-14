---
lang: hu
translation_id: vault-file-system
created: 2025-01-21 18:09:55
update: 2025-01-25 02:06:00
publish: true
tags: 
title: Vault Fájlrendszer
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Vault File System.md
translation_source_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:54:48+00:00
translation_source_body_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_source_metadata_hash: e5706bd684a1a5f866fffe140d52f56035ed28ea15fe48118eff23e9efad70ed
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:25:23+00:00
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

Minden aláhúzásjellel kezdődő mappa egy rendszermappa.

# ```_attachments```
Minden kép, PDF és egyéb melléklet.

- elsősorban a rend fenntartása érdekében
- a képi és szöveges adatok elkülönítése
- a későbbi, nagy adatmennyiségekkel való egyszerűbb kezelés érdekében
- a későbbi automatizálások egyszerűsítése érdekében

❗Jelenleg ezt a mappát a Git figyelmen kívül hagyja, még gondolkodni kell azon, hogyan kezeljük a képi adatokat. Ez azt jelenti, hogy a képi adatok jelenleg csak lokálisan érhetők el (és természetesen a végeredményként létrejövő weboldalon), de jelenleg nem részei a repositorynak. #todo

# ```_canvas```
A Canvas az Obsidian egyik funkciója, amely alkalmas elmetérképekhez és hasonló dolgokhoz.
Mivel ezt csak az Obsidianon belül használjuk, az adatok külön vannak tárolva.
