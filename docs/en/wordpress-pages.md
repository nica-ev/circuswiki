---
lang: en
translation_id: wordpress-pages
publish: true
tags:
  - wordpress
  - tutorial
created: 2025-01-18 21:15:11
update: 2025-01-23 05:46:07
title: Build a new page in WordPress
authors:
  - Piiit
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/wordpress-pages.md
translation_source_hash: 172db702654e913f2b641fffd126e0ccdbae876825b67644c7eb14cb3a45b2b6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T19:30:02+00:00
translation_source_body_hash: 172db702654e913f2b641fffd126e0ccdbae876825b67644c7eb14cb3a45b2b6
translation_source_metadata_hash: abe64f9a224d064ced886f7fb6f6a055b7f6f2ca648d71f5e6feca6b810e6ced
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:19+00:00
translation_source_localized_metadata_hash: abe64f9a224d064ced886f7fb6f6a055b7f6f2ca648d71f5e6feca6b810e6ced
translation_source_structural_metadata_hash: ef2e4594352bb749c96a5083d87bed9f90ad8c5c465e07a187a59612104255b6
---
# Building a New Page in WordPress

It's best to watch this tutorial directly in WordPress (you'll need access, of course – if you don't have any, you can read the tutorial here).

[Watch Directly in WordPress](https://nica.network/kurzanleitung){ .md-button }

---

### Creating Content

A page is made up of **individual blocks**. This here, for example, is a "Paragraph" block, and the block above it is a "Heading" block.

New blocks can be created using the "+" buttons. You can use the blue one in the top left, or when you hover your mouse between two blocks, or by pressing "Enter" and typing "/" in the new line.

## Heading 1

## Heading 2

### Heading 3

Heading 1 (H1) is the **page title** and should only be used once per page. There's a small peculiarity here. The page title (with the color gradient) isn't displayed by default on the published website. If you want it to show, you need to insert the **"Title Block"** onto your page, so it appears twice in the editing mode.

To set the **heading hierarchy**, click "H2" in the block menu and then select from the list, see image.

![](https://nica.network/wp-content/uploads/2025/01/grafik-1024x573.png)

## Adding Background Boxes

So that the content doesn't appear directly on the website's colored background image, we need to **put all blocks into a group and give that group a background color**.

1. **Open the List View** and select all elements, then group them (using the three dots or "Ctrl + G"). Make sure the **Group** is selected at the end. The List View is generally very helpful for keeping an overview, especially when blocks are nested.
2. **Open the Settings**. Here you'll find settings for the entire page or the selected block. We need the latter.
3. In the block settings, select the **"Styles" tab**.
4. Choose **"Background"**.
5. Black and white at the end of the color palette provide the slightly transparent background typical for the site.

![](https://nica.network/wp-content/uploads/2025/01/grafik-1-1024x494.png)

## Design

**Font colors, spacing, and special effects** can also be controlled via the block settings. There are two places to look for these.

### Toolbar

1. Select the parent block.
2. Displays the icon of the current block. You can also change the block type here (e.g., Paragraph to Heading).
3. Move the block.
4. Now come block-specific options like **text alignment, links, bold text...**

![](https://nica.network/wp-content/uploads/2025/01/grafik-2-1024x749.png)

### Styles Sidebar

Here you can adjust **text color, styles** (like the club for the "Separator Block"), and **spacing**, among other things. The Group block, for instance, also offers options for special styles.

---

![](https://nica.network/wp-content/uploads/2025/01/grafik-4-1021x1024.png)

## Tips and Tricks

### Copy & Duplicate!!!

Whenever possible, copy blocks from another page and then replace the content. This way, you only have to deal with a few things. (Ctrl + C > Ctrl + V)

If you need a block multiple times, you can also duplicate it with all its content (Ctrl + Shift + D).

The **List View is incredibly helpful** here ![](https://nica.network/wp-content/uploads/2025/01/grafik-5.png)

---

### Paragraphs

Pressing Enter creates a new block each time.

To prevent this, hold down **"Shift"** (the capitalization key).

---

### Help, the Block Selection is Too Big!

Understandable. When you open the block overview, you can get a sense of what's available. You really only need the blocks under **"Text"**, **"Media," and "Design."** You can safely ignore everything else.

![](https://nica.network/wp-content/uploads/2025/01/grafik-6-1024x972.png)

---

### Columns, Rows, Grids

You need these to **display content side-by-side**. Columns are the easiest to use.

1. Create a Columns block (you can also do this via the blue +).
2. Select the layout. To move blocks into columns, the List View is again very helpful. Taking a look at the toolbar also reveals options like aligning content (top, bottom, middle...).

![](https://nica.network/wp-content/uploads/2025/01/grafik-7-1024x622.png)

[Here's a Button](#)

via "Styles," also with an outline only.

For buttons, the link is added via the link icon (or Ctrl + K).

**Rows** work similarly, but they don't have fixed widths. **Grids** are roughly comparable to dynamic tables.

---

### Readability

No one reads a long block of text anymore [insert current year here]. Whenever it makes sense (!), use visual structuring like:

- ==**Headings**== in different levels (H2, H3...)
    - Lists
- **Bold** for important parts
- ![](https://nica.network/wp-content/uploads/2025/01/nica-logo-simple-small.png) Images
- _Paragraphs_
- Buttons instead of normal [links](https://nica.network/kurzanleitung/)
- Background colors for individual blocks

All clear ;)

## Publishing

This is relatively easy using the corresponding **button in the top right**.

However, it's worth doing a **quick check** of the finished page beforehand, as the page in the editing mode doesn't always look the same as the public version.

![](https://nica.network/wp-content/uploads/2025/01/grafik-8.png)

![](https://nica.network/wp-content/uploads/2025/01/grafik-9-490x1024.png)

1. Here you can set, for example, that a page is saved as **Private or as a Draft**, so you don't have to delete it to hide it.
2. Here you can edit the **link** under which the page will eventually be displayed.
3. If the page is intended to be a **sub-page of another page**, this option is available here.

## Problems & Questions

Not everything always works as it should. Some settings, for example, may have no effect. This can have two reasons. Either it's a bug, or that setting is being overridden by the parent website display settings.

**It's best to report problems of this nature, or simply ask questions, directly with a screenshot to:**

[**mail@piiit-creates.de**](mailto:mail@piiit-creates.de)
