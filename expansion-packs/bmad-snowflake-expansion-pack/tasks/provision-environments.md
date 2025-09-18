# Provision Environments (DEV/STG/PRD)

purpose: Declaratively provision account objects with IaC + bootstrap SQL
steps:

- Confirm architecture doc exists and approved
- Plan environment topology: {dev, stg, prd} accounts or prefixes, network policy, SSO/SCIM
- Generate Terraform plan with Snowflake Provider; review & apply
- Bootstrap SQL: roles, warehouses, databases, schemas, resource monitors
- Register budgets/thresholds + notifications
- Smoke validation & handover checklist
  bootstrap_sql: |
  -- Example roles/warehouses
  CREATE ROLE IF NOT EXISTS SYS_ADMIN;
  CREATE ROLE IF NOT EXISTS SEC_ADMIN;
  CREATE WAREHOUSE IF NOT EXISTS WH_ETL WITH WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 60 AUTO_RESUME = TRUE;
  CREATE RESOURCE MONITOR IF NOT EXISTS RM_ETL WITH CREDIT_QUOTA = 200 TRIGGERS ON 80 PERCENT DO NOTIFY ON 100 PERCENT DO SUSPEND;
  -- Sample RBAC grants (adjust per policy)
  GRANT ROLE SYS_ADMIN TO USER {{admin_user}};
  GRANT USAGE ON WAREHOUSE WH_ETL TO ROLE SYS_ADMIN;
  artifacts:
- terraform/ (providers.tf, main.tf, variables.tf)
- sql/bootstrap.sql
- docs/runbook/provisioning.md
