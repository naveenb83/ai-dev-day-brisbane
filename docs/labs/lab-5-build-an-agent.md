---
tags:
  - L300
  - agents
---

# Lab 5 — Build an agent <span class="lvl lvl-300">L300</span>

**~35 minutes** · notebook (Python)

## Goal

Turn a model into an **agent** that can **use a tool** — so it answers from live
data instead of guessing. You'll see the [agent loop](../building-with-ai/the-agent-loop.md)
run for real.

## You'll learn

- How tool calling turns "I can't access that" into a real answer.
- Why a governed tool (a Unity Catalog function) is the safe way to give an agent
  power.

!!! note "Two doors"
    You can do this the **easy way** (Agent Bricks — configure a Knowledge
    Assistant or Genie Space, no code) or the **build way** (Mosaic AI Agent
    Framework, below). If you're new, try the easy way first. Exact framework APIs
    evolve — confirm in the current docs / the `databricks-model-serving` guidance.

## Steps (build way)

1. **Create a tool as a Unity Catalog function.** A governed function the agent is
   allowed to call — here, a stock lookup:
   ```sql
   CREATE OR REPLACE FUNCTION {your_catalog}.{your_schema}.get_stock(product STRING)
   RETURNS INT
   COMMENT 'Return units in stock for a product name.'
   RETURN CASE lower(product)
     WHEN 'battery' THEN 12
     WHEN 'panel'   THEN 0
     ELSE 5 END;
   ```
2. **Give the agent the tool.** In a notebook, wire the model to that UC function
   using the Agent Framework (illustrative):
   ```python
   # illustrative — confirm current API in docs
   # register the UC function as a tool, attach it to a chat model,
   # and let the framework run reason -> act -> observe.
   ```
3. **Set a clear system prompt** (see
   [agent system prompts](../prompt-library/databricks-prompts.md)):
   ```text
   You are a sales assistant. Use the get_stock tool to answer stock questions.
   If a product is out of stock, say so and suggest asking about alternatives.
   Never invent stock numbers.
   ```
4. **Ask it questions** that force a tool call:
   - "Do you have the battery in stock?" → should call `get_stock('battery')` → 12.
   - "Is the panel available?" → tool returns 0 → agent says out of stock.
5. **Watch the loop.** Look at the steps the agent took — the tool call and its
   result — not just the final answer.

## Expected result

- The agent calls your tool and answers from **real data** (12 in stock, panel out
  of stock) rather than guessing — and refuses to invent numbers.

## Stretch

- Add a second tool (e.g. `get_price`) and ask a question needing both.
- Add a supervisor over two specialist agents (see
  [multi-agent systems](../building-with-ai/multi-agent-systems.md)).
- Try the **Agent Bricks** door: build a Knowledge Assistant over the Lab 4 KB and
  compare the effort.

## Concepts

- **[What is an agent?](../building-with-ai/what-is-an-agent.md)** ·
  **[The agent loop](../building-with-ai/the-agent-loop.md)** ·
  **[Building agents on Databricks](../building-with-ai/building-agents-on-databricks.md)** ·
  Glossary: **agent**, **tool / function calling**, **UC function**, **agent loop**.
