---
template_id: compositing-lead/aov-rebuild
version: 1
purpose: AOV 重建/误差报告
fields:
  seq: { type: string }
  cases: { type: table, columns: [shot, renderer, aov_set, ops, target, tolerance, result] }
outputs:
  - qc/aov-rebuild-{{seq}}.md
---

# AOV Rebuild — {{seq}}

{{cases}}
