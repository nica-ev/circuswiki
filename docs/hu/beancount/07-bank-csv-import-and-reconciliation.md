---
lang: hu
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Banki CSV importálás és egyeztetés
description: Munkafolyamat Sparkasse CSV adatok importálásához és bankszámlaegyenlegek egyeztetéséhez.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:13+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:13+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Banki CSV import és egyeztetés

Ez a munkafolyamat új Sparkasse tranzakciókat visz be a Beancountba, és megerősíti, hogy a főkönyv továbbra is megegyezik a valós bankszámlával.

## Hol történik az importálás

| Egyesület | Import mappa | Szkript | Kimeneti fájl |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Mielőtt exportálunk a Sparkasse-ból

1. Nyissuk meg a megfelelő főkönyvi fájlt.
2. Keressük meg a `Balance Checks` (Egyenlegellenőrzések) szekciót.
3. Keressük meg a Sparkasse számla legfrissebb egyenlegdátumát.
4. Ellenőrizzük az alján található `Bank Dump` (Banki mentés) szekcióban az utolsó importálás dátumát is.
5. A két dátum közül a későbbit használjuk kiindulópontként.

Ez elkerüli az elmaradt tranzakciókat vagy az ugyanazon időszak kétszeri importálását.

## Exportálás a Sparkasse-ból

1. Nyissuk meg a számla áttekintést.
2. Szűrjünk dátumtartomány szerint.
3. Kezdjük az utolsó ellenőrzött vagy importált dátummal.
4. Fejezzük be a mai dátummal vagy a kívánt egyeztetési dátummal.
5. Exportáljunk `Excel (CSV-CAMT V2)` formátumban.
6. Másoljuk a letöltött CSV fájlt a megfelelő `test` mappába.

A szkriptek a Sparkasse CSV-CAMT-V2 formátumot várják, pontosvesszővel elválasztott oszlopokkal.

## A CSV konvertálása

Nyissunk egy terminált a megfelelő `test` mappában, és futtassuk:

```powershell
python csv2bean.py "NEVE-A-LETÖLTÖTT-FÁJLNAK.CSV"
```

Példa:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Ha működik, a szkript kiírja a `Process finished.` (Feldolgozás befejeződött.) üzenetet, és létrehozza vagy felülírja a `beancount_file.beancount` fájlt.

## Mit csinál a konverter

A konverter alapvető Beancount bejegyzéseket hoz létre:

- A bejövő összegek alapértelmezetten a Sparkasse eszközszámlára és az `Einnahmen:Sonstiges` (Bevételek: Egyéb) számlára kerülnek.
- A kimenő összegek alapértelmezetten az `Ausgaben:Sonstiges` (Kiadások: Egyéb) és a Sparkasse eszközszámlára kerülnek.
- Néhány bevételi leírást automatikusan az `Einnahmen:Vereinsbeitrag` (Bevételek: Tagdíj) számlára osztályozunk.
- Néhány Tohuwabohu-val kapcsolatos szöveg projekt bevételi számlára osztályozódhat.

A konverter csak egy első lépés. Nem ismeri minden tranzakció végső könyvelési jelentését.

## Másolás a fő főkönyvbe

1. Nyissuk meg a `test/beancount_file.beancount` fájlt.
2. Hagyjuk figyelmen kívül a generált opciós fejlécet.
3. Másoljunk csak a tranzakciókat.
4. Illesszük be őket először a fő főkönyv `Bank Dump` (Banki mentés) szekciója alá.
5. Adjon hozzá egy dátummal ellátott elválasztót az importálás dátumához, ha szükséges.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

A `Bank Dump` egy átmeneti terület. Az importált tranzakciók később áthelyezhetők a megfelelő tematikus vagy projekt szekcióba.

## Importált bejegyzések osztályozása

Minden importált tranzakció esetében döntsük el:

- Egyesületi vagy projekt szintű?
- Bevétel vagy kiadás?
- Visszatérítés vagy kötelezettség törlesztése?
- A `Freies-Geld` (Szabad pénz) vagy egy projekt-specifikus eszközszámlához tartozik?
- Van-e hozzá csatolni való nyugta vagy számla?

Cseréljük le a tág általános számlákat, mint például az `Ausgaben:Sonstiges` (Kiadások: Egyéb), ha létezik pontosabb számla.

## Egyenlegellenőrzés hozzáadása

NICA példa:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Tohuwabohu példa:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Használjuk a Sparkasse által mutatott egyenleget az adott dátumra.

## Érvényesítés a Favában

1. Mentsük el a főkönyvi fájlt.
2. Töltsük újra a Favát.
3. Ellenőrizzük a hibákat a Fava oldal tetején.
4. Nyissuk meg a Sparkasse számla oldalát.
5. Erősítsük meg a futó egyenleget és a legfrissebb tranzakciókat.
6. Ellenőrizzük a Mérleget.
7. Ellenőrizzük a projekt irányítópultokat, ha projekt számlák érintettek voltak.

## Ha az egyenlegellenőrzés sikertelen

Gyakori okok:

- A CSV export kihagyott egy napot az elején vagy a végén.
- Egy tranzakciót kétszer importáltunk.
- Egy tranzakciót rossz egyesületi főkönyvbe másoltunk be.
- Egy számot hibásan szerkesztettünk.
- Egy projekt felosztásnál rossz előjelet használtunk.
- A PayPal vagy készpénz mozgásokat nem rögzítettük.

Ne távolítsuk el az egyenlegellenőrzést csak azért, hogy eltűnjön a hiba. Javítsuk meg az alapvető tranzakciós különbséget.
