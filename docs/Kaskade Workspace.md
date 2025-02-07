---
created: 2025-01-21 18:09:55
update: 2025-02-07 00:39:18
publish: true
tags:
  - moc
title: Transkripte des Kaskade Magazines
description: 
authors:
  - Marc Bielert
---

>[!info]- Einleitung
>Ich bin mit der Kaskade aufgewachsen. Bevor es Youtube gab, bevor wir im Internet alles finden konnten - war dieses Magazin eines der ersten regelmäßigen Informationen die ich zum Thema Jonglieren, Zirkus, Shows in die Finger bekam.
>Als das Magazin 2013 eingestellt wurde, fühlte sich das nach dem Ende einer Era an - zumindest für mich.
>Für mehrere Jahre waren die Magazine als PDF noch zum Download erhältlich, seit ca. 2017 ist die Seite offline gegangen. 
>Ich habe mich oft an kleine Workshops, Tutorials oder Artikel erinnert die mich damals inspiriert haben. Als ich nun Jahre später etwas nachlesen wollte - gab es keine Möglichkeit mehr.
>
>Mithilfe der Wayback Machine (The Internet Archive) habe ich glücklicherweise noch einen Checkpunkt von 2017 mit den kompletten Downloads gefunden (das ist nicht immer der Fall, insbesondere da es ca. 3 GB an PDFs waren) - komplett mit Deutscher, Englischer und Französischer Ausgabe.
>
>Beim durchsehen merkte ich, das zwar eine Menge toller Artikel und Tutorials in den Magazinen versteckt waren - aber in der heutigen Zeit wohl kaum noch jemand 112 Magazine, welche lediglich photokopiert sind, durchsehen würde. Naja, ausser man hat nostalgisches Interesse =P
>
>Da es aber schade um das Wissen ist, wollte ich versuchen mithilfe aktueller Technik das ganze so zu digitalisieren, das es auch heute noch sinnvoll nutzbar ist.

>[!info]- Wie wurden die Magazine transkribiert
>Zuerst habe ich alle Seiten aus der PDF entfernt, welche keine relevanten Texte enthielten.
>
>Zum eigentlichen transkribieren (oder OCR) habe ich ein multimodales Sprachmodell von Google verwendet.
>Ich nutze ```Gemini 2.0 Pro Experimental 02-05``` mit dem Prompt 
>```
>The attached PDF is a photocopy of a magazine. Extract all text, keep the document structure intact as much as possible, also extract single images and have them correctly in context.
>```
>sowie der PDF mit dem gescanntem Magazin.
>Settings: Temperature 0.1  (Wichtig um Halluzinationen zu vermeiden)
>
>Der Output wird bereinigt mit ```gemini-2.0-flash-exp``` und folgendem Prompt (sowie dem angehängten Text den wir extrahiert haben):
>```
>The following text is extracted with OCR from an old magazin. Your task is to clean this up. Remove artifacts (like page-numbering, unneccessary linebreaks) or unneeded parts but keep the structure, articles etc. intact. Use a proper Markdown formatting to structure the text correctly.
>
>Text:
>```
>
>Das Ergebniss wird dann nochmal manuell durchgesehen und korrigiert.
>
>>[!Danger]+ Wichtig: 
>>Der Fokus war auf dem extrahieren von Artikeln, Workshops, Interviews etc. 
>>Beiträge wie z.B. Kleinanzeigen etc. habe ich verworfen.
>>Das extrahieren und säubern der Texte wurde mit LLMs durchgeführt, somit besteht immer die Möglichkeit das Texte nicht 1:1 transkribiert wurden bzw. der Inhalt leicht vom Original abweicht. Ich habe versucht die Fehlerquote so gering wie möglich zu halten indem ich stichprobenartig Textstellen verglichen habe. 

[[Kaskade 001]]
[[Kaskade 002]]
[[Kaskade 003]]
[[Kaskade 004]]
[[Kaskade 005]]

---

# Falsch benannte / zusammengefasste Ausgaben (002 - 004)

Kaskade 002:
Im deutschen Original PDF sind die Ausgaben 2+3 zusammen. 

Kaskade 003: 
Im deutschen Original PDF ist hier die Ausgabe 004 zu finden

Kaskade 004:
Hier fehlt das Titelblatt, ich konnte noch nicht herausbekommen zu was das gehört...
Es sieht aus wie eine Kopie von Ausgabe 009, ohne Titelblatt

Fix:
Ich habe die PDF von Kaskade 002 (original) geteilt in 002 und 003.
Kaskade 003 (original) in Kaskade 004 umbenannt.
Sowie Kaskade 004(Original) gelöscht.