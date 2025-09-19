# task: upsell-campaign

version: 1.0
role: sales-account-manager
purpose: 策划并执行扩销/交叉销售活动。
inputs: [分层客群, 产品包, 价规]
outputs: [docs/sales/upsell-campaign-<name>.md]
steps:

- templates/upsell-campaign-tmpl.yaml 渲染
- 运行并跟踪KPI
  acceptance:
- 活动目标与KPI明确
- 复盘输出并入知识库
