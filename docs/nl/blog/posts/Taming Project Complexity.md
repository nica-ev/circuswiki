---
lang: nl
translation_id: blog/posts/taming-project-complexity
created: 2025-05-02 04:37:37
update: 2026-10-10 20:09:23
date: 2025-05-03T11:00:00
publish: true
tags: 
title: Omgaan met Projectcomplexiteit - De Saga
description: De reis om een complexe ontwikkelomgeving effectief te versioneren zonder de hoofdprojectrepository te vervuilen.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Taming Project Complexity.md
translation_source_hash: 15300a3605c6b0a1fbd64d24db3d47f664d6814dc7ad022e57bdace07abf1462
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T20:54:49+00:00
translation_source_body_hash: 15300a3605c6b0a1fbd64d24db3d47f664d6814dc7ad022e57bdace07abf1462
translation_source_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T20:54:49+00:00
translation_source_localized_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_source_structural_metadata_hash: e3d56cc63df642dafa063d27bdc292098f6ac52159e83b1249537b0aebc40ffb
---
# Projectcomplexiteit temmen - De Saga
**Versiebeheer van de ontwikkelomgeving zonder je hoofd-repository te vervuilen**

Naarmate projecten evolueren, met name kennisbanken of documentatiesites die meerdere tools zoals MkDocs, Obsidian, aangepaste scripts en gespecialiseerde IDE's zoals Cursor omvatten, neemt de complexiteit natuurlijk toe. Het integreren van deze tools creëert krachtige workflows, maar introduceert ook een nieuwe uitdaging: het beheren van het groeiende aantal configuratiebestanden, concepten, scripts en planningsdocumenten die de kern van het project ondersteunen.
<!-- more -->
## Het pijnpunt: Wanneer `.gitignore` niet genoeg is

Ik bereikte onlangs een pijnlijk mijlpaal die veel ontwikkelaars tegenkomen: **het verliezen van uren werk**. De boosdoener? Bestanden die cruciaal waren voor mijn ontwikkelworkflow stonden niet onder versiebeheer.

Zoals velen wilde ik mijn publieke GitHub-repository schoon houden. Voor dit project betekende dit dat ik alleen de kern-Markdown-inhoud en de essentiële MkDocs-bestanden committeerde die nodig waren om de website te bouwen. Al het andere – mijn Obsidian-vault-configuratie, Cursor-instellingen, concept-vertaalscripts, taakplanningsnotities – stond ijverig vermeld in `.gitignore`. Dit hield de hoofd-repository netjes, maar liet mijn vitale ontwikkelingsinfrastructuur onbeschermd.

Deze wake-up call kwam gelukkig relatief vroeg. Tijdens het integreren van vertaaltools en het plannen van de workflow met behulp van notities binnen mijn projectstructuur, overschreef een ongeluk aanzienlijk planningswerk. Frustrerend, ja, maar een waardevolle les geleerd voordat de inzet hoger werd.

## Op zoek naar een oplossing: De mislukte pogingen

Mijn eerste ideeën draaiden om het slimmer gebruiken van Git zelf, maar ik liep tegen obstakels aan.

### Poging 1: Geneste repositories - De nachtmerrie van het wisselen van branches

Mijn eerste gedachte was om te onderzoeken hoe je meerdere Git-geschiedenissen binnen dezelfde projectmap kunt hebben, misschien met behulp van geneste repositories. Het idee was om een "dev"-repository op het hoogste niveau te hebben die *alles* bijhoudt (IDE-instellingen, concepten, de bestanden van de binnenste repository), terwijl de binnenste "publieke" repository alleen de schone, implementeerbare projectbestanden bevatte. De buitenste repository zou de `.git`-map van de binnenste repository negeren.

