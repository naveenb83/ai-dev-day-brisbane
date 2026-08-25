---
tags:
  - Industry Apps
---

# Financial Services — App Lab

The **`workshop_demo.financial_services`** schema spans both sides of a bank:
deposits and card **transactions with fraud labels**, and a lending book with
**monthly arrears snapshots**. The fraud and delinquency signals are real (and
deliberately imbalanced), so models built here actually work.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `transactions` | Card transactions: `amount` (log-normal), `category`, `channel`, `is_international`, `merchant_id`. |
| `fraud_labels` | One `is_fraud` per transaction — ~1% positive; accuracy is the *wrong* metric. |
| `merchants` | `category`, `country`, `risk_score` (crypto/travel run hotter). |
| `loans` | Lending book: `product`, `balance`, `interest_rate_pct`, `loan_to_value_pct`, `status`. |
| `arrears` | Monthly snapshot per loan: `days_past_due` (30/60/90/120+ buckets), `hardship_flag`. |
| `customers` / `accounts` / `branches` | Masters + `risk_rating`, account status, origination branch. |

## Featured app: Fraud Triage Console

A console for a fraud analyst: a **prioritised queue** of suspicious
transactions (high amount, risky merchant, international, off-pattern), each with
the context needed to approve or escalate, and a portfolio view of fraud rate by
merchant category and channel.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Fraud Triage Console".
It reads (read-only) from workshop_demo.financial_services via a SQL warehouse using the
Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/queue?min_amount=&channel=&international= -> recent transactions joined to
  merchants (risk_score, category, country) and customers (risk_rating, segment); compute a simple
  rule-based risk score (amount percentile + merchant risk_score + is_international + category) and
  return the top N ordered by that score. Include is_fraud from fraud_labels as "known outcome".
- GET /api/transaction/{id} -> full detail: customer, account, merchant, amount, category, channel.
- GET /api/kpis?from=&to= -> total transactions, fraud rate (%), $ at risk, top risky merchant category.
- GET /api/breakdown -> fraud rate by merchant category and by channel.

Frontend (React):
- KPI tiles (fraud rate, $ at risk, flagged count).
- A triage queue table with a risk badge, "known fraud" indicator, and filters (amount, channel, international).
- A detail drawer with full transaction + customer + merchant context and Approve/Escalate buttons (local state).
- A bar chart of fraud rate by merchant category.
Do scoring/aggregation in SQL where possible; keep it responsive.
```

!!! tip "Run it"
    Reads only. To persist analyst decisions (approve/escalate), deep-clone a
    `decisions` table into your own schema and write there.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **ML fraud scoring** | Replace the rule score with a trained model (handle the 1% imbalance). | `transactions` + `fraud_labels` → Model Serving |
| 2 | **Arrears early-warning** | Flag loans deteriorating across consecutive snapshots. | `arrears.days_past_due` by `snapshot_month` |
| 3 | **Branch origination quality** | Compare arrears rates by originating branch. | `loans` × `arrears` × `branches` |
| 4 | **Explain-this-transaction** | One-line natural-language rationale for why a txn is risky. | `ai_query` over the txn context |
| 5 | **Vintage / prepayment analysis** | Track balance pay-down by origination cohort. | `loans.originated_on`, `balance` |
| 6 | **Ask-your-portfolio (Genie)** | "What's the 90+ day arrears rate on unsecured loans?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for financial services

| App | What it does |
| --- | --- |
| **Credit Risk & Arrears Early-Warning** | Monitors delinquency migration and hardship flags across the loan book. |
| **Branch Performance Scorecard** | Ranks branches on origination volume, quality and arrears. |
| **Portfolio Vintage Analysis** | Balance and default curves by origination month and product. |
| **Customer 360 & Cross-Sell** | Unifies accounts, loans and transactions to spot next-best-product. |
| **Merchant Risk / AML Monitor** | Surfaces high-risk merchants and unusual international flows. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) (imbalanced metrics) ·
  [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
