---
created: 2025-01-21 18:09:55
update: 2025-03-19 16:30:53
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Spiele - Datenkram
description: 
authors:
  - Marc Bielert
---

Der erste große Content-Part sind die Spiele. Ich habe ca 170 Spielebeschreibungen welche in unterschiedlichster Art formatiert, geschrieben und zugänglich waren. Oft durch harte (statische) Links - welches das hinzufügen von neuen Spielen, oder auch das ändern der Struktur schwer machte.

In einem ersten Schritt habe ich ein einheitliches Format gefunden, ...
<!-- more -->
...in Anlehnung an Spielebeschreibungen aus dem  "Tasifan Spielebuch". Diese wurden ergänzt mit Kurzbeschreibungen, so das nun alle wichtigen Informationen schnell (und in einem Preview) sichtbar sind. 

Die wichtigste Neuerung kommt jedoch mit der Nutzung von Metadaten. "Gespeichert" sind diese am Anfang der Markdown Datei, in einem Format welches "YAML" oder Frontmatter genannt wird. 
In diesem neuen Format werden nun alle wichtigen Informationen (z.B. Gruppengröße, Material, Zeit etc.) auch als Metadaten gespeichert und können an anderer Stelle genutzt werden.

Um nun schnell ein Spiel zu finden, haben wir folgende Logik :
1. Als erstes entscheide ich mich für eine Kategorie, was für eine Art von Spiel soll es sein. Ist eis eher ein Cool-Down Spiel, ein Fangspiel, etwas zum kennenlernen und so weiter. Ich habe verschiedene Kategorien angelegt, diese können aber beliebig geändert oder erweitert werden - sie stellen im Moment nur einen Startpunkt dar.
   
 Als nächstes sehe ich eine Tabelle die alle Spiele die in diese Kategorie fallen, auflistet. Da diese Tabelle sehr lang werden kann, gibt es die Möglichkeit diese zu sortieren (durch Klicken auf die jeweiligen Kopfzeilen der Tabellen). In der Tabelle werden auch einige der Metadaten dargestellt, so das man auch z.B. nach der Spielzeit oder dem Schwierigkeitsgrad sortieren kann.
 
 Oft finden sich Spiele auch in mehreren Kategorien wieder.

# Nicht ganz so dynamische Tabellen

Wirklich nützlich wird das ganze im Zusammenspiel mit zwei Plugins die ich in Obsidian benutze. Diese sind "Dataview" und "Dataview Serializer".
Dataview erlaubt es dynamisch Listen oder Tabellen mit Datenbank ähnlichen Suchabfragen zu erstellen. Leider funktioniert dies nur innerhalb von Obisidan, da die zugrundeliegende Markdowndatei nicht genändert wird.

Hier kommt das zweite Plugin ins Spiel. Es konvertiert eine solche, dynamisch erzeugte Tabelle in ein Makrdown Format und schreibt dies auch in die Datei.

Wird nun die Webseite mittels MkDocs gebaut, sind es am Ende natürlich statische Tabellen, wurden aber sozusagen offline dynamisch erzeugt.

Diese Suchabfragen können sehr komplex sein, und erlauben es mir Teile des Wikis gezielt zu durchsuchen bzw. anzuzeigen. Also z.b nur alle Spielebeschreibungen. Oder nur Artikel welche in der Vereinsdokumentation von einem bestimmten Autor geschrieben wurden.
Und da sie sich "updaten", macht es das einfügen neuer Information und das bauen einer Struktur die leicht zu navigieren ist, deutlich einfacher.

Es hat jedoch auch einen Nachteil. Es ist leider nicht voll-automatisch. "Dataview Serializer" kann nur die Datei neu schreiben wenn diese in Obsidian gerade geöffnet ist. Im Moment geht das - um keine zu vergessen hat jede Seite die eine solche dynamische Tabelle oder Liste enthält, einen bestimmten Tag bekommen. Somit ist es einfach durch alle durchzugehen. Sollte die Zahl dieser Seiten jedoch deutlich steigen, müsste man schauen ob man das plugin umschreibt - es ist auf github verfügbar. Würde ich jedoch gerne vermeiden....

# Tools und Sprachmodelle

Da die originalen Spiele in unterschiedlichster Formatierung und Qualität vorlagen, habe ich Sprachmodelle genutzt um die Arbeit zu vereinfachen. Dazu habe ich gezielt einen Prompt geschrieben, inklusive Beispiel formatierungen. Dieser war darauf ausgelegt keine Änderungen an dem eigentlichen Inhalt vorzunehmen (auch keine Umformulierungen wenn möglich). Trotzdem habe ich natürlich die Ergebnisse einzeln geprüft und oft auch noch kleine Änderungen per Hand gemacht.

Ich kann das nicht oft genug sagen - wenn man diese Tools auf die richtige Weise nutzt hilft das unglaublich. Man muss nur sehr genau und exakt sein, indem wie man seine Aufgaben formuliert.

Die letztlichen Änderungen sind lediglich Formatierungen. Die Art wie die Informationen und Spielbeschreibungen dargestellt werden.

Die Metadaten habe ich allerdings alle per Hand eingegeben. Da ich sowieso alles hätte doppelt checken müssen, ging das so schneller.

Trotz alledem ein langsamer Prozess. So nebenbei komme ich vieleicht auf 10-15 Spiele pro Tag... Das dauert ein bissel.

## Probleme

Ich sehe ein mögliches Problem mit Übersetzungen. Insbesondere da die Suchanfragen ja angepasst werden müssten (da sie dann ja die sprach-spezifische Variante finden soll). Das kann man händisch lösen solange es eine überschaubare Anzahl an dynamischen Seiten gibt. 
Auch hier gilt wieder - wächst das ganze muss man schauen wie man das automatisieren kann.

Übersetzung ist technisch tatsächlich ein komplexes Thema, welches ich ein anderes Mal aufgreifen werde.

# Was ist nun der Vorteil ? Warum die ganze Arbeit ?

Das System kann besser skalieren.

# Was ist sonst neu...
Die Suchfunktion hat ein paar "Upgrades" bekommen.
Sie beherrscht nun Autovervollständigung - diese zeigt, abhängig von den bereits eingegenem Text die Suchanfrage die die häufigsten Treffer erhält. Dies ist nicht abhängig von Nutzereingaben - wir tracken keine Suchanfragen oder nutzen diese um die Suche zu beeinflussen.
Der Algorithmus basiert nur auf der statischen Suchdatenbank. Diese wird bei Erstellung der Seite mittels MkDocs automatisch erzeugt.

Zudem kann man seine Anfrage (und somit die Ergebnisse) "speichern" indem man auf ein kleines Symbol auf der rechten Seite der Suchleiste klickt. Dies updated den Link im Browser. Speichert man diesen und ruft ihn erneut auf, bekommt man genau diese Suchanfrage.
Das ist eher ein kleines Gimmick - könnte aber interessant werden wenn das Wiki deutlich wächst und sehr unterschiedliche Themenbereiche abdeckt.