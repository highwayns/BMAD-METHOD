# task: post-tour-debrief

version: 1.0
role: guide-leader-manager
purpose: 收团复盘并沉淀改进行动。
inputs: [准点/投诉/事故/失物, NPS/点评, 改进建议]
outputs: [reports/guide-debrief-YYYYMMDD.md]
steps:

- 渲染 templates/post-tour-debrief-tmpl.yaml
- 执行 post-tour-debrief-check 清单
  acceptance:
- 证据与数据到位
- 改进行动可跟踪
