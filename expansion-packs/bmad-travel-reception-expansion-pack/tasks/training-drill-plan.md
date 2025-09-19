# task: training-drill-plan

version: 1.0
role: risk-safety-manager
purpose: 设计训练/演练计划并评估效果。
inputs: [主题/频次/对象, 评估与改进]
outputs: [reports/training-drill-<period>.md]
steps:

- 渲染 templates/training-drill-plan-tmpl.yaml
- 形成评分与改进项
  acceptance:
- 覆盖与合格率达标
- 行动闭环
