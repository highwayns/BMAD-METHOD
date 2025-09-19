# task: safety-briefing

version: 1.0
role: risk-safety-manager
purpose: 生成出行安全讲解并覆盖敏感与弱势群体。
inputs: [集合/点名/紧急集合点, 交通/天气/拥挤, 过敏/无障碍/弱势]
outputs: [docs/risk/safety-brief-<group>.md]
steps:

- 渲染 templates/safety-briefing-tmpl.yaml
- 执行 safeguarding-check 清单（如有未成年人）
  acceptance:
- 重点清晰可复述
- 多语言可用
