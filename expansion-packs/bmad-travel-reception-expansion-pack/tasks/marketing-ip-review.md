# task: marketing-ip-review

version: 1.0
role: legal-compliance
purpose: 评审营销素材与IP授权边界，防误导。
inputs: [文案/图片/视频/授权, 风险提示]
outputs: [docs/legal/marketing-review-<campaign>.md]
steps:

- 渲染 templates/marketing-ip-review-tmpl.yaml
- 执行 marketing-comms-check 清单
  acceptance:
- 素材授权明确
- 陈述真实可证
