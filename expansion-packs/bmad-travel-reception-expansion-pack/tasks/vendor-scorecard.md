# task: vendor-scorecard

version: 1.0
role: vendor-procurement-manager
purpose: 建立供应商评分并联动激励/整改。
inputs: [指标/KPI, 评级/措施]
outputs: [reports/vendor-scorecard-<period>.md]
steps:

- 渲染 templates/vendor-scorecard-tmpl.yaml
- 与QBR与停卖机制联动
  acceptance:
- 评分客观
- 措施落地
