---
lang: cs
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Přehledy a reporty Fava
description: Přehled reportů Fava a vlastních dashboardů pro kontrolu účetnictví.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:35+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:35+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 – Přehledy a reporty Favy

Fava poskytuje standardní účetní reporty. Systém také využívá `fava-dashboards` pro vlastní přehledové stránky.

## Standardní pohledy Favy

| Pohled | Použití pro |
| --- | --- |
| Rozvaha | Kontrolu aktiv, pasiv, volných prostředků, zůstatků na PayPal, hotovosti a projektech. |
| Výkaz zisku a ztráty | Zobrazení příjmů a výdajů v čase. |
| Stránka účtu | Prohlížení všech transakcí pro jeden účet. |
| Deník | Vyhledávání chronologické historie transakcí. |
| Dotaz | Spouštění vlastních dotazů Beancount podle potřeby. |
| Dokumenty | Vyhledávání propojených účtenek a souborů. |

## Rozšíření dashboardu

Ledgery obsahují tuto direktivu:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Tím se aktivuje rozšíření dashboardu, pokud je nainstalován balíček `fava-dashboards`.

## Konfigurační soubory dashboardu

Soubory dashboardu se jmenují `dashboards.yaml`. Jsou uloženy poblíž souborů ledgeru a na sdílené úrovni účetnictví.

## Hlavní sekce dashboardu

| Dashboard | Účel |
| --- | --- |
| `Vorstand-Cockpit` | Přehled pro management: volné peníze, celkový zůstatek Sparkasse, PayPal, hotovost, trend likvidity, měsíční výsledek, zůstatky aktivních projektů. |
| `Details & Daten` | Detailní grafy: výdaje podle kategorií, příjmy podle kategorií, tok peněz, síť projektů/osob. |

## Důležité ukazatele dashboardu

### Freies Geld (Volné peníze)

Ukazuje peníze dostupné mimo prostředky vyhrazené pro projekty. Typické účty jsou `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` a `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt (Celkem Sparkasse)

Ukazuje celkový zůstatek na účtech Sparkasse, včetně hlavního bankovního účtu a interních podúctů.

### PayPal

Ukazuje zůstatek na PayPalu. Záporný zůstatek na PayPalu naznačuje, že je třeba něco zkontrolovat.

### Barkasse (Hotovostní pokladna)

Ukazuje zůstatek v hotovostní pokladně.

### Saldo Aktiver Projekte (Zůstatek aktivních projektů)

Ukazuje projekty s nenulovým zůstatkem. To je užitečné pro zjištění, které projekty stále drží peníze nebo jsou přečerpané.

### Monatlicher Ueberschuss / Fehlbetrag (Měsíční přebytek / schodek)

Ukazuje měsíční provozní přebytek nebo schodek, s vyloučením projektových účtů v dotazu dashboardu.

## Jak zodpovědně používat dashboardy

Dashboardy jsou souhrny. Pokud se nějaké číslo zdá překvapivé:

1. Klikněte na propojený účet nebo report Favy.
2. Prohlédněte si podkladové transakce.
3. Zkontrolujte, zda transakce stále není v kategorii `Sonstiges` (Ostatní) nebo `Bank Dump` (Výpis z banky).
4. Zkontrolujte, zda název účtu odpovídá vzoru dotazu dashboardu.
5. Potvrďte kontroly zůstatků, než budete důvěřovat číslům managementu.

## Když se čísla na dashboardu zdají nesprávná

Běžné příčiny:

- Transakce byla zaúčtována na hlavní bankovní účet místo na projektový podúčet.
- Projektový účet byl uzavřen, ale stále má nenulový zůstatek.
- Nový projekt používá vzor pojmenování, který není zahrnut v dotazu dashboardu.
- Transakce je stále v široké záložní kategorii.
- Soubor dashboardu patří k jinému ledgeru, než který je právě otevřen.