In theorie klonk dit als een nette gelaagde aanpak. Toen ik dit echter daadwerkelijk probeerde op te zetten, realiseerde ik me al snel dat dit niet werkte. Allereerst ondersteunt Git geneste repositories niet echt, althans niet zoals ik het me voorstelde. En het is logisch. Er is een kanttekening waar ik niet aan had gedacht: laten we zeggen dat ik in de binnenste repository (`docs-nica`) werk en naar een andere branch schakel. Nu veranderen alle bestanden in die map (om de branch weer te geven) – maar de buitenste repository (`docs-nica-dev`) staat nog steeds op zijn hoofdbranch. De buitenste repository ziet nu al deze bestands wijzigingen en denkt dat *dit* wijzigingen zijn aan *zijn* hoofdbranch... Het is duidelijk waarom dit een probleem is. Oké, dus deze aanpak werkte niet.

### Poging 2: Aparte repositories + Git-hooks - De kopieer-catastrofe

Terug naar de tekentafel. Mijn volgende idee was om twee volledig gescheiden repositories te hebben. Een `dev`-repository die alles bevat wat ik nodig heb (scripts, notities, configuraties, *en* de kernprojectbestanden). En een `public`-repository die alleen de markdown-inhoud en de MkDocs-setup bevat – alleen de essentie, zoals bedoeld voor implementatie.

Maar hier komt de addertje onder het gras: als we iets veranderen in de `public`-repository (misschien een snelle fix direct daar, of wijzigingen van medewerkers ophalen), hoe moet de `dev`-repository hiervan op de hoogte zijn? En vaker, hoe worden wijzigingen in `dev` weerspiegeld in `public`? We hebben een manier nodig om ze te koppelen.

Het eerste idee was om GitHub-hooks (of lokale Git-hooks) te gebruiken. Hiermee kun je commando's definiëren die na bepaalde Git-acties worden uitgevoerd, zoals een commit. Ik heb een hook ingesteld die, na een commit in de `dev`-repository, in feite gewoon de relevante bestanden (de `docs/`-map, `mkdocs.yml`, etc.) naar de `public`-repositorymap zou kopiëren.

Het leek op het eerste gezicht te werken, maar deze aanpak had twee hoofdzaken:

1.  **Ruisige geschiedenis:** De hook kopieerde *alle* relevante bestanden bij *elke* commit. Dit betekende dat de `public`-repository altijd dacht dat *al* zijn inhoud was gewijzigd. Hoewel technisch gezien niets brak, werd de commit-geschiedenis minder nuttig, met honderden (of duizenden) bestanden die bij elke commit werden gewijzigd, waardoor het onmogelijk werd om direct te pinpointen welke *bestandsinhoud* daadwerkelijk was gewijzigd.
2.  **Blindheid voor verwijderingen:** Het script *kopieerde* alleen bestanden. Als ik een bestand of map in de `dev`-repository verwijderde, werd deze wijziging niet weerspiegeld in de `public`-repository. Het oude bestand bleef daar gewoon rondslingeren.

Verdomme, al uren hieraan besteed – en nog steeds geen werkende oplossing.

## De doorbraak: Aparte repositories + bestandsynchronisatie

Toen herinnerde ik me een open-source software die ik lange tijd geleden had getest voor het synchroniseren van lokale mappen: **FreeFileSync**. Hoewel het jammer is om nog een set tools/software aan de stack toe te voegen die nodig is, voldeed het eigenlijk precies aan wat ik wilde.

De setup omvat nu:

1.  Twee aparte Git-repositories: `docs-nica-dev` (die alles bevat) en `docs-nica` (de schone, publieke versie).
2.  **FreeFileSync:** Gebruikt om de regels te definiëren voor hoe de specifieke mappen (zoals `docs/`, thema-bestanden, `mkdocs.yml`) tussen de twee repositorylocaties worden gesynchroniseerd. Het kan tweerichtingssynchronisatie, mirroring en cruciaal, het correct doorvoeren van verwijderingen aan.
3.  **RealTimeSync (onderdeel van FreeFileSync):** Gebruikt om de gedefinieerde mappen te monitoren op wijzigingen en de synchronisatie automatisch te triggeren op basis van de FreeFileSync-regels.

Deze combinatie overbrugt eindelijk effectief de kloof tussen de twee repositories. Wijzigingen die worden aangebracht in de kerninhoud-mappen van de `dev`-repository worden gespiegeld naar de `public`-repository, en vice versa indien nodig (hoewel mijn primaire stroom dev -> public is). Verwijderingen worden correct afgehandeld, en omdat het alleen *gewijzigde* bestanden synchroniseert, weerspiegelt de commit-geschiedenis in de `public`-repository nauwkeurig de daadwerkelijke wijzigingen.

