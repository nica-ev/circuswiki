---
created: 2025-08-29 19:12:50
update: 2025-08-29 23:22:04
publish: false
tags:
  - case-study
  - moc
title:
description:
authors:
  - Marc Bielert
  - Craig Quat
---

# Prolog

The world of circus pedagogy is in the midst of a quiet but powerful shift. For a long time, circus in education was seen as something mostly for kids—playful, physical, and rooted in learning a specific set of technical tricks. But across the globe, a growing wave of practitioners is pushing beyond that narrow frame. They’re showing that circus can be something much more: a tool for inclusion, for connection, and for deep personal and social transformation.

This publication offers a window into that evolving landscape. It brings together case studies from educators and facilitators across Europe who are reimagining what circus can look like—and who it can be for. Through their stories, we see how movement, play, and presence are being used to open new doors for learning, healing, and community building.

# Case Studies

| name                        | authors        | title                                                | land    |
| --------------------------- | -------------- | ---------------------------------------------------- | ------- |
| [[Case Study 01 - Germany]] | Marc Bielert   | Movement & Play in Early Childhood Ed                | Germany |
| [[Case Study 02 - Germany]] | Marc Bielert   | Circus Workshop for Children with Special Needs      | Germany |
| [[Case Study 03 - Greece]]  | Eva Parlani    | Feeling Safe: A Key for Autism                       | Greece  |
| [[Case Study 04 - Greece]]  | Monokyklo team | Colours and Patterns to Unlock Friendly Interactions | Greece  |

---

>[!info]- Technical Stuff
>

```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.hasTag("case-study")
        - '!file.hasTag("moc")'
    order:
      - file.name
      - authors
      - title
      - land
    columnSize:
      note.title: 368

```

