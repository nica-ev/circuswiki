---
lang: uk
translation_id: buchhaltung
publish: true
tags:
  - moc
created: 2025-01-19 16:47:55
update: 2026-06-07 00:06:48
title: Огляд бухгалтерії
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/buchhaltung.md
translation_source_hash: 66a642a774547843fee7c0bdb1ce18206708a6fbca5073d4ab4150c381925c2e
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:18:57+00:00
translation_source_body_hash: 66a642a774547843fee7c0bdb1ce18206708a6fbca5073d4ab4150c381925c2e
translation_source_metadata_hash: 4fd315b74fcbb62021e5ad51f552056b0dea15c69f18a03a1d3992a50f687e97
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:44+00:00
translation_source_localized_metadata_hash: 4fd315b74fcbb62021e5ad51f552056b0dea15c69f18a03a1d3992a50f687e97
translation_source_structural_metadata_hash: 50f1f18cad2c4ebdd8284c2c85de7dd1c5fa87e6d1a499f8cdd300ec1a798d96
---
# Огляд бухгалтерії

Наша бухгалтерія базується на так званому "Plaintext Accounting" (бухгалтерія у простому тексті).
Усі дані / транзакції записуються у текстовий файл у форматі, який легко читається людиною.

Ось як виглядає транзакція у цьому форматі:
```
2023-01-09 document Витрати:Офіс:Інше "Квитанції Витрати/Внесено/2023_004.jpg" ^2023_004

2023-01-09 ! "Hornbach" "Офісна лампа" #open #scanned ^2023_004

    Витрати:Офіс:Інше                                             64.95 EUR

    Зобов'язання:Особа:Marc-Bielert
```

# Завдання

Пожертви завжди слід чітко відстежувати, або через окремий рахунок, або за допомогою тегів.
Це важливо для [звітів про діяльність](../_inbox/Tätigkeitsberichte.md), які ми повинні складати щорічно. #todo
