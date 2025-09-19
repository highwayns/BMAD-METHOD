# task: crowd-safety-plan

version: 1.0
role: risk-safety-manager
purpose: 人群密集活动防踩踏方案与广播模板。
inputs: [密度阈值/流线/节拍, 溢出/集合/广播]
outputs: [docs/risk/crowd-safety-<venue>-<date>.md]
steps:

- 渲染 templates/crowd-safety-plan-tmpl.yaml
- 执行 crowd-crush-check 清单
  acceptance:
- 阈值科学
- 现场可落地
