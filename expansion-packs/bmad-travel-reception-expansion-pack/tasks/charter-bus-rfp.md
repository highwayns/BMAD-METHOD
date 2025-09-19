# task: charter-bus-rfp

version: 1.0
role: transport-logistics-coordinator
purpose: 发起包车/大巴 RFP，收集合规与价格。
inputs: [车辆规格与时段, 路线与停靠, SLA与合规, 价格与结算]
outputs: [docs/transport/charter-bus-rfp.md]
steps:

- 渲染 templates/charter-bus-rfp-tmpl.yaml
- 形成评分与推荐
  acceptance:
- 字段完整可比
- 合规项覆盖
