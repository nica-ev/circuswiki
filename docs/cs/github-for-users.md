---
lang: cs
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: GitHub – přímá spolupráce v repozitáři
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:53+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: ac5f43c5c49905b729ab3c3f288e96be0cf997b5a5f1e94ca4f7eb6a77c1686f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-12T17:31:53+00:00
---
> [!info] Stručně řečeno
> Tato stránka je určena pro lidi, kteří chtějí přímo pracovat s Markdown soubory CircusWiki. Pro běžné příspěvky tuto cestu nepotřebujete: Materiály můžete také jednoduše poslat e-mailem.

Přímá spolupráce přes GitHub je praktická, pokud chcete pravidelně opravovat stránky, vytvářet nové Markdown soubory nebo pracovat s trezorem CircusWiki v editoru, jako je Obsidian.

Pokud chcete přispět pouze hrou, metodou, PDF, odkazem nebo opravou, je jednodušší cesta obvykle lepší:

[Zpět na Přispět](mitmachen.md){ .md-button }

## Co potřebujete

- bezplatný účet na GitHubu: [https://github.com/join](https://github.com/join)
- volitelně GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- textový editor pro Markdown soubory, například Obsidian, VS Code nebo jednoduchý editor

GitHub Desktop není povinný, ale pro mnoho lidí je jednodušší než příkazový řádek.

## Najít repozitář

Veřejný repozitář najdete zde:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Zde se nacházejí skutečné Markdown soubory, obrázky, překlady a nástroje, ze kterých se sestavuje webová stránka.

## Pracovní postup stručně

Typický postup je:

1. Vytvořit fork repozitáře na GitHubu.
2. Naklonovat svou kopii na vlastní počítač.
3. Provádět změny v novém branchi.
4. Upravit soubory nebo vytvořit nové Markdown soubory.
5. Potvrdit změny (commit).
6. Nahrát branch na GitHub.
7. Otevřít Pull Request, aby mohla být změna zkontrolována a přijata.

## Krok za krokem s GitHub Desktop

### 1. Vytvoření forku repozitáře

Otevřete repozitář CircusWiki na GitHubu:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Klikněte na `Fork`. Tím se vytvoří vlastní kopie repozitáře ve vašem účtu na GitHubu. V této kopii můžete pracovat, aniž byste přímo měnili hlavní projekt.

### 2. Naklonování repozitáře

Otevřete GitHub Desktop a vyberte:

```text
File -> Clone repository...
```

Vyberte svůj fork `nica-ev/circuswiki` a určete složku na svém počítači.

Poté budete mít lokální kopii souborů.

### 3. Vytvoření branch

Pro svou změnu je nejlepší vytvořit vlastní branch, například:

```text
popis-hry-doplnit
opravit-odkaz
nova-metoda-balancovani
```

Branch udržuje vaši práci odděleně od hlavní verze. To usnadňuje pozdější kontrolu.

### 4. Úprava souborů

Veřejný obsah se nachází především ve složkách jazyků pod `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Všechny jazyky jsou rovnocenné. Neexistuje žádný hlavní jazyk, ve kterém by se nový obsah měl primárně vytvářet.

Pokud vytváříte novou původní stránku, umístěte ji do složky jazyka, ve kterém je text napsán. Například španělský původní text patří do `docs/es/`, německý do `docs/de/`, anglický do `docs/en/`.

Důležité je frontmatter na začátku souboru. Zde musí být rozpoznatelné, že stránka je originál, například:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` odpovídá jazyku původního textu. Z tohoto originálu lze později automaticky generovat překlady do všech podporovaných jazyků.

Při úpravách dbejte na následující:

- Nemazat frontmatter na začátku souboru.
- U nových původních stránek nastavit `translation_status: original` a odpovídající `translation_source_lang`.
- Stávající odkazy co nejvíce zachovat.
- Nezveřejňovat soukromá data, API klíče nebo interní poznámky.
- Obrázky používat pouze tehdy, jsou-li jasná práva k jejich užití.
- Raději provádět malé, jasné změny než velmi velké smíšené změny.

### 5. Potvrzení změn (commit)

V GitHub Desktop uvidíte své upravené soubory v sekci `Changes`.

Napište krátké shrnutí, například:

```text
Opravit seznam materiálů v pohybové hře
Doplnit bezpečnostní pokyn k Beigoma
Přidat popis nové hry
```

Poté klikněte na `Commit to <branch-name>`.

### 6. Nahrání změn

Klikněte na `Push origin`, abyste nahráli svůj branch na GitHub.

### 7. Otevření Pull Requestu

GitHub Desktop nebo GitHub v prohlížeči poté nabídne vytvoření Pull Requestu.

Pull Request znamená: Navrhujete svou změnu pro hlavní repozitář. Změna bude zkontrolována, případně okomentována a poté přijata nebo dále upravena.

## Základy Markdownu

Markdown je jednoduchý textový formát. Pro většinu příspěvků postačí nejdůležitější znaky:

```markdown
# Velký nadpis
## Nadpis sekce

Běžný text s **tučnou částí** a *kurzivní částí*.

- Bod seznamu
- Další bod seznamu

[Text odkazu](https://www.example.com)
```

## Pokud něco není jasné

Přímou spolupráci přes GitHub nemusíte hned dokonale umět. Pokud otevřete Pull Request a něco ještě není v pořádku, lze to vyjasnit v revizi.

Pokud chcete přispět pouze obsahem a technická cesta se zdá příliš složitá, jednoduše využijte e-mail na [stránce Přispět](mitmachen.md).
