---
template_id: rigging-lead/perf-bench-plan
version: 1
purpose: 绑定性能基准
fields:
  asset: { type: string }
  scenes: { type: table, columns: [scene, chars, frame_range, notes] }
  metrics: { type: table, columns: [name, goal, method] }
outputs:
  - bench/perf-bench-{{asset}}.md
---

# Perf Bench — {{asset}}

{{scenes}}
{{metrics}}
