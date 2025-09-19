# task: ros-script

version: 1.0
role: guide-leader-manager
purpose: 输出导游讲解脚本（ROS），统一口径与体验。
inputs: [场景分镜, 要点与时长, 敏感话题注意]
outputs: [docs/guide/ros-script.md]
steps:

- 渲染 templates/ros-guide-script-tmpl.yaml
- 执行 content-boundary-check 清单
  acceptance:
- 场景与要点清晰
- 边界与礼仪明确
