---
created: 2025-01-21 18:09:55
update: 2025-02-25 04:22:03
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki und mehr - meine Motivation für dieses Projekt
description: 
authors:
  - Marc Bielert
---

Warum ich dieses Projekt starte, welche Ideen und Überlegungen dahinter stecken und wo die Reise eventuell hingehen kann - all das möchte ich gerne ein wenig erläutern.

2013 habe ich als Projektleiter in einem Kinder und Jugendzirkus gearbeitet. Oft kamen Trainer:innen zu mir und fragten ob ich noch andere Spiele kenne, oder andere Methoden, oder Tricks etc.
Ich hatte selber zu diesem Zeitpunkt zwar viele Ressourcen (Bücher, Magazine, Mitschriften von Weiterbildungen) - aber alles ungeordnet und kaum digitalisiert.

<!-- more -->

Ein erster Versuch dies für die Trainer:innen zugänglich zu machen, war ein klassisches Wiki. 
Viele Spielebeschreibungen stammen ursprünglich aus dieser Zeit. 
Gleichzeitig fing ich an, meine Quellen zu digitalisieren. Ich lernte das "Zettelkasten" Prinzip von Niklas Luhmann kennen und versuchte meine Daten nach diesen Prinzipien zu organisieren.

Das Wiki war ein Misserfolg - es gab kaum Interaktion, die Trainer:innen nutzten es ein paar Mal und es geriet schnell in Vergessenheit.
Mein privater Zettelkasten fing jedoch an zu wachsen. Während ich anfangs noch mit spezieller Software arbeitete, fing ich später an mir zunehmend Gedanken zu machen wie ich diese, immer wertvoller werdende, Sammlung zukunftssicher gestalten kann.

Und was meint das eigentlich?
Der erste Moment war, als ich merkte das die Software die ich nutzte nicht länger weiter entwickelt wurde.
Ich musste also eine neue Software finden - und meine Daten in diese neue Software "reinbekommen".
An diesem Punkt lernte ich Markdown kennen. Ein sehr einfaches Dateiformat - ähnlich einer simplen Textdatei - welches darauf ausgelegt war, unabhängig von einer speziellen Software zu funktionieren. Oder anders gesagt - ein Standard der weit verbreitet ist, und mit einfachsten Mitteln gelesen und bearbeitet werden kann.

Das Format unterstütze alles was ich brauchte - einfache Textformatierung, Verlinkungen und Tags sowie Metadaten (z.b. Titel, Autor, Beschreibung etc...)

Ich fand eine neue Software welche dieses Format nutzte - und konnte meinen Zettelkasten weiterführen. Zu diesem Zeitpunkt hatte ich in etwa 600 Notizen (oder Dateien / Seiten ).
Später wechselte ich noch einmal die Software, was reibungslos funktionierte.

>[!info]
>Ein wichtiger Punkt für zukunftssicherheit ist somit ein einfaches, weitverbreites Datenformat, welches unabhängig von bestimmter Software funktioniert.

## Zusammenarbeit und Verbreitung

Mein erster Versuch eines Wiki´s hat nicht funktioniert - unter anderem weil ich es nicht geschafft habe andere dafür zu begeistern und zum mitmachen anzuregen.
Mein persönlicher Zettelkasten ist über die Jahre zu mittlerweile über 3000 Notizen angewachsen, vieles davon zu den Themen Zirkuspädagogik, Spiele, Jonglage und ähnliches.

Eine zeitlang habe ich dies einfach online zugänglich gemacht - aber bis auf einige wenige Personen die davon wussten und vereinzelt nach Spielbeschreibungen geschaut haben - ist keine weitere Zusammenarbeit oder Verbreitung passiert.

Nun, ca. 12 Jahre nachdem ich meinen eigenen Zettelkasten gestartet habe - möchte ich dies erneut versuchen.
Eine gemeinsam genutzte und gemeinsam mit Inhalten gefüllte Wissensdatenbank zu dem groben Themenbereichen Zirkus- und Bewegungspädagogik, Zirkus & Kunst und darüber hinaus.

Wichtige Aspekte und Fragen
- unabhängigkeit von bestimmten Systemen
- möglichst einfaches, leichtverständliches Datenformat
- Nutzen und Zielgruppe
- strukturierte Daten

Eine Wikisoftware kam nicht in Frage (ebensowenig wie Wordpress oder andere Content-Management Systeme) - da dies eine abhängigkeit von einem einzelnen System darstellt. Das kann kurz- und mittelfristig gutgehen - langfristig ist das jedoch eine klare Schwäche.

Ein anderes Konzept ist es die Daten (als Markdown und Bilddateien) unabhängig von der letztendlichen Darstellung zu verwalten / bearbeiten (und aufgrund offener Dateiformate keine spezifische Software zu brauchen) - und die Darstellung mit anderer Software umzusetzen.
Somit ist gewährleistet, das auch in 20 Jahren die Daten nutzbar bleiben. Die Art der Darstellung und Bearbeitung mag sich drastisch ändern, aber die zugrundeliegenden Daten bleiben die gleichen.

Es gibt nun verschiedenste Möglichkeiten die Daten darzustellen. Wir können sie als Webseite umsetzen, als eBook oder PDF drucken, eine App erstellen welche diese Daten anzeigt. 
Sie können einfach als ZIP oder RAR Datei gepackt werden und offline mit einem Texteditor gelesen und geändert werden.

Möchte man das ganze als Wordpress oder Wiki darstellen, ist auch das nur eine Frage des importierens - da die Daten strukturiert und einfach lesbar sind, ist es (mit entsprechenden Kenntnissen) relativ unproblematisch dies umzusetzen.

## Meine aktuelle Lösung für die Webseite

Ich nutze MkDocs sowie MkDocs-Materials (Theme) um die Daten als statische Webseite zu generieren.
Es gibt eine Vielzahl an Programme welche aus Markdown Dateien statische Html Dateien erzeugen, MkDocs ist spezialisiert auf die Darstellung von Dokumentationen. Viele Funktionen die auf der statischen Webseite erzeugt werden helfen dabei (Volltextsuche, Navigation etc.).
Zudem ist MkDocs eine weitverbreitete und vielgenutze Open-Source Lösung, welche von großen Firmen genutzt und finanziell unterstützt wird. Dies sichert zumindest mittelfristig eine funktierende Software.

## Zusammenarbeit

