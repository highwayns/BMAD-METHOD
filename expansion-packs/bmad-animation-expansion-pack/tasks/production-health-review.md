# Task · production-health-review

**intent**: 周度生产健康巡检与 S 曲线评估  
**elicit**: false

## 输入

- 当前周 WBS 进展、Dailies 通过率、渲染队列 KPI

## 输出

- `reports/health-week-YYYYWW.md` 与 JSON 摘要（burnup、通过率、阻塞TOP5）
