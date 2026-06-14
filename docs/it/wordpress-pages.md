---
lang: it
translation_id: wordpress-pages
publish: true
tags:
  - wordpress
  - tutorial
created: 2025-01-18 21:15:11
update: 2025-01-23 05:46:07
title: Creare una nuova pagina in WordPress
authors:
  - Piiit
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/wordpress-pages.md
translation_source_hash: 172db702654e913f2b641fffd126e0ccdbae876825b67644c7eb14cb3a45b2b6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:09:56+00:00
translation_source_body_hash: 172db702654e913f2b641fffd126e0ccdbae876825b67644c7eb14cb3a45b2b6
translation_source_metadata_hash: abe64f9a224d064ced886f7fb6f6a055b7f6f2ca648d71f5e6feca6b810e6ced
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:21+00:00
translation_source_localized_metadata_hash: abe64f9a224d064ced886f7fb6f6a055b7f6f2ca648d71f5e6feca6b810e6ced
translation_source_structural_metadata_hash: ef2e4594352bb749c96a5083d87bed9f90ad8c5c465e07a187a59612104255b6
---
# Creare una nuova pagina in WordPress

Ti consigliamo di guardare questo tutorial direttamente in WordPress (ovviamente avrai bisogno di un accesso; se non ne hai uno, puoi leggere il tutorial qui)

