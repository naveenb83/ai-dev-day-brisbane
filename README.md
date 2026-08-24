# AI Dev Day Brisbane

An **L100 → L400 AI literacy encyclopedia**, glossary, prompt library and
hands-on Databricks labs — built for mixed-audience client dev days.

Rendered as a [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) site.
Every concept is explained **plain-English first, then "how Databricks does it"**,
and tagged by learning level so a beginner and an expert can use the same site.

## What's inside

- **Encyclopedia** — foundations → production, grouped by level.
- **Glossary** — plain-English terms, each with a Databricks note.
- **Prompt library** — how to write good prompts, templates, worked examples, and
  meta-prompting.
- **Hands-on labs** — exercises attendees run in their own Databricks workspace.
- **Facilitator guide** — run-of-day and prep checklists.

## Quick start (local preview)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve        # http://127.0.0.1:8000
```

## Repository layout

```
docs/                 # all content (Markdown)
  index.md            # home
  start-here/         # how to use the site, levels, prerequisites
  stylesheets/        # level badges + tweaks
mkdocs.yml            # site config + navigation
requirements.txt      # docs toolchain
tools/check_docs.py   # stdlib docs validator (nav / orphans / links)
.github/workflows/    # CI: strict build + gated Pages deploy
CONTRIBUTING.md       # authoring guide + house style
```

## Contributing & publishing

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the authoring template, house
style, tests, and how to publish to GitHub Pages once the repo is public.

## Status

Built section by section. Scaffold + "Start here" are in; encyclopedia sections,
glossary, prompt library, labs and facilitator guide follow as separate PRs.
