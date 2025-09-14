---
template_id: rigging-lead/retarget-setup
version: 1
purpose: 动补/重定向设置
fields:
  asset: { type: string }
  solver: { type: string }
  mapping: { type: table, columns: [src, dst, scale, notes] }
  filters: { type: list, items: string }
outputs:
  - retarget/retarget-setup-{{asset}}.md
---

# Retarget Setup — {{asset}}

- Solver: {{solver}}
  {{mapping}}
- Filters: {{filters}}
