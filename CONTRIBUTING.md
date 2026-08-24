# Contributing & authoring guide

This repo is a **MkDocs Material** site. Content lives in `docs/`, navigation in
`mkdocs.yml`. This guide keeps every page consistent.

## Local preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # live preview at http://127.0.0.1:8000
```

Build a production copy:

```bash
mkdocs build --strict  # fails on broken links / missing nav / orphan pages
```

## Tests

Two gates run on every pull request (see `.github/workflows/ci.yml`):

1. **`python3 tools/check_docs.py`** — a standard-library validator (no install
   needed) that checks: every nav entry exists, no orphan pages, no broken
   internal links. Run it before you push.
2. **`mkdocs build --strict`** — the real build.

## House style

### The four levels

Tag every concept page by depth using front matter:

```yaml
---
tags:
  - L100      # foundations
  # L200 working with AI · L300 building · L400 production & governance
---
```

Add topic tags too where useful (`prompting`, `rag`, `agents`, `governance`,
`evaluation`, `cost`).

In prose, show a level with a badge span:

```html
<span class="lvl lvl-100">L100</span>
```

Classes: `lvl-100` `lvl-200` `lvl-300` `lvl-400`.

### The concept-page template

Vendor-neutral idea **first**, Databricks **second**. Use this skeleton:

```markdown
---
tags: [L200, rag]
---

# <Concept>

## In plain terms
One or two sentences, no jargon. What it is and why anyone should care.

## How it works
A little more depth. Still vendor-neutral — no product names yet.

## How Databricks does it
The same idea on Databricks. Name the products/features here (Genie, AI
Functions, Vector Search, Agent Bricks, Mosaic AI, MLflow, Unity Catalog).

## Try it
Link to the relevant hands-on lab, if any.

## Pitfalls
The mistakes people actually make.

## See also
- [Related page](../path/to/page.md)
- Glossary: **term**
```

Not every page needs every section, but keep the **order** so readers can
predict where things are.

### Writing rules

- **Plain English.** Explain, don't impress. Expand an acronym the first time.
- **Vendor-neutral before Databricks.** Concepts outlive products.
- **Be honest about limits.** Say when AI gets things wrong or when a claim is
  uncertain. Don't overstate.
- **Link generously** to the glossary and related pages.
- **Prefer examples** over abstractions — show a bad prompt next to a good one.
- **Only sample/synthetic data** in any lab instructions. Never real customer data.

### Admonitions

Use `!!! note`, `!!! tip`, `!!! warning`, `!!! danger`, `!!! example`. Reserve
`danger` for security / cost / data-leakage traps.

## Adding a page

1. Create the `.md` under `docs/…`.
2. Add it to `nav:` in `mkdocs.yml` (or it will fail the orphan check).
3. Run `python3 tools/check_docs.py`, then `mkdocs build --strict`.

## Branch & PR flow

- One PR per content section (Foundations, Working with AI, Building, Production,
  Glossary, Prompt Library, Labs, Facilitator Guide).
- Branch names: `pr-NN-<section>`.
- Every PR must pass CI before merge.

## Publishing the site

The repo is private during authoring. To publish once it's public:

1. **Settings → Pages → Source: GitHub Actions.**
2. **Settings → Secrets and variables → Actions → Variables →** add
   `PUBLISH_PAGES` = `true`.
3. Push/merge to `main` — the `deploy` job publishes to
   `https://naveenb83.github.io/ai-dev-day-brisbane/`.

Until `PUBLISH_PAGES` is set, the deploy job is skipped (no failing runs).
