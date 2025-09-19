# task: hotel-rfp

version: 1.0
role: hotel-contracting-manager
purpose: 发起酒店/旅馆 RFP，收集价表/SLA/合规信息。
inputs: [供应商基本信息, 服务范围, SLA与合规, 价表与结算]
outputs: [docs/hotel/rfp-<hotel>-<YYYY>.md]
steps:

- 渲染 templates/hotel-rfp-tmpl.yaml 并逐节提问
- 形成可比对表与评分
  acceptance:
- 字段完整，可比性强
- 审批与留痕齐备
