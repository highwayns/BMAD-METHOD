---
template_id: anim-supervisor/blocking-plan
version: 1
purpose: Blocking 计划
fields:
  seq: { type: string }
  coverage: { type: list, items: string }
  gates: { type: list, items: string }
  submissions: { type: list, items: string }
outputs:
  - plans/blocking-plan-{{seq}}.md
---

# Blocking Plan — {{seq}}

- Coverage: {{coverage}}
- Gates: {{gates}}
- Submissions: {{submissions}}
