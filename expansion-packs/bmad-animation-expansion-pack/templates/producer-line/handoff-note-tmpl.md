---
template_id: producer-line/handoff-note
version: 1
purpose: 部门交接记录
fields:
  dept_from: { type: string }
  dept_to: { type: string }
  package_list: { type: list, items: string }
  gate_results: { type: list, items: string }
  sign_offs: { type: table, columns: [name, role, datetime] }
outputs:
  - handoff/{{dept_from}}-to-{{dept_to}}-{{date}}.md
---

# 交接：{{dept_from}} → {{dept_to}}

- 包内清单：{{package_list}}
- 门禁结论：{{gate_results}}
- 签署：{{sign_offs}}
