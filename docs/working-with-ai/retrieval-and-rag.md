---
tags:
  - L200
  - rag
---

# Retrieval & RAG <span class="lvl lvl-200">L200</span>

## In plain terms

Out of the box, an LLM only knows what it learned in training — not your policies,
your products or last week's numbers. **Retrieval-augmented generation (RAG)**
fixes that with a simple move: **find the relevant bits of your own content
first, paste them into the prompt, then ask the model to answer using them.**

It's the difference between asking a smart stranger to guess your refund policy,
and handing them the policy document and *then* asking. Same model — grounded,
accurate answer.

## How it works

RAG is a small pipeline. Once, up front, you **prepare** your content:

1. **Collect** the documents (PDFs, wiki pages, tickets…).
2. **Chunk** them into passages a few paragraphs long.
3. **Embed** each chunk into a [vector](../foundations/embeddings-and-vectors.md).
4. **Store** the vectors in a [vector index](vector-search.md).

Then, every time someone asks a question:

```
Question ─► embed ─► search the index ─► top matching chunks
                                              │
                                              ▼
        "Answer using ONLY this context: «chunks»   Question: «q»"
                                              │
                                              ▼
                                     LLM ─► grounded answer (with sources)
```

The retrieved chunks become the **context** in the prompt. The model now answers
from *your* material, and can cite which chunk it used.

!!! tip "Why RAG beats fine-tuning for most 'answer from our docs' jobs"
    - **Fresh:** update a document and the next answer reflects it — no retraining.
    - **Cheaper & faster** to set up than fine-tuning.
    - **Traceable:** you can show the exact source behind an answer.
    - **Governed:** you can restrict which documents a given user can retrieve.

## How Databricks does it

The whole pipeline is native to the platform:

- **Vector Search** stores your embeddings and does the retrieval, and can stay
  automatically in sync with a source table as documents change.
- **AI Functions** and **Foundation Model APIs** handle embedding and the final
  generation.
- **Unity Catalog** governs *which* documents each user's questions can reach — so
  RAG respects your existing permissions rather than bypassing them.
- **Agent Bricks Knowledge Assistant** packages this end-to-end: point it at your
  documents and it builds a governed Q&A assistant for you.

## Pitfalls

!!! warning "Where RAG goes wrong"
    - **Bad chunking** (too big, too small, split mid-idea) → poor retrieval →
      poor answers. Chunk on natural boundaries.
    - **Retrieved ≠ correct.** The index returns *relevant* text; if your source
      docs are wrong or outdated, so is the answer. Curate the source.
    - **Forgetting "use only this context".** Without that instruction the model
      may blend in its own memory and reintroduce hallucination.
    - **No sources shown.** Always surface citations so humans can verify.

## Try it

:material-flask: **Lab 4** builds a small RAG assistant over sample docs with
Vector Search.

## See also

- **[Vector search](vector-search.md)** — the retrieval engine in detail.
- **[Embeddings & vectors](../foundations/embeddings-and-vectors.md)** — the L100 idea.
- **[Why we evaluate](why-we-evaluate.md)** — measuring groundedness.
- Glossary: **RAG**, **chunk**, **context**, **grounding**, **retrieval**.
