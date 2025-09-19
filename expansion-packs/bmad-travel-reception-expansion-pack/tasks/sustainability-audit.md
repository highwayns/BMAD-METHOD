# task: sustainability-audit

version: 1.0
role: vendor-procurement-manager
purpose: 审计供应商ESG状况并提出改进。
inputs: [环保/节能/废弃物, 无障碍/公平/社区]
outputs: [reports/vendor-esg-<vendor>.md]
steps:

- 渲染 templates/sustainability-audit-tmpl.yaml
- 执行 sustainability-check 清单
  acceptance:
- 指标与改进项明确
- 跟踪复核
