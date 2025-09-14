---
template_id: lighting-lead/continuity-map
version: 1
purpose: 灯光连续性地图
fields:
  seq: { type: string }
  items: { type: table, columns: [shot, key, fill, rim, temp_k, contrast, notes] }
outputs:
  - docs/continuity-map-{{seq}}.md
---

# Lighting Continuity — {{seq}}

{{items}}
