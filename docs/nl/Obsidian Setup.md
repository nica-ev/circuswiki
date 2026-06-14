---
lang: nl
translation_id: obsidian-setup
publish: true
tags: 
title: Obsidian Setup
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:23:02+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:21+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Obsidian is extreem aanpasbaar, wat voor nieuwkomers een probleem kan zijn.
We bieden een basis-setup die direct te gebruiken is, inclusief plugins en thema's, evenals hun fijn afgestelde instellingen.
Dit is een basis-setup en kan verder worden aangepast aan ieders persoonlijke voorkeur.
We bieden simpelweg een werkende oplossing – die we hier zullen documenteren en uitleggen.

## Gebruikte termen
**Vault** – een verzameling markdown-bestanden en afbeeldingen die de kennisbank vormen

## Plugins

- Advanced Canvas
- BRAT
- Better Wordcount
- Clear Unused Images
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
Biedt toegang tot veel nieuwe functionaliteit en stylingopties voor Canvas

### BRAT
Nodig om onofficiële plugins / plugins die niet geregistreerd zijn in Obsidians ecosysteem te installeren, namelijk:
- Dataview Serializer
- Sortable

### Better Word Count
Voornamelijk gebruikt vanwege de mogelijkheid om het aantal woorden/tekens in geselecteerde tekst weer te geven.
Is zichtbaar in de statusbalk

### Beautitab
Puurl cosmetisch, biedt een aanpasbare "lege nieuwe tab"-pagina

### Clear Unused Images
Zoals de naam al aangeeft, helpt het bij het organiseren van de vault door ongebruikte afbeeldingen te identificeren

❗Ik heb de submap ```/site/``` uitgesloten, zodat de afbeeldingen van de gebouwde website niet altijd worden verwijderd (wat geen probleem is, meer een ergernis)

❗Wees voorzichtig met het commando 'clear attachments' – dit verwijdert altijd ```mkdocs.yml``` en de ```license.``` --> als dit gebeurt, staan de bestanden in de .trash-map en kunnen ze worden hersteld. Maar het is gemakkelijk te missen.

### Dataview
Maakt SQL-achtige queries op de vault mogelijk

### Dataview Serializer
Zet Dataview-resultaten om in markdown
Helpt bij het hergebruiken van de resultaten van dataview-queries in de daadwerkelijke notities

### Emoji Toolbar
Geeft, tja, gemakkelijke toegang tot emoji's
**Sneltoets ingesteld op: ALT-E**
😍

### Linter
Ruimt markdown-bestanden en frontmatter-gegevens op
Helpt bij het handhaven van een consistente vorm

### Note Toolbar
Maakt aanpasbare toolbars bovenaan een notitie mogelijk die op map-/bestandsniveau kunnen worden gedefinieerd

### Tag Wrangler
Biedt extra opties om met tags te werken
- Tags hernoemen
Helpt bij het organiseren van de vault

### Templater
Maakt aanpasbare sjablonen mogelijk die handmatig of op basis van voorwaarden (zoals het maken van een notitie) kunnen worden ingevoegd

### Status Bar Organizer
Maakt het mogelijk om items uit de statusbalk te verbergen

### Sortable
Maakt het sorteren van tabellen (zowel markdown- als dataview-tabellen) mogelijk door op hun kopteksten te klikken.

### Workspaces Plus
Maakt een eenvoudige snelle schakeling vanuit de statusbalk mogelijk

## Vault Bestandssysteem

[Vault Bestandssysteem](Vault%20File%20System.md){ .md-button }
