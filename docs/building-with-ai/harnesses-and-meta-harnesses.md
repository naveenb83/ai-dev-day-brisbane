---
tags:
  - L300
  - agents
---

# Harnesses & meta-harnesses <span class="lvl lvl-300">L300</span>

## In plain terms

A raw language model can't *do* anything on its own — it just turns text in into
text out. To make it act like an agent, you wrap it in software that feeds it the
right prompts, runs the tools it asks for, remembers results, handles errors and
enforces limits. **That wrapper is the harness.**

> **The model is the engine. The harness is the rest of the car** — steering,
> pedals, dashboard, brakes. Same engine, very different vehicle depending on the
> harness around it.

A **meta-harness** goes one level up: it's a system that **builds, configures or
coordinates harnesses/agents** — a harness *for harnesses*. Instead of running one
agent, it stands up and directs *many*.

## How it works

### The harness

A harness is everything around the model that makes an agent work:

- **Prompt construction** — assembling the system prompt, history, retrieved
  context and tool definitions into each request.
- **The loop** — running [reason → act → observe](the-agent-loop.md) until done.
- **Tool execution** — actually calling the functions the model asks for and
  feeding results back.
- **Memory** — short-term scratchpad and long-term stores.
- **Guardrails** — input/output checks, step and cost limits, human-approval
  gates.
- **Parsing & error handling** — turning messy model output into actions, and
  recovering when a step fails.

!!! example "You've used harnesses"
    A coding assistant that reads your repo, edits files, runs tests and iterates
    is a **harness** around a model. So is a customer-support agent that looks up
    orders and drafts replies. The intelligence is the model; the *usefulness*
    comes largely from a good harness.

### The meta-harness

As soon as you have more than one agent — a researcher, a coder, a reviewer — you
need something to **create, route between and manage** them. That's the
meta-harness. It typically:

- **spins up** specialised agents (each its own harness) on demand;
- **routes** a task to the right agent(s);
- **coordinates** their work and combines results;
- provides **shared** memory, tools, governance and observability across all of
  them.

```
                 ┌──────────────── META-HARNESS ────────────────┐
                 │  routes tasks · spins up agents · coordinates  │
                 │  shared memory · shared tools · governance     │
                 └───────┬───────────────┬───────────────┬───────┘
                         │               │               │
                  ┌──────▼─────┐  ┌──────▼─────┐  ┌──────▼─────┐
                  │  HARNESS   │  │  HARNESS   │  │  HARNESS   │
                  │  (agent A) │  │  (agent B) │  │  (agent C) │
                  │ model+loop │  │ model+loop │  │ model+loop │
                  │  +tools    │  │  +tools    │  │  +tools    │
                  └────────────┘  └────────────┘  └────────────┘
```

This is the natural bridge to [multi-agent systems](multi-agent-systems.md).

## How Databricks does it

The general ideas map onto Databricks like this:

- **The harness → the Mosaic AI Agent Framework.** It gives you the loop, tool
  wiring (including governed **Unity Catalog functions**), retrieval, memory and
  the packaging to deploy an agent to **Model Serving**, all observable through
  **MLflow**. You supply the model, tools and logic; the framework is the harness.
- **Ready-made harnesses → Agent Bricks.** A **Knowledge Assistant** or a **Genie
  Space** is a pre-built harness for a common job — you configure rather than build
  from scratch.
- **The meta-harness → Omnigent (and the Agent Bricks Supervisor).** Databricks'
  work toward a **general-purpose enterprise agent** — often referred to as
  **Omnigent** — is the meta-harness idea: a system that orchestrates many
  specialised agents and tools over your governed data, so one request can be
  decomposed and routed across them. The **Multi-Agent Supervisor** in Agent
  Bricks is the productised, usable form of this coordination today.

!!! note "The agent landscape moves fast"
    Product names and capabilities in the agent space change quickly. Treat the
    Databricks names here as *pointers to the concept* and confirm current
    specifics in the Databricks documentation. The **concept** — model → harness →
    meta-harness — is stable and worth learning; the products are how a given
    platform packages it this quarter.

## Pitfalls

!!! warning "Where teams trip"
    - **Blaming the model for a weak harness.** Poor tool descriptions, no memory
      and no guardrails make even a great model look dumb.
    - **Reaching for a meta-harness too early.** One well-built agent beats a
      fleet of shaky ones. Add coordination only when a single agent genuinely
      can't cover the job.
    - **No observability.** Without tracing across the harness(es), multi-step
      failures are impossible to debug.

## See also

- **[The agent loop](the-agent-loop.md)** — what a harness runs.
- **[Multi-agent systems](multi-agent-systems.md)** — meta-harnesses in action.
- **[Building agents on Databricks](building-agents-on-databricks.md)** — the tools.
- Glossary: **harness**, **meta-harness**, **agent framework**, **orchestration**, **Omnigent**.
