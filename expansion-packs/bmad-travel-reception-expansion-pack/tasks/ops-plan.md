# task: ops-plan

version: 1.0
role: operations-director
purpose: 产出日本旅游接待的年度/季度运营方案。
inputs:

- 业务范围/客群/季节窗口
- 资源容量与SLA目标
- 定价与条款/风险预案
  outputs:
- docs/ops/ops-plan.md
  steps:
- 启动 create-doc 使用 templates/ops-plan-tmpl.yaml
- 补充KPI口径、报表频率与签核关口
- 归档至版本库并发布摘要给相关方
  acceptance:
- 含容量/定价/SLA/风险/报表章节
- KPI与签核关口明确
- 发布记录与受众确认
