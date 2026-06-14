---
lang: en
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
translation_updated: 2026-06-06T19:29:44+00:00
translation_source_body_hash: 3bc0110134e109236bc99536708bc16f7b492cf3d0fbb5e05bf12deef33d3de2
translation_source_metadata_hash: e5706bd684a1a5f866fffe140d52f56035ed28ea15fe48118eff23e9efad70ed
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:25:21+00:00
translation_source_localized_metadata_hash: e5706bd684a1a5f866fffe140d52f56035ed28ea15fe48118eff23e9efad70ed
translation_source_structural_metadata_hash: 7117b80962cd904a4681c4da9fa10219d16d910b6eb351ac67097e8855fb830b
---
```code
/_attachments/        
/_canvas/             
/_dataview/           
/_inbox/
/_other/
/_templates/
/docs/
/site/
license
mkdocs.yml
readme.md
```

Every folder with the prefix _ is a system folder.

# ```_attachments```  
All images, PDFs, and other attachments.

- Primarily to maintain order.
- To keep image and text data separate.
- To simplify later organization with large amounts of data.
- To simplify later automation.

❗This folder is currently ignored by Git. Further consideration is needed on how we handle image data. This means image data is currently only available locally (and of course on the resulting website), but it is not part of the repository at the moment. #todo

# ```_canvas```
Canvas is a feature of Obsidian that is well-suited for mind maps and similar visualizations.
Since we only use this within Obsidian, the data is kept separate.
