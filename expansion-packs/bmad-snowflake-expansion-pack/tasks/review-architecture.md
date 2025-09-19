# Review Architecture

purpose: Progressive review of account/identity/governance/data-engineering/observability/finops
run:

- execute-checklist checklists/snowflake-architecture-checklist.md
- execute-checklist checklists/snowflake-security-checklist.md
- execute-checklist checklists/snowflake-performance-checklist.md
- execute-checklist checklists/snowflake-cost-checklist.md
- execute-checklist checklists/snowflake-data-engineering-checklist.md
  output: docs/reports/architecture-review-report.md
