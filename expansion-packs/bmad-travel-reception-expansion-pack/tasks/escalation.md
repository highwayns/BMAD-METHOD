# task: escalation

version: 1.0
role: customer-service-care-lead
purpose: 建立按事件分级的升级与支援Runbook。
inputs: [类型/等级/联系人/电话/触发]
outputs: [docs/care/escalation-runbook.md]
steps:

- 渲染 templates/escalation-runbook-tmpl.yaml
- 执行 escalation-check 清单
  acceptance:
- 线路清晰/打得通
- 演练通过
