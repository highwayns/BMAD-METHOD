# SQL Style Guide (摘)

- CTE分段清晰，命名含义化；避免SELECT \*
- 所有时间戳以UTC存储，展示按时区
- 先过滤后JOIN，控制行数与基数
- 使用 COALESCE/NULLIF 处理缺失
- 注释口径来源与已知限制
