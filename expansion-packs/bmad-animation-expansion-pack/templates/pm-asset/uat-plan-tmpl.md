---
template_id: pm-asset/uat-plan
version: 1
purpose: UAT 计划与用例
fields:
  release: { type: string }
  cases: { type: table, columns: [id, title, pre, steps, expected, owner] }
outputs:
  - qc/uat-{{release}}.md
---

# UAT — {{release}}

{{cases}}
