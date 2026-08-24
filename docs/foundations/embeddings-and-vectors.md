---
tags:
  - L100
  - rag
---

# Embeddings & vectors <span class="lvl lvl-100">L100</span>

## In plain terms

Computers are great with numbers and hopeless with meaning — unless you turn
meaning *into* numbers. An **embedding** does exactly that: it converts a piece of
text (a word, a sentence, a whole document) into a **list of numbers** — a
**vector** — that captures what it *means*.

The magic property: **things with similar meaning get similar numbers.** So
"dog" and "puppy" land close together; "dog" and "tax return" land far apart —
even though they share no letters.

## How it works

Picture every piece of text as a **dot on a map of meaning**. Related ideas
cluster together:

```
        cat •   • kitten
      dog •  • puppy
                                    • invoice
                          • receipt   • tax return
     canoe •
        • kayak
```

To find things related to "puppy", you don't match words — you look for the
**nearest dots**. That's **semantic search**: search by *meaning*, not by exact
keywords. Ask "how do I get my money back?" and it can find a document titled
"Refund policy" even though none of your words appear in it.

The distance between two vectors is a **similarity score**. Closer = more alike.

This one idea powers a lot:

- **Search that understands you**, not just your keywords.
- **Recommendations** ("more like this").
- **RAG** — retrieval-augmented generation — where we find the most relevant
  chunks of *your* documents and hand them to an LLM so it can answer using your
  content. (You'll see RAG properly at [L200](../index.md).)

!!! note "Where do the numbers come from?"
    A special model called an **embedding model** produces them. It's trained so
    that similar meanings get similar vectors. You don't need to understand its
    internals to use it — just know it turns text into comparable numbers.

## How Databricks does it

- An **embedding model** (available through Foundation Model APIs) turns your text
  into vectors.
- **Vector Search** stores those vectors and finds nearest matches fast, even
  across millions of documents — a managed "vector database" wired into your
  governed data.
- Because it lives in the platform, the documents you search stay under **Unity
  Catalog** governance — no shipping data to a separate service.

This is the backbone of the RAG and Genie labs later on.

## Pitfalls

!!! warning "Good to know"
    - **Embeddings capture meaning, not truth.** Two false statements about the
      same topic will still sit near each other. Retrieval finds *relevant* text,
      not *correct* text.
    - **Chunk size matters.** Embedding an entire 100-page manual as one vector
      blurs its meaning. Documents are split into **chunks** first — a detail you
      meet in the RAG section.

## See also

- **[Large language models](large-language-models.md)** — the partner that writes the answer.
- **[Why AI gets things wrong](why-ai-gets-things-wrong.md)** — why "relevant" ≠ "right".
- Glossary: **embedding**, **vector**, **semantic search**, **vector database**, **RAG**.
