# jp-tourism-ops-kb.md

## 1. 典型业务对象（Domain Entities）

Guest, Booking, Itinerary, Service(接送/包车/门票/导游), Vendor(车队/酒店/票务), Vehicle, Guide, SLA, Dispatch, Incident, Invoice, Payment。

## 2. 关键KPI字典

- 准点率（On-time%）
- 当日履约率 / 取消率
- 投诉率 / NPS
- 人均消费（含二销） / 客单毛利率
- 资源利用率（车/导/房/票）
- 投诉闭环时长 / 事故首响时长

## 3. 运营节律（Seasonality）

樱花/黄金周/暑期/红叶/年末年初/雪季；旺季采用弹性资源池（兼职导游/临时车队/房券/票券）与差异化价格策略。

## 4. 典型流程（简版）

- 订单导入→资质/SLA校验→容量匹配→行程编排→供应商锁定→日派单→现场执行→收尾与结算→复盘与知识沉淀。
- 异常处置：监测→告警→分级→指挥→调度→关怀→取证→报告→复盘。

## 5. 文档与目录建议

- `docs/ops/plan.md` 运营方案；`docs/ops/runbook-*.md` 运行手册；`data/vendor/*.yaml` 供应商；`reports/` 报表。

## 6. 人在回路（签核关口）

- 高风险行程变更、重大投诉赔付、事故报告定稿、旺季价格策略变更。
