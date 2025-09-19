# task: margin-bridge

version: 1.0
role: finance-billing-specialist
purpose: 输出毛利桥分解预算与实际差异。
inputs: [价格/数量/结构/汇率/一次性]
outputs: [reports/margin-bridge-<period>.md]
steps:

- 渲染 templates/margin-bridge-tmpl.yaml
- 执行 margin-variance-check 清单
  acceptance:
- 差异来源清晰
- 可形成行动