[Guarda direttamente in WordPress](https://nica.network/kurzanleitung){ .md-button }

---

### Creare contenuti

Una pagina è composta da **singoli blocchi**. Questo, ad esempio, è un blocco "Paragrafo", mentre il blocco sopra è un blocco "Intestazione".

Nuovi blocchi possono essere creati tramite i pulsanti "+". Sia quello blu in alto a sinistra, sia quando si passa il mouse tra due blocchi, sia scrivendo "/" nella nuova riga dopo aver premuto "Invio".

## Intestazione 1

## Intestazione 2

### Intestazione 3

L'Intestazione 1 (H1) è il **titolo della pagina** e dovrebbe essere utilizzata una sola volta nella pagina. Qui c'è una piccola particolarità. Il titolo della pagina (con la sfumatura di colore) non viene visualizzato di default sul sito pubblicato. Se lo desideri, devi inserire il **blocco "Titolo"** nella tua pagina, in modo che venga visualizzato due volte in modalità di modifica.

Per impostare la **gerarchia delle intestazioni**, fai clic su "H2" nel menu dei blocchi e poi seleziona dall'elenco, vedi immagine.

![](https://nica.network/wp-content/uploads/2025/01/grafik-1024x573.png)

## Inserire riquadri di sfondo

Affinché il contenuto non venga visualizzato direttamente sull'immagine di sfondo colorata del sito, dobbiamo **raggruppare tutti i blocchi in un gruppo e dare a questo un colore di sfondo**.

1. Aprire la **visualizzazione elenco** e selezionare tutti gli elementi e raggrupparli (tramite i 3 punti o "Ctrl + G"). Assicurarsi che alla fine sia selezionato il **gruppo**.
    La visualizzazione elenco è generalmente molto utile per avere una panoramica, soprattutto quando i blocchi sono annidati.
2. Aprire le **Impostazioni**. Qui ci sono opzioni di impostazione per l'intera pagina o per il blocco selezionato. A noi serve quest'ultimo.
3. Nelle impostazioni del blocco, selezionare la scheda **"Stile"**.
4. Selezionare **Sfondo**.
5. Nero e bianco alla fine della palette di colori hanno lo sfondo leggermente trasparente tipico del sito.

![](https://nica.network/wp-content/uploads/2025/01/grafik-1-1024x494.png)

## Design

**Colori del testo, spaziatura ed effetti speciali** possono essere regolati anche tramite le impostazioni del blocco. Ci sono due punti di riferimento qui.

### Barra degli strumenti

1. Seleziona il blocco genitore
2. Mostra l'icona del blocco corrente. Qui è possibile cambiare anche il tipo di blocco (ad es. da Paragrafo a Intestazione)
3. Spostamento del blocco
4. Ora ci sono opzioni specifiche del blocco come **allineamento del testo, collegamenti, grassetto...**

![](https://nica.network/wp-content/uploads/2025/01/grafik-2-1024x749.png)

### Barra laterale Stili

Qui è possibile impostare, tra le altre cose, **colore del testo, stili** (come la "mazza" nel blocco "Separatore") e **spaziatura**. Anche nel blocco gruppo ci sono opzioni per impostare stili speciali.

---

![](https://nica.network/wp-content/uploads/2025/01/grafik-4-1021x1024.png)

## Suggerimenti e trucchi

### Copia e Duplica!!!

Quando possibile, copia i blocchi da un'altra pagina e poi sostituisci i contenuti. In questo modo dovrai occuparti solo di pochissime cose. (Ctrl + C > Ctrl + V)

Se hai bisogno di un blocco più volte, puoi anche duplicarlo con tutti i suoi contenuti (Ctrl + Maiusc + D)

La **visualizzazione elenco aiuta** davvero enormemente qui ![](https://nica.network/wp-content/uploads/2025/01/grafik-5.png)

---

### Paragrafi

Premendo Invio viene creato ogni volta un nuovo blocco.

Per evitarlo, tieni premuto **"Maiusc"** (tasto maiuscolo)

---

### Aiuto, la selezione dei blocchi è troppo vasta!

Comprensibile. Quando apri la panoramica dei blocchi, puoi farti un'idea. In realtà hai bisogno solo dei blocchi sotto "**Testo**", "**Media**" e "**Design**". Tutto il resto puoi tranquillamente ignorarlo.

![](https://nica.network/wp-content/uploads/2025/01/grafik-6-1024x972.png)

---

### Colonne, Righe, Griglie

Sono necessarie per **visualizzare i contenuti uno accanto all'altro**. Le colonne sono le più facili da usare.

1. Crea un blocco Colonne (si può fare anche tramite il "+" blu)
2. Seleziona il layout. Per spostare i blocchi nelle colonne, la visualizzazione elenco aiuta di nuovo molto. Anche uno sguardo alla barra degli strumenti offre opzioni come l'allineamento dei contenuti (in alto, in basso, al centro...).

![](https://nica.network/wp-content/uploads/2025/01/grafik-7-1024x622.png)

[Qui un pulsante](#)

anche solo con contorno tramite "Stili"

Nei pulsanti, il link viene aggiunto tramite l'icona del link (o Ctrl + K).

Le **Righe** funzionano in modo simile, solo che non hanno larghezze fisse. Le **Griglie** possono essere paragonate grossolanamente a tabelle dinamiche.

---

### Leggibilità

Nessuno legge più un lungo blocco di testo [inserire anno corrente qui]. Ogni volta che ha senso (!), utilizza la strutturazione visiva come:

- ==**Intestazioni**== di diversi livelli (H2, H3...)
    - Elenchi
- **Grassetto** per le parti rilevanti
- ![](https://nica.network/wp-content/uploads/2025/01/nica-logo-simple-small.png) Immagini
- _Paragrafi_
- Pulsanti invece di [link](https://nica.network/kurzanleitung/) normali
- Colori di sfondo dei singoli blocchi

Tutto chiaro ;)

## Pubblicazione

È relativamente semplice tramite l'apposito **pulsante in alto a destra**.

Prima, però, vale la pena dare un'**occhiata di controllo** alla pagina finita, perché la pagina in modalità di modifica non sempre appare come quella pubblica.

![](https://nica.network/wp-content/uploads/2025/01/grafik-8.png)

![](https://nica.network/wp-content/uploads/2025/01/grafik-9-490x1024.png)

1. Qui si può impostare, ad esempio, che una pagina venga salvata come **Privata o Bozza**, per non visualizzarla più senza doverla eliminare.
2. Qui si può modificare il **link** sotto cui la pagina verrà visualizzata alla fine.
3. Se la pagina deve essere una **sottopagina di un'altra pagina**, c'è l'opzione qui.

## Problemi e domande

Non sempre tutto funziona come dovrebbe. Alcune impostazioni, ad esempio, rimangono senza effetto. Questo può avere due ragioni. O un bug, o questa impostazione viene sovrascritta dalle impostazioni di visualizzazione generali del sito.

**Si prega di inviare problemi di questo tipo o anche semplici domande, preferibilmente con uno screenshot, a:**

[**mail@piiit-creates.de**](mailto:mail@piiit-creates.de)
