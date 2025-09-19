# task: incentive-promo

version: 1.0
role: guide-leader-manager
purpose: 设计导游激励与晋升方案。
inputs: [指标门槛, 奖金与称号, 有效期与复核]
outputs: [docs/guide/incentive-promo.md]
steps:

- 渲染 templates/incentive-promo-tmpl.yaml
- 公告并跟踪生效
  acceptance:
- 指标可衡量
- 生效日期明确
