# BMAD Snowflake Workflows - Quick Start Guide

**Version**: v5
**Last Updated**: 2025-10-08

---

## What's Included

The BMAD Snowflake expansion pack includes **273 production-ready workflows** covering all aspects of Snowflake platform operations.

---

## Quick Navigation

### Find Workflows

**By Domain**:
- See `workflows/INDEX.md` for complete categorized list
- 17 domains: Architecture, Security, Data Engineering, Analytics, ML/AI, and more

**By Name**:
- All workflows in: `bmad/snowflake/workflows/[workflow-name]/`
- Each workflow has its own directory with 2-3 files

---

## Workflow Structure

Each workflow directory contains:

```
workflows/[workflow-name]/
├── workflow.yaml        # Configuration and metadata (REQUIRED)
├── instructions.md      # Step-by-step execution instructions (REQUIRED)
└── template.md         # Output template (OPTIONAL - document workflows only)
```

### File Purposes

**workflow.yaml**:
- Workflow name and description
- Configuration references
- Output paths
- Workflow type (document/action)

**instructions.md**:
- XML-tagged execution steps
- User interactions
- Conditional logic
- Template section references

**template.md** (document workflows only):
- Markdown output template
- Variable placeholders
- Section definitions
- Document structure

---

## Workflow Types

### Document Workflows (206)
Generate structured markdown documents.

**Example**: `create-ingestion-plan`, `rbac-blueprint`, `finops-plan`

**Output**: Markdown documents in `{output_folder}/[domain]/`

### Action Workflows (67)
Execute actions, validations, or processes.

**Example**: `validate-infrastructure`, `close-incident`, `bug-triage`

**Output**: Validation results, action logs, or status updates

---

## Common Workflows by Use Case

### Getting Started with Snowflake
1. `create-account-architecture` - Design your Snowflake organization
2. `rbac-blueprint` - Define role-based access control
3. `network-policies` - Configure network security
4. `create-governance-policy` - Establish data governance

### Data Ingestion
1. `create-ingestion-plan` - Plan your data loading strategy
2. `snowpipe-plan` - Set up continuous ingestion
3. `snowpipe-streaming-plan` - Configure low-latency streaming
4. `cdc-plan` - Implement change data capture

### Data Engineering
1. `build-dbt-project` - Set up dbt project structure
2. `elt-pipelines` - Design ELT workflows
3. `dynamic-tables-plan` - Plan materialized views
4. `dq-plan` - Implement data quality checks

### Analytics & BI
1. `dashboard-spec` - Design dashboard requirements
2. `metric-layer` - Define semantic metrics
3. `bi-release` - Release BI assets to production

### ML/AI
1. `ai-governance` - Establish AI governance framework
2. `model-card` - Document ML model details
3. `experiment-plan` - Design ML experiments
4. `batch-scoring` - Set up batch inference

### FinOps & Cost Management
1. `finops-plan` - Create cost optimization strategy
2. `warehouse-rightsizing` - Optimize warehouse sizes
3. `cost-attribution-tags` - Tag resources for cost tracking
4. `budget-forecast` - Forecast spending

### Observability
1. `observability-plan` - Design monitoring strategy
2. `slo-workshop` - Define service level objectives
3. `alerts-routing` - Configure alerting
4. `warehouse-observability` - Monitor warehouse performance

### Incident Management
1. `incident-runbook` - Create incident response procedures
2. `incident-intake` - Standardize incident reporting
3. `incident-postmortem` - Conduct post-incident reviews
4. `war-room` - Manage critical incidents

### Security & Compliance
1. `data-classification` - Classify sensitive data
2. `masking-policies` - Implement data masking
3. `compliance-audit-pack` - Prepare compliance artifacts
4. `risk-assessment` - Assess security risks

### Release Management
1. `release-plan` - Plan feature releases
2. `ci-cd` - Set up CI/CD pipelines
3. `canary-bluegreen` - Implement safe deployments
4. `rollback-plan` - Define rollback procedures

---

## Configuration

All workflows reference the centralized configuration:

```yaml
# bmad/snowflake/config.yaml
user_name: "Your Name"
communication_language: "English"
output_folder: "path/to/outputs"
```

Workflows automatically inherit these settings via:
```yaml
config_source: "{project-root}/bmad/snowflake/config.yaml"
user_name: "{config_source}:user_name"
```

---

## Output Organization

Workflow outputs are organized by domain:

