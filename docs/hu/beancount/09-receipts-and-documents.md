---
lang: hu
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Bizonylatok és dokumentumok
description: Elmagyarázza, hol tárolják a támogató dokumentumokat, és hogyan hivatkoznak a tranzakciók a bizonylatokra.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:37+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:37+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Bizonylatok és dokumentumok

A nyugták, számlák, szerződések és egyéb támogató dokumentumok auditálhatóvá teszik a tranzakciókat. A főkönyvnek lehetővé kell tennie, hogy a kiadás mögötti dokumentumot megtaláljuk.

## Hol tárolódnak a dokumentumok

A Tohuwabohu jelenleg egy jól elkülönített bizonylatmappával rendelkezik:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

A főkönyvbe már bevezetett bizonylatok gyakran itt találhatók:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

A NICA támogató fájlokat használ a könyvelési és projektmappáiban. Ha később egy egységes NICA bizonylatmappát vezetnek be, dokumentálják itt, és használják következetesen.

## `document` bejegyzések

Egy dokumentumbejegyzés összekapcsol egy fájlt egy számlával és egy dátummal:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

A fájl elérési útja a főkönyvi fájlt tartalmazó mappához viszonyított relatív.

## Dokumentumhivatkozások címkékkel

Néhány régebbi bejegyzés tartalmaz dokumentumcímkéket, mint például:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

A `^2023_001` rész egy Beancount hivatkozás. Összekapcsolhatja a bizonylatot a hozzá tartozó tranzakcióval, ha ott is ugyanazt a hivatkozást használják.

## A `scanned` jelentése

A főkönyvekben található megjegyzések határozzák meg a beolvasott bizonylatokra vonatkozó konvenciót. Amikor a `scanned` címkét használják, az azt jelenti:

- A bizonylatot beolvasták vagy digitalizálták.
- A képet csökkentették és optimalizálták, például a TinyPNG segítségével.
- A fájlt egy év és szám mintázat szerint mentették el, például `2023_002.jpg`.
- A számra a kapcsolódó főkönyvi bejegyzés hivatkozik.

## Jó fájlnevek

A jó bizonylatfájlnevek stabilak és olvashatók:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Kerüljék az olyan neveket, mint a `scan.jpg`, `image1.jpg` vagy `download.pdf`.

## Munkafolyamat egy új bizonylat esetén

1. Mentsék a bizonylatot a megfelelő bizonylatmappába.
2. Nevezzék át úgy, hogy később felismerhető legyen.
3. Vezessék be vagy keressék meg a kapcsolódó tranzakciót.
4. Adjanak hozzá egy `document` sort vagy hivatkozás metaadatot, ha hasznos.
5. Ha a bizonylatot feldolgozták, helyezzék át az `Eingetragen` mappába, ha ez a mappa konvenció.
6. Töltsék újra a Favát, és ellenőrizzék, hogy a dokumentumhivatkozás működik-e.

## Ha hiányzik egy bizonylat

Ha hiányzik egy bizonylat, adjanak hozzá egy megjegyzést a tranzakció közelében:

```beancount
; Receipt missing. Ask responsible person.
```

Ne tegyenek úgy, mintha lenne dokumentum, ha az nem áll rendelkezésre.

## Szerződések és honorárium számlák

A szerződéseket és a honorárium számlákat a kapcsolódó projekt vagy könyvelési mappa közelében kell tárolni, és egyértelműen hivatkozni rájuk. Projekt auditok esetén a fontos kérdés nem csak az, hogy a tranzakció létezik-e, hanem az is, hogy a kiadást igazoló dokumentum gyorsan megtalálható-e.
