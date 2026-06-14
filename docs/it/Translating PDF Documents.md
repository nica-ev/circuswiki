---
lang: it
translation_id: translating-pdf-documents
created: 2025-05-03 21:32:10
update: 2025-05-03 22:24:12
publish: true
tags:
  - tutorial
title: Traduzione di documenti PDF tramite modelli linguistici di grandi dimensioni
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Translating PDF Documents.md
translation_source_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-14T19:33:26+00:00
translation_source_body_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_source_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T19:33:26+00:00
translation_source_localized_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_source_structural_metadata_hash: 2b0fe62dfc02049e3f55e308c77f83a911789c48b0827769d60d3f00737d38b6
---
# Tutorial: Tradurre Documenti PDF Utilizzando Grandi Modelli Linguistici

## Introduzione

Questo tutorial delinea un processo per tradurre il contenuto di documenti PDF, in particolare quelli contenenti testo basato su immagini non selezionabile, utilizzando Grandi Modelli Linguistici (LLM). Il flusso di lavoro prevede l'ottimizzazione del PDF, l'estrazione del testo tramite Riconoscimento Ottico dei Caratteri (OCR), la traduzione del testo e, infine, la riformattazione della traduzione in un PDF.

**Prerequisiti:**

*   Un account Google (per accedere a Google AI Studio).
*   Opzionale: Software di ottimizzazione PDF (ad es. pdf24 Creator).
*   Opzionale: Un editor di testo o un elaboratore di testi in grado di gestire Markdown ed esportare in PDF (ad es. Obsidian, Microsoft Word).

## Fase 1: Preparazione del Documento PDF

**Obiettivo:** Ridurre le dimensioni del file PDF per ottimizzarlo per l'elaborazione da parte dell'LLM, mantenendo al contempo la leggibilità del testo. Gli LLM hanno spesso limiti di dimensione dell'input e i file più piccoli vengono elaborati in modo più efficiente.

**Considerazioni:**

*   **PDF basati su testo:** Se il testo all'interno del PDF è selezionabile (significa che è incorporato elettronicamente), la riduzione delle dimensioni del file è generalmente più semplice e può raggiungere dimensioni inferiori senza perdita di qualità.
*   **PDF basati su immagini:** Se le pagine del PDF sono immagini di testo (il testo non può essere selezionato singolarmente), la riduzione delle dimensioni comporta la compressione delle immagini. È necessario prestare attenzione a non ridurre la qualità al punto che il testo diventi illeggibile per l'OCR.

**Procedura (Esempio con pdf24):**

