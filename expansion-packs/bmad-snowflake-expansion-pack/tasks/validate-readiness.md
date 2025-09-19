# Validate Readiness

purpose: 16-域 Snowflake 平台就绪度验证（架构/身份/网络/治理/数据工程/共享/可观测/成本/DR）
run:

- execute-checklist checklists/snowflake-architecture-checklist.md
- execute-checklist checklists/snowflake-dr-readiness-checklist.md
  deliverable: docs/reports/snowflake-readiness-report.md
