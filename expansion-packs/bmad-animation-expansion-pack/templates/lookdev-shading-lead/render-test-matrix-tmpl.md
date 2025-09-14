---
template_id: lookdev-shading-lead/render-test-matrix
version: 1
purpose: 渲染参数/降噪/核时 试验矩阵
fields:
  renderer: { type: string }
  tests: { type: table, columns: [name, spp, denoise, time_s, notes] }
outputs:
  - tests/render-matrix-{{renderer}}.md
---

# Render Test Matrix — {{renderer}}

{{tests}}
