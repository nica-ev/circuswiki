---
lang: it
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Sistema di documentazione
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:00:37+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:08+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifesto](doc-sys-manifest.md){ .md-button }
[Configurazione Obsidian](Obsidian%20Setup.md){ .md-button }
## Architettura di Sistema

L'idea generale
> [!info] Panoramica dell'architettura
>
> Qui è presente una rappresentazione grafica dell'architettura di sistema:
>```mermaid
>flowchart LR
>A(Contenuti) --> B(Controllo versione)
>C(Software di editing) --> A
>A --> D(Rendere accessibile online)
>```

Nel dettaglio:

> [!info] Panoramica dell'architettura
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{File}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Tema: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Un editor di testo opzionale, ma da me consigliato, per l'editing di file Markdown.
> *   **File:** I file Markdown che contengono il contenuto della mia documentazione.
> *   **Github Desktop:** Uno strumento per la gestione semplice dei miei repository Git.
> *   **Github:** Un servizio online per il controllo versione e la collaborazione.
> *   **Github Pages:** Un servizio gratuito per la pubblicazione del mio sito web.
> *   **MkDocs:** Uno strumento per la creazione automatica del sito web a partire dai miei file Markdown.
> *   **MkDocs-Material:** Un tema per MkDocs che offre un layout moderno e accattivante.
> *   **MkDocs-Publisher**: Una raccolta di plugin che semplifica la collaborazione con Obsidian e offre funzionalità aggiuntive.

## Componenti nel dettaglio

### 1. Markdown

> [!info] Markdown come base
> Utilizzo il [formato Markdown](Markdown.md) per la mia documentazione. Markdown è un linguaggio di markup semplice che mi permette di formattare il testo con semplici formattazioni (ad esempio, titoli, elenchi, link).

**Vantaggi:**

*   È facile da imparare e utilizzare, il che mi permette di concentrarmi sul contenuto.
*   È indipendente dalla piattaforma, quindi posso continuare il mio lavoro su qualsiasi dispositivo.
*   È ideale per il controllo versione, il che mi consente di tracciare e gestire le modifiche.
*   È a prova di futuro e non proprietario, il che mi dà la certezza che il mio lavoro rimarrà accessibile a lungo termine.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian come editor di testo
> [Obsidian](Obsidian%20Setup.md) è un editor di testo opzionale, ma da me consigliato. Mi offre i seguenti vantaggi:

*   Posso salvare i miei dati localmente e modificarli offline, il che mi dà flessibilità e controllo.
*   Posso collegare facilmente i file tra loro, il che mi aiuta a organizzare informazioni complesse.
*   Posso taggare i file e gestirli facilmente, il che mi offre una dimensione aggiuntiva di organizzazione.
*   Posso visualizzare i miei dati graficamente, il che mi aiuta a riconoscere schemi e relazioni.
*   Posso estendere la funzionalità di Obsidian tramite plugin, il che mi permette di adattare lo strumento alle mie esigenze specifiche.

### 3. Git e Github

> [!info] Git per il controllo versione
> [Git](https://git-scm.com/) è un sistema di controllo versione che mi permette di tracciare e gestire le modifiche alla documentazione. [Github](https://github.com/) è un servizio online che mi permette di archiviare i miei repository Git e collaborare con altri.

**Vantaggi:**

*   Controllo versione: Ogni modifica viene documentata e può essere tracciata in qualsiasi momento, il che mi aiuta a evitare errori e a mantenere una visione d'insieme.
*   Collaborazione: Più persone possono lavorare contemporaneamente alla documentazione, il che mi dà la possibilità di integrare feedback e contributi da altri.
*   Backup: La mia documentazione è sicura e viene regolarmente sottoposta a backup, il che mi dà la certezza che il mio lavoro non andrà perso.

### 4. Github Desktop

> [!info] Github Desktop come strumento
> [Github Desktop](../_inbox/Github%20Desktop.md) è un'interfaccia grafica per Git che mi permette di utilizzare Git in modo semplice e senza riga di comando.

**Vantaggi:**

*   Facilità d'uso, il che mi semplifica l'utilizzo di Git.
*   Non sono necessarie conoscenze della riga di comando, il che mi fa risparmiare tempo e fatica.
*   Semplifica il mio flusso di lavoro, il che mi permette di concentrarmi sulla creazione di contenuti.

### 5. MkDocs

> [!info] MkDocs come generatore di siti web
> [MkDocs](https://mkdocs.org) è un generatore di siti statici che converte i miei file Markdown in un sito web statico.

**Vantaggi:**

*   Creazione di siti web semplice, il che mi permette di pubblicare la mia documentazione in modo rapido e semplice.
*   Aggiornamento rapido, il che mi permette di vedere le modifiche in tempo reale.
*   Layout coerente, il che garantisce una presentazione professionale e uniforme della mia documentazione.
*   Anteprima offline, il che mi permette di controllare la mia documentazione prima di pubblicarla.

### 6. Github Pages

> [!info] Github Pages per l'hosting
> [Github Pages](../_inbox/Github%20Pages.md) è un servizio di hosting gratuito di Github che mi permette di pubblicare facilmente il mio sito web online.

**Vantaggi:**

*   Hosting gratuito, il che mi permette di pubblicare la mia documentazione senza costi aggiuntivi.
*   Pubblicazione semplice, il che mi solleva dall'implementazione tecnica della pubblicazione.
*   Affidabile, il che mi dà la certezza che la mia documentazione sarà sempre disponibile.

### 7. MkDocs-Material

> [!info] MkDocs-Material come tema
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) è un tema per MkDocs che offre un layout moderno e accattivante.

**Vantaggi:**

*   Design moderno, il che fa apparire la mia documentazione professionale e attuale.
*   Personalizzabile, il che mi permette di adattare il layout alle mie esigenze specifiche.
*   Facile da usare, il che mi semplifica l'utilizzo della documentazione.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher come raccolta di plugin
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) è una raccolta di plugin MkDocs che semplifica la collaborazione con Obsidian e offre funzionalità aggiuntive.

**Vantaggi:**

- **Integrazione semplificata con Obsidian:** Adattamento automatico della sintassi Markdown di Obsidian (Callouts, Wikilinks, ecc.).
- **Metadati estesi:** Integrazione di tag e categorie dal frontmatter di Obsidian.

## Flusso di lavoro

> [!info] Il mio flusso di lavoro
> Ecco il mio tipico flusso di lavoro:

1.  Creo e modifico file Markdown con un editor di testo (opzionalmente Obsidian).
2.  Salvo i file Markdown localmente.
3.  Trasferisco le mie modifiche al repository Git con Github Desktop.
4.  Faccio creare automaticamente il sito web con MkDocs.
5.  Pubblico il sito web con Github Pages.

## File system

> [!info] Struttura delle directory
> Ecco la struttura delle directory del mio sistema:
>
> ```
>/docs/     (Qui si trovano i miei file Markdown)
>/site/     (Qui viene generato il sito web)
>license    (Informazioni sulla licenza)
>mkdocs.yml (File di configurazione per MkDocs)
>readme.md  (File per la descrizione del repository)
>```

## Alternative per la creazione di contenuti

> [!info] Alternative per la creazione di contenuti
> Sono consapevole che non tutti hanno familiarità con Markdown e Git. Pertanto, offro le seguenti alternative:

1.  **Wordpress:** I contenuti possono essere creati in Wordpress come pagina.
2.  **File di testo, file Word:** I contenuti possono essere creati come file di testo, file Word (o in altri formati tipici).

In questi casi, posso quindi integrare i contenuti nel sistema.
