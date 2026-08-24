---
tags:
  - L300
  - agents
---

# The agent loop <span class="lvl lvl-300">L300</span>

## In plain terms

An agent gets things done by running a **loop**: think a little, do one thing, look
at what happened, then decide the next thing — over and over until the goal is met
or it gives up. It's the AI version of how a person tackles an unfamiliar task:
try a step, see the result, adjust.

## How it works

The classic loop is **reason → act → observe**, repeated:

```
        ┌───────────────────────────────────────────┐
        │                                           │
        ▼                                           │
   1. REASON   "What should I do next to reach the goal?"
        │
        ▼
   2. ACT      call a tool  (search / query / API / code)
        │
        ▼
   3. OBSERVE  read the tool's result, add it to context
        │
        ▼
   4. DONE?  ── no ──────────────────────────────────┘
        │
       yes
        ▼
     final answer
```

The pieces that make the loop work:

- **Reasoning / planning** — the model decides the next step (and for hard tasks,
  may plan several ahead or break the goal into sub-tasks).
- **Tools** — the actions available (from read-only lookups to real operations).
- **Memory** — two kinds:
    - **Short-term:** the running context of this task (steps so far, tool
      results). Bounded by the [context window](../foundations/large-language-models.md).
    - **Long-term:** facts stored outside the model (a database, a vector index)
      that persist across sessions — how an agent "remembers" you tomorrow.
- **Stopping conditions** — a goal check, a step limit, a budget, or a human
  approval gate. Without these, agents can loop forever or run up cost.

!!! note "Connecting tools: MCP"
    A growing standard, the **Model Context Protocol (MCP)**, gives agents a
    common way to plug into external tools and data sources — think "a universal
    adapter" so the same agent can reach many systems without bespoke wiring.

## How Databricks does it

- The **Mosaic AI Agent Framework** implements this loop for you: you supply the
  tools (often **Unity Catalog functions**) and retrieval; it runs reason → act →
  observe and manages the messages.
- **Long-term memory** and retrieval lean on **Vector Search** and governed tables
  (and Lakebase for transactional agent state).
- **MLflow Tracing** records every turn of the loop — each thought, tool call and
  observation — which is essential for debugging why an agent did what it did.
- Databricks also supports **MCP** so agents can reach standardised tool servers.

## Pitfalls

!!! warning "Loops bite"
    - **Runaway loops.** Always cap steps/time/cost.
    - **Context overflow.** Long runs fill the window; summarise or externalise
      state to long-term memory.
    - **Silent tool failures.** If a tool errors and the agent ignores it, answers
      go wrong quietly — surface and handle failures.

## Try it

:material-flask: **Lab 5** builds a small tool-using agent and watches the loop in
MLflow traces.

## See also

- **[What is an agent?](what-is-an-agent.md)** — the concept.
- **[Harnesses & meta-harnesses](harnesses-and-meta-harnesses.md)** — what runs the loop.
- Glossary: **agent loop**, **reasoning**, **memory**, **MCP**, **tracing**.
