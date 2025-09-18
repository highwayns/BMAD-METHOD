# Review Security & Governance

purpose: Validate RBAC/ABAC, masking, row access, tags, lineage, access history, key mgmt, network policies
inputs:

- snowflake-governance-policy document
  check:
- Apply checklists/snowflake-security-compliance-checklist.md
- Sample SQL in data/policy-tag-examples.sql
  output:
- security-review.md (findings, risks, remediation plan, owners, ETA)
