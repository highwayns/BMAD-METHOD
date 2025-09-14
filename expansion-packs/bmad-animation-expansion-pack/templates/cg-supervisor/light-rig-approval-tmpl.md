---
template_id: cg-supervisor/light-rig-approval
version: 1
purpose: 灯光 Rig/模板审批
fields:
  seq: { type: string }
  exposure_targets: { type: list, items: string }
  test_shots: { type: list, items: string }
  render_time_budget: { type: string }
  decision: { type: string, enum: [approve, minor-fix, major-rework] }
outputs:
  - approvals/light-rig-{{seq}}.md
---

# Light Rig Approval — {{seq}}

- Exposure Targets: {{exposure_targets}}
- Test Shots: {{test_shots}}
- Render Time Budget: {{render_time_budget}}
- Decision: {{decision}}
