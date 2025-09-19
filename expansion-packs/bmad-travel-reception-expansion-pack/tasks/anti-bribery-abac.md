# task: anti-bribery-abac

version: 1.0
role: legal-compliance
purpose: 建立ABAC政策与申报/调查/处分流程。
inputs: [礼品/招待/回扣门槛, 利益冲突/第三方风险]
outputs: [docs/legal/abac-policy.md]
steps:

- 渲染 templates/anti-bribery-abac-tmpl.yaml
- 执行 anti-bribery-check 清单
  acceptance:
- 门槛明确
- 记录留痕
