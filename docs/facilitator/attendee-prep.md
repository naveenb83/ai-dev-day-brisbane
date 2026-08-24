# Attendee prep

Send this a few days before. Keep it short — the goal is people arrive able to
sign in, not stressed. Copy-paste and fill the `{brackets}`.

---

## What to send attendees

**Subject: Getting ready for the AI Dev Day ({date})**

Hi — a few quick things so you hit the ground running on the day. **None of this
requires any AI or coding experience.** If a step doesn't work, don't worry — we
fix access together in the first 15 minutes.

**1. You'll need**

- A laptop and a modern browser (Chrome, Edge, Firefox or Safari).
- Your sign-in details for the workspace: **{workspace URL}**
  *(login: {SSO / provided credentials})*.

**2. Please check before the day (5 minutes)**

- [ ] You can sign in to **{workspace URL}**.
- [ ] After signing in, you can see the workspace home screen.

That's it. If you can log in, you're ready.

**3. Nice to have (optional)**

- Skim **{link to the site's Start here / Foundations}** if you'd like a head
  start — but it's genuinely fine to arrive cold.
- Think of **one question you'd love to ask your own data**, or **one task you'd
  love to speed up**. We'll use real motivations during the labs.

**4. Please DON'T bring**

- Real customer data, passwords, or anything sensitive. We use **sample data
  only** in the shared training environment.

See you on the {date}!

---

## Facilitator setup checklist (your side)

Do these before attendees arrive:

- [ ] Workspace(s) provisioned with logins for every attendee (or SSO tested).
- [ ] A **SQL warehouse** available and started (or serverless enabled).
- [ ] A **training catalog/schema** each attendee can write to (e.g.
      `training.<name>`), or a shared one with clear guidance.
- [ ] **AI features** enabled: Playground access, Foundation Model API / AI
      Functions working (test `SELECT ai_gen('hi');`).
- [ ] A **serving endpoint** name attendees can use in Lab 2/4/5, written on a
      slide.
- [ ] **Vector Search** endpoint available for Lab 4 (or plan to demo it).
- [ ] Sample datasets loaded (or confirm the labs' inline `CREATE TABLE` data
      works in your environment).
- [ ] This site reachable by attendees (URL on a slide) — or offline copies ready.
- [ ] Wi-Fi tested; a backup plan for flaky access.
- [ ] Helpers briefed on the [two tracks](run-of-day.md) and common issues.

## See also

- **[Run of day](run-of-day.md)** · **[Prerequisites](../start-here/prerequisites.md)**