1.  Apri il tuo documento PDF in uno strumento come pdf24 Creator ([https://www.pdf24.org/](https://www.pdf24.org/)).
2.  Utilizza le funzionalità di compressione o riduzione delle dimensioni. Impostazioni efficaci comuni includono:
    *   Abilitazione dell'ottimizzazione per il web.
    *   Conversione dei colori in scala di grigi.
3.  Sperimenta con i livelli di compressione, puntando a una dimensione del file inferiore a **5 MB**, assicurandoti che il testo rimanga chiaro e leggibile.
4.  Salva il file PDF ottimizzato.

## Fase 2: Estrazione del Testo tramite Google AI Studio (Trascrizione/OCR)

**Obiettivo:** Utilizzare le capacità multimodali di un LLM per eseguire l'OCR sul PDF preparato ed estrarre il contenuto testuale in un formato strutturato.

**Procedura:**

1.  Naviga su **Google AI Studio** ([https://aistudio.google.com/](https://aistudio.google.com/)) ed effettua l'accesso con il tuo account Google. Nota: AI Studio è principalmente uno strumento per sperimentare con modelli e prompt.
2.  Avvia una nuova sessione o chat.
3.  Allega il file PDF ottimizzato alla tua sessione (ad es. utilizzando il pulsante di allegato o trascinando e rilasciando).
4.  Inserisci il seguente prompt nell'area del messaggio utente:
    ```
    Per favore, trascrivi il PDF allegato. Contiene immagini con testo, che richiedono l'OCR. Emetti la trascrizione in formato Markdown corretto, utilizzando intestazioni ed elenchi per creare una struttura che imiti da vicino il layout del documento originale.
    ```
5.  Configura le impostazioni del modello:
    *   Mantieni le impostazioni predefinite a meno che tu non abbia requisiti specifici.
    *   Imposta la **Temperatura** su **0.1**. Una temperatura più bassa incoraggia un output più deterministico e meno creativo, adatto per una trascrizione accurata.
6.  Invia il prompt. Il processo di trascrizione potrebbe richiedere diversi minuti (potenzialmente 4-6 minuti o più, a seconda delle dimensioni e della complessità del PDF).
7.  Una volta completata la generazione, copia il testo Markdown risultante.
    *   *Metodo 1:* Utilizza l'opzione di copia spesso fornita all'interno dell'interfaccia (ad es. tramite un menu associato alla risposta).
    *   *Metodo 2:* Seleziona manualmente tutto il testo generato e copialo (Ctrl+C o clic destro -> Copia).
8.  Incolla il testo Markdown copiato in un editor di testo semplice (come Blocco note, VS Code, Obsidian, ecc.).
9.  Salva questo contenuto come file di testo semplice. Si consiglia di utilizzare le estensioni `.txt` o `.md` (Markdown). La formattazione Markdown aiuta a preservare la struttura del documento (intestazioni, elenchi).

![Google AI Studio - Screenshot Trascrizione](../img/Screenshot-Google-AiStudio-Transcription.png){ width=600 }

## Fase 3: Traduzione del Testo Estratto tramite Google AI Studio

**Obiettivo:** Tradurre il testo Markdown estratto nella lingua di destinazione desiderata, preservando la struttura e la formattazione originali.

**Procedura:**

1.  In **Google AI Studio**, avvia una **nuova chat** per garantire un contesto fresco per l'attività di traduzione.
2.  Allega il file `.txt` o `.md` salvato contenente il testo Markdown estratto.
3.  Inserisci un prompt di traduzione, specificando le lingue di origine e di destinazione. Esempio da inglese a italiano:
    ```
    Per favore, traduci il file Markdown allegato (inglese) in italiano. Mantieni precisamente la struttura, la formattazione, il tono e lo stile di conversazione originali.
    ```
    *   **Modifica il prompt** in base alle tue lingue di origine e di destinazione specifiche (ad es. "...traduci il file Markdown allegato (tedesco) in spagnolo..."). La qualità della traduzione può variare a seconda della coppia linguistica.
4.  Configura le impostazioni del modello:
    *   Assicurati che le impostazioni predefinite siano appropriate.
    *   Imposta la **Temperatura** su **0.1** per promuovere la fedeltà al testo e alla struttura di origine durante la traduzione.
5.  Invia il prompt. Anche la traduzione potrebbe richiedere diversi minuti, paragonabile al tempo di trascrizione.
6.  Una volta generato, copia il testo Markdown tradotto utilizzando i metodi descritti nella Fase 2 (pulsante di copia nell'interfaccia o selezione manuale).

![Google AI Studio - Screenshot Traduzione](../img/Screenshot-Google-AiStudio-Translation.png){ width=600 }

## Fase 4: Riformattazione del Testo Tradotto in un Documento PDF

**Obiettivo:** Convertire il testo Markdown tradotto nuovamente in un documento PDF per la condivisione o l'archiviazione.

**Procedura:**

1.  Incolla il testo Markdown tradotto copiato in un'applicazione adatta.
2.  **Consigliato:** Utilizza un editor di testo o un elaboratore di testi che comprenda la formattazione Markdown per preservare la struttura (intestazioni, elenchi, ecc.).
    *   **Obsidian** ([https://obsidian.md/](https://obsidian.md/)) è uno strumento gratuito che funziona bene con i file Markdown e spesso dispone di funzionalità di esportazione PDF (direttamente o tramite plugin).
    *   I moderni elaboratori di testi (come Microsoft Word) possono anche importare o incollare Markdown e consentire il salvataggio/esportazione come PDF, sebbene la fedeltà della formattazione possa variare.
    *   Sono disponibili anche convertitori dedicati da Markdown a PDF online o come software installabile.
3.  Utilizza la funzione "Esporta in PDF" o "Salva con nome PDF" dell'applicazione.
4.  Rivedi il PDF risultante per assicurarti che la formattazione e il contenuto appaiano come previsto.

## Conclusione

Questo tutorial ha dimostrato un flusso di lavoro per sfruttare Google AI Studio per trascrivere e tradurre documenti PDF, inclusi quelli che richiedono l'OCR. Preparando il PDF, estraendo il testo utilizzando un LLM configurato, traducendo il risultato e riformattandolo, gli utenti possono ottenere versioni tradotte dei propri documenti. Sebbene questo metodo offra una soluzione gratuita o a basso costo, gli utenti dovrebbero essere consapevoli delle potenziali variazioni nell'accuratezza dell'OCR e nella qualità della traduzione, in particolare per layout complessi o lingue meno comuni. I tempi di elaborazione dipendono in modo significativo dalle dimensioni del documento e dal carico del server.
