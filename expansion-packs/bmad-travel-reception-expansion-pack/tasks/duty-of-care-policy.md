# task: duty-of-care-policy

version: 1.0
role: risk-safety-manager
purpose: 建立照护义务政策与记录要求。
inputs: [责任/边界/沟通/记录]
outputs: [docs/risk/duty-of-care-policy.md]
steps:

- 渲染 templates/duty-of-care-policy-tmpl.yaml
- 对外公示并培训
  acceptance:
- 条款明确
- 覆盖全面
