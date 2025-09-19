# task: medical-assistance-plan

version: 1.0
role: risk-safety-manager
purpose: 准备医疗协助网络与就医/垫付/转运流程。
inputs: [医院/翻译/支付, 就医/垫付/转运]
outputs: [docs/risk/medical-assistance-<area>.md]
steps:

- 渲染 templates/medical-assistance-plan-tmpl.yaml
- 执行 medical-evac-check 清单
  acceptance:
- 路径明确
- 联系有效
