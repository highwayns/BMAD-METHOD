---
template_id: fx-supervisor/solver-calibration
version: 1
purpose: 求解器标定
fields:
  solver: { type: string }
  tests: { type: table, columns: [param, value, metric, goal, result] }
outputs:
  - calib/solver-calib-{{solver}}.md
---

# Solver Calibration — {{solver}}

{{tests}}
