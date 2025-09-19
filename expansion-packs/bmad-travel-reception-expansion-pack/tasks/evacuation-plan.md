# task: evacuation-plan

version: 1.0
role: risk-safety-manager
purpose: 形成撤离路线/集合点与联动通讯方案。
inputs: [动线/集合点/替代点, 对讲/场地方/警方/救护]
outputs: [docs/risk/evacuation-<venue>.md]
steps:

- 渲染 templates/evacuation-plan-tmpl.yaml
- 执行 medical-evac-check 清单
  acceptance:
- 路线可达/障碍可知
- 联动可拨通
