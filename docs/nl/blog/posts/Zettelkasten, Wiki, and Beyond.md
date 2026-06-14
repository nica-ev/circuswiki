---
lang: nl
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki en verder
description: 
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Zettelkasten, Wiki, and Beyond.md
translation_source_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:12:29+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:11+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki en Meer**  
**Waarom ik dit project ben gestart, de ideeën erachter en waar het naartoe kan leiden.**

In 2013 werkte ik als projectmanager voor een jeugdcircus. Trainers kwamen vaak naar me toe met de vraag of ik andere spelletjes, methoden of trucjes kende. Destijds had ik tal van bronnen – boeken, tijdschriften, notities van workshops – maar alles was ongeorganiseerd en nauwelijks gedigitaliseerd.  
<!-- more -->
Mijn eerste poging om deze bronnen toegankelijk te maken voor de trainers was een klassieke wiki. Veel van de spelbeschrijvingen die je vandaag de dag ziet, zijn uit die periode afkomstig. Tegelijkertijd begon ik mijn bronnen te digitaliseren. Ik ontdekte de *Zettelkasten* (prikbord) methode van Niklas Luhmann en begon mijn gegevens te organiseren volgens zijn principes.  

De wiki was een mislukking. Er was weinig interactie; de trainers gebruikten hem een paar keer en hij werd snel vergeten. Mijn persoonlijke Zettelkasten groeide echter wel. Hoewel ik aanvankelijk gespecialiseerde software gebruikte, begon ik al snel na te denken over hoe ik deze steeds waardevollere verzameling toekomstbestendig kon maken.  

Wat betekent dat? De eerste wake-up call kwam toen ik besefte dat de software die ik gebruikte niet meer werd ontwikkeld. Ik moest nieuwe software vinden – en uitzoeken hoe ik mijn gegevens daarin kon migreren. Toen ontdekte ik Markdown.  

Markdown is een eenvoudig bestandsformaat – in wezen een platte tekstbestand – ontworpen om onafhankelijk te zijn van specifieke software. Met andere woorden, het is een wijdverbreide standaard die kan worden gelezen en bewerkt met de meest basale tools.  

Het formaat ondersteunde alles wat ik nodig had: basis tekstopmaak, links, tags en metadata (bijv. titel, auteur, beschrijving, etc.). Ik vond nieuwe software die Markdown gebruikte en bleef mijn Zettelkasten uitbouwen. Op dat moment had ik ongeveer 600 notities (of bestanden/pagina's). Later stapte ik opnieuw over op andere software, en de overgang verliep naadloos.  

>[!info]  Belangrijkste les
>Je gegevens toekomstbestendig maken betekent gebruikmaken van een eenvoudig, wijdverbreid formaat dat onafhankelijk is van specifieke software.  

## Samenwerking en Delen  

Mijn eerste poging met een wiki werkte niet – deels omdat het me niet lukte anderen te inspireren om bij te dragen. In de loop der jaren groeide mijn persoonlijke Zettelkasten uit tot meer dan 3.000 notities, waarvan vele over onderwerpen als circuspedagogie, spelletjes, jongleren en meer.  

Een tijdlang maakte ik het gewoon online toegankelijk, maar afgezien van een paar mensen die ervan wisten en af en toe spelbeschrijvingen opzochten, was er geen echte samenwerking of bredere deling.  

Nu, ongeveer 12 jaar na het starten van mijn Zettelkasten, geef ik het nog een kans. Het doel is om een gedeelde kennisbank te creëren voor onderwerpen als circus- en bewegingspedagogie, circuskunsten en meer.  

### Belangrijke overwegingen en vragen  
- **Onafhankelijkheid van specifieke systemen**  
- **Eenvoudig, makkelijk te begrijpen dataformaat**  
- **Bruikbaarheid en doelgroep**  
- **Gestructureerde data**  

Traditionele wiki-software (of platforms zoals WordPress) vielen af omdat ze afhankelijkheid creëren van één enkel systeem. Hoewel dit op korte of middellange termijn kan werken, is het op lange termijn een duidelijke zwakte.  

In plaats daarvan beheer ik de gegevens (als Markdown- en afbeeldingsbestanden) onafhankelijk van hoe ze uiteindelijk worden gepresenteerd. Dit zorgt ervoor dat de gegevens, zelfs over 20 jaar, bruikbaar blijven. De manier waarop ze worden weergegeven of bewerkt, kan drastisch veranderen, maar de onderliggende gegevens blijven hetzelfde.  

Er zijn talloze manieren om de gegevens te presenteren: als website, e-book, PDF of zelfs een app. Het kan in een bestand worden gezipped en offline worden gelezen of bewerkt met een eenvoudige teksteditor. Als je het wilt weergeven als een WordPress-site of wiki, is dat slechts een kwestie van de gegevens importeren – omdat het gestructureerd en makkelijk te lezen is, is het relatief eenvoudig te implementeren (met de juiste kennis).  

## Mijn huidige oplossing voor de website  

Ik gebruik MkDocs en het MkDocs-Material thema om een statische website te genereren. Er zijn veel programma's die statische HTML-bestanden maken van Markdown, maar MkDocs is specifiek ontworpen voor documentatie. Veel van de functies die het genereert – zoals full-text search en navigatie – zijn ongelooflijk nuttig.  

MkDocs is ook een veelgebruikte, open-source oplossing die wordt ondersteund door grote bedrijven, wat garandeert dat het op zijn minst op middellange termijn functioneel blijft.  

## Samenwerking  

De volgende stap is om dit een gezamenlijke inspanning te maken. Ik onderzoek manieren om anderen uit te nodigen om bij te dragen, hetzij door nieuwe inhoud toe te voegen, bestaande vermeldingen te verfijnen, of verbeteringen voor te stellen. Het doel is om een levende, evoluerende bron te creëren die profiteert van collectieve kennis en expertise.
