---
lang: nl
translation_id: test
created: 2025-01-19 04:14:36
update: 2025-02-26 05:52:07
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Test.md
translation_source_hash: 8402c58d616ce7f6b5ad40be50170377d0a7bff15644855b2d4ef2e33c7c900c
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:24:52+00:00
translation_source_body_hash: 8402c58d616ce7f6b5ad40be50170377d0a7bff15644855b2d4ef2e33c7c900c
translation_source_metadata_hash: a549a7fc8f107b2d3d9d4bff18748df1087180aa7f8547f248ba06a76a03bf98
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:22:38+00:00
translation_source_localized_metadata_hash: a549a7fc8f107b2d3d9d4bff18748df1087180aa7f8547f248ba06a76a03bf98
translation_source_structural_metadata_hash: d90a7bd2c833fec1d0943faa40a4f711254d83c820b1b991e6d63925144cd5c9
---
# Rasters & Tabbladen

<div class="grid" markdown>

=== "Ongeordende lijst"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Geordende lijst"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Inhoudstabbladen"
=== "Ongeordende lijst"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Geordende lijst"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __In 5 minuten ingesteld__

    ---

    Installeer [mkdocs-material](#) met [pip](#) en ga direct aan de slag

    [:octicons-arrow-right-24: Aan de slag](#){  .md-button }

-   :fontawesome-brands-markdown:{ .lg .middle } __Gewoon Markdown__

    ---

    Focus op je inhoud en genereer een responsieve en doorzoekbare statische site

    [:octicons-arrow-right-24: Referentie](#){  .md-button }

-   :material-format-font:{ .lg .middle } __Op maat gemaakt__

    ---

    Wijzig kleuren, lettertypen, taal, iconen, logo en meer met een paar regels

    [:octicons-arrow-right-24: Maatwerk](#){  .md-button }

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is gelicentieerd onder MIT en beschikbaar op [GitHub]

    [:octicons-arrow-right-24: Licentie](#){  .md-button }

</div>

# Annotaties

> [!INFO]- Titel
> Een informatieve callout van Obsidian
> geïnspireerd door de syntax van Microsoft Docs

> [!INFO] Titel
> Een informatieve callout van Obsidian
> geïnspireerd door de syntax van Microsoft Docs

# Codeblokken

```
En hier een codeblok
eens kijken of het werkt
```

# Knoppen

[[Frontmatter]] { .md-button }

# IFrames

## Voorbeeld van ingesloten video

<iframe width="950" height="500" src="https://www.youtube.com/embed/zFPsr1L13Vs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Voorbeeld van ingesloten Padlet

<iframe src="https://padlet.com/lilithdekow/nica-i7hu4ssvwhamrc5x" style="border: 0" width="600" height="600" frameborder="0" scrolling="no"\></iframe>

# test pdf 

<!--- file: docs/howto/embedding_pdf.md --->
{% with pdf_file = "_attachements/Functional%20Juggling%20-%20The%20Book%20-%20EN.pdf" %}

{% set solid_filepdf = '<i class="fas fa-file-pdf"></i>' %}
{% set empty_filepdf = '<i class="far fa-file-pdf"></i>' %}

## Voorbeeld: PDF-bestand insluiten

<object data="{{ pdf_file }}" type="application/pdf">
    <embed src="{{ pdf_file }}" type="application/pdf" />
</object>

obsidian://open?vault=docs&file=_attachements%2FFunctional%20Juggling%20-%20The%20Book%20-%20EN.pdf
