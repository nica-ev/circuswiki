---
lang: hu
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Játékok - Az Adatoldal
description: Hogyan tették szabványossá és dinamikusabbá a játékinformációkat metaadatok és Obsidian bővítmények segítségével.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:00:33+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:54+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Játékok – Az adatok oldaláról**
**Hogyan tették egységessé és dinamikusabbá a játékleírásokat a metaadatok és az Obsidian bővítmények segítségével.**

Amikor a tartalomkezelésről van szó, a következetesség kulcsfontosságú. A projekt első nagyobb szakaszában a játékokkal foglalkoztam – mintegy 170-et, mindegyik saját, egyedi formátummal, stílussal és hozzáférhetőséggel. A probléma? Sok leírás mereven kódolt, statikus linkekre támaszkodott, ami rémálommá tette új játékok hozzáadását vagy a struktúra módosítását.

Tehát felgyűrtem az ingujjam, és nekiláttam a munkának.
<!-- more -->
## 1. Lépés: Egységes formátum
Az elsődleges feladat az egységes formátum kialakítása volt az összes játékleíráshoz. Ehhez a „Tasifan Spielebuch” (Tasifan Játékkönyv) inspirált, amely egy jól strukturált forrás a játékleírásokhoz. A felhasználóbarátság fokozása érdekében rövid összefoglalókat is hozzáadtam, így minden lényeges részlet egy pillantással látható – még előnézetben is.

De az igazi áttörést a metaadatok jelentették.

## 2. Lépés: Metaadat varázslat
Mostantól minden kulcsfontosságú információ – csoportméret, anyagok, időtartam és így tovább – metaadatként szerepel minden Markdown fájl elején, YAML (vagy frontmatter) formátumban. Ez nemcsak a rendszerezést segíti, hanem az adatok újrafelhasználhatóságát is biztosítja az egész rendszerben.

A megfelelő játék megtalálásának megkönnyítése érdekében egy egyszerű, de hatékony logikát valósítottam meg:
1. **Válassz egy kategóriát**: Milyen típusú játékot keresel? Levezető játékot? Fogócskát? Csapatépítő foglalkozást? Kezdetben létrehoztam néhány kategóriát, de ezek igény szerint módosíthatók vagy bővíthetők.
2. **Böngészd át a táblázatot**: Miután kiválasztottad a kategóriát, egy táblázat jelenik meg, amely felsorolja az összes odaillő játékot. A táblázat rendezhető – csak kattints a fejlécéire az időtartam, nehézség vagy más szempontok
