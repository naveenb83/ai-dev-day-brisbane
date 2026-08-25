---
tags:
  - Industry Apps
---

# Superannuation — App Lab

The **`workshop_demo.superannuation`** schema is an Australian pension fund:
members, **contributions**, investment options, holdings and a `rollout_labels`
table (did the member roll their balance to another fund?). Rollout is driven by
disengagement, small balances and no insurance — so retention modelling works.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `rollout_labels` | Per member: `rolled_out`, `destination_fund`, `contributed_12m`, `contributions_12m`, `last_contribution_at`. |
| `members` | `balance` (log-normal on age), `account_status`, `employer_name`, `insurance_cover`. |
| `contributions` | `contribution_type`, `amount`, `received_at` (employer SG gaps signal underpayment). |
| `investment_options` | `risk_profile`, `growth_allocation_pct`, `benchmark_return_pct`, `fee_bps`. |
| `member_holdings` | `option_id`, `units`, `balance` (most hold only the MySuper default). |

## Featured app: Member Rollout (Retention) Risk

A retention app that ranks members by **rollout risk**, explains the drivers
(no recent contributions, small balance, no insurance, default-only investment),
and gives a retention team a prioritised outreach list.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Member Rollout Risk".
It reads (read-only) from workshop_demo.superannuation via a SQL warehouse using the Databricks
SQL connector.

Backend (FastAPI), parameterized:
- GET /api/at-risk?state= -> rollout_labels joined to members: member_id, state, balance,
  insurance_cover, contributed_12m, contributions_12m, last_contribution_at, rolled_out (known label);
  compute a risk score from no/low recent contributions + small balance + no insurance; order desc.
- GET /api/member/{id} -> member profile + contributions timeline + holdings (option_name, balance)
  joined to investment_options.
- GET /api/kpis?state= -> total members, rollout rate, funds under management (sum balance),
  % with no contribution in 6+ months, % default-only.
- GET /api/drivers -> rollout rate by balance band, by insurance_cover, by engagement (contributions_12m).

Frontend (React):
- KPI tiles (rollout rate, FUM, disengaged %).
- An at-risk member worklist with risk badge and state filter.
- A member drawer: contributions timeline (spot employer-SG gaps) + holdings breakdown.
- A drivers panel: bar charts of rollout rate by balance band and insurance status.
Aggregate in SQL; keep it clean.
```

!!! tip "Run it"
    Reads only. To record outreach outcomes, deep-clone an `outreach` table into
    your own schema and write there.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **ML rollout model** | Trained retention classifier (imbalanced). | `rollout_labels` + `members`/`contributions` → Model Serving |
| 2 | **Contribution compliance audit** | Detect employer-SG payment gaps per member. | `contributions.received_at` cadence |
| 3 | **Account consolidation** | Flag members likely to have multiple funds to consolidate. | `contributions`, `rollout_labels` |
| 4 | **Insurance take-up** | Target uninsured members for cover offers. | `members.insurance_cover` |
| 5 | **Retirement readiness** | Project balance-at-retirement by age and contribution rate. | `members.balance`, `contributions` |
| 6 | **Ask-your-fund (Genie)** | "What's the rollout rate for members under $10k with no insurance?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for superannuation

| App | What it does |
| --- | --- |
| **Contribution Compliance Audit** | Surfaces employer underpayment gaps and at-risk members. |
| **Retirement Readiness** | Projects retirement balances and flags members off-track. |
| **Fee Benchmarking** | Compares `fee_bps` and returns across investment options. |
| **Account Consolidation** | Identifies multi-fund members and quantifies the opportunity. |
| **Default Option Performance** | Tracks MySuper default outcomes vs benchmarks. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) ·
  [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
