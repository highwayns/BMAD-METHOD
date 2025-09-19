# task: vehicle-maintenance-check

version: 1.0
role: transport-logistics-coordinator
purpose: 建立车辆维护抽检与复核机制。
inputs: [部件/状态/证据, 处理与复核]
outputs: [reports/vehicle-maintenance-YYYYMM.md]
steps:

- 渲染 templates/vehicle-maintenance-check-tmpl.yaml
- 抽检记录与整改闭环
  acceptance:
- 安全项达标
- 复核在案
