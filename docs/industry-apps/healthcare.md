---
tags:
  - Industry Apps
---

# Healthcare — App Lab

The **`workshop_demo.healthcare`** schema is a synthetic clinical dataset:
patients, encounters, diagnoses, claims and providers. Its headline outcome is
`readmitted_30d` — and every predictor is known at admission, so a readmission
model is honest.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `encounters` | `encounter_type`, `department`, `length_of_stay_days`, `age_at_encounter`, `readmitted_30d`. |
| `diagnoses` | `icd10_code`, `description`, `is_primary` (~1.8 per encounter). |
| `claims` | One per encounter: `billed_amount`, `paid_amount`, `status` (denied/pending = $0 paid). |
| `patients` | `birth_year`, `sex`, `insurance_type`, `state` (no names — synthetic). |
| `providers` | `provider_name`, `specialty`, `department`, `years_practising`. |

## Featured app: 30-Day Readmission Risk Explorer

A clinical-ops app that shows the **cohort of patients at risk of readmission**,
explains the drivers (length of stay, age, primary diagnosis), and lets a care
coordinator work a prioritised list before discharge.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Readmission Risk Explorer".
It reads (read-only) from workshop_demo.healthcare via a SQL warehouse using the Databricks
SQL connector.

Backend (FastAPI), parameterized:
- GET /api/at-risk?department=&min_los= -> encounters joined to patients and the primary
  diagnosis (diagnoses where is_primary), returning encounter_id, department, age_at_encounter,
  length_of_stay_days, primary icd10 description, and readmitted_30d as the known label; compute a
  simple risk score from age + LOS + diagnosis group and order desc.
- GET /api/encounter/{id} -> full detail: patient (birth_year, sex, insurance_type), provider,
  all diagnoses, and the claim (billed vs paid, status).
- GET /api/kpis?from=&to= -> encounter count, 30-day readmission rate, avg LOS, denial rate.
- GET /api/drivers -> readmission rate by age band, by department, and by top primary diagnoses.

Frontend (React):
- KPI tiles (readmission rate, avg LOS, denial rate).
- An at-risk worklist table with a risk badge and department/LOS filters.
- A detail drawer with diagnoses, provider and claim status.
- A "drivers" panel: bar charts of readmission rate by age band and department.
Aggregate in SQL; keep it clean and clinical.
```

!!! tip "Run it"
    Reads only. Data is fully synthetic (no real patients), but still treat the
    pattern as PHI-grade when you adapt it.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **ML readmission model** | Replace the rule score with a trained classifier. | `encounters` + `diagnoses` → Model Serving |
| 2 | **Length-of-stay forecast** | Predict LOS at admission for bed planning. | `encounters` predictors |
| 3 | **Denial & revenue-leakage** | Quantify unpaid billed amounts by department and status. | `claims.billed_amount` vs `paid_amount` |
| 4 | **Provider quality benchmarking** | Compare readmission/LOS by provider and specialty. | `providers` × `encounters` |
| 5 | **Diagnosis clustering** | Group encounters by ICD-10 patterns to find high-cost pathways. | `diagnoses.icd10_code` |
| 6 | **Ask-your-cohort (Genie)** | "Which department has the highest readmission rate over 65?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for healthcare

| App | What it does |
| --- | --- |
| **Claims Denial Analytics** | Finds where revenue leaks — denial/pending rates by department and payer. |
| **Provider Quality Scorecard** | Benchmarks clinicians on outcomes, LOS and volume. |
| **Capacity & LOS Planner** | Forecasts bed-days from admissions and predicted length of stay. |
| **High-Utiliser Care Management** | Identifies frequent-encounter patients for proactive care. |
| **Insurance Mix Analysis** | Profiles revenue and outcomes by `insurance_type`. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) ·
  [Guardrails & safety](../production-governance/guardrails-and-safety.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
