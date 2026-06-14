---
lang: nl
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Spelletjes - De Data Kant
description: Hoe spelinformatie werd gestandaardiseerd en dynamischer gemaakt met behulp van metadata en Obsidian plugins.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:00:44+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:55+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Spelletjes - De Datakant**
**Hoe spelbeschrijvingen gestandaardiseerd en dynamischer werden gemaakt met behulp van metadata en Obsidian-plugins.**

Als het aankomt op het beheren van content, is consistentie cruciaal. Voor het eerste grote deel van dit project heb ik de spelletjes aangepakt – zo'n 170 stuks, elk met een eigen uniek format, stijl en toegankelijkheid. Het probleem? Veel van deze beschrijvingen waren afhankelijk van hardgecodeerde, statische links, wat het een nachtmerrie maakte om nieuwe spelletjes toe te voegen of de structuur aan te passen.

Dus, ik stroopte mijn mouwen op en ging aan de slag.
<!-- more -->
## Stap 1: Een Uniform Formaat
Het eerste wat moest gebeuren, was het vaststellen van een consistent formaat voor alle spelbeschrijvingen. Ik haalde inspiratie uit het "Tasifan Spielebuch", een goed georganiseerde bron voor spelbeschrijvingen. Om het nog gebruiksvriendelijker te maken, heb ik korte samenvattingen toegevoegd, zodat alle essentiële details direct zichtbaar zijn – zelfs in een preview.

Maar de echte gamechanger? Metadata.

## Stap 2: Magie van Metadata
Nu is alle kerninformatie – groepsgrootte, materialen, duur, en meer – opgeslagen als metadata bovenaan elk Markdown-bestand in een formaat genaamd YAML (of frontmatter). Dit houdt niet alleen alles georganiseerd, maar maakt de data ook herbruikbaar binnen het hele systeem.

Om het vinden van het juiste spel te vergemakkelijken, heb ik een simpele maar effectieve logica geïmplementeerd:
1. **Kies een categorie**: Wat voor spel zoek je? Een afsluitingsspel? Een tikkertje? Iets voor teambuilding? Ik heb een reeks categorieën gemaakt om mee te beginnen, maar deze kunnen naar behoefte worden aangepast of uitgebreid.
2. **Bekijk de tabel**: Zodra je een categorie hebt gekozen, zie je een tabel met alle spelletjes die daaronder vallen. De tabel is sorteerbaar – klik gewoon op de kopteksten om te ordenen op duur, moeilijkheidsgraad of andere criteria.

En hier is het sluitstuk: veel spelletjes komen in meerdere categorieën voor, dus je bent nooit beperkt tot slechts één manier om te vinden wat je nodig hebt.

## Niet-Helemaal-Dynamische Tabellen
De echte magie gebeurt met twee Obsidian-plugins: **Dataview** en **Dataview Serializer**.

Dataview stelt me in staat om dynamische lijsten en tabellen te maken met database-achtige queries. De clou? Deze tabellen werken alleen binnen Obsidian, omdat de onderliggende Markdown-bestanden niet worden gewijzigd.

Daar komt Dataview Serializer om de hoek kijken. Deze plugin converteert die dynamische tabellen naar statisch Markdown-formaat en schrijft ze direct in het bestand. Wanneer de site wordt gebouwd met MkDocs, zijn de tabellen statisch, maar werden ze in wezen dynamisch gegenereerd offline.

Deze queries kunnen behoorlijk complex worden, waardoor ik specifieke delen van de wiki kan doorzoeken of weergeven – zoals alle spelbeschrijvingen of artikelen geschreven door een specifieke auteur. En omdat ze automatisch worden bijgewerkt (via de serializer-stap), is het toevoegen van nieuwe informatie en het bouwen van een navigeerbare structuur een eitje.

Maar het is niet allemaal zonneschijn en rozengeur. Het proces is niet volledig automatisch. Dataview Serializer kan een bestand alleen herschrijven als het geopend is in Obsidian. Voor nu is dit beheersbaar – ik heb elke pagina getagd met een dynamische tabel of lijst, waardoor het makkelijk is om erdoorheen te bladeren. Maar als het aantal van deze pagina's aanzienlijk groeit, moet ik de aanpak misschien heroverwegen.

## Tools en Taalmodellen
De originele spelbeschrijvingen waren een mengelmoes qua opmaak en kwaliteit. Om het proces te stroomlijnen, heb ik taalmodellen (LLM's) ingezet. Ik heb een specifieke prompt opgesteld, compleet met voorbeeldopmaak, om ervoor te zorgen dat de content zelf niet werd gewijzigd (geen onnodige herschrijvingen). Toch heb ik elk resultaat handmatig beoordeeld en waar nodig kleine aanpassingen gemaakt.

Hier is de conclusie: mits correct gebruikt, zijn deze tools *ongelooflijk* krachtig. De sleutel is om precies en doelgericht te zijn in hoe je je taken formuleert.

De uiteindelijke wijzigingen gaan voornamelijk over opmaak – hoe de informatie en spelbeschrijvingen worden gepresenteerd. De metadata daarentegen is allemaal handmatig ingevoerd. Aangezien ik toch alles dubbel moest controleren, was het in dit geval sneller om het met de hand te doen.

Het is echter een langzaam proces. Omdat ik er parttime aan werk, doe ik ongeveer 10-15 spelletjes per dag. De vooruitgang is gestaag, maar het zal nog wel even duren.

## Uitdagingen die Voorliggen
Een mogelijke horde zijn vertalingen. Zoekopdrachten zouden aangepast moeten worden om taalspecifieke versies van spelletjes of tags te vinden. Voor nu kan dit handmatig worden afgehandeld, maar als het systeem groeit, kan automatisering noodzakelijk zijn.

Vertaling is een complex onderwerp, en daar duik ik een andere keer dieper in.

## Waarom de Moeite?
Het korte antwoord? Schaalbaarheid.

Dit systeem is ontworpen om te groeien. Door het formaat te standaardiseren, metadata te benutten en dynamische tools te gebruiken, heb ik een fundament gecreëerd dat meer content kan verwerken zonder onhandelbaar te worden.

## Wat is er Verder Nog Nieuw?
De zoekfunctie heeft een paar upgrades gekregen:
- **Automatisch aanvullen**: Terwijl je typt, stelt de zoekfunctie queries voor die de meeste treffers opleveren. Dit is niet gebaseerd op gebruikersgedrag – we volgen geen zoekopdrachten – maar op de statische zoekindex die wordt gegenereerd bij het bouwen van de site.
- **Opgeslagen zoekopdrachten**: Klik op een klein icoontje naast de zoekbalk en je query (en resultaten) worden opgeslagen in de URL. Bladwijzer dit, en je krijgt elke keer dezelfde resultaten.

Het is een kleine functie, maar het kan ongelooflijk nuttig worden naarmate de wiki groeit en meer diverse onderwerpen behandelt.
