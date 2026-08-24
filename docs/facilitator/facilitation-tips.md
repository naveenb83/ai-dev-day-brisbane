# Facilitation tips

Teaching AI to a room of mixed backgrounds and companies is its own skill. Here's
what helps.

## Running a mixed-level room

- **Name the levels early.** Tell people about L100–L400 and the two tracks so
  nobody feels lost or held back. "There's a lane for everyone today" is worth
  saying out loud.
- **Explain, then name.** Say the plain-English idea *before* the product name —
  the same shape as the site. "A place to find things by meaning… on Databricks
  that's Vector Search." Beginners follow; experts get the mapping.
- **Pair people up.** A confident builder next to a nervous beginner helps both.
- **Protect the beginners from jargon.** When an expert asks a deep question,
  answer briefly and offer to go deeper at the break — don't lose the room.
- **Celebrate small wins.** The first generated sentence, the first Genie answer —
  make a moment of it. Confidence is the real deliverable.

## The demos that land

- **Weak → strong prompt**, live. Type a lazy prompt, get a mediocre answer,
  then improve it in front of them. Instant, universal "aha".
- **Hallucination on purpose.** Ask a bare model about "our refund policy"; watch
  it invent one. Then ground it. Nobody forgets the lesson.
- **Genie showing its SQL.** Ask a question, reveal the query. "It didn't guess —
  it computed" builds trust.
- **Indirect prompt injection**, described. A webpage that tells an agent to leak
  data. Sobering, memorable, and it makes governance feel necessary, not boring.

## Questions you'll get (and crisp answers)

- **"Will this replace my job?"** → It changes tasks more than jobs; the skill
  becomes directing and checking AI. Today you're building exactly that skill.
- **"Can it use our real data?"** → Yes — that's the point of doing it on a data
  platform — but under governance, and today we use sample data only.
- **"Is it accurate?"** → Not automatically. That's why we ground it in your data
  and *evaluate* it. Accuracy is something you build, not assume.
- **"Should we fine-tune?"** → Usually not first. Prompt, then give it your data
  (RAG), then tools. Fine-tuning is far down the list. (See
  [Customizing a model](../building-with-ai/model-customization.md).)
- **"Is our data safe?"** → Governance (Unity Catalog) controls what the AI can
  see; least privilege is the strongest safeguard. (See
  [Governance](../production-governance/governance.md).)

## When things go wrong

- **Setup is eating the morning.** Everything depends on Lab 0 — spend the time,
  use helpers, and demo Lab 1 from the front while stragglers catch up.
- **An API/menu has moved.** Expected — the platform evolves. Model calm: use
  workspace search, check the in-product docs, and move on. The *concept* is the
  lesson, not the exact button.
- **A lab's code errors in your environment.** Have the endpoint names and a known
  dataset ready; fall back to demoing while attendees watch.
- **The room splits in pace.** Lean on stretch goals for the fast group and the
  no-code (Agent Bricks) paths for the rest.

## Leave them with next steps

Close by pointing at **[Resources](../resources/index.md)** and the
[cheat-sheets](../resources/cheat-sheets.md), and give one concrete "try this
Monday" suggestion tied to their own work.

## See also

- **[Run of day](run-of-day.md)** · **[Attendee prep](attendee-prep.md)**
