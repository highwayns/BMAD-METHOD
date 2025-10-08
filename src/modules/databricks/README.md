# Databricks Lakehouse Development Pack

**Version:** 2.0.0 (BMAD v5)
**Original:** 1.0.0 (BMAD v4)
**Conversion Date:** 2025-10-08
**Status:** Phase 1 Complete (Agents Converted)

---

## Overview

This is a comprehensive expansion pack for **Databricks Lakehouse system development** that provides standardized management team roles, agents, workflows, templates, checklists, and orchestration aligned to BMAD Core standards.

The pack covers the complete lifecycle from **Architecture → Implementation → Validation → Operations** for Databricks projects.

---

## What's Included

### ✅ **18 Specialized Agents** (v5 Converted)

All agents have been converted to BMAD v5 `.agent.yaml` format:

1. **01-platform-owner** (🗄️) - Platform governance, Unity Catalog, SLO, security/compliance, FinOps
2. **02-lakehouse-architect** (🏗️) - Architecture design, data contracts, DLT, performance
3. **03-product-manager** (📋) - Product roadmap, requirements, stakeholder management
4. **04-business-analyst** (📊) - Business requirements, metrics, KPIs
5. **05-data-contract-owner** (📜) - Data contracts, schema management, versioning
6. **06-data-engineering-lead** (⚙️) - ETL/ELT pipelines, data quality, orchestration
7. **07-streaming-engineer** (🌊) - Real-time streaming, Structured Streaming, Kafka integration
8. **08-analytics-engineer-bisql** (📈) - SQL analytics, semantic layer, BI dashboards
9. **09-ml-engineer-mlops** (🤖) - ML pipelines, model serving, MLOps, Feature Store
10. **10-dataops-sre** (🔧) - Operations, monitoring, incident response, reliability
11. **11-security-governance-uc** (🔐) - Security, Unity Catalog governance, RBAC/ABAC
12. **12-privacy-compliance** (🛡️) - Privacy, GDPR, data classification, compliance
13. **13-finops-cost-optimizer** (💰) - Cost optimization, budget management, resource allocation
14. **14-observability-reliability** (📡) - Monitoring, alerting, SLO/SLA tracking
15. **15-release-change-manager** (🚀) - Release management, change control, deployments
16. **16-devex-platform-automation** (🔨) - Developer experience, automation, tooling
17. **17-quality-assurance-data-tests** (✅) - Data quality tests, validation, testing frameworks
18. **18-support-incident-manager** (🆘) - Support, incident management, escalation

**Location:** `bmad/databricks/agents/*.agent.yaml`

### ✅ **206 Data Files** (Migrated)

Knowledge bases, reference data, technical preferences, and domain-specific information.

**Location:** `bmad/databricks/data/`

### ✅ **315 Checklists** (Migrated)

Quality gates, validation checklists, compliance checks, and production readiness criteria.

**Location:** `bmad/databricks/checklists/`

### ⏳ **Workflows** (Pending On-Demand Conversion)

**Legacy Assets Available:**
- **374 Task files** - Execution workflows and procedures
- **358 Template files** - Document generation templates

**Status:** Available for on-demand conversion to v5 workflows when specific functionality is needed.

**Approach:** Use the `convert-legacy` workflow to convert specific tasks+templates into v5 workflows as required.

---

## Purpose

Extends BMAD core capabilities for Databricks scenarios:

- **Unity Catalog** (RBAC/governance)
- **Cluster policies** and cost control (FinOps)
- **Data contracts**, ELT (Autoloader/DLT/Jobs)
- **Silver → Gold** semantic layer, Feature Store, Model Serving
- **CI/CD**, observability (Lakehouse Monitoring/SQL Alerts), SLO and incident response

---

## When to Use This Pack

- Building or migrating to Databricks data platform/data products
- Need standardized role separation, document templates, quality gates
- Require task-driven automation agents with unified checklists
- Implementing Lakehouse architecture with governance and FinOps controls

---

## Installation Status

### ✅ Phase 1: Complete
- [x] 18 agents converted to v5 format
- [x] 206 data files migrated
- [x] 315 checklists migrated
- [x] Module config.yaml created
- [x] Directory structure established

### ⏳ Phase 2: On-Demand (As Needed)
- [ ] Convert tasks to v5 workflows (374 available)
- [ ] Convert templates to workflow templates (358 available)
- [ ] Test workflow execution
- [ ] Create workflow orchestrations

### ⚠️ Known Issues
- **Agent menu items** require manual population (automated conversion had issues)
- **Workflows** not yet converted (use legacy tasks/templates as reference)
- **Path validation** needed to ensure all {project-root} references resolve

---

## Quick Start

### 1. Activate an Agent

