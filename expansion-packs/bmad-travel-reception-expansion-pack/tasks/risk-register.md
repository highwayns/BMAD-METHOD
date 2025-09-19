# task: risk-register

version: 1.0
role: risk-safety-manager
purpose: 建立与维护风险登记册，明确控制与责任。
inputs: [场景/危害/触发, 概率/影响/等级, 控制/缓解/责任]
outputs: [docs/risk/risk-register.md]
steps:

- 渲染 templates/risk-register-tmpl.yaml（逐节提问）
- 与现场/运输/导游/酒店联动确认
  acceptance:
- 风险项完整与优先级清晰
- 控制措施可执行
