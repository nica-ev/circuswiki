---
lang: de
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Interaktiver Prototyp zum Suchen und Erkunden von Zirkusorten und Netzwerken aus CircusWiki-Daten.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: de
---

# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">CircusFinder wird geladen …</p>
</div>

> [!info] Genaue Orte und ungefähre Netzwerkpositionen
> Blaue Marker beruhen auf veröffentlichten Adressen. Orangefarbene Marker der importierten Netzwerk-Kontakte zeigen dagegen nur Stadt- oder Regionszentren. Bitte prüfe zeitabhängige Angaben wie Kurs- und Trainingszeiten vor dem Besuch auf der verlinkten Website.

<noscript>
CircusFinder benötigt JavaScript für Karte und Filter. Die einzelnen Einträge bleiben als normale Wiki-Seiten zugänglich.
</noscript>

## Was dieser Prototyp testet

Die Daten stammen aus Markdown-Dateien mit YAML-Metadaten. Beim Zensical-Build werden sie geprüft und als JSON exportiert. Diese Seite lädt ausschließlich diesen Export und kennt die ursprünglichen Markdown-Dateien nicht.

- Freitextsuche über Namen, Beschreibung, Ort und Angebote
- Filter nach Art des Eintrags
- Kartenmarker mit Popup-Informationen
- blaue Marker für veröffentlichte, genaue Adressen
- orangefarbene Marker für ungefähre Stadt- oder Regionspositionen
- freiwillige Umkreissuche über die Browser-Geolokalisierung
- Einträge ohne geografischen Punkt, etwa internationale Netzwerke
