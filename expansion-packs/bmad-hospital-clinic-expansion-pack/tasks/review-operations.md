# Review Operations Task

## Purpose

院级运营“快速体检”。支持 **交互式逐段** 或 **YOLO 批量** 两种方式，结合 `checklists/hospital-operations-checklist.md` 出具改进建议与行动单。

## Instructions

1. 询问用户选择模式（1. 逐段 / 2. YOLO）。
2. 收集必要资料（组织架构、SOP、上月 KPI、QPS 报表、合规与事故记录）。
3. 依据清单执行：将每节标记 ✅/⚠️/❌/N/A 并给出证据与建议。
4. 生成《运营体检报告》：结论、风险优先级、30/60/90 日行动计划、责任人、复盘节奏。

## Output

使用模板 `templates/output/audit-report-tmpl.yaml` 通过 \*create-doc 生成报告。
