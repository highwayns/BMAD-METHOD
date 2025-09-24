# Validate Infrastructure Readiness (Pre-Prod Gate)

type: task
id: pm-validate-infrastructure
owner: Product Manager
updated: 2025-09-24

intent: |
Validate that Snowflake infrastructure and guardrails are ready for feature delivery,
passing the PM-owned pre-production gate.

inputs:

- checklists/snowflake-infrastructure-checklist.md
- evidence from DevEx/SRE/Security/FinOps (dashboards, monitors, policies)

steps:

- Execute checklist with owners
- Collect evidence links (dashboards, resource monitors, RBAC audits)
- Record GO/NO-GO and remediation plan
- Publish `docs/gates/preprod-infra-validation-2025-09-24.md`

outputs:

- docs/gates/preprod-infra-validation-2025-09-24.md

acceptance_criteria:

- ✅ All MUST items passed; SHOULD items have owners/ETA
- ✅ Evidence attached and traceable
- ✅ Decision communicated to release/change manager
