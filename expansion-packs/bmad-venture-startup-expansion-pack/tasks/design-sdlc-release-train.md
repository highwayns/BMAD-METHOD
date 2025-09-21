# Design SDLC & Release Train

## Purpose

定义SDLC工作流、分支策略、质量关卡与发布列车节奏。

## Inputs

- 当前研发流程与工具链
- 质量/合规需求
- templates/release-plan-tmpl.yaml

## Outputs

- 发布列车计划与质量关卡清单、回滚预案。

## Steps

1. 统一需求/设计/开发/测试/发布的状态机与工件
2. 定义质量门（单测覆盖/安全扫描/性能基线）
3. 确立蓝绿/灰度/回滚策略
4. 制定列车节奏与冻结窗口
5. 同步变更管理流程
