# task: pipeline-guided-selling

version: 1.0
role: tech-systems-dms-crm
purpose: 定义管道阶段与进出条件，落地引导式销售。
inputs: [阶段/进出条件/赢率]
outputs: [docs/sys/pipeline-<segment>.md]
steps:

- 渲染 templates/pipeline-stages-tmpl.yaml
- 执行 pipeline-health-check 清单
  acceptance:
- 阶段清晰/转化提升
- 报表一致
