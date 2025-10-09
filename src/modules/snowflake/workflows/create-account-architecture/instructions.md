# Create Account Architecture - Instructions

<critical>The workflow execution engine is governed by: {project_root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project_root}/bmad/snowflake/workflows/create-account-architecture/workflow.yaml</critical>

<workflow>

<step n="1" goal="Organization/Account Topology">
<action>Generate section covering multi-account isolation, regions, replication and failover strategy</action>
<action>Include:</action>
- Organization structure (if using Snowflake Organizations)
- Account hierarchy and naming conventions
- Regional distribution and data residency requirements
- Cross-region replication architecture
- Failover and disaster recovery topology
- Environment separation (dev/staging/prod accounts or databases)

<template-output section="org-topology"/>
</step>

<step n="2" goal="Identity and Access Management">
<action>Generate section covering identity provider integration, SSO/SCIM, role hierarchy, and audit</action>
<action>Include:</action>
- Identity Provider (IdP) integration details
- SSO/SCIM configuration approach
- Role hierarchy:
  - SYSADMIN - System administration
  - SECURITYADMIN - Security management
  - PLATFORMADMIN - Platform operations
  - Application-specific roles
  - READONLY roles for reporting
- Emergency access procedures
- Audit logging and review process
- Password policies and MFA requirements

<template-output section="identity"/>
</step>

<step n="3" goal="Network and Connectivity">
<action>Generate section covering network policies, private connectivity, data access paths, and egress control</action>
<action>Include:</action>
- Network policies (IP whitelisting/blacklisting)
- Private connectivity options (AWS PrivateLink, Azure Private Link, GCP Private Service Connect)
- Data ingestion paths and security
- Data egress minimization strategies
- VPN or direct connect requirements
- Client connection methods and security

<template-output section="network"/>
</step>

<step n="4" goal="Governance and Policies">
<action>Generate section covering data classification, access policies, masking, and retention</action>
<action>Include:</action>
- Data classification and tagging strategy
- Row access policies
- Column-level access controls
- Dynamic data masking policies
- Data retention and lifecycle policies
- Object ownership and grants management
- Tag-based security automation

<template-output section="governance"/>
</step>

<step n="5" goal="FinOps and Cost Management">
<action>Generate section covering budgets, resource monitors, warehouse scheduling, and cost dashboards</action>
<action>Include:</action>
- Budget allocation by team/project
- Resource monitors and credit alerts
- Warehouse sizing and auto-suspend policies
- Warehouse scheduling (business hours vs off-hours)
- Cost attribution tags
- Chargeback/showback strategy
- Cost optimization practices

<template-output section="finops"/>
</step>

<step n="6" goal="Observability and SLOs">
<action>Generate section covering metrics, alerting, on-call rotation, and capacity planning</action>
<action>Include:</action>
- Key observability metrics (query performance, warehouse utilization, data freshness)
- Alerting strategy and thresholds
- Integration with monitoring tools (Datadog, Grafana, etc.)
- On-call rotation and escalation procedures
- SLO definitions for critical data products
- Capacity planning process
- Incident response procedures

<template-output section="observability"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document for consistency and completeness</action>
<ask>Would you like to make any final adjustments? (y/n)</ask>
<check>If yes:</check>
  <action>Allow user to specify sections to edit</action>
  <action>Make requested changes</action>
</step>

</workflow>
