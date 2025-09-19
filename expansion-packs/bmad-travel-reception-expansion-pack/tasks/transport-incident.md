# task: transport-incident

version: 1.0
role: transport-logistics-coordinator
purpose: 记录并复盘交通事件，完成取证与根因分析。
inputs: [时间地点车辆司机, 参与人联系方式, 证据材料]
outputs: [reports/transport-incident-YYYYMMDD.md]
steps:

- 渲染 templates/transport-incident-report-tmpl.yaml
- 48小时内提交复盘
  acceptance:
- 首轮响应留痕
- 根因与预防明确
