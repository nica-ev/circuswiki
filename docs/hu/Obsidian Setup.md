---
lang: hu
translation_id: obsidian-setup
publish: true
tags: 
title: Obsidian Beállítás
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:48:07+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:20+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Az Obsidian rendkívül testreszabható, ami gondot okozhat az újonnan érkezőknek.
Egy alapbeállítást biztosítunk, amely tetszés szerint használható, beleértve a beépülő modulokat és témákat, valamint azok finomhangolt beállításait.
Ez egy alapbeállítás, amelyet mindenki a saját igényei szerint tovább alakíthat.
Mi csak egy működő megoldást kínálunk – amelyet itt dokumentálunk és magyarázunk el.

## Használt kifejezések
**Vault** – markdown fájlok és képek gyűjteménye, amelyek az ismeretbázist alkotják

## Beépülő modulok (Plugins)

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
Rengeteg új funkciót és stílusbeállítási lehetőséget kínál a Canvas számára.

### BRAT
Szükséges nem hivatalos beépülő modulok / az Obsidian ökoszisztémájában nem regisztrált beépülő modulok telepítéséhez, nevezetesen:
- Dataview Serializer
- Sortable

### Better Word Count
Főként a kijelölt szöveg szavainak/karaktereinek számát megjelenítő képessége miatt használatos.
A státuszsávon látható.

### Beautitab
Tisztán kozmetikai, testreszabható "üres új lap" oldalt biztosít.

### Clear unused Images
Ahogy a neve is mutatja, segít a vault rendszerezésében az el nem használt képek azonosításával.

❗Kizártam az ```/site/``` almappát, hogy ne törölje mindig a buildelt weboldal képeit (ami nem probléma, inkább bosszúság).

❗Legyen óvatos a "clear attachments" paranccsal – ez mindig törölni fogja az ```mkdocs.yml``` és a ```license.``` fájlokat. Ha ez megtörténik, a fájlok a .trash mappában vannak, és visszaállíthatók. De könnyű elfelejteni.

### Dataview
SQL-szerű lekérdezéseket tesz lehetővé a vaultban.

### Dataview Serializer
A Dataview eredményeit markdownná alakítja.
Segít a dataview lekérdezések eredményeinek újrafelhasználásában a tényleges jegyzetekben.

### Emoji Toolbar
Nos, könnyű hozzáférést biztosít az emojikhoz.
**Gyorsbillentyű beállítva: ALT-E**
😍

### Linter
Markdown fájlokat és frontmatter adatokat tisztít.
Segít a következetes formátum megőrzésében.

### Note Toolbar
Testreszabható eszköztárakat tesz lehetővé egy jegyzet tetején, amelyeket mappa/fájl szinten lehet definiálni.

### Tag Wrangler
További lehetőségeket kínál a címkékkel való munkához.
- Címkék átnevezése
Segít a vault rendszerezésében.

### Templater
Testreszabható sablonokat tesz lehetővé, amelyeket manuálisan vagy feltételek alapján (például jegyzet létrehozásakor) lehet beszúrni.

### Status Bar Organizer
Lehetővé teszi az elemek elrejtését a státuszsávból.

### Sortable
Lehetővé teszi a táblázatok (mind a markdown, mind a dataview táblázatok) rendezését a fejlécükre kattintva.

### Workspaces Plus
Könnyű gyorsváltást tesz lehetővé a státuszsávból.

## Vault fájlrendszer

[Vault File System](Vault%20File%20System.md){ .md-button }
