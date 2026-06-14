---
lang: pt
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Sistema de Documentação
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:38:26+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:11+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifesto](doc-sys-manifest.md){ .md-button }
[Configuração do Obsidian](Obsidian%20Setup.md){ .md-button }
## Arquitetura do Sistema

A ideia geral
> [!info] Visão geral da arquitetura
>
> Aqui está uma representação gráfica da arquitetura do sistema:
>```mermaid
>flowchart LR
>A(Conteúdo) --> B(Controle de versão)
>C(Software de edição) --> A
>A --> D(Tornar acessível online)
>```

Em detalhe:

> [!info] Visão geral da arquitetura
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Arquivos}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Tema: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Um editor de texto opcional, mas recomendado por mim, para editar arquivos Markdown.
> *   **Arquivos:** Os arquivos Markdown que contêm o conteúdo da minha documentação.
> *   **Github Desktop:** Uma ferramenta para gerenciar facilmente meus repositórios Git.
> *   **Github:** Um serviço online para controle de versão e colaboração.
> *   **Github Pages:** Um serviço gratuito para publicar meu site.
> *   **MkDocs:** Uma ferramenta para criar automaticamente o site a partir dos meus arquivos Markdown.
> *   **MkDocs-Material:** Um tema para MkDocs que oferece um layout moderno e atraente.
> *   **MkDocs-Publisher:** Uma coleção de plugins que facilita a colaboração com o Obsidian e oferece funcionalidades adicionais.

## Componentes em detalhe

### 1. Markdown

> [!info] Markdown como base
> Eu uso o [formato Markdown](Markdown.md) para minha documentação. Markdown é uma linguagem de marcação simples que me permite formatar texto com formatação básica (por exemplo, títulos, listas, links).

**Vantagens:**

*   É fácil de aprender e usar, o que me permite focar no conteúdo.
*   É independente de plataforma, então posso continuar meu trabalho em qualquer dispositivo.
*   É ideal para controle de versão, o que me permite rastrear e gerenciar alterações.
*   É à prova de futuro e não proprietário, o que me dá a certeza de que meu trabalho permanecerá acessível a longo prazo.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian como editor de texto
> [Obsidian](Obsidian%20Setup.md) é um editor de texto opcional, mas recomendado por mim. Ele me oferece as seguintes vantagens:

*   Posso armazenar meus dados localmente e editá-los offline, o que me dá flexibilidade e controle.
*   Posso vincular e conectar arquivos facilmente, o que me ajuda a organizar informações complexas.
*   Posso marcar arquivos com tags e gerenciá-los facilmente, o que me dá uma dimensão adicional de organização.
*   Posso visualizar meus dados graficamente, o que me ajuda a identificar padrões e relacionamentos.
*   Posso estender a funcionalidade do Obsidian com plugins, o que me permite adaptar a ferramenta às minhas necessidades específicas.

### 3. Git e Github

> [!info] Git para controle de versão
> [Git](https://git-scm.com/) é um sistema de controle de versão que me permite rastrear e gerenciar alterações na documentação. [Github](https://github.com/) é um serviço online que me permite armazenar meus repositórios Git e colaborar com outras pessoas.

**Vantagens:**

*   Controle de versão: Cada alteração é documentada e pode ser rastreada a qualquer momento, o que me ajuda a evitar erros e a manter o controle.
*   Colaboração: Várias pessoas podem trabalhar na documentação simultaneamente, o que me dá a oportunidade de integrar feedback e contribuições de outras pessoas.
*   Backup: Minha documentação está segura e é regularmente copiada, o que me dá a certeza de que meu trabalho não será perdido.

### 4. Github Desktop

> [!info] Github Desktop como ferramenta
> [Github Desktop](../_inbox/Github%20Desktop.md) é uma interface gráfica para Git que me permite usar Git de forma fácil e sem linha de comando.

**Vantagens:**

*   Fácil de usar, o que facilita o uso do Git.
*   Não são necessários conhecimentos de linha de comando, o que me poupa tempo e esforço.
*   Simplifica meu fluxo de trabalho, o que me permite focar na criação de conteúdo.

### 5. MkDocs

> [!info] MkDocs como gerador de sites
> [MkDocs](https://mkdocs.org) é um gerador de sites estáticos que converte meus arquivos Markdown em um site estático.

**Vantagens:**

*   Criação de sites simples, o que me permite publicar minha documentação de forma rápida e fácil.
*   Atualização rápida, o que me permite ver as alterações em tempo real.
*   Layout consistente, o que garante uma apresentação profissional e uniforme da minha documentação.
*   Pré-visualização offline, o que me permite verificar minha documentação antes de publicá-la.

### 6. Github Pages

> [!info] Github Pages para hospedagem
> [Github Pages](../_inbox/Github%20Pages.md) é um serviço de hospedagem gratuito do Github que me permite publicar meu site facilmente online.

**Vantagens:**

*   Hospedagem gratuita, o que me permite publicar minha documentação sem custos adicionais.
*   Publicação fácil, o que me livra da implementação técnica da publicação.
*   Confiável, o que me dá a certeza de que minha documentação estará sempre disponível.

### 7. MkDocs-Material

> [!info] MkDocs-Material como tema
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) é um tema para MkDocs que oferece um layout moderno e atraente.

**Vantagens:**

*   Design moderno, o que faz minha documentação parecer profissional e atual.
*   Personalizável, o que me permite adaptar o layout às minhas necessidades específicas.
*   Fácil de usar, o que facilita o uso da documentação.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher como coleção de plugins
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) é uma coleção de plugins MkDocs que simplifica a colaboração com o Obsidian e oferece funcionalidades adicionais.

**Vantagens:**

- **Integração simplificada com Obsidian:** Ajuste automático da sintaxe Markdown do Obsidian (Callouts, Wikilinks, etc.).
- **Metadados expandidos:** Integração de tags e categorias do frontmatter do Obsidian.

## Fluxo de trabalho

> [!info] Meu fluxo de trabalho
> Aqui está meu fluxo de trabalho típico:

1.  Crio e edito arquivos Markdown com um editor de texto (opcionalmente Obsidian).
2.  Salvo os arquivos Markdown localmente.
3.  Envio minhas alterações para o repositório Git com o Github Desktop.
4.  Gero automaticamente o site com o MkDocs.
5.  Publico o site com o Github Pages.

## Sistema de arquivos

> [!info] Estrutura de diretórios
> Aqui está a estrutura de diretórios do meu sistema:
>
> ```
>/docs/     (Aqui estão meus arquivos Markdown)
>/site/     (Aqui o site é gerado)
>license    (Informações de licença)
>mkdocs.yml (Arquivo de configuração para MkDocs)
>readme.md  (Arquivo para descrever o repositório)
>```

## Alternativas para criação de conteúdo

> [!info] Alternativas para criação de conteúdo
> Estou ciente de que nem todos estão familiarizados com Markdown e Git. Portanto, ofereço as seguintes alternativas:

1.  **Wordpress:** O conteúdo pode ser criado no Wordpress como uma página.
2.  **Arquivo de texto, arquivo Word:** O conteúdo pode ser criado como um arquivo de texto, arquivo Word (ou em outros formatos típicos).

Nesses casos, posso então integrar o conteúdo ao sistema.
