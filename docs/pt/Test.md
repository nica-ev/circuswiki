---
lang: pt
translation_id: test
created: 2025-01-19 04:14:36
update: 2025-02-26 05:52:07
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Test.md
translation_source_hash: 8402c58d616ce7f6b5ad40be50170377d0a7bff15644855b2d4ef2e33c7c900c
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:13:20+00:00
translation_source_body_hash: 8402c58d616ce7f6b5ad40be50170377d0a7bff15644855b2d4ef2e33c7c900c
translation_source_metadata_hash: a549a7fc8f107b2d3d9d4bff18748df1087180aa7f8547f248ba06a76a03bf98
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:22:38+00:00
translation_source_localized_metadata_hash: a549a7fc8f107b2d3d9d4bff18748df1087180aa7f8547f248ba06a76a03bf98
translation_source_structural_metadata_hash: d90a7bd2c833fec1d0943faa40a4f711254d83c820b1b991e6d63925144cd5c9
---
# Grades e Abas

<div class="grid" markdown>

=== "Lista não ordenada"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Lista ordenada"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Abas de conteúdo"
=== "Lista não ordenada"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Lista ordenada"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Configuração em 5 minutos__

    ---

    Instale o [mkdocs-material](#) com o [pip](#) e comece a usar em minutos

    [:octicons-arrow-right-24: Primeiros passos](#){  .md-button }

-   :fontawesome-brands-markdown:{ .lg .middle } __É apenas Markdown__

    ---

    Concentre-se no seu conteúdo e gere um site estático responsivo e pesquisável

    [:octicons-arrow-right-24: Referência](#){  .md-button }

-   :material-format-font:{ .lg .middle } __Feito à medida__

    ---

    Altere cores, fontes, idioma, ícones, logotipo e mais com poucas linhas

    [:octicons-arrow-right-24: Personalização](#){  .md-button }

-   :material-scale-balance:{ .lg .middle } __Código Aberto, MIT__

    ---

    O Material for MkDocs é licenciado sob MIT e está disponível no [GitHub]

    [:octicons-arrow-right-24: Licença](#){  .md-button }

</div>

# Anotações

> [!INFO]- Título
> Uma caixa de informação do Obsidian
> inspirada na sintaxe da documentação da Microsoft

> [!INFO] Título
> Uma caixa de informação do Obsidian
> inspirada na sintaxe da documentação da Microsoft

# Blocos de código

```
E aqui um bloco de código
vamos ver se funciona
```

# Botões

[[Frontmatter]] { .md-button }

# IFrames

## Exemplo de vídeo incorporado

<iframe width="950" height="500" src="https://www.youtube.com/embed/zFPsr1L13Vs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Exemplo de Padlet incorporado

<iframe src="https://padlet.com/lilithdekow/nica-i7hu4ssvwhamrc5x" style="border: 0" width="600" height="600" frameborder="0" scrolling="no"\></iframe>

# testar pdf

<!--- file: docs/howto/embedding_pdf.md --->
{% with pdf_file = "_attachements/Functional%20Juggling%20-%20The%20Book%20-%20EN.pdf" %}

{% set solid_filepdf = '<i class="fas fa-file-pdf"></i>' %}
{% set empty_filepdf = '<i class="far fa-file-pdf"></i>' %}

## Exemplo: Incorporar um arquivo PDF

<object data="{{ pdf_file }}" type="application/pdf">
    <embed src="{{ pdf_file }}" type="application/pdf" />
</object>

obsidian://open?vault=docs&file=_attachements%2FFunctional%20Juggling%20-%20The%20Book%20-%20EN.pdf
