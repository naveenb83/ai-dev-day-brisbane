---
tags:
  - L100
  - L200
  - L300
  - L400
---

# Glossary — Databricks & Mosaic AI terms

The platform names you'll meet in the labs, in plain English. *(Product names and
capabilities evolve — confirm specifics in the current Databricks documentation.)*

**Databricks**
:   The unified **data and AI platform** this dev day runs on — one place for data,
    analytics, ML and generative AI.

**Lakehouse**
:   Databricks' architecture combining a data lake's flexibility with a data
    warehouse's structure and performance — one governed home for all your data.

**Delta Lake / Delta table**
:   The reliable, transactional table format underpinning the lakehouse.

**Unity Catalog (UC)**
:   The **unified governance layer** across data, files, models and functions —
    permissions (RBAC/ABAC), column masks, row filters, lineage and audit. The
    backbone of AI safety on Databricks; AI features inherit its permissions.

**Volumes**
:   Governed storage for files (documents, images, PDFs) under Unity Catalog.

**System tables**
:   Built-in governed tables exposing platform metadata — usage, cost, lineage,
    audit — queryable with SQL.

**Mosaic AI**
:   The umbrella name for Databricks' AI capabilities — foundation models, vector
    search, agents, model serving, training and evaluation.

**Foundation Model APIs (FMAPI)**
:   Instant access to leading open and commercial LLMs and embedding models, billed
    **pay-per-token** or via **provisioned throughput**.

**AI Playground**
:   An in-workspace chat screen to try models, compare them, tune settings
    (temperature, max tokens) and see cost — a great first stop.

**AI Functions**
:   SQL functions that call models over your tables — `ai_query`, `ai_classify`,
    `ai_extract`, `ai_summarize`, `ai_analyze_sentiment`, `ai_translate`,
    `ai_mask`, `ai_gen`, `ai_parse_document`, `ai_forecast`. AI without leaving SQL.

**`ai_query()`**
:   The general-purpose AI Function: send any prompt to any serving endpoint from
    SQL.

**Vector Search**
:   Databricks' managed vector database — stores embeddings, does fast semantic
    retrieval, and can auto-sync from a Delta table. The engine under RAG here.

**Genie (Databricks AI/BI Genie)**
:   Natural-language questions over your governed tables — it writes and runs real
    SQL and shows it, so answers are computed, not guessed.

**AI/BI**
:   Databricks' business-intelligence experience (dashboards + Genie) for exploring
    data, including in natural language.

**Genie Space**
:   A configured Genie experience over chosen tables, tuned with instructions,
    descriptions, certified example queries and metrics for accuracy.

**Metric view**
:   A governed definition of a business metric (e.g. "revenue") so terms mean the
    same thing everywhere — a semantic layer that improves Genie accuracy.

**Agent Bricks**
:   Higher-level, configure-don't-code agents — the **Knowledge Assistant**,
    **Genie Spaces**, and the **Multi-Agent Supervisor**.

**Knowledge Assistant (KA)**
:   An Agent Bricks agent for **document Q&A** (governed RAG) — point it at
    documents, get a grounded assistant.

**Multi-Agent Supervisor (MAS)**
:   An Agent Bricks agent that **coordinates several agents** (e.g. a Genie Space +
    a Knowledge Assistant) behind one interface.

**Mosaic AI Agent Framework**
:   The toolkit for **building custom agents** — wiring a model to tools (often UC
    functions), retrieval and memory, then deploying and evaluating them.

**Omnigent**
:   The name associated with Databricks' direction toward a **general-purpose
    enterprise agent** (a meta-harness orchestrating many agents/tools over
    governed data). *(Fast-moving; confirm current specifics in docs.)*

**Model Serving (Mosaic AI Model Serving)**
:   Managed, scalable **endpoints** for foundation models, custom/fine-tuned models
    and agents — with autoscaling, versioning and A/B traffic splitting.

**Mosaic AI Model Training**
:   Fine-tune open models on your governed data (including efficient methods),
    tracked in MLflow and served via Model Serving.

**MLflow**
:   The open-source platform (built into Databricks) for the AI lifecycle —
    experiment tracking, model registry, **evaluation** and **tracing** for GenAI.

**MLflow Tracing**
:   Captures end-to-end **traces** of an app/agent (prompt, context, tool calls,
    output) for debugging, evaluation and monitoring.

**Databricks Assistant**
:   The in-platform AI coding assistant — writes/fixes SQL, Python and notebook
    code, explains errors, and is aware of your Unity Catalog data.

**Databricks Apps**
:   Host full web applications (dashboards, tools, AI apps) inside Databricks,
    close to your data and models, with workspace auth.

**Databricks Asset Bundles (DABs)**
:   Define a project (code, jobs, config) as **version-controlled files** for
    repeatable, reviewable deploys across dev/staging/prod — the basis of CI/CD.

**Lakebase**
:   Databricks' managed PostgreSQL for transactional/operational workloads — useful
    for app state and agent memory.

**Jobs / pipelines**
:   Scheduled or triggered back-end work — batch inference, data prep, retraining.

**Secret scope**
:   Databricks' secure store for credentials and keys, keeping them out of code and
    prompts.

**Serverless**
:   Compute that Databricks provisions and scales for you — no cluster management —
    available for SQL, jobs and more.

**DBRX**
:   An open large language model released by Databricks; one of the models you can
    access and serve on the platform.
