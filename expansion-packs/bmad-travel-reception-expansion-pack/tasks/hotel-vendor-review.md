# task: hotel-vendor-review

version: 1.0
role: hotel-contracting-manager
purpose: 按季度评审酒店供应商，更新黑白名单与条款。
inputs: [近90天KPI, 投诉/退款, 合规/事故]
outputs: [reports/hotel-vendor-review-<hotel>-<YYYYQ>.md]
steps:

- 渲染 templates/hotel-vendor-review-tmpl.yaml
- 形成改进行动与复核节奏
  acceptance:
- 指标证据充分
- 改进闭环
