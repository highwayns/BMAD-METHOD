# task: refund-request

version: 1.0
role: finance-billing-specialist
purpose: 处理退款申请并固定审批与路径。
inputs: [客户/订单/金额/渠道, 责任/审批/路径]
outputs: [docs/fin/refund-<client>-<order>.md]
steps:

- 渲染 templates/refund-request-tmpl.yaml
- 执行 refund-control-check 清单
  acceptance:
- 责任清楚/审批齐全
- 资金原路/合规到位
