# Task: Create Program Catalog

## Purpose

建立学术项目/专业目录（项目目标、产出、课程构成、学制、学分、对标标准）。

## Inputs

- 市场/行业输入（可选）
- 认证与对标标准（kb/academic-standards.md, templates/data/accreditation_standards.csv）
- 现有课程清单（templates/data/courses.csv）

## Steps

1. 读取对标标准与项目目标 → 起草项目画像与学习产出(PO)
2. 生成项目-课程-学分框架与修读路径
3. 对齐合规（可及性/隐私/诚信）与质量门（Rubric/KPI）
4. 产出 program-catalog.md（使用 program-catalog-tmpl.yaml）

## Elicitation

- 对每节内容启用 `elicit: true` 的 1–9 交互评审。
