---
lang: hu
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Kiadási megjegyzések
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:13:49+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:01+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
>[!info]
>Ezek a kiadási megjegyzések csak durva áttekintést adnak, az apróbb változtatásokat (mint például egyedi új oldalak, meglévő tartalom módosításai) nem soroljuk fel mindet. Ezek azonban a tár repozitórium előzményeiben pontosan nyomon követhetők.

>[!info]- **Verzió:** v0.04 - **Kiadás dátuma**: 2026. június 9.
>**Tartalom**
>- Erősen bővített többnyelvű tartalom: a tartalom mostantól strukturáltan a `docs/<nyelv>` alatt található.
>- Új és frissített fordítások számos játékleíráshoz és projektioldalhoz.
>- Lengyel workshop anyagok importálása és integrálása a többnyelvű tartalomstruktúrába.
>- A játékok tartalom- és metaadat-struktúrájának további egységesítése.
>
>**Technikai**
>- A weboldalgenerátort MkDocs/MkDocs Materialról Zensicalra váltottuk.
>- Új többnyelvű build és staging struktúra bevezetése.
>- A német marad az alapértelmezett nyelv nyelvi előtag nélkül; további nyelvek nyelvi kódok alatt lesznek elérhetők, pl. `/en/`, `/pl/`, `/es/`.
>- Központi nyelvkonfiguráció bevezetése a `tools/config/languages.json` fájlon keresztül.
>- GitHub-Pages telepítés frissítve az új Zensical struktúrához.
>- Helyi fordítási eszközök és fejlesztői konzol jelentős bővítése: állapotellenőrzések, kötegelt ütemezés, fordítási állapot, grafikus nézetek, navigációs eszközök, linkjavítás és takarítási munkafolyamatok.
>- Nyelvválasztó, fordítási állapotjelzők és hiányzó fordítások esetén tartalékoldalak hozzáadása.
>- Táblázatok javítása a végső webhelykimenetben: rendezhető táblázatok, jobb megjelenítés sűrű táblázatok esetén és opcionálisan összecsukható oldalrészek.
>
>**Javítva**
>- A belső és a Markdown linkek megbízhatóbban megmaradnak és javításra kerülnek a lefordított oldalakon.
>- A többnyelvű navigáció és az URL struktúra stabilizálódott.
>- A navigáció reszponzív viselkedése javult, különösen a Zensical mobil hamburger menüjével való együttműködés során.

>[!info]- **Verzió:** v0.03 - **Kiadás dátuma**: 2025. március 11.
>**Tartalom**
>- Hiányzó játékleírások hozzáadása
>
>**Technikai**
>- Favicon + logó hozzáadása
>- UI újratervezése
>- Az első szintű navigáció most az oldal fejlécében található, míg a kontextusfüggő jobb oldali navigációs sáv módosul.
>- A táblázatok a fejlécükre kattintva rendezhetők
>
>**Javítva**
>- A címkék újra működnek

>[!info]- **Verzió:** v0.02 - **Kiadás dátuma**: 2025. február 26.
>**Technikai**
>- Blog funkció
>- Analitika (Google)
>- Cookie banner
>- Visszajelzési widget (minden oldal alján)

>[!info]- **Verzió:** v0.01 - **Kiadás dátuma** 2025. január 15.
>**Tartalom**
>- 150 játékleírás hozzáadása
>- Dokumentáció alapleírása
>
>**Technikai**
>- Alapbeállítás Mkdocs és Mkdocs-materials számára
>- Obsidian támogatás Mkdocs-publisherrel (lehetővé teszi az Obsidian Markdown használatát, mint pl. Markdown linkek, Callout Boxok)
