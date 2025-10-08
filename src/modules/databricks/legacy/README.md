# Legacy Assets (v4)

This directory contains the original BMAD v4 tasks and templates preserved for reference and on-demand conversion to v5 workflows.

## Contents

- **tasks/** (374 files) - Original v4 task execution workflows
- **templates/** (358 files) - Original v4 document generation templates

## Purpose

These legacy assets serve as:
1. **Reference material** for understanding original functionality
2. **Source files** for on-demand conversion to v5 workflows
3. **Documentation** of the complete v4 feature set

## Converting to v5 Workflows

When you need a specific workflow, use the `convert-legacy` workflow:

```bash
/bmad:bmb:workflows:convert-legacy
```

Then specify:
- **Source task:** `bmad/databricks/legacy/tasks/{task-name}.md`
- **Source template (if applicable):** `bmad/databricks/legacy/templates/{template-name}.yaml`
- **Target:** `bmad/databricks/workflows/{workflow-name}/`

The conversion process will:
1. Analyze the task logic and template structure
2. Create v5 workflow directory with:
   - `workflow.yaml` - Workflow configuration
   - `instructions.md` - Step-by-step execution instructions
   - `template.md` - Document template (if applicable)
   - `checklist.md` - Validation criteria (if applicable)

## File Mapping

### Task + Template = Workflow

Many v4 tasks reference templates for document generation. Common patterns:

- `create-doc.md` + `{name}-tmpl.yaml` → Document workflow
- `{action}.md` (no template) → Action workflow
- `{validation}.md` + checklist → Validation workflow

### Task Types

**Document Generation Tasks:**
- Reference a template file
- Produce structured documents
- Usually have `docOutputLocation` field

**Action Tasks:**
- Perform operations (provision, configure, deploy)
- May produce logs or configuration files
- Focus on execution steps

**Validation Tasks:**
- Execute checklists
- Assess quality gates
- Produce assessment reports

## Preservation Notes

- All files preserved exactly as-is from v4
- Chinese language content intact
- File structure and naming conventions maintained
- No modifications to original files

## Statistics

- **Total legacy files:** 732
- **Tasks:** 374
- **Templates:** 358
- **Conversion status:** Available for on-demand conversion

---

_These files are part of the Databricks module v2.0.0 conversion from v4 to v5._
_Original source: BMAD-METHOD-new/expansion-packs/bmad-databricks-expansion-pack_
