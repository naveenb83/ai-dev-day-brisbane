---
tags:
  - L300
  - rag
---

# Lab 4 — RAG with Vector Search <span class="lvl lvl-300">L300</span>

**~35 minutes** · works best in a **notebook** (Python)

## Goal

Build a small **question-answering assistant over your own documents**: chunk →
embed → index with **Vector Search** → retrieve → answer. This is RAG end to end.

## You'll learn

- The RAG pipeline as working code, not a diagram.
- Why "use only this context" and showing sources matter.

!!! note "Code is a starting point"
    Exact class/method names in the Vector Search and Foundation Model SDKs evolve.
    Treat the snippets as scaffolding and confirm current syntax in the in-product
    docs or the Databricks Vector Search guide. Your facilitator will point you at
    a ready endpoint.

## Steps

1. **Prepare source docs.** Create a table of short "policy" snippets to act as
   your knowledge base:
   ```sql
   CREATE OR REPLACE TABLE {your_catalog}.{your_schema}.kb AS
   SELECT * FROM VALUES
     (1, 'Refunds are available within 30 days of purchase with a receipt.'),
     (2, 'Batteries carry a 10-year warranty; panels carry 25 years.'),
     (3, 'Installation is free for orders over $5,000 in Queensland.'),
     (4, 'Support hours are 8am-6pm AEST, Monday to Friday.')
   AS t(id, content);
   ```
2. **Create a Vector Search index** over that table (in the Vector Search UI, or
   via the SDK). Point it at the `content` column and an embedding model; enable
   sync so it stays current. Conceptually:
   ```python
   # illustrative — confirm current API in docs
   from databricks.vector_search.client import VectorSearchClient
   vsc = VectorSearchClient()
   # create/get an endpoint, then create a delta-sync index on {your}.kb(content)
   ```
3. **Retrieve** the most relevant chunks for a question:
   ```python
   question = "How long do I have to get a refund?"
   results = index.similarity_search(
       query_text=question, columns=["content"], num_results=2)
   chunks = [r["content"] for r in results["result"]["data_array"]]
   ```
4. **Answer, grounded in the chunks**, using a Foundation Model:
   ```python
   context = "\n".join(f"- {c}" for c in chunks)
   prompt = (
     "Answer using ONLY the context. If it's not there, say you don't know. "
     "Quote the line you used.\n\n"
     f"Context:\n{context}\n\nQuestion: {question}"
   )
   # send `prompt` to a chat endpoint via the Foundation Model API / ai_query
   ```
5. **Check grounding.** Ask something the KB *doesn't* cover ("Do you ship
   overseas?"). A good RAG answer says it doesn't know — not a guess.

## Expected result

- Relevant chunks retrieved for each question, and answers that stick to them and
  cite the source line — plus an honest "I don't know" when the KB is silent.

## Stretch

- Remove "use only the context" from the prompt and watch hallucination creep
  back in.
- Add a clearly-wrong document to the KB and see the answer follow it — a lesson
  in *retrieved ≠ correct*.

## Concepts

- **[Retrieval & RAG](../working-with-ai/retrieval-and-rag.md)** ·
  **[Vector search](../working-with-ai/vector-search.md)** ·
  Glossary: **RAG**, **chunk**, **vector index**, **grounding**, **citations**.
