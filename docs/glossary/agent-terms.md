---
tags:
  - L300
  - agents
---

# Glossary — Agents

The vocabulary of AI that acts. See [Building with AI](../building-with-ai/index.md).

**Agent**
:   An LLM given the ability to take actions (use tools), remember, and work
    toward a goal over multiple steps — not just answer once. "A chatbot talks; an
    agent acts."

**Agentic**
:   Describing systems with agent-like autonomy — taking multi-step actions toward
    goals.

**Tool**
:   A function an agent can call to reach the outside world — query a database, hit
    an API, run code, search documents. → *On Databricks:* often a governed Unity
    Catalog function.

**Tool use / function calling**
:   The mechanism by which a model asks to run a tool and uses the result. The core
    of agents and of connecting models to real systems.

**Agent loop**
:   The repeated cycle of **reason → act → observe** an agent runs until it reaches
    the goal or a stopping condition.

**Reasoning / planning**
:   The model deciding what to do next, or breaking a goal into steps.

**Memory (short-term / long-term)**
:   *Short-term:* the running context of the current task (bounded by the context
    window). *Long-term:* facts stored outside the model (a database or vector
    index) that persist across sessions.

**Scratchpad**
:   A working space where an agent writes intermediate thoughts/results during a
    task.

**Reflection**
:   An agent reviewing or critiquing its own output to improve it before finishing.

**Model Context Protocol (MCP)**
:   An emerging open standard giving agents a common way to connect to external
    tools and data sources — a "universal adapter" for tools.

**Harness**
:   The software scaffolding around a model that turns it into a working agent —
    prompt construction, the loop, tool execution, memory, guardrails, parsing. The
    model is the engine; the harness is the rest of the car. → *On Databricks:*
    the Mosaic AI Agent Framework; ready-made harnesses are Agent Bricks.

**Meta-harness**
:   A system that builds, configures or coordinates multiple agents/harnesses — a
    "harness for harnesses". → *On Databricks:* the direction of Omnigent, with the
    Agent Bricks Multi-Agent Supervisor as today's productised form.

**Orchestration**
:   Coordinating multiple steps, tools or agents to complete a task.

**Multi-agent system (MAS)**
:   A team of specialised agents coordinated (usually by a supervisor) to solve a
    task together. → *On Databricks:* Agent Bricks Multi-Agent Supervisor.

**Supervisor / router**
:   The coordinating agent that breaks work up, routes each piece to the right
    specialist, and combines results.

**Worker agent**
:   A specialised agent that handles one kind of sub-task within a multi-agent
    system.

**Autonomy**
:   How much an agent decides and does on its own. More isn't always better — use
    the least autonomy that does the job.

**Human-in-the-loop (HITL)**
:   Keeping a person in control of consequential actions — approving, correcting or
    overriding the AI.

**Omnigent**
:   The name associated with Databricks' work toward a general-purpose enterprise
    agent that orchestrates many agents and tools over governed data — a
    meta-harness. *(Fast-moving area; confirm current specifics in Databricks
    docs.)*
