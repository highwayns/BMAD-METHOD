---
template_id: anim-supervisor/pass-schedule
version: 1
purpose: Pass 节律（Block/Spline/Polish）计划
fields:
  seq: { type: string }
  schedule: { type: table, columns: [shot, block_due, spline_due, polish_due, notes] }
outputs:
  - plans/pass-schedule-{{seq}}.md
---

# Pass Schedule — {{seq}}

| Shot | Block | Spline | Polish | Notes |
| ---- | ----- | ------ | ------ | ----- |

{{schedule}}
