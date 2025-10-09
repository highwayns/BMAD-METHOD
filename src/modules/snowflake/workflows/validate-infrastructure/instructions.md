# Validate Infrastructure - Instructions

<critical>The workflow execution engine is governed by: {project_root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project_root}/bmad/snowflake/workflows/validate-infrastructure/workflow.yaml</critical>

<workflow>

<step n="1" goal="Load Checklist and Context">
<action>Load the infrastructure checklist: {project-root}/bmad/snowflake/checklists/snowflake-infrastructure-checklist.md</action>
<action>Review checklist structure and validation categories</action>
<action>Understand MUST vs SHOULD item priorities</action>
<ask>Do you have evidence ready (dashboards, monitors, policies, audit reports)? (y/n)</ask>
<check>If no:</check>
  <action>Guide user to collect evidence from:</action>
  - DevEx/Platform team: Infrastructure dashboards
  - SRE: Monitoring and alerting setup
  - Security: RBAC audits and access policies
  - FinOps: Resource monitors and cost controls
  <ask>Ready to proceed? (y/n)</ask>
</step>

<step n="2" goal="Execute Checklist Validation">
<action>Work through each checklist section systematically</action>
<action>For each checklist item:</action>
- Determine status: PASS / FAIL / PARTIAL / NOT_APPLICABLE
- Collect evidence links or descriptions
- Note responsible owner
- Record any blockers or issues

<action>Checklist categories to validate:</action>
1. Account & Organization Setup
2. Identity & Access Management (IAM)
3. Network & Connectivity
4. Security & Governance Policies
5. Data Classification & Protection
6. Warehouse Configuration
7. Storage & Object Management
8. Data Pipelines (ELT/Streaming)
9. Monitoring & Observability
10. Cost Management (FinOps)
11. Disaster Recovery & Business Continuity
12. Compliance & Audit
13. Performance Optimization
14. CI/CD Integration
15. Documentation
16. Operational Readiness

<template-output section="checklist-results"/>
</step>

<step n="3" goal="Analyze Results and Determine GO/NO-GO">
<action>Calculate validation score:</action>
- Count MUST items: Total / Passed / Failed
- Count SHOULD items: Total / Passed / Failed
- Calculate pass rate

<action>Apply decision criteria:</action>
- GO: All MUST items passed, SHOULD items have plans
- CONDITIONAL GO: Minor MUST failures with immediate remediation plan
- NO-GO: Critical MUST failures or no remediation plan

<action>Document decision rationale</action>

<template-output section="decision"/>
</step>

<step n="4" goal="Create Remediation Plan" if="has-failures">
<action>For each failed or partial item:</action>
- Describe the issue
- Assess impact and risk level
- Assign remediation owner
- Set target completion date
- Define verification method

<template-output section="remediation"/>
</step>

<step n="5" goal="Collect Evidence and Artifacts">
<action>Document all evidence collected:</action>
- Dashboard URLs and screenshots
- Policy documents and configurations
- Audit reports
- Resource monitor configurations
- Test results
- Sign-off records

<action>Link to supporting documents</action>

<template-output section="evidence"/>
</step>

<step n="6" goal="Generate Final Report">
<action>Compile complete validation report with:</action>
- Executive summary
- Overall GO/NO-GO decision
- Detailed checklist results
- Evidence references
- Remediation plan (if needed)
- Sign-offs from key stakeholders

<action>Save report to output file</action>

<template-output section="final-report"/>
</step>

<step n="7" goal="Communicate Decision">
<action>Prepare communication to stakeholders:</action>
- Release/Change Manager
- Platform Owner
- Engineering Leads
- Product Manager
- Executive sponsors (if needed)

<ask>Would you like to generate a communication template? (y/n)</ask>
<check>If yes:</check>
  <action>Generate email/Slack template with decision and next steps</action>
  <template-output section="communication"/>
</step>

<step n="8" goal="Review and Finalize">
<action>Review complete validation report</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes</action>
  <goto step="8">Re-review</goto>
<action>Finalize and publish report</action>
</step>

</workflow>
