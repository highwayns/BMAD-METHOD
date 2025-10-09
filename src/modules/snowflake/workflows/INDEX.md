# BMAD Snowflake Workflows - Index

**Total Workflows**: 273
**Last Updated**: 2025-10-08
**Version**: v5

---

## Quick Navigation by Domain

### Architecture (10 workflows)
- capacity-plan
- create-account-architecture
- create-architect-brief
- create-doc-snowflake-architecture
- create-platform-brief
- create-snowflake-architecture
- dim-fact-modeling
- feature-store-design
- metric-layer
- review-architecture
- semantic-model

### Security & Governance (19 workflows)
- abac-tags-plan
- access-audit-analytics
- access-policy
- access-review
- governance-access
- masking-policies
- masking-row-policy
- network-policies
- object-ownership
- rbac-abac-declarative
- rbac-blueprint
- rbac-lockout-incident
- row-access-policies
- security-governance
- security-policy-change
- security-privacy
- security-tests
- secrets-keys
- sso-scim-oauth

### Data Engineering (29 workflows)
- build-dbt-project
- cdc-plan
- copy-load-plan
- create-engineering-blueprint
- create-ingestion-plan
- create-ingestion-spec
- create-transformation-blueprint
- dq-plan
- dq-rulebook
- dq-rules
- dq-streaming-plan
- dynamic-tables-plan
- dynamic-tables-promo
- dynamic-tables-refresh
- elt-pipelines
- event-contract
- external-stage-config
- file-format-config
- kafka-connector-plan
- mv-dt-plan
- ordering-dedup-plan
- pruning-clustering
- schema-contract
- snowpipe-plan
- snowpipe-streaming-plan
- sql-migration-plan
- streaming-pipeline
- streaming-pipelines
- streams-tasks-dt-promo
- watermark-backfill-plan

### Analytics & BI (9 workflows)
- analysis-plan
- bi-dataset-contract
- bi-release
- create-analytics-plan
- dashboard-spec
- dashboards-plan
- kpi-tree
- metric-spec
- metrics-catalog

### ML/AI (16 workflows)
- ai-governance
- batch-scoring
- bias-fairness
- ci-cd-mlops
- drift-detection
- evaluation-plan
- experiment-plan
- hyperparam-tuning
- labeling-plan
- ml-release
- model-card
- monitoring-drift
- realtime-scoring
- registry-release
- retraining-schedule
- snowpark-components
- training-plan

### Observability (12 workflows)
- alerts-routing
- anomaly-detection
- create-observability-plan
- data-quality-observability
- monitoring-plan
- o11y-ci-cd
- o11y-hooks
- observability-plan
- observability-slo
- snowpipe-streaming-observability
- tasks-dt-observability
- warehouse-observability

### FinOps (20 workflows)
- budget-forecast
- cost-attribution-tags
- cost-forecast
- cost-inventory
- cost-reliability-signals
- cost-tests
- create-finops-plan
- create-pricing-plan
- credit-exhaustion
- dynamic-tables-cost
- finops-guardrails
- finops-plan
- finops-runbook
- finops-security
- replication-egress
- resource-monitor-trigger
- resource-monitors
- sharing-marketplace-cost
- showback-chargeback
- snowpipe-cost
- sos-mv-dt-roi
- warehouse-rightsizing

### Release Management (16 workflows)
- canary-bluegreen
- change-calendar
- ci-cd
- freeze-window
- gate-check
- gitops-pipelines
- go-live
- post-deploy-verification
- post-release-verification
- release-gates
- release-hooks
- release-notes
- release-plan
- release-train-plan
- rollback-plan

### Incident Management (15 workflows)
- close-incident
- data-corruption
- incident-analytics
- incident-breach
- incident-intake
- incident-postmortem
- incident-runbook
- incident-security
- post-incident-review
- postmortem
- snowflake-dynamic-table-lag
- snowflake-query-failures
- snowflake-task-failures
- snowflake-warehouse-incident
- streaming-ingest-incident
- war-room

### Compliance & Privacy (20 workflows)
- audit-forensics
- audit-reporting
- compliance-audit-pack
- compliance-calendar
- compliance-mapping
- consent-purpose
- data-classification
- dpia-pia
- dsr-handling
- evidence-pack
- lawful-basis-mapping
- minimization-pseudonymization
- posture-review
- privacy-by-design-review
- purpose-limitation
- quarterly-posture-review
- retention-deletion
- retention-lifecycle
- risk-assessment
- ropa-register
- vendor-dpa

### Operations (34 workflows)
- backup-retention
- change-management
- change-rfc
- create-dr-strategy
- dr-bcp-plan
- env-provisioning
- oncall-rotation
- oncall-setup
- performance-ops
- platform-runbook
- policy-as-code
- problem-management
- provision-environments
- replication-failover
- rfc-new
- runbook-incidents
- runbooks-index
- scheduling-policies
- status-page
- task-scheduler-ops
- validate-infrastructure
- warehouse-ops
- warehouse-policy-change

### Data Governance (16 workflows)
- catalog-discovery
- contract-ci
- contract-tests
- contract-versioning
- create-contract-suite
- create-data-contract
- create-data-contracts
- create-governance-policy
- data-contract
- data-inventory
- data-sharing-governance
- dataset-versioning
- lineage-and-catalog
- lineage-catalog
- versioning-deprecation

### Data Sharing (6 workflows)
- consumer-onboarding
- create-data-sharing-contract
- create-marketplace-listing
- cross-border-sharing
- marketplace-governance
- marketplace-sharing
- producer-onboarding

### Testing & QA (18 workflows)
- acceptance
- contract-tests
- cost-tests
- coverage-report
- create-acceptance
- flaky-tests
- performance-tests
- pipeline-tests
- qa-test-plan
- schema-tests
- security-tests
- synthetic-data
- test-cicd
- test-data-management
- testing-data
- testing-plan
- uat-scripts
- uat-signoff
- uat-support
- verification

### Project Management (10 workflows)
- bug-triage
- comms-plan
- create-backlog
- create-brd
- create-prd
- create-roadmap
- create-stakeholder-map
- monthly-review
- stakeholder-map
- triage

### Developer Experience (9 workflows)
- developer-kpis
- docsite-generation
- golden-paths
- project-scaffold
- scaffolding
- selfservice-portal
- service-catalog
- sql-styleguide
- training-awareness

### Optimization (6 workflows)
- freshness-sla
- performance-tuning
- query-optimization
- query-reliability
- slislos-contract
- sos-acceleration

---

## Workflow Types

### Document Workflows (206)
Generate structured markdown documents using templates.

### Action Workflows (67)
Execute actions, validations, or interactive processes without document generation.

---

## Using Workflows

Each workflow is located in its own directory:
```
bmad/snowflake/workflows/[workflow-name]/
├── workflow.yaml        # Configuration and metadata
├── instructions.md      # Step-by-step execution instructions
└── template.md         # Output template (document workflows only)
```

### Execution
Workflows are executed through the BMAD workflow engine:
```
{project-root}/bmad/core/tasks/workflow.xml
```

### Configuration
All workflows reference:
```
{project-root}/bmad/snowflake/config.yaml
```

### Output
Workflow outputs are organized by domain:
```
{output_folder}/[domain]/[workflow-name]-{{date}}.md
```

---

## Related Documentation

- **Conversion Report**: `CONVERSION-REPORT.md`
- **Configuration**: `../config.yaml`
- **Checklists**: `../checklists/`
- **Data Files**: `../data/`
- **Agents**: `../agents/`

---

**Index Generated**: 2025-10-08
**BMAD Version**: v5
**Snowflake Module Version**: 1.0.0
