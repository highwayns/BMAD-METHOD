# task: property-safety-audit

version: 1.0
role: hotel-contracting-manager
purpose: 对物业开展安全/无障碍/温泉合规稽核。
inputs: [消防/疏散/无障碍/温泉规则]
outputs: [reports/property-safety-audit-<hotel>.md]
steps:

- 渲染 templates/property-safety-audit-tmpl.yaml
- 形成整改计划与复核时间表
  acceptance:
- 问题/整改/时限明确
- 复核记录在案
