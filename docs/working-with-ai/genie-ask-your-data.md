---
tags:
  - L200
---

# Genie: ask your data <span class="lvl lvl-200">L200</span>

## In plain terms

**Genie lets people ask questions of your data in plain English and get real
answers** — "What were sales in Queensland last month?" — without writing SQL.
It's a natural-language front door to your tables, aimed squarely at the
business users who know the questions but not the query language.

The critical thing that makes it trustworthy: **Genie doesn't guess the answer
from memory. It writes SQL, runs it against your actual tables, and shows you both
the number and the query it ran.** The answer is *computed*, not *recalled*.

## How it works

This is the general pattern behind "text-to-SQL" tools:

1. A user asks a question in English.
2. The model translates it into a SQL query, using the **table names, columns and
   descriptions** it's been given.
3. The query runs on the real data.
4. The result comes back as a number, table or chart — with the SQL on show so it
   can be checked.

The quality depends less on the model and more on **how well your data is
described**: clear table and column names, good descriptions, defined
relationships, and example questions. Garbage metadata → confidently wrong SQL.

!!! note "This is the theme of a whole readiness practice"
    Getting text-to-SQL trustworthy is mostly a *data curation* job — semantic
    descriptions, certified example queries, and governance. It's worth doing
    deliberately, not switching on and hoping.

## How Databricks does it

- **Genie** (part of Databricks AI/BI) provides the natural-language experience
  over your Unity Catalog tables, showing the generated SQL for transparency.
- You improve accuracy by curating a **Genie Space**: adding instructions,
  column descriptions, certified example SQL, and trusted metrics (**metric
  views**) so the model has a semantic layer to lean on.
- **Unity Catalog** governance still applies — Genie can only query what the user
  is permitted to see, and column masks/row filters are respected.
- **Agent Bricks Genie Spaces** package this for reuse across a team.

## Pitfalls

!!! warning "Set it up to succeed"
    - **Thin metadata = wrong SQL.** Invest in descriptions and example queries
      before judging accuracy.
    - **Ambiguous business terms.** "Revenue", "active user" and "region" often
      mean different things to different teams — define them (metric views help).
    - **Trusting a single answer.** Encourage users to read the generated SQL, and
      certify the queries that matter.

## Try it

:material-flask: **Lab 3** creates a Genie Space over sample tables and tunes it for
accuracy. *(Labs added in a later section.)*

## See also

- **[AI over your data](ai-over-your-data.md)** — the bulk-processing cousin.
- **[Why we evaluate](why-we-evaluate.md)** — measuring text-to-SQL accuracy.
- Glossary: **Genie**, **text-to-SQL**, **semantic layer**, **metric view**, **certified query**.
