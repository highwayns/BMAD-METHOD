# BMAD Snowflake Module

**Version:** 1.0.0
**Status:** Converted from v4 expansion pack to v5 format
**Date:** 2025-10-08

## Overview

This module provides **standardized management team roles, agents, workflows, templates, checklists, and orchestration** for Snowflake (Data Cloud) projects, helping you implement a complete loop from **Architecture → Implementation → Validation → Operations** using the BMAD methodology.

## Purpose

Beyond BMAD core workflows, this module fills gaps specific to Snowflake scenarios:

- RBAC/Governance, Warehouse Policies & Credit Control (FinOps)
- Data Contracts, ELT (Stage/Copy/Snowpipe/Streams/Tasks)
- Dynamic Tables & Semantic Layers, Snowpark/Model UDFs
- CI/CD, Observability (ACCOUNT_USAGE/ORGANIZATION_USAGE), SLOs & Event Reviews

## When to Use This Module

- Building or migrating to Snowflake for data platforms/products
- Need standardized role definitions, document templates, quality gates
- Need task-driven automated agents with unified checklists

## What's Included

### Agents

18 role-based agents covering the complete Snowflake development lifecycle:
- Platform Owner
- Snowflake Architect
- Product Manager
- Business Analyst
- Data Contract Owner
- Data Engineering Lead
- Ingestion/Streaming Engineer
- Analytics Engineer (BI/SQL)
- ML Engineer (Snowpark)
- DataOps/SRE
- Security/Governance/RBAC
- Privacy/Compliance
- FinOps/Credit Optimizer
- Observability/Reliability
- Release/Change Manager
- DevEx/Platform Automation
- Quality Assurance/Data Tests
- Support/Incident Manager

### Workflows

250+ workflows organized by domain:
- Architecture & Planning
- Security & Governance
- Data Engineering (ELT, Streaming, Dynamic Tables)
- Analytics & BI
- ML/AI (Snowpark)
- Observability & Monitoring
- FinOps & Cost Management
- Release Management
- Incident Management
- Compliance & Privacy

### Checklists

Production-readiness quality gates covering:
- Infrastructure validation (16 major sections)
- Security & compliance checks
- Performance optimization
- Cost controls

### Data Files

Reference data including:
- KPI catalogs
- Warehouse profiles
- Credit budgets
- Policy examples (SQL)
- Dynamic table examples

## Integration with Core BMAD

1. **After Architecture**: Lock contracts, then enter Snowflake architecture (DB/Schema/Warehouse/RBAC)
2. **Parallel to Development**: Implement ELT/Streaming, Dynamic Tables/Semantic Layers, Snowpark
3. **Before Deployment**: Run validation workflows and checklist quality gates

## Installation

This module is part of the BMAD core installation. Ensure you have BMAD Core >= 1.10.

## Usage Examples

### Generate Architecture Document
```
Use snowflake-architect agent → create-account-architecture workflow
```

### Review Infrastructure
```
Use snowflake-architect agent → review-architecture workflow
```

### Validate & Gate Check
```
Use snowflake-architect agent → validate-infrastructure workflow
```

## Team Integration

Use this module's checklists as **pre-release quality gates** in team workflows; reference **document validation sections** in architecture templates.

## Dependencies

- Requires Snowflake account & workspace with available warehouses
- CI must have access to credentials (assign values before using placeholder variables)

## Customization

- Customize RBAC hierarchy/masking policies
- Adjust warehouse policies & budget thresholds
- Modify compliance items & reporting styles

## Notes

- Template variables use `{{var}}` format
- Rules marked `<critical_rule>` are mandatory
- Always validate in non-production environment first and retain evidence

## Conversion Notes

This module was converted from BMAD v4 expansion pack format to v5:
- Agents converted from embedded YAML in markdown to .agent.yaml format
- Tasks converted to workflow folders with workflow.yaml + instructions.md
- Templates integrated into workflow structures
- All paths updated to use {project-root} variables

---

**Compatible with:** BMAD Core >= 1.10
**License:** MIT
**Author:** BMAD Team
