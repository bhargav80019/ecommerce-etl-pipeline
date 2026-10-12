# Automated E-Commerce Data Pipeline & Analytics Dashboard

An end-to-end, enterprise-ready data pipeline that automates the daily extraction, transformation, and ingestion of e-commerce retail data using Python, GitHub Actions, and Power BI.

---

## Architecture Overview

```text
[ External API / Source ]
           │
           ▼
[ Python ETL Script (pipeline.py) ]
  • Extraction: Requests library (API ingestion)
  • Transformation: Pandas (schema validation, currency handling, date formatting)
           │
           ▼
[ GitHub Actions CI/CD (pipeline.yml) ]
  • Daily cron scheduler (Cloud-based Ubuntu runner)
  • Automated execution & push of updated dataset
           │
           ▼
[ Cleaned Cloud Data (clean_data.csv) ]
           │
           ▼
[ Microsoft Power BI Dashboard ]
  • Web connector integration
  • KPI tracking: Average price, SKU counts, category distribution
