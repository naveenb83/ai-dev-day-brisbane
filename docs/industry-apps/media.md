---
tags:
  - Industry Apps
---

# Media & Entertainment — App Lab

The **`workshop_demo.media`** schema is a streaming service: viewers,
subscriptions, a content catalog, **viewing events** and a `churn_labels` table
whose signal genuinely lives in viewing behaviour — so an engagement-based churn
model beats the base rate.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `view_events` | Viewing sessions (9 months): `content_id`, `watched_minutes`, `completion_pct` (bimodal), `device`. |
| `churn_labels` | Per-viewer `churned` + 60-day features (`recent_sessions`, `avg_completion`). |
| `subscriptions` | `plan`, `monthly_price`, `started_on`, `cancelled_on`, `is_active`. |
| `content` | `title`, `content_type`, `genre`, `is_original`, `runtime_minutes`. |
| `viewers` | `age_band`, `country`, `household_size`, `signed_up_on`. |

## Featured app: Churn & Engagement Cockpit

A retention app that combines **who's at risk of churning** with **why** —
falling sessions, low completion, plan tier — and lets a retention manager work a
prioritised list and see which content keeps people subscribed.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Churn & Engagement Cockpit".
It reads (read-only) from workshop_demo.media via a SQL warehouse using the Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/at-risk?plan= -> churn_labels joined to viewers and subscriptions: viewer_id, plan,
  monthly_price, recent_sessions, avg_completion, churned (known label); compute a risk score from
  low recent_sessions + low avg_completion + out-of-plan signals; order desc.
- GET /api/viewer/{id} -> viewer profile + subscription + recent view_events (content title, genre,
  completion_pct, device).
- GET /api/kpis -> active subscribers, churn rate, MRR (sum monthly_price where is_active),
  avg completion.
- GET /api/content-engagement -> by genre and is_original: total watched_minutes, avg completion_pct,
  unique viewers.

Frontend (React):
- KPI tiles (subscribers, churn rate, MRR).
- An at-risk viewer worklist with risk badge and plan filter.
- A viewer drawer: engagement sparkline + recent titles watched.
- A content-engagement panel: bar chart of avg completion by genre, originals vs licensed toggle.
Aggregate in SQL; keep it snappy.
```

!!! tip "Run it"
    Reads only. To log retention actions/offers, deep-clone an `actions` table
    into your own schema and write there.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **ML churn model** | Trained classifier on 60-day engagement features. | `churn_labels` + `view_events` → Model Serving |
| 2 | **Content recommender** | "Because you watched…" from co-viewing patterns. | `view_events` co-occurrence |
| 3 | **Completion analysis** | Explain the bimodal `completion_pct` (bail vs binge). | `view_events.completion_pct` |
| 4 | **Plan-tier A/B view** | Compare churn and engagement across plans. | `subscriptions.plan` |
| 5 | **Genre performance** | Which genres drive watch-time and retention. | `content.genre`, `view_events` |
| 6 | **Ask-your-audience (Genie)** | "What's the churn rate for viewers under 25 on the basic plan?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for media

| App | What it does |
| --- | --- |
| **Content Recommender** | Personalised "recommended for you" from viewing history. |
| **Genre Performance Dashboard** | Watch-time, completion and retention lift by genre. |
| **Engagement Segmentation** | Clusters viewers (bingers, dabblers, lapsers) for targeting. |
| **Retention Cohort Analysis** | Survival curves by signup cohort and plan. |
| **Original Content ROI** | Compares originals vs licensed on engagement and retention. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) ·
  [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
