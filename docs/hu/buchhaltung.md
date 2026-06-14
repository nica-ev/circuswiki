---
lang: hu
translation_id: buchhaltung
publish: true
tags:
  - moc
created: 2025-01-19 16:47:55
update: 2026-06-07 00:06:48
title: Könyvelés áttekintés
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/buchhaltung.md
translation_source_hash: 66a642a774547843fee7c0bdb1ce18206708a6fbca5073d4ab4150c381925c2e
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:35:01+00:00
translation_source_body_hash: 66a642a774547843fee7c0bdb1ce18206708a6fbca5073d4ab4150c381925c2e
translation_source_metadata_hash: 4fd315b74fcbb62021e5ad51f552056b0dea15c69f18a03a1d3992a50f687e97
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:41+00:00
translation_source_localized_metadata_hash: 4fd315b74fcbb62021e5ad51f552056b0dea15c69f18a03a1d3992a50f687e97
translation_source_structural_metadata_hash: 50f1f18cad2c4ebdd8284c2c85de7dd1c5fa87e6d1a499f8cdd300ec1a798d96
---
# Könyvelés áttekintése

A könyvelésünk az úgynevezett "plaintext accounting" (szöveges könyvelés) elven alapul.
Minden adatot / tranzakciót egy szöveges fájlba írunk, ember által jól olvasható formátumban.

Egy tranzakció így néz ki ebben a formátumban:
```
2023-01-09 dokumentum Kiadások:Iroda:Egyéb "Bizonylatok/Kiadások/Bejegyezve/2023_004.jpg" ^2023_004

2023-01-09 ! "Hornbach" "Irodai lámpa" #nyitott #beolvasva ^2023_004

    Kiadások:Iroda:Egyéb              64.95 EUR

    Kötelezettségek:Személy:Marc-Bielert
```

# Teendők

Az adományokat mindig egyértelműen kell nyomon követni, akár külön számlán, akár tagekkel.
Ez fontos a [tevékenységi jelentések](../_inbox/Tätigkeitsberichte.md) szempontjából, amelyeket évente el kell készítenünk. #teendő
