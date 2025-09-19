# task: refund-comp

version: 1.0
role: customer-service-care-lead
purpose: 确定退款/补偿政策与审批链，沉淀口径与对账路径。
inputs: [触发条件/金额区间/审批, 退款路径/票据/对账]
outputs: [docs/care/refund-comp-policy.md]
steps:

- 渲染 templates/refund-comp-policy-tmpl.yaml
- 执行 refund-policy-check 清单
  acceptance:
- 条款合规/路径清晰
- 对账可核
