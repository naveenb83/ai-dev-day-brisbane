---
tags:
  - L300
  - agents
---

# Building with AI <span class="lvl lvl-300">L300</span>

This is the builders' level. Up to now the model answered questions. Now it
**does things** — takes steps, uses tools, remembers, and works toward a goal.
That's an **agent**, and this section is about what agents are, how they're wired,
and how you build them on Databricks.

By the end you'll be able to sketch how an agent would solve a real task
end-to-end — including where it might go wrong.

## Pages in this section

<div class="grid cards" markdown>

-   :material-robot-outline: **[What is an agent?](what-is-an-agent.md)**

    ---

    From "answers questions" to "gets things done" — the key leap.

-   :material-sync: **[The agent loop](the-agent-loop.md)**

    ---

    Reason → act → observe → repeat. Tools, memory and planning.

-   :material-layers-triple-outline: **[Harnesses & meta-harnesses](harnesses-and-meta-harnesses.md)**

    ---

    The scaffolding that turns a model into an agent — and the systems that build
    agents. Then Databricks' Omnigent.

-   :material-account-group-outline: **[Multi-agent systems](multi-agent-systems.md)**

    ---

    Teams of specialised agents with a supervisor coordinating them.

-   :material-hammer-wrench: **[Building agents on Databricks](building-agents-on-databricks.md)**

    ---

    Agent Bricks, the Mosaic AI Agent Framework, and shipping to an endpoint.

</div>

!!! tip "Prerequisite"
    This builds directly on
    [Structured output & tools](../working-with-ai/structured-output-and-tools.md)
    from L200 — tool calling is the mechanic that makes agents possible.
