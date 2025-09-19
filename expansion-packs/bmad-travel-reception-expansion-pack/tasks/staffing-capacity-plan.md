# task: staffing-capacity-plan

version: 1.0
role: operations-director
purpose: 盘点人车房票资源池，做峰值缺口与招募/外包计划。
inputs:

- 资源库存/订单预测/合规边界
  outputs:
- docs/ops/staffing-capacity-plan.md
  steps:
- create-doc → templates/staffing-capacity-plan-tmpl.yaml
- 招募培训/外包与联络清单落地
  acceptance:
- 缺口与落实人/时限清晰
- 与峰季方案/价规联动
