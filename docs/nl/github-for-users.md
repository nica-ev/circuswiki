---
lang: nl
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: GitHub - Direct meewerken in de repository
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:23+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:17+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] Kort samengevat
> Deze pagina is bedoeld voor mensen die direct aan de Markdown-bestanden van CircusWiki willen werken. Voor normale bijdragen heb je deze weg niet nodig: je kunt materiaal ook gewoon per e-mail sturen.

Direct meewerken via GitHub is handig als je regelmatig pagina's wilt corrigeren, nieuwe Markdown-bestanden wilt aanmaken of met de CircusWiki-vault wilt werken in een editor zoals Obsidian.

Als je alleen een spel, een methode, een PDF, een link of een correctie wilt bijdragen, is de eenvoudigere weg meestal beter:

[Terug naar Meedoen](mitmachen.md){ .md-button }

## Wat je nodig hebt

- een gratis GitHub-account: [https://github.com/join](https://github.com/join)
- optioneel GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- een teksteditor voor Markdown-bestanden, bijvoorbeeld Obsidian, VS Code of een eenvoudige editor

GitHub Desktop is niet verplicht, maar voor veel mensen eenvoudiger dan de commandoregel.

## Repository vinden

Het openbare repository staat hier:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Daar staan de eigenlijke Markdown-bestanden, afbeeldingen, vertalingen en tools waaruit de website wordt opgebouwd.

## Werkwijze in het kort

De typische gang van zaken is:

1. Repository op GitHub forken.
2. Je kopie naar je eigen computer klonen.
3. Wijzigingen aanbrengen in een nieuwe branch.
4. Bestanden bewerken of nieuwe Markdown-bestanden aanmaken.
5. Wijzigingen committen.
6. Branch naar GitHub uploaden.
7. Pull Request openen, zodat de wijziging gecontroleerd en overgenomen kan worden.

## Stap voor stap met GitHub Desktop

### 1. Repository forken

Open het CircusWiki-repository op GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Klik op `Fork`. Hierdoor ontstaat een eigen kopie van het repository in je GitHub-account. In deze kopie kun je werken zonder het hoofdproject direct te wijzigen.

### 2. Repository klonen

Open GitHub Desktop en kies:

```text
File -> Clone repository...
```

Kies je fork van `nica-ev/circuswiki` en bepaal een map op je computer.

Daarna heb je een lokale kopie van de bestanden.

### 3. Een branch aanmaken

Maak voor je wijziging bij voorkeur een eigen branch aan, bijvoorbeeld:

```text
spel-beschrijving-aanvullen
link-corrigeren
nieuwe-methode-balanceren
```

Een branch houdt je werk gescheiden van de hoofdversie. Dit maakt de latere controle eenvoudiger.

### 4. Bestanden bewerken

De openbare inhoud staat voornamelijk in de taalmappen onder `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Alle talen zijn gelijkwaardig. Er is geen hoofdtaal waarin nieuwe inhoud in principe moet ontstaan.

Als je een nieuwe originele pagina maakt, plaats deze dan in de taalmap van de taal waarin de tekst is geschreven. Een Spaanse originele tekst hoort bijvoorbeeld in `docs/es/`, een Duitse in `docs/de/`, een Engelse in `docs/en/`.

Belangrijk is de 'frontmatter' aan het begin van het bestand. Daar moet herkenbaar zijn dat de pagina een origineel is, bijvoorbeeld:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` komt overeen met de taal van de originele tekst. Vanuit dit origineel kunnen later automatisch vertalingen in alle ondersteunde talen worden gegenereerd.

Let bij het bewerken op het volgende:

- Verwijder de frontmatter aan het begin van het bestand niet.
- Stel bij nieuwe originele pagina's `translation_status: original` en de juiste `translation_source_lang` in.
- Behoud bestaande links zoveel mogelijk.
- Publiceer geen privégegevens, API-sleutels of interne notities.
- Gebruik afbeeldingen alleen als de gebruiksrechten duidelijk zijn.
- Maak liever kleine, duidelijke wijzigingen dan zeer grote gemengde wijzigingen.

### 5. Wijzigingen committen

In GitHub Desktop zie je je gewijzigde bestanden in het gedeelte `Changes`.

Schrijf een korte samenvatting, bijvoorbeeld:

```text
Corrigeer materiaal-lijst in bewegingsspel
Voeg veiligheidsinstructie toe voor Beigoma
Voeg nieuwe spelbeschrijving toe
```

Klik daarna op `Commit to <branch-name>`.

### 6. Wijzigingen uploaden

Klik op `Push origin` om je branch naar GitHub te uploaden.

### 7. Pull Request openen

GitHub Desktop of GitHub in de browser biedt daarna aan om een Pull Request te maken.

Een Pull Request betekent: je stelt je wijziging voor aan het hoofd-repository. De wijziging wordt gecontroleerd, eventueel becommentarieerd en dan overgenomen of verder bewerkt.

## Markdown-basis

Markdown is een eenvoudig tekstformaat. De belangrijkste tekens zijn voldoende voor de meeste bijdragen:

```markdown
# Grote kop
## Sectie kop

Normale tekst met **vetgedrukte tekst** en *cursieve tekst*.

- Lijstitem
- Nog een lijstitem

[Linktekst](https://www.example.com)
```

## Als iets onduidelijk is

Direct meewerken via GitHub hoef je niet meteen perfect te kunnen. Als je een Pull Request opent en iets nog niet klopt, kan dat in de review worden opgehelderd.

Als je alleen inhoud wilt bijdragen en de technische weg te ingewikkeld lijkt, gebruik dan gewoon de e-mail op de [Meedoen-pagina](mitmachen.md).
