# Cheat-sheets

Four one-page references. Print them, or keep the tab open during the labs.

---

## 1. The prompt skeleton

> **Role · Context · Task · Constraints · Format · Honesty rule**

```text
You are a {ROLE}.
Your task: {TASK, one clear sentence}.
Work only from the material below; if it's not there, say so — don't guess.

--- MATERIAL ---
{CONTEXT / INPUT}
--- END MATERIAL ---

Constraints: {audience} · {length} · {tone} · {do / don't}
Output format: {exact shape}
```

**Quick fixes when an answer is bad:**

| Symptom | Fix |
| --- | --- |
| Too generic | Add a role + audience + specifics |
| Made-up facts | Ground it: "use only this", + honesty rule |
| Unusable shape | Specify exact format (or JSON schema) |
| Fudged numbers | Split precise steps from creative ones |
| Flattering / biased | Ask for an objective, balanced take |

*(Full detail: [Anatomy of a good prompt](../prompt-library/anatomy-of-a-good-prompt.md).)*

---

## 2. Which tool when? (on Databricks)

| I want to… | Use | Level |
| --- | --- | --- |
| Try models, tune prompts | **AI Playground** | L100 |
| Add AI to a table/column in SQL | **AI Functions** (`ai_query`, `ai_classify`, …) | L200 |
| Let people ask my tables questions | **Genie** | L200 |
| Answer from my documents | **RAG + Vector Search** (or **Knowledge Assistant**) | L200–L300 |
| Have AI take actions / use tools | **Agent** (Agent Bricks or Agent Framework) | L300 |
| Coordinate several agents | **Multi-Agent Supervisor** | L300 |
| Make it consistent in style | **Fine-tuning** *(last resort — try prompting/RAG first)* | L300 |
| Prove it's good | **MLflow evaluation + tracing** | L400 |
| Control who sees what | **Unity Catalog** | all |
| Deploy & scale it | **Model Serving + Databricks Apps + Asset Bundles** | L400 |

**Customization ladder:** prompt → RAG → tools → fine-tune → (rarely) pre-train.
*Fine-tune for form, retrieve for facts.*

---

## 3. The level map

| | Level | You'll be able to… |
| --- | --- | --- |
| <span class="lvl lvl-100">L100</span> | Foundations | Explain AI/LLMs/prompts and why AI errs |
| <span class="lvl lvl-200">L200</span> | Working with AI | Prompt well; use RAG, Genie, AI Functions; know to evaluate |
| <span class="lvl lvl-300">L300</span> | Building with AI | Design agents, tools, multi-agent systems; ship software with AI |
| <span class="lvl lvl-400">L400</span> | Production & governance | Evaluate, secure, govern and cost-manage AI in production |

---

## 4. 30-term glossary quick-reference

**Model** — the trained thing you run. **Inference** — using it (what a prompt
does). **Training / fine-tuning** — teaching it (rare for you).
**LLM** — next-token text model. **Token** — ~¾ word; billing unit.
**Context window** — how much text it can see at once.
**Prompt / completion** — your input / its output. **System prompt** — standing
rules. **Temperature** — randomness dial.
**Hallucination** — confident made-up answer. **Grounding** — anchoring answers in
real provided info. **Knowledge cut-off** — its training end date.
**Embedding / vector** — meaning as numbers. **Semantic search** — search by
meaning. **RAG** — answer from your docs by retrieving relevant chunks.
**Chunk** — a passage of a document. **Vector search** — find nearest-meaning
items.
**Agent** — an LLM that uses tools and takes steps. **Tool / function calling** —
how it acts. **Agent loop** — reason→act→observe. **Harness** — the scaffolding
that makes a model an agent. **MCP** — standard way to connect tools.
**Multi-agent system** — a team of agents with a supervisor.
**Evaluation** — measuring quality. **LLM-as-a-judge** — a model grading outputs.
**Groundedness** — is the answer supported by the source? **Tracing** — a record
of each step, for debugging. **Guardrail** — a check enforcing rules outside the
prompt. **Prompt injection** — smuggled instructions hijacking the model.
**Unity Catalog** — the governance layer (who can see/do what).

*(Full glossary: [all ~200 terms](../glossary/index.md).)*

## See also

- **[Resources](index.md)** · **[Prompt Library](../prompt-library/index.md)** ·
  **[Glossary](../glossary/index.md)**
