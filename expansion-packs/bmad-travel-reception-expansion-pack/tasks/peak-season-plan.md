# task: peak-season-plan

version: 1.0
role: operations-director
purpose: 旺季弹性产能、差异化定价与备选方案落地。
inputs:

- 需求预测与峰值时段
- 兼职导游/临时车队/酒店联动
- 旺季价规/超售策略
  outputs:
- docs/ops/peak-season-plan.md
  steps:
- 启动 create-doc 使用 templates/peak-season-plan-tmpl.yaml
- 衔接 staffing-capacity-plan 与价格审批
- 演练高峰日调度/事故处置
  acceptance:
- 缺口测算与资源落实清单
- 价规/审批链路与生效时间
- 演练记录与抽查通过
