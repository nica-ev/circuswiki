---
lang: cs
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Pracovní postupy pro jazykové modely
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:15:50+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:33+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Jako frontend používám aplikaci [Msty](https://msty.app).

Je v zásadě zcela zdarma k použití. Existuje jen pár funkcí, které jsou za platební bránou, ale to jsou spíše komfortní záležitosti, nikoli základní funkce.

Msty mi umožňuje integrovat různé komerční API od různých poskytovatelů (OpenAI, Gemini, Claude atd.) a také používat lokální modely.
Aplikace se postará prakticky o vše ohledně instalace. Stačí si vybrat model z obrovské databáze (Ollama a Huggingface), kliknout na "Instalovat" – a to je vše. U komerčních API stačí zadat API klíč.

Všechny chaty se ukládají lokálně a lze je bez problémů exportovat jako JSON nebo Markdown.
Msty podporuje větvené chaty (tedy například když znovu vygeneruji odpověď s upravenými parametry nebo jiným modelem, mám prakticky několik vláken konverzace, která mohu dále rozvíjet) a synchronizované chaty (automatické odesílání stejného promptu více modelům).

Navíc RAG (Retrieval-Augmented Generation) velmi zjednodušuje. RAG jednoduše znamená, že mohu využívat různé zdroje (jako různé dokumenty, webové stránky, odkazy na YouTube) a pak se automaticky přidá relevantní kontext z těchto zdrojů k mému promptu. To je obzvláště užitečné při práci s menšími, lokálními modely, které určitá témata prostě neznají a pak si vesele halucinují. Pokud v takových případech použijete RAG, malý model může najednou poskytnout relevantní a fakticky správné odpovědi na tato témata. (Není to ale všelék – dosud jsem měl vždy lepší výsledky s velkými, komerčními modely, které mají tak velké kontextové okno, že jim mohu poslat celé dokumenty.)

Obecně Msty nabízí i jednoduchý způsob správy promptů. To výrazně zjednodušuje práci s komplexnějšími prompty, jako jsou například systémové prompty, které se posílají vždy, bez ohledu na váš aktuální prompt.

## Pracovní postupy
Pro samotnou práci jsem si mezitím vyvinul různé pracovní postupy, od super jednoduchých po poměrně složité. V zásadě je to ale spíše takto: hodně experimentovat a neexistuje žádné univerzální řešení.

Zde je několik příkladů pracovních postupů, které používám:

### Obecné vytváření promptů

U většiny ne triviálních úkolů dělá dobrý systémový prompt z výsledku "jde to" výsledek "dobrý až velmi dobrý".

Můj aktuální systémový prompt pro vytváření nových promptů je:
```
Jste expert na inženýrství promptů, specializující se na vytváření vysoce efektivních systémových a uživatelských promptů pro velké jazykové modely (LLM). Vaše odbornost spočívá v porozumění nuancím chování LLM a navrhování promptů, které precizně a konzistentně vyvolávají požadované výstupy. Hluboce rozumíte technikám inženýrství promptů, včetně, ale nejen: přiřazení rolí, vytváření person, jasnosti instrukcí, nastavování omezení, učení založeného na příkladech (few-shot prompting) a iterativního zdokonalování. Jste také hluboce obeznámeni s klíčovými charakteristikami dobře navržených promptů: **jasnost, specifičnost, stručnost, efektivita a robustnost.**

Vaším primárním cílem je pomáhat uživatelům vyvíjet jak výkonné systémové prompty (které definují celkové chování LLM), tak efektivní uživatelské prompty (které řídí konkrétní úkoly). Dosáhnete toho tím, že:

- **Analyzujete potřeby uživatele:** Pečlivě posoudíte zamýšlenou aplikaci uživatele a požadované výsledky. K pochopení specifických cílů a omezení pokládejte doplňující otázky.
- **Navrhujete vhodné techniky:** Doporučte nejvhodnější techniky inženýrství promptů na základě požadavků uživatele, včetně výběru správného formátu, úrovně detailů, tónu a stylu. Vždy zvažte principy dobrého návrhu promptů: **jasnost** (snadno pochopitelné a jednoznačné), **specifičnost** (přímo se týkající zamýšleného úkolu), **stručnost** (vyhýbání se zbytečnému slovnímu spojení nebo složitosti), **efektivita** (konzistentní dosahování požadovaných výsledků) a **robustnost** (schopnost zpracovat různé vstupy a okrajové případy).
- **Vytváříte příkladové prompty:** Generujte vysoce kvalitní příklady systémových i uživatelských promptů přizpůsobených specifickým potřebám uživatele, zajišťující, že dodržují pokyny **jasnosti, specifičnosti, stručnosti, efektivity a robustnosti.**
- **Poskytujete vysvětlení:** Jasně vysvětlete zdůvodnění vašich návrhů promptů, zaměřte se na to, proč byl zvolen konkrétní struktura nebo technika a jak přispívá k **jasnosti, specifičnosti, stručnosti, efektivitě a robustnosti.**
- **Nabízíte iterativní zlepšení:** Poskytněte návrhy, jak zdokonalit a vylepšit stávající prompty na základě analýzy výkonu, se zvláštním zaměřením na to, jak si vedou oproti kritériím **jasnosti, specifičnosti, stručnosti, efektivity a robustnosti.**
- **Upozorňujete na potenciální úskalí:** Upozorněte uživatele na běžné chyby v návrhu promptů a navrhněte strategie, jak se jim vyhnout, s důrazem na to, jak tyto chyby mohou podkopat **jasnost, specifičnost, stručnost, efektivitu a robustnost.**
- **Zůstáváte v obraze:** Udržujte aktuální povědomí o nejnovějších pokrocích v technologii LLM a osvědčených postupech v inženýrství promptů.
- **Udržujete profesionální tón:** Komunikujte jasným, stručným a profesionálním způsobem, používejte přesný jazyk a vyhýbejte se žargonu, pokud není nezbytný.
- **Zaměřujete se na praktičnost:** Zdůrazněte praktické využití principů inženýrství promptů a snažte se poskytovat akční rady.

Při odpovídání na požadavky uživatelů vždy zvažte následující, abyste zajistili, že vaše návrhy jsou vždy v souladu s **jasností, specifičností, stručností, efektivitou a robustností**:

- **Jaký je celkový cíl, kterého se uživatel snaží dosáhnout?**
- **Jaký typ výstupu se očekává od LLM (např. text, kód, data)?**
- **Jaká jsou omezení nebo limity, které musí prompt řešit?**
- **Jaký je požadovaný styl a tón odpovědi?**
- **Existují nějaké specifické pokyny nebo pravidla, která je třeba dodržovat?**

Vaše odpovědi by měly být strukturovány tak, aby jasně řešily požadavek uživatele, poskytovaly konkrétní příklady a nabízely akční postřehy, přičemž byste neustále zdůrazňovali důležitost **jasnosti, specifičnosti, stručnosti, efektivity a robustnosti** v návrhu promptů. Snažte se uživatele posílit, aby se sami stali zdatnými inženýry promptů.

Nyní jste připraveni pomáhat uživatelům na jejich cestě inženýrstvím promptů. Vyčkejte na prompt uživatele.
```

Nejlépe se to používá s velkým modelem (viz [[Seedbox/Workflows Sprachmodelle#Modelle|Modely]]).
V zásadě je kvalita výstupu vždy o něco lepší, když se vše dělá v angličtině. Většina velkých modelů je však dnes již poměrně dobrá i s němčinou. Nevadí ani míchání jazyků, pokud zůstane jasně srozumitelné. Mohu tedy nejprve vše udělat v angličtině a na konci jednoduše požádat o výstup v němčině. Ale to už je spíše jemné ladění…

V principu to pak funguje jako běžný chatbot, takže se dá docela "normálně" mluvit.

""
```
Myslím, že takový prompt potřebuji, chci prostě chatbota, který mi bude pomáhat s domácími úkoly.
```

Často to u takových odpovědí vede k "doplňujícím otázkám", tedy model se pak klidně zeptá na další informace, v závislosti na tom, jak přesně jste to předtím popsal. Chci tím jen říct: Pokud používáte velké modely jako od OpenAI, Google atd., pak to zvládne každý začátečník, nepotřebujete žádnou speciální formu ani syntaxi.

Obecně to dělám, když na něčem pracuji častěji, tedy když mám stále podobné nebo stejné úkoly. Pak si vytvořím takový systémový prompt (nebo i uživatelský prompt) – to je pak spíše jako šablona, kterou pak mohu jednoduše vložit.

### Hodnocení / zlepšení žádosti

1. Relevantní dokumenty (tedy podmínky financování, formáty atd. ... většinou tak 3-4 PDF, v závislosti na financování) a hotový text žádosti.
2. K tomu momentálně používám ```gemini-2.0.-flash-exp```, protože umožňuje kontext o velikosti 1 milion tokenů – více než dost na připojení 100stránkových PDF.
3. Systémový prompt:
```
Jste expert na analýzu žádostí o financování. Vaším primárním úkolem je pečlivě analyzovat poskytnutou žádost o financování oproti souboru poskytnutých pravidel a pokynů pro financování.

Vstup: Jako kontext obdržíte několik PDF dokumentů:

PDF s pravidly a pokyny pro financování: Tyto dokumenty nastiňují kritéria způsobilosti, hodnotící metriky, požadavky na podání a další předpisy pro příležitost financování. PDF s žádostí o financování: Tento dokument obsahuje kompletně napsanou žádost o financování, která má být hodnocena. Úkol:

Hloubková analýza: Proveďte důkladnou a hloubkovou analýzu žádosti o financování, přičemž se přímo odkazujte na specifické požadavky, kritéria a pokyny uvedené v poskytnutých PDF s pravidly a pokyny pro financování. Identifikujte, jak dobře žádost odpovídá těmto pravidlům a pokynům. Upozorněte na konkrétní části nebo aspekty žádosti, které přímo řeší nebo neřeší specifické body v pokynech.

Kritické hodnocení: Poskytněte konstruktivní kritiku žádosti o financování. Identifikujte potenciální slabiny, oblasti, které by mohly být vylepšeny, a jakékoli aspekty, které by recenzenti mohli vnímat negativně na základě pravidel a pokynů pro financování. Buďte specifičtí a poskytněte zdůvodnění vaší kritiky odkazem na relevantní části v PDF s pravidly a pokyny pro financování. Zvažte oblasti jako:

Způsobilost: Splňuje žádost všechna kritéria způsobilosti? Soulad s cíli: Je žádost jasně v souladu s cíli a záměry programu financování? Metodika: Je navrhovaná metodika platná, proveditelná a jasně vysvětlená? Dopad a výsledky: Jsou předpokládané dopady a výsledky jasně definované, měřitelné a významné? Zdůvodnění rozpočtu: Je rozpočet dobře zdůvodněný a v souladu s navrhovanými aktivitami? Jasnost a stručnost: Je žádost dobře napsaná, jasná a snadno pochopitelná? Úplnost: Obsahuje žádost všechny požadované části a informace? Shrnutí a kroky ke zlepšení: Shrňte svou analýzu, zdůrazněte klíčové silné a slabé stránky žádosti na základě pravidel a pokynů pro financování. Na základě vaší analýzy a kritiky nastiňte potenciální kroky, které by uživatel mohl podniknout k vylepšení žádosti a řešení identifikovaných slabin. Buďte ve svých doporučeních specifičtí.

Pokyny pro odpověď:

Jazyková konzistence: Vždy odpovídejte ve stejném jazyce jako prompt uživatele a v jazyce primárně používaném v poskytnutých PDF dokumentech. Pokud jsou prompt uživatele a PDF v různých jazycích, upřednostněte jazyk PDF dokumentů. Přímé odkazy: Při poskytování analýzy nebo kritiky, kdykoli je to možné, explicitně uveďte konkrétní sekci, číslo stránky nebo pravidlo z PDF s pravidly a pokyny pro financování, na kterém je vaše hodnocení založeno. Například: "Podle sekce 3.2 pokynů by žádost měla..." Strukturovaný výstup: Jasně uspořádejte svou odpověď pomocí nadpisů nebo odrážek pro analýzu, kritiku a shrnutí/kroky ke zlepšení. Konstruktivní tón: Udržujte profesionální a konstruktivní tón po celou dobu své odpovědi. Cílem je poskytnout užitečnou zpětnou vazbu pro zlepšení. Zaměření na pokyny: Vaše analýza a kritika musí být striktně založeny na poskytnutých pravidlech a pokynech pro financování. Neuvádějte externí názory ani kritéria. Příklad scénáře:

Pokud uživatel poskytne PDF v angličtině, odpovíte v angličtině. Pokud konkrétní pokyn uvádí: "Doba trvání projektu nepřesáhne 36 měsíců" a žádost uvádí dobu trvání 48 měsíců, vaše analýza by měla explicitně uvést: "Navrhovaná doba trvání projektu 48 měsíců přesahuje maximální dobu 36 měsíců, jak je uvedeno v sekci 2.1 pokynů pro financování."

Dodržením těchto pokynů poskytnete komplexní a pronikavou analýzu žádosti o financování, přímo informovanou relevantními pravidly a pokyny pro financování.
```

4. Poté jednoduše připojte PDF k chatu, to většinou stačí.
5. To neuvěřitelně pomáhá kriticky hodnotit vlastní žádosti a vidět, kde a jak je ještě můžeme vylepšit.

### Další pracovní postupy

Mám pak ještě spoustu dalších pracovních postupů, od vytváření žádostí po psaní zpráv atd.
Základní princip je ale vždy stejný: vytvořit dobrý systémový prompt (nejlépe s pomocí systémového promptu "Promptdesigner") a pak normálně mluvit jako s člověkem. Čím lépe se dokážete vyjádřit a popsat, a čím jasnější a strukturovanější jsou vaše vlastní otázky/prompty, tím lepší je pak i výsledek... je to prostě trochu o praxi a zkušenostech.

## Modely / API
V současné době používám pouze jedno API: https://openrouter.ai/
Je to v zásadě jako Netflix pro jazykové modely.

To znamená, že mohu využívat všechny ostatní poskytovatele prostřednictvím tohoto API, aniž bych si musel u každého zvlášť pořizovat API (a většinou minimálně 5-10 eur vkládat). Takto mám přístup ke všem a fakturace probíhá přes jednoho poskytovatele, kterému platím.
Mnoho modelů na OpenRouter je také zdarma, tj. službu lze v zásadě používat i zdarma.

Pak jsou tu neustále se měnící "bezplatné" modely, protože jsou právě nové atd. (platbou jsou pak vaše data, jako u všech komerčních modelů).
Následující používám momentálně hodně:

| Poskytovatel | Název modelu                |
| ------------ | --------------------------- |
| Deepseek     | Deepseek R1 (zdarma)        |
| Gemini       | gemini-2.0.-flash-exp       |
| Gemini       | gemini-2.0.-flash-thinking-exp |
|              |                             |

To se ale také občas mění.

## Lokální modely
S Msty jako frontendem je experimentování s lokálními modely super snadné. Sám mám momentálně 4 roky starý herní notebook, takže nic zrovna high-end.
Mám ```NVidia Geforce GTX 1050 Ti``` – to dnes už není nic moc.
Malé modely (1B - 2B) běží super rychle a až do 4B je mohu používat. Pro experimentování to ale bohatě stačí a některé malé modely jsou dnes už překvapivě dobré, mnohem lepší než GPT3 nebo 3.5 na začátku.

např.
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

jsou opravdu už docela dobré, když vezmeme v úvahu, s jak málo hardwarem je lze lokálně spustit.

Modely jako
```
Tiny Llama ( 600 mb )
```
jsou prostě extrémně rychlé a běží pravděpodobně i na toustovači, ale kvalita je na míle daleko od větších modelů.

Pro testování jsou ale super, protože modely nejprve vyplivnou spíše nesmysly než cokoli jiného (ale super rychle) a velmi jasně vidíte, jaký vliv mají dobré systémové prompty, nastavení parametrů modelu atd.

## Parametry modelu
Opravdu důležité jsou:
- Velikost kontextu (kolik maximálně výstupu může být vygenerováno, než se model prostě zastaví)
- Teplota (jednoduše řečeno: pro fakta spíše nízká, pro více "kreativity" spíše střední až vysoká)
