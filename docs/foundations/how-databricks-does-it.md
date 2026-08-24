---
tags:
  - L100
---

# How Databricks does it (foundations) <span class="lvl lvl-100">L100</span>

You've met the ideas — AI, LLMs, prompts, embeddings, and the honest limits. This
page is the **map**: where each idea shows up on Databricks, so the labs feel
familiar. Don't memorise it; just know it exists to come back to.

## The one-line mental model

> Databricks is a **data platform with AI built in**. Because your data and the AI
> live together, you can point powerful models at *your* governed data — safely.

The AI capabilities are grouped under the name **Mosaic AI**.

## Where each foundation lives

| The idea (vendor-neutral) | On Databricks | You'll use it in |
| --- | --- | --- |
| A ready-to-use LLM | **Foundation Model APIs** + the **AI Playground** | Lab 1 |
| Prompts, system messages, temperature | **AI Playground** sliders and system-prompt box | Lab 1 |
| AI over your data with plain SQL | **AI Functions** (`ai_query`, `ai_classify`, `ai_summarize`, …) | Lab 2 |
| Ask questions of your tables in English | **Genie** (natural language → SQL) | Lab 3 |
| Embeddings & semantic search | **Vector Search** | Lab 4 |
| Build an assistant / agent | **Agent Bricks** & **Mosaic AI Agent Framework** | Lab 5 |
| Measure and trust the output | **MLflow** evaluation & tracing | Lab 6 |
| Control who sees what data | **Unity Catalog** (governance) | throughout |



## Why "on your data" is the whole point

A chatbot on the public internet can't see your refund policy, your sales table or
your customer records — and shouldn't. The reason to do AI *on your data platform*
is that the model can be given access to **real, current, governed** information:

- **Genie** answers "what were August sales in Queensland?" by writing and running
  actual SQL — so the number is *real*, not remembered.
- **RAG + Vector Search** lets an assistant answer from *your* documents.
- **Unity Catalog** makes sure it only ever sees data the user is allowed to see.

That combination — capable models + your governed data + the ability to measure
quality — is what turns "neat demo" into "something you can rely on at work." The
rest of this site builds towards it, one level at a time.

## See also

- Back to **[Foundations overview](index.md)**.
- Next level up: **Working with AI (L200)**.
- Glossary: **Mosaic AI**, **Foundation Model APIs**, **Unity Catalog**, **AI Playground**.
