# task: evaluation

version: 1.0
role: guide-leader-manager
purpose: 进行绩效评估并输出晋升/培训建议。
inputs: [KPI, 软性评分, 口碑与异常时效]
outputs: [reports/guide-evaluation-<period>.md]
steps:

- 渲染 templates/guide-evaluation-tmpl.yaml
- 归档证据与签核
  acceptance:
- 评分依据明确
- 建议可执行
