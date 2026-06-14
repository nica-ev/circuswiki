---
lang: it
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki e Oltre
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
translation_updated: 2026-06-06T22:58:26+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:10+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki e Oltre**  
**Perché ho avviato questo progetto, le idee alla base e dove potrebbe portare.**

Nel 2013, lavoravo come project manager per un circo giovanile. I formatori venivano spesso da me chiedendomi se conoscessi altri giochi, metodi o trucchi. All'epoca, avevo un sacco di risorse a disposizione: libri, riviste, appunti da workshop, ma tutto era disorganizzato e a malapena digitalizzato.  
<!-- more -->
Il mio primo tentativo di rendere queste risorse accessibili ai formatori fu un classico wiki. Molte delle descrizioni dei giochi che vedete oggi sono nate in quel periodo. Contemporaneamente, ho iniziato a digitalizzare le mie fonti. Ho scoperto il metodo *Zettelkasten* (scatola per schede) di Niklas Luhmann e ho iniziato a organizzare i miei dati secondo i suoi principi.  

Il wiki fu un fallimento. C'era poca interazione; i formatori lo usarono un paio di volte e fu presto dimenticato. Il mio Zettelkasten personale, tuttavia, iniziò a crescere. Sebbene inizialmente utilizzassi software specializzato, presto iniziai a pensare a come rendere a prova di futuro questa collezione sempre più preziosa.  

Cosa significa? Il primo campanello d'allarme arrivò quando mi resi conto che il software che stavo usando non era più in fase di sviluppo. Dovetti trovare un nuovo software e capire come migrare i miei dati al suo interno. Fu allora che scoprii Markdown.  

Markdown è un formato di file semplice, essenzialmente un file di testo semplice, progettato per funzionare indipendentemente da qualsiasi software specifico. In altre parole, è uno standard ampiamente adottato che può essere letto e modificato con gli strumenti più basilari.  

Il formato supportava tutto ciò di cui avevo bisogno: formattazione di base del testo, collegamenti, tag e metadati (ad esempio, titolo, autore, descrizione, ecc.). Ho trovato un nuovo software che utilizzava Markdown e ho continuato a costruire il mio Zettelkasten. A quel punto, avevo circa 600 note (o file/pagine). Successivamente, ho cambiato di nuovo software e la transizione è stata fluida.  

>[!info]  Concetto chiave
>Rendere i propri dati a prova di futuro significa utilizzare un formato semplice, ampiamente adottato e indipendente da software specifici.  

## Collaborazione e Condivisione  

Il mio primo tentativo di wiki non funzionò, in parte perché non riuscii a ispirare gli altri a contribuire. Nel corso degli anni, il mio Zettelkasten personale è cresciuto fino a oltre 3.000 note, molte delle quali su argomenti come pedagogia circense, giochi, giocoleria e altro ancora.  

Per un po', l'ho semplicemente reso accessibile online, ma al di là di poche persone che ne erano a conoscenza e che occasionalmente cercavano descrizioni di giochi, non c'era una vera collaborazione o condivisione più ampia.  

Ora, circa 12 anni dopo aver iniziato il mio Zettelkasten, ci riprovo. L'obiettivo è creare una base di conoscenza condivisa per argomenti come la pedagogia circense e del movimento, le arti circensi e oltre.  

### Considerazioni e Domande Chiave  
- **Indipendenza da sistemi specifici**  
- **Formato dati semplice e di facile comprensione**  
- **Utilità e pubblico di riferimento**  
- **Dati strutturati**  

Il software wiki tradizionale (o piattaforme come WordPress) erano fuori questione perché creano dipendenza da un unico sistema. Sebbene questo possa funzionare nel breve o medio termine, è una chiara debolezza a lungo termine.  

Invece, gestisco i dati (come file Markdown e immagini) indipendentemente da come vengono presentati. Ciò garantisce che, anche tra 20 anni, i dati rimangano utilizzabili. Il modo in cui vengono visualizzati o modificati potrebbe cambiare drasticamente, ma i dati sottostanti rimangono gli stessi.  

Ci sono innumerevoli modi per presentare i dati: come sito web, eBook, PDF o persino un'app. Può essere compresso in un file e letto o modificato offline con un semplice editor di testo. Se si desidera visualizzarlo come sito WordPress o wiki, si tratta solo di importare i dati, poiché sono strutturati e facili da leggere, è relativamente semplice da implementare (con il know-how giusto).  

## La Mia Soluzione Attuale per il Sito Web  

Sto utilizzando MkDocs e il tema MkDocs-Material per generare un sito web statico. Esistono molti programmi che creano file HTML statici da Markdown, ma MkDocs è specificamente progettato per la documentazione. Molte delle funzionalità che genera, come la ricerca full-text e la navigazione, sono incredibilmente utili.  

MkDocs è anche una soluzione open-source ampiamente utilizzata e supportata da grandi aziende, il che garantisce che rimarrà funzionale almeno nel medio termine.  

## Collaborazione  

Il passo successivo è renderlo uno sforzo collaborativo. Sto esplorando modi per invitare altri a contribuire, sia aggiungendo nuovi contenuti, perfezionando le voci esistenti o suggerendo miglioramenti. L'obiettivo è creare una risorsa viva ed evolutiva che benefici della conoscenza e dell'esperienza collettiva.
