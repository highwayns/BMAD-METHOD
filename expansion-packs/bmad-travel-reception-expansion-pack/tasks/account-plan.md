# task: account-plan

version: 1.0
role: sales-account-manager
purpose: 规划账户增长目标、机会包与行动闭环。
inputs: [历史订单, KPI, 预算/节律]
outputs: [docs/sales/account-plan-<client>.md]
steps:

- templates/account-plan-tmpl.yaml 渲染
- 识别续签/扩销机会
- 形成里程碑与负责人
  acceptance:
- 目标明确可量化
- 行动清单有负责人与截止
