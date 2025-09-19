# task: rail-coordination

version: 1.0
role: transport-logistics-coordinator
purpose: 设计铁路换乘缓冲与无障碍动线，确保衔接成功率。
inputs: [关键换乘段, 步行距离/设备, 备用车次]
outputs: [docs/transport/rail-connection-plan.md]
steps:

- 渲染 templates/rail-connection-plan-tmpl.yaml
- 执行 rail-buffer-check 清单
  acceptance:
- 缓冲分钟数合理
- 无障碍与备用方案可行
