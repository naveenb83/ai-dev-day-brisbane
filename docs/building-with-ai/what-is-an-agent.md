---
tags:
  - L300
  - agents
---

# What is an agent? <span class="lvl lvl-300">L300</span>

## In plain terms

An **agent** is an LLM that's been given the ability to **take actions and work
toward a goal**, not just reply once. Instead of "here's an answer", it can decide
*"to answer this, I need to look up the order, check stock, then calculate a
refund"* — and actually do those steps, using **tools**, before responding.

The slogan: **a chatbot talks; an agent acts.**

## How it works

Three capabilities separate an agent from a plain chat model:

- **Tools** — functions it can call to reach the outside world: query a database,
  search documents, hit an API, run code. (See
  [Structured output & tools](../working-with-ai/structured-output-and-tools.md).)
- **A loop** — it can take a step, see the result, and decide the next step,
  repeating until the goal is met. (See [The agent loop](the-agent-loop.md).)
- **Memory** — it can carry state across steps (and sometimes across
  conversations), so it doesn't start from scratch each time.

Add a **goal** and some **autonomy** over which tools to use and in what order, and
you have an agent.

!!! example "Same request, chatbot vs agent"
    *"Has my order arrived and, if not, when will it?"*

    - **Chatbot:** "I can't access order systems, but generally shipping takes
      3–5 days." (Plausible, useless.)
    - **Agent:** calls `get_order(123)` → sees "in transit, ETA Friday" → replies
      "Order 123 is in transit and arrives **Friday**." (Real, useful.)

### How much autonomy?

Agents sit on a spectrum, and more autonomy is not automatically better:

| Level | What it does | Good for |
| --- | --- | --- |
| **Assistant** | Answers, suggests; a human acts | Drafting, Q&A |
| **Tool-using** | Calls read-only tools to fetch facts | Lookups, RAG, analysis |
| **Acting** | Takes real actions (writes, sends, spends) | Automation — with guardrails |
| **Autonomous** | Plans and pursues multi-step goals alone | Powerful; needs strong limits |

The right design usually uses the **least autonomy that does the job**, with humans
in the loop wherever an action is costly or hard to undo.

## How Databricks does it

- The **Mosaic AI Agent Framework** is the toolkit for building agents — wiring a
  model to tools (including **Unity Catalog functions**), retrieval and memory.
- **Agent Bricks** offers higher-level, ready-made agents: a **Knowledge
  Assistant** (document Q&A), **Genie Spaces** (data Q&A), and a **Supervisor**
  that coordinates several ([multi-agent systems](multi-agent-systems.md)).
- Agents are deployed on **Model Serving** and observed with **MLflow** — so an
  agent is a governed, monitored, evaluatable asset, not a black box.

## Pitfalls

!!! warning "Agent-specific risks"
    - **Over-autonomy.** Don't give write/spend power without confirmation steps
      and limits.
    - **Compounding errors.** A wrong step early can derail the whole run — good
      tools, prompts and evaluation matter more, not less.
    - **Cost & latency.** Each step is another model call; loops can get expensive.
      Cap steps and monitor.

## See also

- **[The agent loop](the-agent-loop.md)** — the mechanics.
- **[Harnesses & meta-harnesses](harnesses-and-meta-harnesses.md)** — the scaffolding.
- Glossary: **agent**, **tool**, **autonomy**, **human-in-the-loop**.
