# task: fuel-toll-recon

version: 1.0
role: transport-logistics-coordinator
purpose: 对账燃油/过路/停车成本与差异处理。
inputs: [账期, 订单/司机/车辆, 账单与应计]
outputs: [reports/fuel-toll-recon-<period>.md]
steps:

- 渲染 templates/fuel-toll-recon-tmpl.yaml
- 列出差异/责任人/期限
  acceptance:
- 差异闭环≥95%
- KPI更新
