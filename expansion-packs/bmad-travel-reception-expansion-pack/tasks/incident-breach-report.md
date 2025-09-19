# task: incident-breach-report

version: 1.0
role: legal-compliance
purpose: 记录事故/数据事件并对齐通知义务与口径。
inputs: [类型/范围/人数/影响, 通知对象与期限]
outputs: [reports/legal/incident-<id>.md]
steps:

- 渲染 templates/incident-breach-report-tmpl.yaml
- 执行 incident-breach-check 与 regulator-reporting-check
  acceptance:
- 证据链完整
- 报备合规
