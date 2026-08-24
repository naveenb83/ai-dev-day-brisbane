---
tags:
  - L200
  - agents
---

# Structured output & tools <span class="lvl lvl-200">L200</span>

## In plain terms

Two upgrades turn a chatty model into a **dependable component** you can wire into
software:

1. **Structured output** — instead of a paragraph, the model returns **clean,
   predictable data** (usually JSON) your code can read directly.
2. **Tool use (function calling)** — the model can **ask to run a function you've
   given it** — look up an order, do a calculation, search a database — and use
   the result in its answer.

Together they're the bridge from "nice demo" to "part of a system", and the first
step toward [agents](../index.md).

## How it works

**Structured output.** You describe the exact shape you want — a **schema** — and
the model fills it in:

```json
// You ask for this shape…
{ "sentiment": "positive | neutral | negative",
  "topics": ["string"],
  "urgent": true }
// …and get valid JSON back every time, ready to store or branch on.
```

No more parsing free text with fragile string-matching.

**Tool use.** You hand the model a menu of functions (each with a name,
description and inputs). Given a task, the model **chooses** whether to call one,
returns the call it wants ("`get_order(id=123)`"), your code runs it, and the
result goes back to the model to finish the answer.

```
User: "Where's my order 123?"
        │
Model decides ─► call get_order(id=123)      ◄── you run this
        │                                         returns {status:"shipped", eta:"Fri"}
        ▼
Model: "Order 123 shipped and arrives Friday."
```

This is how a model reaches beyond its training into **live, real systems** — the
core mechanic of agents.

## How Databricks does it

- **Foundation Model APIs** support **structured / JSON output** and **tool
  calling** on capable models.
- Tools can be **Unity Catalog functions** — governed SQL or Python functions your
  model is allowed to call — so tool use inherits your permissions and is
  auditable.
- The **Mosaic AI Agent Framework** builds on exactly this to create agents that
  combine retrieval, tools and reasoning (the [L300](../index.md) material).

## Pitfalls

!!! warning "Keep it robust"
    - **Validate the JSON.** Even with schemas, check it before acting on it.
    - **Least privilege for tools.** A tool that can *write* or *spend* needs
      guardrails and, often, a human confirmation step.
    - **Describe tools well.** The model picks tools from their descriptions —
      vague descriptions cause wrong or missed calls.

## See also

- **[Building with AI (L300)](../index.md)** — agents built on tools. *(Added later.)*
- **[Prompting that works](prompting-that-works.md)** — asking for a format.
- Glossary: **structured output**, **JSON schema**, **tool use**, **function calling**, **UC function**.
