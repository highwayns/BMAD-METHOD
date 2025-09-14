---
template_id: fx-supervisor/perf-bench
version: 1
purpose: FX 性能基准
fields:
  renderer: { type: string }
  tests: { type: table, columns: [case, resolution, voxel, substeps, time_s, notes] }
outputs:
  - bench/fx-perf-{{renderer}}.md
---

# FX Perf Bench — {{renderer}}

{{tests}}
