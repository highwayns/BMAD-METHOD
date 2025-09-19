# task: crowd-control

version: 1.0
role: onsite-ops-lead
purpose: 设计并落地人群管控，降低拥挤与走失风险。
inputs: [密度阈值, 动线策略, 围栏/物料, 联动渠道]
outputs: [docs/onsite/crowd-control-<venue>-<date>.md]
steps:

- 渲染 templates/crowd-control-plan-tmpl.yaml
- 执行 crowd-safety-check 清单
  acceptance:
- 阈值与策略明确
- 物料/联动就绪
