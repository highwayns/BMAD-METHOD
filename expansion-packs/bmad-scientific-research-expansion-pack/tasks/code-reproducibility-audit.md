# Code Reproducibility Audit

## Purpose

验证代码/分析可复现：环境锁定、依赖快照、随机种子、数据版本、结果一致性。

## Checks

- 环境与依赖：`requirements.lock` / `conda.yaml` / `dockerfile`
- 随机性：固定种子、可重复训练/推理日志
- 结果：再运行误差阈值与统计稳定性

## Output

- `reports/reproducibility.md`（通过/需修复项）
