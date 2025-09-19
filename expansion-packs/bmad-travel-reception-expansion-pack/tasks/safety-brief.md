# task: safety-brief

version: 1.0
role: guide-leader-manager
purpose: 统一安全讲解要点与应急提示。
inputs: [集合与点名, 乘车与安全带, 天气与灾害]
outputs: [docs/guide/safety-brief.md]
steps:

- 渲染 templates/safety-briefing-tmpl.yaml
- 执行 safety-equipment-check 清单
  acceptance:
- 安全主题覆盖
- 物资齐备