```
{output_folder}/
├── architecture/           # Architecture documents
├── security/              # Security policies & designs
├── data-engineering/      # Data pipeline specs
├── analytics/             # BI & analytics artifacts
├── ml-ai/                 # ML/AI documentation
├── observability/         # Monitoring & SLO docs
├── finops/               # Cost optimization plans
├── release/              # Release plans & notes
├── incidents/            # Incident reports
├── compliance/           # Compliance documentation
├── operations/           # Operational runbooks
├── governance/           # Governance policies
├── data-sharing/         # Data sharing agreements
├── testing/              # Test plans & reports
├── project-management/   # PM artifacts
├── devex/                # Developer docs
└── optimization/         # Performance tuning
```

---

## Execution Flow

### For Document Workflows

1. **Load Configuration**: Read `workflow.yaml`
2. **Execute Instructions**: Follow `instructions.md` steps
3. **Gather Input**: Interact with user as needed
4. **Generate Output**: Populate `template.md` with data
5. **Save Document**: Write to `{output_folder}/[domain]/[name]-{{date}}.md`

### For Action Workflows

1. **Load Configuration**: Read `workflow.yaml`
2. **Execute Instructions**: Follow `instructions.md` steps
3. **Perform Actions**: Execute validations, checks, or operations
4. **Report Results**: Log outcomes and status

---

## Example Usage

### Create an Ingestion Plan

```yaml
# Workflow: create-ingestion-plan
# Location: workflows/create-ingestion-plan/
# Type: Document workflow
# Output: {output_folder}/data-engineering/ingestion-plan-{date}.md

Steps:
1. Understand data source requirements
2. Define staging strategy
3. Configure COPY commands
4. Set up Snowpipe (if needed)
5. Document security measures
6. Generate final document
```

### Validate Infrastructure

```yaml
# Workflow: validate-infrastructure
# Location: workflows/validate-infrastructure/
# Type: Action workflow
# Output: Validation report + checklist results

Steps:
1. Load infrastructure checklist
2. Validate each checkpoint
3. Document findings
4. Determine gate pass/fail status
5. Report results
```

---

## Tips & Best Practices

### Finding the Right Workflow
1. Check `workflows/INDEX.md` for complete list
2. Browse by domain for related workflows
3. Search by keyword (e.g., "snowpipe", "rbac", "incident")

### Customizing Workflows
- Workflows support variable substitution via `{{variable}}` syntax
- Edit `workflow.yaml` to change output paths
- Modify `template.md` to adjust document structure
- Customize `instructions.md` to add/remove steps

### Chaining Workflows
Common workflow sequences:
1. **Initial Setup**: `create-account-architecture` → `rbac-blueprint` → `network-policies`
2. **Data Ingestion**: `create-ingestion-plan` → `snowpipe-plan` → `dq-plan`
3. **Production Release**: `release-plan` → `gate-check` → `go-live` → `post-release-verification`
4. **Incident Response**: `incident-intake` → `war-room` → `incident-postmortem`

### Quality Gates
Key validation workflows:
- `validate-infrastructure` - Pre-production infrastructure checks
- `gate-check` - Release readiness validation
- `preprod-readiness` - Pre-production environment validation
- `uat-signoff` - User acceptance testing sign-off

---

## Getting Help

### Documentation
- **Complete Report**: `CONVERSION-REPORT.md`
- **Workflow Index**: `workflows/INDEX.md`
- **Phase Summary**: `../PHASE-2-COMPLETE.md`
- **Module README**: `README.md`

### Validation Reports
- **Conversion Log**: `conversion-log.json` (detailed conversion data)
- **Validation Report**: `validation-report.json` (quality metrics)

### Common Issues

**Issue**: Workflow output path not found
**Solution**: Ensure `output_folder` is configured in `config.yaml`

**Issue**: Template variables not populating
**Solution**: Check that all required variables are defined in `workflow.yaml`

**Issue**: Instruction steps not executing
**Solution**: Verify XML tags are properly formatted in `instructions.md`

---

## Related Resources

### Snowflake Assets
- **Agents**: `bmad/snowflake/agents/` (18 specialized agents)
- **Checklists**: `bmad/snowflake/checklists/` (218 operational checklists)
- **Data Files**: `bmad/snowflake/data/` (181 reference data files)
- **Configuration**: `bmad/snowflake/config.yaml`

### Core BMAD
- **Workflow Engine**: `bmad/core/tasks/workflow.xml`
- **Core Config**: `bmad/core/config.yaml`
- **Core Agents**: `bmad/core/agents/`

---

## Statistics

- **Total Workflows**: 273
- **Document Workflows**: 206 (75.5%)
- **Action Workflows**: 67 (24.5%)
- **Domains**: 17
- **Total Files**: 753

**Quality**:
- YAML Validation: 100% ✅
- Instruction Format: 99.3% ✅
- Zero Critical Errors ✅

---

**Version**: v5.0
**Last Updated**: 2025-10-08
**Status**: Production Ready ✅
