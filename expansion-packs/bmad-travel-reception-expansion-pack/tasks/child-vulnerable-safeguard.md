# task: child-vulnerable-safeguard

version: 1.0
role: risk-safety-manager
purpose: 建立未成年人/弱势群体保护SOP与应对。
inputs: [监护与授权, 单独接触边界, 报告与协助]
outputs: [docs/risk/safeguard-policy.md]
steps:

- 渲染 templates/child-vulnerable-safeguard-tmpl.yaml
- 执行 safeguarding-check 清单
  acceptance:
- 边界清晰/流程合法
- 多语言可用
