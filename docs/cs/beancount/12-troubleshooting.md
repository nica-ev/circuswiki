---
lang: cs
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Řešení problémů
description: Běžné problémy Fava a Beancount a jejich řešení.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:49+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:49+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 – Řešení problémů

## Fava se neotevře

Zkontrolujte:

- Je okno terminálu stále otevřené?
- Byla Fava spuštěna ve správné složce?
- Je použít správný port?
- Běží na stejném portu již jiná instance Favy?
- Je Fava nainstalovaná a dostupná v terminálu?

Příkazy:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Každý příkaz spusťte pouze ze správné složky s účetními knihami.

## Fava zobrazuje chybu Beancountu

Běžné příčiny:

- Překlep v názvu účtu.
- Chybějící směrnice `open` pro účet.
- Částka používá čárku místo tečky.
- Chybí uvozovky kolem příjemce platby nebo popisu.
- Transakce není v rovnováze.
- Kontrola zůstatku neodpovídá.
- Transakce používá účet poté, co byl uzavřen.

Opravte textový soubor, uložte jej a poté znovu načtěte Favu.

## Kontrola zůstatku selže

Nevymazávejte kontrolu zůstatku jako dočasné řešení. Prozkoumejte rozdíl.

Kontrolní seznam:

- Byl rozsah dat v CSV kompletní?
- Byl stejný CSV soubor importován dvakrát?
- Byly některé transakce vloženy do nesprávné účetní knihy?
- Byl transakci přiřazen nesprávný podúčet Sparkasse?
- Byl nesprávně změněn znaménko částky?
- Byla platba přes PayPal nebo hotovost zadaná pouze na jedné straně?
- Existují starší manuální úpravy po předchozí kontrole zůstatku?

## Konverze CSV selže

Zkontrolujte:

- Soubor CSV je ve stejné složce `test` jako `csv2bean.py`.
- Název souboru v příkazu je přesný.
- Soubor je export Sparkasse `Excel (CSV-CAMT V2)`.
- Soubor je oddělen středníkem.
- CSV nebyl otevřen a znovu uložen způsobem, který změnil jeho formát.

## Importované položky vypadají příliš obecně

To je očekávané. Převodník používá záložní kategorie, jako jsou:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

Uživatel musí importované položky ručně zkontrolovat a klasifikovat.

## Dashboard chybí

Zkontrolujte:

- Je nainstalován `fava-dashboards`.
- Účetní kniha obsahuje směrnici `custom "fava-extension" "fava_dashboards"`.
- Vedle účetní knihy existuje soubor `dashboards.yaml`.
- Fava byla po instalaci nebo změnách konfigurace restartována.

## Projekt se nezobrazuje v dashboardech

Zkontrolujte:

- Projekt má účet projektového aktiva pod očekávaným prefixem Sparkasse nebo PayPal.
- Účet projektu není uzavřen.
- Zůstatek projektu není přesně nula.
- Název účtu odpovídá vzoru dotazu v dashboardu.

## Odkaz na dokument nefunguje

Zkontrolujte:

- Cesta k souboru je relativní ke složce souboru účetní knihy.
- Název souboru je přesně napsán.
- Dokument nebyl po propojení přesunut.
- Cesta používá lomítka nebo standardní styl relativní cesty.

## Nejste si jisti, jak klasifikovat transakci

Použijte toto pořadí:

1. Vyhledejte podobné starší transakce ve Favě.
2. Zkontrolujte kontext projektu nebo faktury.
3. Zkontrolujte, zda patří do rozpočtové položky sponzora.
4. V případě nejistoty přidejte komentář.
5. Dočasně použijte `Sonstiges` pouze v případě, že není známa lepší kategorie.
6. Před finalizací se zeptejte odpovědné osoby pro projekt nebo finance.
