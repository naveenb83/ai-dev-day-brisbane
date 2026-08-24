---
tags:
  - L200
  - rag
---

# Vector search <span class="lvl lvl-200">L200</span>

## In plain terms

**Vector search** is how you find things by *meaning* at scale. You've turned your
content into [vectors](../foundations/embeddings-and-vectors.md); a **vector
index** lets you ask "what's closest in meaning to *this*?" across millions of
items in milliseconds. It's the retrieval engine underneath RAG, recommendations
and semantic search.

## How it works

- You store one vector per item (per document chunk, product, ticket…).
- At query time you embed the query into a vector and ask the index for its
  **nearest neighbours** — the items whose vectors are closest.
- "Closest" is measured by a **similarity metric** (often cosine similarity).
  Scanning every vector would be slow, so indexes use **approximate nearest
  neighbour (ANN)** algorithms that are near-instant with tiny accuracy trade-offs.

You can attach **metadata** to each vector (author, date, department) and
**filter** on it — e.g. "nearest chunks *from HR documents this year*". This
matters for both relevance and governance.

!!! note "Semantic vs keyword — use both"
    Keyword search nails exact terms and codes ("error 4021"); semantic search
    nails intent ("why won't it start?"). **Hybrid search** combines them and
    usually beats either alone.

## How Databricks does it

- **Mosaic AI Vector Search** is the managed vector database. You can create an
  index that **auto-syncs** from a Delta table, so as your source data changes the
  index stays current — no manual re-indexing.
- It integrates with **Foundation Model APIs** for the embeddings and with **Unity
  Catalog** for governance, so metadata filters can enforce who sees what.
- It's the retrieval layer behind the RAG and Knowledge Assistant patterns.

## Pitfalls

!!! warning "Watch for"
    - **Mismatched embedding models.** Query and stored vectors must come from the
      *same* embedding model, or distances are meaningless.
    - **Stale index.** If it doesn't sync, answers drift from reality. Auto-sync or
      schedule refreshes.
    - **Ignoring metadata filters.** Filtering first (by permission, recency,
      source) improves both accuracy *and* safety.

## Try it

:material-flask: **Lab 4** creates a Vector Search index and queries it. *(Labs
added in a later section.)*

## See also

- **[Retrieval & RAG](retrieval-and-rag.md)** — where vector search is used.
- **[Embeddings & vectors](../foundations/embeddings-and-vectors.md)** — the underlying idea.
- Glossary: **vector index**, **nearest neighbour**, **cosine similarity**, **hybrid search**, **ANN**.
