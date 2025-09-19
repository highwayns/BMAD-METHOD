# task: cashflow-forecast

version: 1.0
role: finance-billing-specialist
purpose: 产出现金流预测与假设说明。
inputs: [期间/流入/流出/净额, 假设/风险/应对]
outputs: [reports/cashflow-forecast-<period>.md]
steps:

- 渲染 templates/cashflow-forecast-tmpl.yaml
- 与AP/AR节奏对齐
  acceptance:
- 预测合理
- 假设透明
