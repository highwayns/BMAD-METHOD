---
template_id: layout-lead/continuity-map
version: 1
purpose: 连贯性地图
fields:
  seq: { type: string }
  lines: { type: table, columns: [shot, eyeline, screen_dir, match_action, prop_state, notes] }
outputs:
  - docs/continuity-map-{{seq}}.md
---

# Continuity Map — {{seq}}

{{lines}}