```bash
# Example: Activate the Platform Owner agent
/bmad:agent databricks/01-platform-owner
```

### 2. Use Agent Commands

Agents provide interactive menus. Type `help` to see available commands.

Example commands:
- `kb-mode` - Load agent knowledge base
- `create-doc` - Generate documentation from templates
- `execute-checklist` - Run validation checklists
- `provision-workspace` - Platform-specific workflows (when converted)

### 3. Access Checklists Directly

```bash
# View a checklist
cat bmad/databricks/checklists/platform-governance-checklist.md
```

### 4. Convert Legacy Workflows On-Demand

When you need a specific workflow:

```bash
/bmad:bmb:workflows:convert-legacy

# Then specify:
# - Source: bmad/databricks/legacy/tasks/{task-name}.md
# - Also check: bmad/databricks/legacy/templates/{template-name}.yaml
# - Convert to: bmad/databricks/workflows/{workflow-name}/
```

---

## Integration with Core BMAD

1. **After Architecture:** Lock contracts, then enter Lakehouse architecture (Catalog/Schema/Tables/Permissions)
2. **Parallel to Development:** Implement DLT/Jobs, Silver→Gold transformations, Feature/Model/Serving
3. **Before Deployment:** Execute `validate-infrastructure` and checklist quality gates

---

## Module Structure

```
bmad/databricks/
├── agents/                    # 18 v5 agent definitions (.agent.yaml)
├── workflows/                 # v5 workflows (to be created on-demand)
├── data/                      # 206 knowledge base and reference files
├── checklists/               # 315 quality gate and validation checklists
├── legacy/                   # Original v4 assets for reference
│   ├── tasks/               # 374 task files (source for workflow conversion)
│   └── templates/           # 358 template files (source for workflow templates)
├── config.yaml              # Module configuration
└── README.md                # This file
```

---

## Configuration

Module settings in `config.yaml`:

- **Supported clouds:** AWS, Azure, GCP
- **Default region:** us-east-1
- **Unity Catalog:** Enabled by default
- **Locales:** zh-CN (default), en

---

## Dependencies

- **BMAD Core:** >= 6.0.0
- **BMAD Method:** >= 1.10
- **Databricks:** Workspace, Unity Catalog, Service Principal
- **CI Access:** Token required for template rendering

---

## Customization

You can customize:
- Unity Catalog hierarchy/masking policies
- Cluster policies and budget thresholds
- Compliance rules and report formats
- Agent personas and command menus

---

## Migration Notes

### From v4 to v5

**What Changed:**
- Agent file format: `.md` (YAML embedded) → `.agent.yaml` (pure YAML)
- Agent structure: Flat YAML → Structured sections (metadata, persona, menu, prompts, etc.)
- Commands: Simple list → Menu array with handlers (workflow, exec, action, data)
- Dependencies: Direct file references → {project-root} variable paths
- Tasks: Standalone files → Part of v5 workflow (workflow.yaml + instructions.md + template.md)
- Templates: Standalone YAML → Part of v5 workflow template.md

**Preserved:**
- All Chinese language content
- Quality gates and DoR/DoD criteria
- Checklist structures
- Data files and knowledge bases
- Agent personas and principles

**New Features:**
- Modular menu system with multiple handler types
- Inline prompts with action IDs
- Critical actions and activation rules
- Enhanced dependency tracking
- Better path resolution with variables

---

## Usage Examples

### 1) Generate Architecture Documentation

```bash
/bmad:agent databricks/02-lakehouse-architect
> create-doc databricks-architecture
```

### 2) Review Platform Infrastructure

```bash
/bmad:agent databricks/01-platform-owner
> review-infrastructure
```

### 3) Execute Validation Gate

```bash
/bmad:agent databricks/01-platform-owner
> platform-acceptance-gate
```

---

## Team Integration

- Use checklists as **pre-release quality gates** in team workflows
- Reference document validation sections in architecture templates
- Integrate agent commands into CI/CD pipelines
- Use agent knowledge bases for team onboarding

---

## License

MIT License

---

## Links

- **Original Pack:** `BMAD-METHOD-new/expansion-packs/bmad-databricks-expansion-pack`
- **Conversion Report:** `docs/conversion-report-databricks-2025-10-08.md`
- **BMAD Core:** `bmad/core/`
- **Module Config:** `bmad/databricks/config.yaml`

---

## Support

For issues or questions:
1. Check agent knowledge bases (`data/*-kb.md`)
2. Review checklists for guidance
3. Consult legacy tasks/templates for reference implementations
4. Use `convert-legacy` workflow to create needed workflows on-demand

---

_Version: 2.0.0_ · _Compatible with BMAD Core >= 6.0.0_ · _Converted: 2025-10-08_
