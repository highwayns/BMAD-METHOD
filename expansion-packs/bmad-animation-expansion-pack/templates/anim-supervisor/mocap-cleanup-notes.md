---
template_id: anim-supervisor/mocap-cleanup-notes
version: 1
purpose: Mocap 清洗记录
fields:
  session: { type: string }
  fixes: { type: table, columns: [tc, issue, action, owner] }
outputs:
  - mocap/mocap-cleanup-{{session}}.md
---

# Mocap Cleanup — {{session}}

{{fixes}}
