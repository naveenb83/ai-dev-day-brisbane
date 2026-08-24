---
tags:
  - L200
  - rag
---

# Glossary — RAG & search

Retrieving the right information and feeding it to a model. See
[Retrieval & RAG](../working-with-ai/retrieval-and-rag.md).

**Retrieval-augmented generation (RAG)**
:   Finding relevant pieces of *your* content and giving them to the model as
    context so it answers from your material, not its memory. The standard way to
    do trustworthy Q&A over private documents.

**Retrieval**
:   The "find the relevant bits" step — searching a knowledge base for passages
    related to a query.

**Chunk / chunking**
:   Splitting documents into passages small enough to embed and retrieve
    precisely. Chunking on natural boundaries strongly affects RAG quality.

**Embedding model**
:   A model that turns text into embeddings (vectors of meaning). Query and stored
    content must use the *same* embedding model.

**Vector database / vector index**
:   A store that holds embeddings and finds the nearest (most similar) ones fast.
    → *On Databricks:* Mosaic AI Vector Search.

**Semantic search**
:   Searching by **meaning** rather than exact keywords — finds "refund policy" for
    "how do I get my money back?".

**Keyword search / BM25**
:   Traditional search matching exact terms. Precise for codes and names; blind to
    meaning. BM25 is a common keyword-ranking method.

**Hybrid search**
:   Combining semantic and keyword search — usually more accurate than either
    alone.

**Reranking**
:   A second pass that reorders retrieved candidates by relevance (often with a
    specialised model) to put the best results on top.

**Nearest neighbour**
:   The stored item(s) whose vector is closest to the query's — what a vector search
    returns.

**Approximate nearest neighbour (ANN)**
:   Algorithms that find *almost* the closest matches near-instantly at scale,
    trading a tiny bit of accuracy for huge speed.

**Cosine similarity / similarity score**
:   A common measure of how alike two vectors are. Higher = more similar.

**Top-k**
:   The number of best matches to retrieve (e.g. "top 5 chunks"). More context vs
    more noise/cost is a balance.

**Context**
:   The information placed in the prompt for the model to use — in RAG, the
    retrieved chunks.

**Citations / sources**
:   Showing which retrieved documents an answer came from, so humans can verify.

**Knowledge base**
:   The collection of documents/data your retrieval searches over.

**Ingestion / indexing**
:   Loading, chunking, embedding and storing documents so they're retrievable.

**Graph RAG**
:   RAG that uses a knowledge **graph** of entities and relationships to retrieve
    connected facts, not just similar text.

**Agentic RAG**
:   RAG where an *agent* decides when and what to retrieve (and may search multiple
    times) rather than a single fixed retrieval step.
