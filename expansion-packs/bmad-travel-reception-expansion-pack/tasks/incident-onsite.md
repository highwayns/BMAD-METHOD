# task: incident-onsite

version: 1.0
role: onsite-ops-lead
purpose: 记录并复盘现场事件，完成取证与预防改进。
inputs: [时间地点参与人, 处置与联动, 证据, 根因与预防]
outputs: [reports/onsite-incident-YYYYMMDD.md]
steps:

- 渲染 templates/incident-onsite-tmpl.yaml
- 执行 photo-evidence-check 与 radio-comms-check
  acceptance:
- 首轮响应与证据到位
- 预防措施明确