## De resterende kanttekening: Synchronisatie vs. commit-timing

Er is echter nog steeds één nadeel. Wanneer ik een bestand wijzig in de `dev`-repository, en RealTimeSync draait, worden die wijzigingen *onmiddellijk* gesynchroniseerd naar de map van de `public`-repository, zelfs als ze nog niet in de `dev`-repository zijn gecommit. De synchronisatieoplossing is ontkoppeld van Git.

Het is geen enorm probleem, maar het vereist wat meer voorzichtigheid bij het daadwerkelijk committen en pushen van wijzigingen. In feite moet ik, wanneer ik aan de `dev`-repository werk, ervoor zorgen dat ik alles daar commit *voordat* ik me richt op de `public`-repository om te committen en te pushen. Het versterkt ook de gewoonte om de wijzigingen die voor commit zijn voorbereid in de `public`-repository *echt te beoordelen* voordat ik daadwerkelijk commit en push, om er zeker van te zijn dat de staat precies is wat ik bedoel.

## Voor wie is dit bedoeld? (Belangrijke verduidelijking)

Wacht even, voordat je denkt dat deze hele opzet verplicht is om de wiki te gebruiken, laat me dat verduidelijken. **Al deze complexiteit? Het is *niet* nodig als je alleen met de kerninhoud wilt werken.** Het belangrijkste toegangspunt is nog steeds super eenvoudig: kloon de publieke `docs-nica`-repository (die alleen de Markdown-bestanden en de MkDocs-setup bevat) en gebruik de tools die *jij* verkiest. Dat is alles.

Dus, waarom heb ik me al deze moeite getroost? Deze nogal complexe ontwikkelingsopzet dient *voor mij* twee hoofddoelen:

1.  **Mijn persoonlijke vangnet:** Het is cruciale versiebeheer voor *al mijn ontwikkelingsspullen* – de configuraties, de half-afgemaakte scripts, de planningsnotities – spullen die ik me niet opnieuw kan veroorloven te verliezen.
2.  **Het delen van mijn exacte workflow (optioneel):** Als iemand mijn specifieke omgeving wil repliceren, kunnen ze de `docs-nica-dev`-repository klonen. Ze krijgen mijn complete Obsidian-setup (plugins, instellingen, bladwijzers, zoekopdrachten, alles!), mogelijk Cursor-instellingen, en alle andere geïntegreerde tools die ik heb geconfigureerd. Het is een manier om een kant-en-klare basisopzet te delen.

Maar het fundamentele idee is niet veranderd: je kunt absoluut alleen de publieke repository pakken en er je eigen workflow omheen bouwen met je favoriete tools. Deze uitgebreide dans gaat over het beheren van *mijn* ontwikkelingschaos en het aanbieden van een blauwdruk voor degenen die dat willen.

## Conclusie: Een met moeite verkregen oplossing

Over het algemeen ben ik blij dat ik nu een oplossing heb gevonden voor het probleem – ook al heeft dit me wel zo'n twee dagen trial, error en frustratie gekost. Maar het correct krijgen van deze workflow was cruciaal om verdere problemen in de toekomst te voorkomen, en zorgde zowel voor een schone publieke repository als voor een volledig versiebeheerde ontwikkelomgeving.

Is deze opzet perfect? Het vereist het beheren van twee repositories en een externe synchronisatietool, plus een bewuste workflow voor het committen. Het lost echter direct het kritieke probleem op van het versiebeheer van *alles* wat nodig is voor een complex ontwikkelproces, zonder de netheid van de hoofdprojectrepository te compromitteren of te vechten tegen de beperkingen van Git met geneste structuren. Voor projecten die te groot worden voor eenvoudige `.gitignore`-strategieën, biedt deze aanpak een pragmatische weg vooruit, die veiligheid en structuur biedt voor de onvermijdelijke, rommelige realiteit van ontwikkelwerk.
