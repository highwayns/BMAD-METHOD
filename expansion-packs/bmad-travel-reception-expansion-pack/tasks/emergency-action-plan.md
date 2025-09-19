# task: emergency-action-plan

version: 1.0
role: risk-safety-manager
purpose: 建立应急行动预案（ICS/角色/步骤/升级）。
inputs: [指挥/联络/医疗/疏导, 首轮动作/升级/回执]
outputs: [docs/risk/eap.md]
steps:

- 渲染 templates/emergency-action-plan-tmpl.yaml
- 执行 emergency-activation-check 清单
  acceptance:
- 指挥链清晰
- 升级阈值明确
