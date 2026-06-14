---
lang: it
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Giochi - Il Lato dei Dati
description: Come le descrizioni dei giochi sono state standardizzate e rese più dinamiche utilizzando metadati e plugin di Obsidian.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:00:38+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:55+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Giochi - Il Lato dei Dati**
**Come le descrizioni dei giochi sono state standardizzate e rese più dinamiche utilizzando metadati e plugin di Obsidian.**

Quando si tratta di gestire i contenuti, la coerenza è fondamentale. Per la prima sezione principale di questo progetto, mi sono occupato dei giochi, circa 170, ognuno con il proprio formato, stile e accessibilità unici. Il problema? Molte di queste descrizioni si basavano su collegamenti statici e codificati, rendendo un incubo aggiungere nuovi giochi o modificare la struttura.

Così, mi sono rimboccato le maniche e mi sono messo al lavoro.
<!-- more -->
## Fase 1: Un Formato Unificato
La prima cosa da fare è stata stabilire un formato coerente per tutte le descrizioni dei giochi. Ho tratto ispirazione dal "Tasifan Spielebuch" (Libro dei Giochi Tasifan), una risorsa ben organizzata per le descrizioni dei giochi. Per rendere le cose ancora più facili da usare, ho aggiunto brevi riassunti in modo che tutti i dettagli essenziali siano visibili a colpo d'occhio, anche in un'anteprima.

Ma il vero punto di svolta? I metadati.

## Fase 2: Magia dei Metadati
Ora, tutte le informazioni chiave – numero di partecipanti, materiali, durata e altro ancora – sono memorizzate come metadati nella parte superiore di ogni file Markdown in un formato chiamato YAML (o frontmatter). Questo non solo mantiene le cose organizzate, ma rende anche i dati riutilizzabili in tutto il sistema.

Per facilitare la ricerca del gioco giusto, ho implementato una logica semplice ma efficace:
1. **Scegli una categoria**: Che tipo di gioco stai cercando? Un gioco di defaticamento? Un gioco a inseguimento? Qualcosa per il team-building? Ho creato un set di categorie per iniziare, ma queste possono essere modificate o espanse secondo necessità.
2. **Sfoglia la tabella**: Una volta scelta una categoria, vedrai una tabella che elenca tutti i giochi che vi rientrano. La tabella è ordinabile: basta fare clic sulle intestazioni per organizzare per durata, difficoltà o altri criteri.

E il bello è che molti giochi compaiono in più categorie, quindi non sei mai limitato a un solo modo per trovare ciò di cui hai bisogno.

## Tabelle Non Proprio Dinamiche
La vera magia avviene con due plugin di Obsidian: **Dataview** e **Dataview Serializer**.

Dataview mi permette di creare elenchi e tabelle dinamiche utilizzando query simili a quelle di un database. Il problema? Queste tabelle funzionano solo all'interno di Obsidian perché i file Markdown sottostanti non vengono modificati.

Entra in gioco Dataview Serializer. Questo plugin converte quelle tabelle dinamiche in formato Markdown statico e le scrive direttamente nel file. Quando il sito viene creato utilizzando MkDocs, le tabelle sono statiche ma sono state essenzialmente generate dinamicamente offline.

Queste query possono diventare piuttosto complesse, permettendomi di cercare o visualizzare parti specifiche del wiki, come tutte le descrizioni dei giochi o gli articoli scritti da un autore specifico. E poiché si aggiornano automaticamente (tramite il passaggio del serializzatore), aggiungere nuove informazioni e costruire una struttura navigabile è un gioco da ragazzi.

Ma non è tutto rose e fiori. Il processo non è completamente automatico. Dataview Serializer può riscrivere un file solo se è aperto in Obsidian. Per ora, questo è gestibile: ho etichettato ogni pagina con una tabella o un elenco dinamico, rendendo facile scorrerle. Ma se il numero di queste pagine dovesse aumentare in modo significativo, potrei dover ripensare l'approccio.

## Strumenti e Modelli Linguistici
Le descrizioni originali dei giochi erano un miscuglio in termini di formattazione e qualità. Per semplificare il processo, mi sono rivolto ai modelli linguistici (LLM). Ho creato un prompt specifico, completo di esempi di formattazione, per garantire che il contenuto stesso non venisse alterato (nessuna riscrittura non necessaria). Tuttavia, ho esaminato manualmente ogni risultato e apportato piccole modifiche dove necessario.

Ecco il punto chiave: se usati correttamente, questi strumenti sono *incredibilmente* potenti. La chiave è essere precisi e intenzionali nel modo in cui si inquadrano i propri compiti.

Le modifiche finali riguardano principalmente la formattazione: come vengono presentate le informazioni e le descrizioni dei giochi. I metadati, tuttavia, sono stati tutti inseriti manualmente. Poiché ho dovuto ricontrollare tutto comunque, farlo a mano è stato più veloce in questo caso.

È un processo lento, però. Lavorandoci part-time, riesco a gestire circa 10-15 giochi al giorno. Il progresso è costante, ma ci vorrà un po'.

## Sfide Future
Un potenziale ostacolo sono le traduzioni. Le query di ricerca dovrebbero essere adattate per trovare versioni specifiche per lingua dei giochi o dei tag. Per ora, questo può essere gestito manualmente, ma se il sistema crescesse, potrebbe essere necessaria l'automazione.

La traduzione è un argomento complesso e ne parlerò più approfonditamente in un'altra occasione.

## Perché Disturbarsi?
La risposta breve? Scalabilità.

Questo sistema è progettato per crescere. Standardizzando il formato, sfruttando i metadati e utilizzando strumenti dinamici, ho creato una base che può gestire più contenuti senza diventare ingombrante.

## Cos'altro c'è di Nuovo?
La funzione di ricerca ha ricevuto alcuni aggiornamenti:
- **Completamento automatico**: Mentre digiti, la ricerca suggerisce query che producono il maggior numero di risultati. Questo non si basa sul comportamento dell'utente – non tracciamo le ricerche – ma sull'indice di ricerca statico generato quando il sito viene creato.
- **Ricerche salvate**: Fai clic su una piccola icona accanto alla barra di ricerca e la tua query (e i risultati) vengono salvati nell'URL. Aggiungilo ai preferiti e otterrai sempre gli stessi risultati.

È una piccola funzionalità, ma potrebbe diventare incredibilmente utile man mano che il wiki cresce e copre argomenti più diversi.
