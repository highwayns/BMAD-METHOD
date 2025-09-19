# task: qbr

version: 1.0
role: sales-account-manager
purpose: 进行季度业务回顾，巩固关系与确定增量机会。
inputs: [履约KPI, 事件/改进, 路线图/套餐]
outputs: [reports/qbr-<client>-<YYYYQ>.md]
steps:

- templates/qbr-report-tmpl.yaml 渲染
- 行动项与责任人/时限落地
  acceptance:
- KPI呈现清晰，行动闭环可跟踪
- 客户确认收到并认可
