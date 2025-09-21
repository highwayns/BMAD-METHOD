# Canary, Feature Flags & Rollout Policy

## Purpose

制定灰度/特性开关/分批发布与监控策略。

## Inputs

- 指标/用户分群/流量路由/监控
- templates/canary-rollout-plan-tmpl.yaml
- checklists/canary-rollout-steps.md

## Outputs

- 灰度方案与监控阈值。

## Steps

1. 分批、金丝雀与地域/租户/百分比
2. 卫星指标：转化/错误/延迟/崩溃
3. 自动停止与回滚触发
4. AB/逐步扩大与对照组
5. 沟通与问答稿
