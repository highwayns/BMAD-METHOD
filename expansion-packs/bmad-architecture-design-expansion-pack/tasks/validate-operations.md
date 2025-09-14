# validate-operations | Architecture Design

<!-- BMAD Task Spec -->

## Purpose

以标准化 16 章节检查清单执行报批/投标/发图前验证与评分，生成准入与整改报告。

## Inputs

- checklists/arch-operations-checklist.md
- 合同/法规/模型/图纸/台账/报批/投标/CA 证据与审计日志

## Key Activities & Instructions

1. 选择 **Incremental** 或 **YOLO**；默认 Incremental
2. 逐条验证：记录证据链接、是/否与备注
3. 自动汇总评分与阻断项（Critical/High 阻断报批/发图/投标）
4. 形成整改计划与复核时间窗

## Outputs

- 验证结果表、合规率、阻断/警告项、整改计划与负责人
