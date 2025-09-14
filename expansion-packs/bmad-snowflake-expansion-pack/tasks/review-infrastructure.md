# review-infrastructure | Snowflake

<!-- BMAD Task Spec -->

## Purpose

基于 16 节质量门，对 Snowflake 平台的安全、治理、性能、可靠性、成本与运维现状做系统复核，输出改进与路线图。

## Inputs

- 架构/实施文档、CI/CD、监控与账单
- checklists/snowflake-infrastructure-checklist.md

## Key Activities & Instructions

### 1) Confirm Interaction Mode

- **Incremental（默认）**：逐章核对 → 记录证据与缺口 → 节末小结
- **YOLO**：全局扫描 → 输出综合报告（速度优先）

### 2) Prepare for Review

- 范围/时窗/环境/风险承受，证据（监控/日志/事故/成本）

### 3) Conduct Systematic Review (Incremental)

对 1–16 章逐章执行：Current State / Gaps & Recos / Advanced Options(1–7) / Section Summary

### 4) Generate Findings Report

- 分类总结 + 优先级 + 投入/影响 + 路线图 + 成本优化

## BMAD Integration Assessment

- Dev/Product/Architecture 的支撑度、冲突与缺口

## Architectural Escalation Assessment

- Critical | Significant | Operational | Unclear 的分级与建议

## Present & Plan

- 高层摘要、技术说明与行动清单

## Execute Escalation Protocol

- 触发会审/运维改进并留痕

## Outputs

- 评估报告、优先级清单、整改计划与升级记录
