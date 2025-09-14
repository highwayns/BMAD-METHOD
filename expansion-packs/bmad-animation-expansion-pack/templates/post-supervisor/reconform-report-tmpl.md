---
template_id: post-supervisor/reconform-report
version: 1
purpose: Re-conform 对账报告
fields:
  seq: { type: string }
  items: { type: table, columns: [shot, src, edl_event, tc_in, tc_out, delta, action, status] }
outputs:
  - reports/reconform-{{seq}}.md
---

# Re-conform — {{seq}}

{{items}}
