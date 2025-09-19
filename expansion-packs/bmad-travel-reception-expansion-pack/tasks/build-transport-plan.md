# task: build-transport-plan

version: 1.0
role: transport-logistics-coordinator
purpose: 形成可执行的运输总体方案（容量/许可/风险）。
inputs: [行程/客群, 车辆与司机, 许可/上落客点, 风险与改线]
outputs: [docs/transport/transport-master-plan.md]
steps:

- 渲染 templates/transport-master-plan-tmpl.yaml（逐节提问）
- 产出KPI与缓冲策略
  acceptance:
- 容量/许可/预案齐全
- KPI可观测
