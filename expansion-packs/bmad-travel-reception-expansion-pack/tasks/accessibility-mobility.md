# task: accessibility-mobility

version: 1.0
role: transport-logistics-coordinator
purpose: 为无障碍与行动辅助人群制定登车/动线方案。
inputs: [设备与需求, 人员分工, 上落客点]
outputs: [docs/transport/accessibility-mobility-plan.md]
steps:

- 渲染 templates/accessibility-mobility-plan-tmpl.yaml
- 执行 accessibility-boarding-check 清单
  acceptance:
- 设备/动线/责任清晰
- 现场可执行
