# task: invitation-sponsor

version: 1.0
role: visa-insurance-specialist
purpose: 生成邀请/担保材料口径（访友/商务/落地接待）。
inputs: [邀请方/担保方信息, 必要函件与证明]
outputs: [docs/visa/invitation-sponsor-<case>.md]
steps:

- 渲染 templates/invitation-sponsor-pack-tmpl.yaml
- 与产品/运营确认口径
  acceptance:
- 函件齐全/抬头地址准确
- 联系方式与签章有效
