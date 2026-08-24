---
tags:
  - L300
  - agents
---

# Building agents on Databricks <span class="lvl lvl-300">L300</span>

This page pulls the L300 ideas together into a practical picture of **how you
actually build and ship an agent on Databricks** — from "configure a ready-made
one" to "code a custom one".

## Two doors in

**Door 1 — Agent Bricks (configure, don't code).** For common jobs, start here:

- **Knowledge Assistant** — point it at documents; get a governed RAG Q&A agent.
- **Genie Space** — natural-language questions over your tables.
- **Multi-Agent Supervisor** — coordinate several agents behind one interface.

You configure data sources, instructions and guardrails — no framework code — and
it's deployed and monitored for you. Best for standard patterns and fast starts.

**Door 2 — Mosaic AI Agent Framework (build custom).** When you need bespoke
logic, tools or control flow, you code the agent in Python:

- Define **tools** — often **Unity Catalog functions** (governed SQL/Python), plus
  retrievers over **Vector Search**, and external tools (including via **MCP**).
- Wire the **reason → act → observe** loop and any memory.
- Log and package it with **MLflow**, then deploy to **Model Serving**.

## The build-to-run picture

```
   Author            Evaluate            Deploy             Operate
 ┌─────────┐       ┌───────────┐      ┌────────────┐     ┌────────────┐
 │ Agent    │      │ MLflow     │     │ Model       │    │ MLflow      │
 │ Bricks   │  ──► │ eval on an │ ──► │ Serving     │──► │ tracing +   │
 │ or Agent │      │ eval set   │     │ endpoint    │    │ monitoring  │
 │ Framework│      │ (judges)   │     │ (governed)  │    │ (drift,cost)│
 └─────────┘       └───────────┘      └────────────┘     └────────────┘
        └──────────────── Unity Catalog governs it all ──────────────┘
```

Two things are true at every stage:

- **Governance is built in.** Tools, data and the agent itself live under **Unity
  Catalog** — permissions, lineage and audit come along for free.
- **You can see inside.** **MLflow Tracing** records each step, so evaluation and
  debugging are possible rather than guesswork.

## From notebook to product

An agent that works in a notebook isn't done. Taking it to production is a
discipline of its own — evaluation, guardrails, monitoring, cost control — covered
in **[Production & Governance (L400)](../production-governance/index.md)**, and the app
around it is covered in **[Building software with AI](../vibe-coding/index.md)**.

## Pitfalls

!!! warning "Common starting mistakes"
    - **Coding a custom agent when Agent Bricks would do.** Try Door 1 first.
    - **Ungoverned tools.** Prefer Unity Catalog functions so tool use is
      permissioned and audited.
    - **Shipping without an eval set.** You won't know if a change helped or hurt.

## Try it

:material-flask: **Lab 5** builds an agent with tools; **Lab 6** evaluates and traces
it.

## See also

- **[Harnesses & meta-harnesses](harnesses-and-meta-harnesses.md)** — the framework as a harness.
- **[Multi-agent systems](multi-agent-systems.md)** — the Supervisor.
- Glossary: **Agent Bricks**, **Mosaic AI Agent Framework**, **Model Serving**, **UC function**, **MCP**.
