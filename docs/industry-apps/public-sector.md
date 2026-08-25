---
tags:
  - Industry Apps
---

# Public Sector — App Lab

The **`workshop_demo.public_sector`** schema is a local-government dataset:
facilities, **citizen service requests** with SLA targets, permit applications
and budgets. Open requests have null close dates, permits pile up under review,
and some budget lines overspend — so there's real work to surface.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `service_requests` | `category`, `priority`, `reported_at`, `resolution_days`, `target_days`, `within_target`, `status`. |
| `permits` | `permit_type`, `status`, `days_in_process`, `fee` (backlog lives in `under_review`). |
| `budgets` | `fiscal_year`, `service_area`, `ward`, `allocated_amount`, `spent_amount` (some overspend). |
| `facilities` | `facility_name`, `facility_type`, `ward`, `annual_operating_cost`. |

## Featured app: Citizen Service SLA & Backlog Dashboard

A dashboard for a council operations lead: **SLA compliance** on service requests
(are we hitting `target_days`?), the **permit backlog** (what's stuck under
review and for how long), and where both concentrate by ward and category.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Citizen Service SLA & Backlog Dashboard".
It reads (read-only) from workshop_demo.public_sector via a SQL warehouse using the Databricks
SQL connector.

Backend (FastAPI), parameterized:
- GET /api/sla?ward=&category=&from=&to= -> from service_requests: SLA compliance = share of closed
  requests with within_target = true, broken down by category and priority; return counts and %.
- GET /api/open-requests?ward= -> requests with status open (null closed_at): request_id, category,
  priority, reported_at, days-open (now - reported_at), target_days; order by most overdue.
- GET /api/permits/backlog -> permits where status = 'under_review': permit_type, ward,
  days_in_process, fee; order by days_in_process desc.
- GET /api/budget-variance?fiscal_year= -> budgets: service_area, ward, allocated_amount,
  spent_amount, variance and % over/under.
- GET /api/kpis -> SLA %, open request count, permits over 30 days in process, budget lines overspent.

Frontend (React):
- KPI tiles (SLA %, open requests, stuck permits, overspent lines).
- An SLA panel: bar chart of within-target % by category, with ward filter.
- An overdue-requests worklist with a days-open badge.
- A permit-backlog table and a budget-variance table (red for overspend).
Aggregate in SQL; handle open requests (null close) explicitly.
```

!!! tip "Run it"
    Reads only. Decide up front whether to *exclude* or *flag* open requests
    (null `closed_at`) — it changes every SLA number.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **Auto-categorise requests** | Classify free-text requests into service categories. | `ai_classify` over request text |
| 2 | **Permit turnaround predictor** | Estimate days-to-decision for a new application. | `permits.days_in_process` history |
| 3 | **Budget variance analyser** | Rank overspending service areas and wards. | `budgets.allocated_amount` vs `spent_amount` |
| 4 | **Demand forecast** | Project request volume by category for staffing. | `ai_forecast` over `service_requests` |
| 5 | **Ward priority ranking** | Composite score of backlog, SLA breaches and spend. | `service_requests`, `permits`, `budgets` |
| 6 | **Ask-your-council (Genie)** | "Which ward misses SLA most on high-priority requests?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for public sector

| App | What it does |
| --- | --- |
| **Permit Backlog Tracker** | Surfaces stuck applications and turnaround by permit type and ward. |
| **Budget Variance Analyser** | Allocated vs spent with drill-down to overspending lines. |
| **Ward Resource Allocation** | Balances staff/spend against demand and SLA performance. |
| **Service Demand Forecast** | Predicts request volume to plan crews and budgets. |
| **Facility Cost Benchmark** | Compares `annual_operating_cost` across facility types and wards. |

## Concepts & labs

- [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Lab 2 — AI Functions](../labs/lab-2-ai-functions.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
