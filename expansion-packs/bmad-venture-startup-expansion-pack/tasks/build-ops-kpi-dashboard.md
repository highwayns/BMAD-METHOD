# Build Ops KPI Dashboard

## Purpose

选取少而精的运营KPI并建立看板（DORA、SLA、成本、体验）。

## Inputs

- 数据源定义（产品/平台/客服/财务）
- templates/ops-kpi-dashboard-tmpl.yaml

## Outputs

- KPI仪表盘定义与当前数值快照。

## Steps

1. 选择≤10个KPI（如部署频率、变更失败率、MTTR、可用性、On-time交付、工单SLA达成率、单位成本、毛利率）
2. 定义指标公式/口径/Owner/告警阈值
3. 生成并填充模板
4. 与数据团队校验可获取性
5. 纳入ops-weekly-review
