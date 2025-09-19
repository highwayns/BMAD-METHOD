# task: minors-consent

version: 1.0
role: visa-insurance-specialist
purpose: 生成未成年人随行授权与同意文书。
inputs: [亲属/出生证明, 监护声明/公证/认证]
outputs: [docs/visa/minors-consent-<traveler>.md]
steps:

- 渲染 templates/minors-consent-pack-tmpl.yaml
- 执行 minors-consent-check 清单
  acceptance:
- 文书合规
- 认证链条明确
