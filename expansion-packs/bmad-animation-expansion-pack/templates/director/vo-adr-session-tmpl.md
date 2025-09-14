---
template_id: director/vo-adr-session
version: 1
purpose: VO/ADR 指导单
fields:
  scene: { type: string }
  lines: { type: table, columns: [char, line, intent, emphasis, alt_takes] }
  notes: { type: list, items: string }
outputs:
  - sound/vo-adr-session-{{scene}}.md
---

# VO/ADR Session — {{scene}}

## Lines

{{lines}}

## Notes

- {{notes}}
