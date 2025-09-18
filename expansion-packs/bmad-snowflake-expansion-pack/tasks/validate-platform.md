# Validate Platform End-to-End

purpose: 16-域平台就绪度校验（账户、身份、网络、安全、治理、数据工程、共享、可观测、成本等）
run:

- execute-checklist checklists/snowflake-readiness-checklist.md
- execute-checklist checklists/snowflake-performance-tuning-checklist.md
- execute-checklist checklists/snowflake-cost-optimization-checklist.md
  deliverable: docs/reports/snowflake-platform-validation-report.md
