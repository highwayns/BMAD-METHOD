---
template_id: layout-lead/collisions-report
version: 1
purpose: 碰撞/穿帮检测报告
fields:
  seq: { type: string }
  hits: { type: table, columns: [shot, frame, pair, depth_mm, note] }
outputs:
  - reports/collisions-{{seq}}.md
---

# Collisions — {{seq}}

{{hits}}
