# Test Automation Pyramid & Coverage Model

## Purpose

制定自动化金字塔（单元/契约/集成/E2E）与覆盖模型。

## Inputs

- 服务/组件/接口/依赖
- templates/automation-plan-tmpl.yaml
- templates/coverage-matrix-tmpl.yaml
- checklists/automation-code-review.md

## Outputs

- 自动化计划与覆盖矩阵。

## Steps

1. 识别关键路径与回归候选
2. 拆分到层：快速/稳定/低耦合优先
3. Mock与契约测试优先于脆弱的端到端
4. 将测试纳入流水线与质量门
5. 度量：通过率/时长/波动/波及面
