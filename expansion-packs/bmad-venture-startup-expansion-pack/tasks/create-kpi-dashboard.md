# Create KPI Dashboard

## Purpose

构建少而精的公司级KPI看板，服务周/月复盘与董事会。

## Inputs

- 数据源定义（产品/CRM/财务）
- templates/kpi-dashboard-tmpl.yaml

## Outputs

- 一份KPI仪表盘定义与当前数值快照。

## Steps

1. 选择≤8个高置信KPI（含北极星指标）
2. 定义数据口径、更新频率与Owner
3. 生成并填充kpi-dashboard-tmpl.yaml
4. 与PM/数据团队校验一致性与可获取性
5. 纳入ceo-weekly-review清单
