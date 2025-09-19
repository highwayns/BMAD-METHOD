# task: hira-route-activity

version: 1.0
role: risk-safety-manager
purpose: 对关键路线/活动进行HIRA并给出缓冲与PPE。
inputs: [区间/活动/季节, 危害/等级/缓冲, 装备/PPE]
outputs: [docs/risk/hira-<route_or_activity>.md]
steps:

- 渲染 templates/hira-route-activity-tmpl.yaml
- 执行 heat-cold-stress-check / crowd-crush-check（按需）
  acceptance:
- 风险与缓冲合理
- 装备清单明确
