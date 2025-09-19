# task: invoice-recon

version: 1.0
role: sales-account-manager
purpose: 完成发票与应收对账，推进回款。
inputs: [账期, 订单/发票清单]
outputs: [reports/invoice-recon-<period>.md]
steps:

- templates/invoice-recon-tmpl.yaml 渲染
- 列出差异并分配处理动作
- 更新账龄/回款计划
  acceptance:
- 差异闭环率≥95%
- 账龄更新
