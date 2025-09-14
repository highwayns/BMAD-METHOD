---
template_id: post-supervisor/editorial-plan
version: 1
purpose: 剪辑计划/锁定策略
fields:
  show: { type: string }
  timeline: { type: table, columns: [version, fps, tc_base, picture_lock_date, notes] }
  change_policy: { type: list, items: string }
outputs:
  - plans/editorial-plan-{{show}}.md
---

# Editorial Plan — {{show}}

{{timeline}}

- Change Policy: {{change_policy}}
