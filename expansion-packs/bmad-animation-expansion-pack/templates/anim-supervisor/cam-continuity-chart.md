---
template_id: anim-supervisor/cam-continuity-chart
version: 1
purpose: 摄影机/走位连贯性图
fields:
  seq: { type: string }
  links: { type: table, columns: [shot_a, shot_b, axis, eyeline, risk] }
outputs:
  - continuity/cam-continuity-{{seq}}.md
---

# Cam Continuity — {{seq}}

{{links}}
