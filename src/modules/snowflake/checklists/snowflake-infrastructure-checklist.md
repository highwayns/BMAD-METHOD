# Snowflake Infrastructure Checklist (PM Gate)

updated: 2025-09-24
scope:

- Accounts & Regions
- Databases/Schemas/Stages
- Warehouses/Sizing/Auto suspend-resume
- Security/RBAC/ABAC/Tags/Masking/Row Policies
- Observability (SLIs/SLOs/Dashboards/Alerts/Runbooks)
- FinOps (Budgets/Resource Monitors/Unit Cost KPIs)
- DR/Replication/Failover
- CI/CD & GitOps integration

checks:
topology: - [ ] Account topology documented and approved - [ ] Environments (dev/preview/staging/prod) provisioned via IaC with rollback - [ ] Network & access patterns documented (privatelink/sgw as applicable)
security: - [ ] RBAC roles & grants reviewed; least-privilege verified - [ ] Data classifications tagged; masking/row policies attached & tested - [ ] Access History/Audit queries available to PM on request
observability: - [ ] SLIs/SLOs defined for availability/latency/freshness/error-rate/cost - [ ] Dashboards & alert routing configured with runbook links - [ ] Query tags convention agreed (release/build/owner)
finops: - [ ] Resource monitors created with thresholds & actions - [ ] Warehouse sizing policy documented (min/max/queues strategy) - [ ] Unit-cost KPIs & budget alerts wired to stakeholders
reliability: - [ ] DR/replication/backup strategy documented and tested - [ ] Canary/blue-green or rollback approach rehearsed
cicd: - [ ] GitOps pipelines (lint/test/plan/apply/verify/rollback) in place - [ ] Policy-as-code & contract tests block breaking changes
evidence: - [ ] Evidence pack (links/screenshots/SQL) attached - [ ] Owners & ETAs for remaining items

decision:

- [ ] GO
- [ ] NO-GO (list blockers and remediation plan)
