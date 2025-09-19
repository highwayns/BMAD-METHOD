# task: csat-nps-program

version: 1.0
role: customer-service-care-lead
purpose: 设计并运行CSAT/NPS计划与看板目标。
inputs: [抽样与渠道, 指标与目标]
outputs: [reports/csat-nps-<period>.md]
steps:

- 渲染 templates/csat-nps-program-tmpl.yaml
- 看板上线与目标公示
  acceptance:
- 抽样科学/指标有效
- 周期复盘
