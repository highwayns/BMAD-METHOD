# E2E Regression & Critical User Flows

## Purpose

构建关键用户旅程E2E套件与最小回归包（MVP回归）。

## Inputs

- 用户旅程/遥测/历史故障
- templates/e2e-regression-pack-tmpl.yaml
- checklists/production-readiness.md

## Outputs

- E2E回归方案与脚本清单。

## Steps

1. 挑选少而精的关键路径
2. 稳定性工程：数据隔离/等待策略/重试/可观测点
3. 跨浏览器/设备/地域策略
4. 与特性开关/灰度联动
5. 上线后合成监控复用
