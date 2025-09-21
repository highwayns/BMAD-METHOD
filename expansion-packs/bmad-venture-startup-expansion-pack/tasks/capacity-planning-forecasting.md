# Capacity Planning & Forecasting

## Purpose

基于历史速度/请假日历/并发限制进行容量计划与交付预测。

## Inputs

- 速度历史/假期/外部窗口
- templates/capacity-and-velocity-plan-tmpl.yaml
- templates/burndown-burnup-spec-tmpl.yaml

## Outputs

- 容量与预测报告。

## Steps

1. 确定能力单位与团队速度区间
2. 假设与不确定性建模
3. 蒙特卡洛/范围敏感性（可选）
4. 生成燃尽/燃起与承诺区间
5. 对齐风险与缓冲
