---
lang: hu
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Számlák és kategóriák
description: A német számlaszabályzat és a főkönyvekben használt kategóriák ismertetése.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:48+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:48+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Számlák és kategóriák

Ez az oldal a főkönyvben használt számlastruktúrát ismerteti.

## Névnyelv

A számlanevek németek. A jelentések következetességének megőrzése érdekében továbbra is a meglévő számlaneveket használja.

| Németül | Angol jelentés |
| --- | --- |
| `Vermoegen` | Eszközök |
| `Verbindlichkeiten` | Kötelezettségek |
| `Einnahmen` | Bevétel |
| `Ausgaben` | Kiadások |
| `Buero` | Iroda |
| `Verein` | Egyesület/általános egyesületi tevékenység |
| `Projekt` | Projekt |
| `Barkasse` | Készpénzes láda |
| `Freies-Geld` | Szabad/korlátozás nélküli alapok |

## Eszközzámlák

NICA példák:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Tohuwabohu példák:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Általános bevételi számlák

| Számla | Mire használható |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Tagdíjak. |
| `Einnahmen:Spende` | Adományok. |
| `Einnahmen:Verleih` | Bérleti vagy kölcsönzési bevétel. |
| `Einnahmen:Sonstiges` | Egyéb bevétel, amely máshová nem illik. |

## Általános kiadási számlák

| Számla | Mire használható |
| --- | --- |
| `Ausgaben:Buero:Miete` | Iroda- vagy helyiségbérlet. |
| `Ausgaben:Buero:Internet` | Internet és digitális szolgáltatások. |
| `Ausgaben:Buero:Sonstiges` | Egyéb irodai kiadások. |
| `Ausgaben:Verein:Versicherung` | Egyesületi biztosítás. |
| `Ausgaben:Verein:Ehrenamt` | Önkénteseknek juttatott költségtérítés vagy egyesületi önkéntes költségek. |
| `Ausgaben:Essen` | Élelmezési költségek egy adott projekten kívül. |
| `Ausgaben:Sonstiges` | Ideiglenes tartalék tisztázatlan kiadásokra. |

Az `Ausgaben:Sonstiges` és az `Einnahmen:Sonstiges` hasznosak importáláskor, de nem szabad, hogy végleges kategóriává váljanak, ha létezik pontosabb kategória.

## Projekt számlák

A projektszámlák erre a mintára következnek:

```text
Vermoegen:Bank:Sparkasse-EGYESÜLET:PROJEKT
Ausgaben:Projekt:PROJEKT
Einnahmen:Projekt:PROJEKT
```

Példák:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Tipikus projekten belüli alkategóriák

| Alkategória | Jelentés |
| --- | --- |
| `Honorar` | Személyeknek fizetett vagy munkáért kapott díjak. |
| `Aufwand` | Erőfeszítés vagy költségtérítés. |
| `Sachmittel` | Anyagok és kellékek. |
| `Sonstiges` | Egyéb projektköltségek vagy bevételek. |
| `Pauschale` / `Pauschalen` | Átalánydíjas vagy fix összegű projekt költségvetés. |

## Kötelezettségek személyek felé

A kötelezettségi számlák az embereknek tartozott vagy nekik visszafizetett pénzeket követik nyomon. Példák: `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` és `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## A megfelelő számla kiválasztása

1. Ez egyesületi vagy projekt szintű?
2. Ha projekt szintű, melyik projekt birtokolja a pénzt?
3. Bevétel, kiadás, eszközmozgás vagy kötelezettség visszafizetés?
4. Létezik már pontos kategória?
5. Ha nincs megfelelő kategória, ideiglenesen használja a `Sonstiges` kategóriát, és adjon hozzá egy megjegyzést.
