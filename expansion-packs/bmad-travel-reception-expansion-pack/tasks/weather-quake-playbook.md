# task: weather-quake-playbook

version: 1.0
role: risk-safety-manager
purpose: 制定极端天气/地震/海啸的阈值与A/B/C方案。
inputs: [预警等级/停运清单, 改线/取消编号, 责任与时限]
outputs: [docs/risk/weather-quake-playbook.md]
steps:

- 渲染 templates/weather-quake-playbook-tmpl.yaml
- 执行 typhoon-flood-check / quake-response-check
  acceptance:
- 触发清晰/动作明确
- 沟通口径一致
