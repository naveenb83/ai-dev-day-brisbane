#!/usr/bin/env python3
"""Lightweight docs validator (standard library only).

Mirrors the checks that `mkdocs build --strict` enforces, so it can run in
environments without network access to install MkDocs:

  1. Every ``.md`` referenced in ``mkdocs.yml`` exists under ``docs/``.
  2. Every ``.md`` under ``docs/`` is referenced in the nav (no orphan pages).
  3. Every relative Markdown link points at a file that exists (broken-link
     detection), ignoring pure ``#anchor`` and external ``http(s)/mailto`` links.

Usage:
    python3 tools/check_docs.py

Exit code is non-zero if any problem is found. This is the repo's docs "e2e"
test; CI additionally runs the real ``mkdocs build --strict``.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

# Markdown link: [text](target)  — capture the target.
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# Any docs-relative .md path token in mkdocs.yml.
NAV_MD_RE = re.compile(r"([A-Za-z0-9._/\-]+\.md)")


def nav_referenced_md() -> set[str]:
    # Strip inline comments so a `.md` mentioned in a comment isn't mistaken
    # for a nav reference.
    lines = []
    for line in MKDOCS.read_text(encoding="utf-8").splitlines():
        lines.append(line.split("#", 1)[0])
    text = "\n".join(lines)
    return {m.group(1) for m in NAV_MD_RE.finditer(text)}


def all_docs_md() -> set[str]:
    return {
        p.relative_to(DOCS).as_posix()
        for p in DOCS.rglob("*.md")
    }


# A nav item line: `- Title: path.md`. If the title is unquoted and itself
# contains a colon, YAML parsing breaks ("mapping values are not allowed here").
NAV_ITEM_RE = re.compile(r"^\s*-\s+(?P<title>.+?):\s+\S+\.md\s*$")


def check_nav_unquoted_colons() -> list[str]:
    """Catch nav titles with an unquoted colon that would break YAML parsing."""
    errors: list[str] = []
    for i, line in enumerate(MKDOCS.read_text(encoding="utf-8").splitlines(), 1):
        m = NAV_ITEM_RE.match(line)
        if not m:
            continue
        title = m.group("title").strip()
        if title.startswith(('"', "'")):
            continue  # quoted — safe
        if ":" in title:
            errors.append(f"  mkdocs.yml:{i}: unquoted colon in nav title "
                          f"'{title}' — wrap the title in quotes")
    return errors


def check_internal_links() -> list[str]:
    errors: list[str] = []
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            # Skip external, anchors, mail, and images handled elsewhere.
            if target.startswith(("http://", "https://", "mailto:", "#", "<")):
                continue
            # Strip any title:  (path "title")
            target = target.split(" ", 1)[0]
            # Drop anchor fragment.
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue  # was a pure "#anchor"
            # Only validate links to markdown/asset files inside the tree.
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                rel = md.relative_to(ROOT)
                errors.append(f"  {rel}: broken link -> {target}")
    return errors


def main() -> int:
    if not MKDOCS.exists() or not DOCS.exists():
        print("ERROR: run from repo root (mkdocs.yml and docs/ not found)")
        return 2

    nav = nav_referenced_md()
    docs = all_docs_md()

    problems: list[str] = []

    missing_files = sorted(nav - docs)
    if missing_files:
        problems.append("Nav references files that do not exist under docs/:")
        problems += [f"  - {f}" for f in missing_files]

    orphans = sorted(docs - nav)
    if orphans:
        problems.append("Pages under docs/ not referenced in nav (orphans):")
        problems += [f"  - {f}" for f in orphans]

    broken = check_internal_links()
    if broken:
        problems.append("Broken internal links:")
        problems += broken

    nav_colons = check_nav_unquoted_colons()
    if nav_colons:
        problems.append("Nav titles with unquoted colons (break YAML):")
        problems += nav_colons

    if problems:
        print("DOCS CHECK FAILED\n")
        print("\n".join(problems))
        print(f"\n{len(missing_files)} missing, {len(orphans)} orphan(s), "
              f"{len(broken)} broken link(s).")
        return 1

    print(f"DOCS CHECK OK — {len(docs)} pages, all in nav, no broken links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
