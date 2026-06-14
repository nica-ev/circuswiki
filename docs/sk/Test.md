---
lang: sk
translation_id: test
created: 2025-01-19 04:14:36
update: 2025-02-26 05:52:07
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Test.md
translation_source_hash: 8402c58d616ce7f6b5ad40be50170377d0a7bff15644855b2d4ef2e33c7c900c
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:13:26+00:00
translation_source_body_hash: 8402c58d616ce7f6b5ad40be50170377d0a7bff15644855b2d4ef2e33c7c900c
translation_source_metadata_hash: a549a7fc8f107b2d3d9d4bff18748df1087180aa7f8547f248ba06a76a03bf98
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:22:38+00:00
translation_source_localized_metadata_hash: a549a7fc8f107b2d3d9d4bff18748df1087180aa7f8547f248ba06a76a03bf98
translation_source_structural_metadata_hash: d90a7bd2c833fec1d0943faa40a4f711254d83c820b1b991e6d63925144cd5c9
---
# Mriežky a karty

<div class="grid" markdown>

=== "Neusporiadaný zoznam"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Usporiadaný zoznam"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Obsahové karty"
=== "Neusporiadaný zoznam"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Usporiadaný zoznam"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Nastavenie za 5 minút__

    ---

    Nainštalujte [mkdocs-material](#) pomocou [pip](#) a spustite ho za pár minút

    [:octicons-arrow-right-24: Začíname](#){  .md-button }

-   :fontawesome-brands-markdown:{ .lg .middle } __Je to len Markdown__

    ---

    Zamerajte sa na svoj obsah a vygenerujte responzívnu a vyhľadávateľnú statickú stránku

    [:octicons-arrow-right-24: Referencie](#){  .md-button }

-   :material-format-font:{ .lg .middle } __Šité na mieru__

    ---

    Zmeňte farby, písma, jazyk, ikony, logo a ďalšie pomocou niekoľkých riadkov

    [:octicons-arrow-right-24: Prispôsobenie](#){  .md-button }

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs je licencovaný pod MIT a dostupný na [GitHub]

    [:octicons-arrow-right-24: Licencia](#){  .md-button }

</div>

# Anotácie

> [!INFO]- Názov
> Informačný výzva z Obsidianu
> inšpirovaná syntaxou z Microsoft Docs

> [!INFO] Názov
> Informačný výzva z Obsidianu
> inšpirovaná syntaxou z Microsoft Docs

# Kódové bloky

```
Und hier mal ein Codeblock
mal sehen obs geht
```

# Tlačidlá

[[Frontmatter]] { .md-button }

# IFrames

## Príklad vloženia videa

<iframe width="950" height="500" src="https://www.youtube.com/embed/zFPsr1L13Vs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Príklad vloženia Padletu

<iframe src="https://padlet.com/lilithdekow/nica-i7hu4ssvwhamrc5x" style="border: 0" width="600" height="600" frameborder="0" scrolling="no"\></iframe>

# test pdf

<!--- file: docs/howto/embedding_pdf.md --->
{% with pdf_file = "_attachements/Functional%20Juggling%20-%20The%20Book%20-%20EN.pdf" %}

{% set solid_filepdf = '<i class="fas fa-file-pdf"></i>' %}
{% set empty_filepdf = '<i class="far fa-file-pdf"></i>' %}

## Príklad: Vloženie súboru PDF

<object data="{{ pdf_file }}" type="application/pdf">
    <embed src="{{ pdf_file }}" type="application/pdf" />
</object>

obsidian://open?vault=docs&file=_attachements%2FFunctional%20Juggling%20-%20The%20Book%20-%20EN.pdf
