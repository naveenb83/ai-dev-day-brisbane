---
tags:
  - L300
  - agents
---

# Multi-agent systems <span class="lvl lvl-300">L300</span>

## In plain terms

Instead of one agent trying to do everything, a **multi-agent system (MAS)** uses
a **team of specialised agents** — each good at one thing — with a **supervisor**
that breaks the work up, hands pieces to the right specialists, and assembles the
result. It's the org-chart pattern applied to AI: a manager and focused experts
beat one generalist doing everything.

## How it works

The common shape is a **supervisor (or router)** over **worker agents**:

```
                        User request
                             │
                             ▼
                     ┌───────────────┐
                     │  SUPERVISOR   │  plans, routes, combines
                     └──┬────────┬───┬┘
              ┌─────────┘        │   └──────────┐
              ▼                  ▼              ▼
       ┌────────────┐   ┌──────────────┐  ┌────────────┐
       │  Research  │   │   SQL / data │  │   Writer   │
       │   agent    │   │    agent     │  │   agent    │
       └────────────┘   └──────────────┘  └────────────┘
```

Why split things up:

- **Specialisation** — a focused agent with the right tools and a tight prompt
  outperforms one bloated agent with fifty tools.
- **Smaller context** — each agent only carries what its job needs, so it stays
  within the [context window](../foundations/large-language-models.md) and stays
  cheaper.
- **Reuse & clarity** — specialists are easier to test, evaluate and swap.

Agents coordinate in a few patterns: a **supervisor** delegates (most common);
agents can run in a **pipeline** (output of one feeds the next); or **debate/
review** (one agent critiques another's work to improve quality).

## How Databricks does it

- **Agent Bricks — Multi-Agent Supervisor (MAS)** is the productised version: it
  coordinates multiple agents (for example a **Genie Space** for data questions
  plus a **Knowledge Assistant** for document questions) behind one interface,
  routing each request to the right specialist.
- The **Mosaic AI Agent Framework** lets you build custom supervisors and workers
  when you need bespoke logic.
- Everything is deployed on **Model Serving**, governed by **Unity Catalog**, and
  traced with **MLflow** — so you can see *which* agent did *what* on any request.
- The broader **[Omnigent](harnesses-and-meta-harnesses.md)** direction is this
  idea at enterprise scale: many agents and tools orchestrated over governed data.

## Pitfalls

!!! warning "MAS is powerful but costly to get right"
    - **Complexity & cost multiply.** More agents = more model calls, more
      latency, more places to fail. Start with one agent; add specialists only when
      justified.
    - **Routing errors cascade.** If the supervisor picks the wrong worker, the
      whole answer is wrong — evaluate the *routing*, not just the workers.
    - **Coordination overhead.** Passing context between agents can lose
      information; design the hand-offs deliberately.

## Try it

:material-flask: **Lab 5** starts with a single agent; a stretch goal adds a second
specialist behind a supervisor.

## See also

- **[Harnesses & meta-harnesses](harnesses-and-meta-harnesses.md)** — the orchestration idea.
- **[Building agents on Databricks](building-agents-on-databricks.md)** — the toolkit.
- Glossary: **multi-agent system**, **supervisor**, **router**, **worker agent**, **orchestration**.
