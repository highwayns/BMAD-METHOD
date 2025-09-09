# -*- coding: utf-8 -*-
"""
BMAD-Method | Databricks (Lakehouse) RolePack Generator
- 18 角色：人格/任务/输入输出契约/DoR/DoD/编排与交接
- manifests：角色清单/能力矩阵/工作流索引
- workflows：编排手册/泳道图/交接契约
- templates：docs + code(notebooks/dlt/ml) + iac(terraform) + ci-cd + policies + monitoring + data(csv)
- checklists：质量门/命名/契约&DQ/Delta&UC/安全隐私/FinOps/可观测/变更/回填/反模式
- delivery：打包与合并规则
- 输出 ZIP
"""
import os, json, csv, zipfile, textwrap, datetime

TODAY = datetime.date.today().strftime("%Y-%m-%d")
BASE = os.path.abspath("./bmad-databricks-rolepack")

# ---------- helpers ----------
def mkdirs(paths):
    for p in paths: os.makedirs(p, exist_ok=True)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f: f.write(content)

def write_csv(path, headers):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow(headers)

# ---------- 1) directories ----------
mkdirs([
    BASE,
    f"{BASE}/roles",
    f"{BASE}/manifests",
    f"{BASE}/workflows",
    f"{BASE}/templates/docs",
    f"{BASE}/templates/data",
    f"{BASE}/templates/code/notebooks",
    f"{BASE}/templates/code/dlt",
    f"{BASE}/templates/code/ml",
    f"{BASE}/templates/iac/terraform",
    f"{BASE}/templates/ci-cd",
    f"{BASE}/templates/policies",
    f"{BASE}/templates/monitoring",
    f"{BASE}/checklists",
    f"{BASE}/delivery",
])

# ---------- 2) roles ----------
ROLES = [
    {"id":"01","name":"Platform Owner","aliases":["平台负责人"],"file":"01-platform-owner.md"},
    {"id":"02","name":"Lakehouse Architect","aliases":["湖仓一体架构师"],"file":"02-lakehouse-architect.md"},
    {"id":"03","name":"Product Manager","aliases":["产品经理"],"file":"03-product-manager.md"},
    {"id":"04","name":"Business Analyst","aliases":["业务分析师"],"file":"04-business-analyst.md"},
    {"id":"05","name":"Data Contract Owner","aliases":["数据契约负责人"],"file":"05-data-contract-owner.md"},
    {"id":"06","name":"Data Engineering Lead","aliases":["数据工程负责人"],"file":"06-data-engineering-lead.md"},
    {"id":"07","name":"Streaming Engineer","aliases":["流处理工程师（Autoloader/DLT）"],"file":"07-streaming-engineer.md"},
    {"id":"08","name":"Analytics Engineer (BI/SQL)","aliases":["Analytics Engineer（BI/SQL/DBSQL）"],"file":"08-analytics-engineer-biqt.md"},
    {"id":"09","name":"ML Engineer (MLOps)","aliases":["ML 工程师/MLOps"],"file":"09-ml-engineer-mlops.md"},
    {"id":"10","name":"DataOps / SRE","aliases":["DataOps / SRE"],"file":"10-dataops-sre.md"},
    {"id":"11","name":"Security & Governance (Unity Catalog)","aliases":["安全与治理（Unity Catalog）"],"file":"11-security-governance-uc.md"},
    {"id":"12","name":"Privacy & Compliance","aliases":["隐私与合规"],"file":"12-privacy-compliance.md"},
    {"id":"13","name":"FinOps Cost Optimizer","aliases":["FinOps 成本优化"],"file":"13-finops-cost-optimizer.md"},
    {"id":"14","name":"Observability & Reliability","aliases":["可观测性与可靠性"],"file":"14-observability-reliability.md"},
    {"id":"15","name":"Release & Change Manager","aliases":["发布与变更管理"],"file":"15-release-change-manager.md"},
    {"id":"16","name":"DevEx & Platform Automation","aliases":["DevEx 与平台自动化"],"file":"16-devex-platform-automation.md"},
    {"id":"17","name":"Quality Assurance (Data & Code Tests)","aliases":["质量保证（数据/代码测试）"],"file":"17-quality-assurance-data-tests.md"},
    {"id":"18","name":"Support & Incident Manager","aliases":["支持与事件经理"],"file":"18-support-incident-manager.md"},
]

DEPENDS = {
    "Platform Owner": [],
    "Lakehouse Architect": ["Platform Owner","Product Manager","Security & Governance (Unity Catalog)"],
    "Product Manager": ["Business Analyst","Platform Owner"],
    "Business Analyst": ["Product Manager"],
    "Data Contract Owner": ["Business Analyst","Product Manager"],
    "Data Engineering Lead": ["Lakehouse Architect","Data Contract Owner"],
    "Streaming Engineer": ["Lakehouse Architect","Data Engineering Lead"],
    "Analytics Engineer (BI/SQL)": ["Lakehouse Architect","Data Contract Owner","Data Engineering Lead"],
    "ML Engineer (MLOps)": ["Data Engineering Lead","Analytics Engineer (BI/SQL)"],
    "DataOps / SRE": ["Platform Owner","Data Engineering Lead"],
    "Security & Governance (Unity Catalog)": ["Platform Owner","Privacy & Compliance"],
    "Privacy & Compliance": ["Security & Governance (Unity Catalog)","Product Manager"],
    "FinOps Cost Optimizer": ["Platform Owner","Product Manager"],
    "Observability & Reliability": ["DataOps / SRE","Data Engineering Lead","Streaming Engineer","ML Engineer (MLOps)"],
    "Release & Change Manager": ["Data Engineering Lead","Analytics Engineer (BI/SQL)","ML Engineer (MLOps)","Quality Assurance (Data & Code Tests)"],
    "DevEx & Platform Automation": ["Platform Owner","Lakehouse Architect","Release & Change Manager"],
    "Quality Assurance (Data & Code Tests)": ["Data Contract Owner","Data Engineering Lead","Analytics Engineer (BI/SQL)"],
    "Support & Incident Manager": ["Observability & Reliability","DataOps / SRE"],
}
HANDOFF = {
    "Platform Owner": ["Lakehouse Architect","Security & Governance (Unity Catalog)","FinOps Cost Optimizer","DataOps / SRE"],
    "Lakehouse Architect": ["Data Engineering Lead","Streaming Engineer","Analytics Engineer (BI/SQL)","ML Engineer (MLOps)","Security & Governance (Unity Catalog)"],
    "Product Manager": ["Business Analyst","Data Contract Owner","Lakehouse Architect","Release & Change Manager"],
    "Business Analyst": ["Data Contract Owner","Lakehouse Architect"],
    "Data Contract Owner": ["Lakehouse Architect","Data Engineering Lead","Quality Assurance (Data & Code Tests)"],
    "Data Engineering Lead": ["Streaming Engineer","Analytics Engineer (BI/SQL)","DataOps / SRE","Release & Change Manager"],
    "Streaming Engineer": ["Observability & Reliability","Analytics Engineer (BI/SQL)","ML Engineer (MLOps)"],
    "Analytics Engineer (BI/SQL)": ["Release & Change Manager","Quality Assurance (Data & Code Tests)"],
    "ML Engineer (MLOps)": ["Release & Change Manager","Observability & Reliability"],
    "DataOps / SRE": ["Observability & Reliability","Support & Incident Manager"],
    "Security & Governance (Unity Catalog)": ["Release & Change Manager","Data Engineering Lead","Analytics Engineer (BI/SQL)","ML Engineer (MLOps)"],
    "Privacy & Compliance": ["Security & Governance (Unity Catalog)","Release & Change Manager"],
    "FinOps Cost Optimizer": ["Platform Owner","Release & Change Manager"],
    "Observability & Reliability": ["Support & Incident Manager","Platform Owner"],
    "Release & Change Manager": ["DevEx & Platform Automation","Support & Incident Manager"],
    "DevEx & Platform Automation": ["All Roles"],
    "Quality Assurance (Data & Code Tests)": ["Release & Change Manager","Support & Incident Manager"],
    "Support & Incident Manager": ["All Roles"],
}

IO = {
 "Platform Owner": (["templates/docs/tf-landing-zone-guide.md","templates/docs/cluster-policy.md"], ["templates/docs/runbook.md"]),
 "Lakehouse Architect": (["templates/docs/domain-data-map.md","templates/docs/data-contract.md"], ["templates/docs/lakehouse-architecture.md","templates/docs/delta-table-spec.md","templates/docs/uc-catalog-policy.md"]),
 "Product Manager": (["templates/docs/domain-data-map.md"], ["templates/docs/batch-pipeline-design.md","templates/data/jobs_schedule.csv"]),
 "Business Analyst": (["templates/docs/domain-data-map.md"], ["templates/docs/data-contract.md","templates/docs/silver-to-gold-modeling.md"]),
 "Data Contract Owner": (["templates/docs/data-contract.md","templates/data/dq_rules.csv"], ["templates/data/data_contracts.csv"]),
 "Data Engineering Lead": (["templates/docs/dlt-design.md","templates/docs/batch-pipeline-design.md"], ["templates/code/dlt/pipeline.py","templates/docs/job-runbook.md"]),
 "Streaming Engineer": (["templates/docs/streaming-autoloader-design.md"], ["templates/code/notebooks/streaming_autoloader.py"]),
 "Analytics Engineer (BI/SQL)": (["templates/docs/silver-to-gold-modeling.md"], ["templates/code/notebooks/gold_mart.sql"]),
 "ML Engineer (MLOps)": (["templates/docs/feature-store-spec.md","templates/docs/ml-experiment-plan.md"], ["templates/code/ml/feature_engineering.py","templates/docs/model-card.md","templates/docs/serving-config.md"]),
 "DataOps / SRE": (["templates/docs/job-runbook.md","templates/docs/rollback-backfill-playbook.md"], ["templates/data/incidents.csv"]),
 "Security & Governance (Unity Catalog)": (["templates/docs/data-classification-matrix.md","templates/data/table_registry.csv"], ["templates/docs/uc-catalog-policy.md","templates/policies/uc_grants.sql","templates/policies/row_column_masking.sql"]),
 "Privacy & Compliance": (["templates/docs/pii-masking-design.md"], ["templates/policies/row_column_masking.sql"]),
 "FinOps Cost Optimizer": (["templates/data/cost_budgets.csv"], ["templates/docs/finops-budget-policy.md"]),
 "Observability & Reliability": (["templates/monitoring/lakehouse-monitoring.yaml"], ["templates/docs/observability-slo.md"]),
 "Release & Change Manager": (["templates/docs/ci-cd-guide.md"], ["templates/ci-cd/github-actions-databricks.yml"]),
 "DevEx & Platform Automation": (["templates/iac/terraform/workspace_objects.tf"], ["templates/ci-cd/databricks-cli-profile.example"]),
 "Quality Assurance (Data & Code Tests)": (["templates/code/notebooks/expectations_dq.py"], ["templates/data/audit_log.csv"]),
 "Support & Incident Manager": (["templates/data/incidents.csv","templates/monitoring/lakehouse-monitoring.yaml"], ["templates/docs/postmortem-report.md"]),
}

ROLE_TMPL = textwrap.dedent("""
---
role_id: "{role_id}"
role_name: "{role_name}"
aliases: {aliases}
version: "1.0.0"
status: "stable"
owner: "Databricks Platform Ops"
last_updated: "{today}"
bmad_tags: ["BMAD:Agent","DBX:Ops"]
inputs_contract: {inputs}
outputs_contract: {outputs}
depends_on: {depends}
handoff_to: {handoff}
---

## Persona（人格）
**价值观**：契约优先、口径一致、安全合规、可观测、可回滚；以自动化和成本意识驱动一切。  
**沟通风格**：要点化 + 模板化；明确输入/输出与验收标准（Acceptance）。

## Capabilities（可执行任务）
- 任务1：依据模板生成本角色核心文档/代码/数据，落盘并版本化。
- 任务2：维护关键变量（`${{ORG}}`/`${{DOMAIN}}`/`${{PROJECT}}`/`${{ENV}}`/`${{WORKSPACE}}`/`${{CATALOG}}`/`${{SCHEMA}}`/`${{TABLE}}`/`${{DLT_PIPELINE}}`/`${{JOB_ID}}`/`${{MODEL_NAME}}`/`${{VERSION}}`）。
- 任务3：对照 DoD 自检，异常走失败回路或升级（回填/回滚/变更冻结）。

### DoR（准备就绪）
- 上游信息齐全（契约/架构/权限/预算），命名与版本规范，UC 与工作区权限就绪。

### DoD（完成定义）
- 产物齐套（文档+代码+数据+清单）；DQ 全绿/安全合规通过；交接回执与审计留痕完整。

## Commandable Prompts（命令用法）
- `*agent {agent_key} → *create-doc {{template}}`
- `*agent {agent_key} → *status / *plan / *bundle`

> 命名：`DBX_{{ORG}}_{{DOMAIN}}_{{PROJECT}}_{{ENV}}_{{COMP}}_{{DOC}}_vX.Y_YYYYMMDD.ext`；CSV UTF-8，日期 ISO-8601。

## Templates（模板引用）
- 参考 `/templates/docs/*.md`、`/templates/code/*`、`/templates/iac/*`、`/templates/policies/*`、`/templates/monitoring/*` 与 `/templates/data/*.csv`。  
- 变量：`${{ORG}}`, `${{DOMAIN}}`, `${{PROJECT}}`, `${{ENV}}`, `${{WORKSPACE}}`, `${{CATALOG}}`, `${{SCHEMA}}`, `${{TABLE}}`, `${{DLT_PIPELINE}}`, `${{JOB_ID}}`, `${{MODEL_NAME}}`, `${{VERSION}}`.

## Workflow & Handoffs（编排与交接）
- 上游：{depends}
- 触发：上游 DoD 通过 + UC/预算/口径锁定。
- 下游：{handoff}
- 失败路径：契约/权限/成本冲突、DQ 异常 → 退回修复 → 再验证。

## Quality Gates（质量门）
- 命名/版本：语义化递增；破坏性变更需变更单与回执。
- Data Contract & DQ：期望与校验规则库（dq_rules.csv），失败升级路径。
- Delta/UC：审计列/OPTIMIZE/Z-ORDER/约束/时间旅行；UC 精细授权与遮罩。
- 安全与隐私：PII 分类、列/行级屏蔽、访问日志与审计。
- FinOps：集群策略、实例上限、空闲回收、任务标签、预算告警。
- 可观测：监控/告警/SLO；回填与重放标准操作。

## Examples（示例）
- 输入：见 `inputs_contract`。
- 输出：见 `outputs_contract`。
""").strip()

# 写入角色文件
for r in ROLES:
    body = ROLE_TMPL.format(
        role_id=r["id"],
        role_name=r["name"],
        aliases=json.dumps(r["aliases"], ensure_ascii=False),
        today=TODAY,
        inputs=json.dumps(IO.get(r["name"], ([],[]))[0], ensure_ascii=False),
        outputs=json.dumps(IO.get(r["name"], ([],[]))[1], ensure_ascii=False),
        depends=json.dumps(DEPENDS.get(r["name"], []), ensure_ascii=False),
        handoff=json.dumps(HANDOFF.get(r["name"], []), ensure_ascii=False),
        agent_key=r["name"].lower().replace(" ", "-").replace("/", "-").replace("&","and").replace("(","").replace(")","")
    )
    write(f"{BASE}/roles/{r['file']}", body + "\n")

# manifests
manifest = []
for r in ROLES:
    name = r["name"]
    manifest.append({
        "role_id": r["id"], "role_name": name, "aliases": r["aliases"],
        "file": f"roles/{r['file']}",
        "depends_on": DEPENDS.get(name, []),
        "handoff_to": HANDOFF.get(name, []),
        "inputs_contract": IO.get(name, ([], []))[0],
        "outputs_contract": IO.get(name, ([], []))[1],
    })
write(f"{BASE}/manifests/roles.manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

with open(f"{BASE}/manifests/roles.capability-matrix.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f); w.writerow(["Role","Capabilities"])
    CAP = {
        "Platform Owner":"Landing Zone;Policies;Runbook",
        "Lakehouse Architect":"Domain Modeling;Delta/UC;SLA/SLO",
        "Product Manager":"Use Cases;Roadmap;Backlog",
        "Business Analyst":"Requirements;Data Contract",
        "Data Contract Owner":"Contracts;DQ Rules",
        "Data Engineering Lead":"DLT/Jobs;ETL Standards",
        "Streaming Engineer":"Autoloader;Checkpointing;Exactly-once",
        "Analytics Engineer (BI/SQL)":"Gold Layer;Semantic Models;DBSQL",
        "ML Engineer (MLOps)":"Feature Store;MLflow;Serving",
        "DataOps / SRE":"Ops;Rollback;Backfill",
        "Security & Governance (Unity Catalog)":"Grants;Masking;Audit",
        "Privacy & Compliance":"PII;Retention;Legal",
        "FinOps Cost Optimizer":"Budgets;Cost Tags;Optimization",
        "Observability & Reliability":"Monitoring;Alerts;SLO",
        "Release & Change Manager":"CI/CD;Change Control",
        "DevEx & Platform Automation":"Terraform;CLI;Templates",
        "Quality Assurance (Data & Code Tests)":"DQ;Unit/Integration Tests",
        "Support & Incident Manager":"Incident;Postmortem",
    }
    for r in ROLES: w.writerow([r["name"], CAP.get(r["name"], "")])

# workflows
write(f"{BASE}/workflows/orchestration.md", """# Orchestration（编排操作手册）
Use Case → Contract → Lakehouse Arch → DLT/Jobs（Bronze→Silver→Gold）→ Feature/Model/Serving → Governance（UC/Privacy）→ CI/CD → Observability & FinOps → Ops/Backfill/Postmortem

## 常用命令（示例）
- `*agent business-analyst → *create-doc data-contract`
- `*agent lakehouse-architect → *create-doc lakehouse-architecture`
- `*agent data-engineering-lead → *create-doc dlt-design`
- `*agent analytics-engineer-bisql → *create-doc silver-to-gold-modeling`
- `*agent ml-engineer-mlops → *create-doc model-card`
- `*agent security-and-governance-unity-catalog → *create-doc uc-catalog-policy`
- `*agent release-and-change-manager → *create-doc ci-cd-guide`
""")

write(f"{BASE}/workflows/swimlane.mmd", """```mermaid
flowchart LR
  subgraph PF[Platform]
    LZ[Landing Zone]
    POL[Cluster Policy]
  end
  subgraph ARCH[Architect]
    ARCHDOC[Lakehouse Arch]
    DELTA[Delta Spec]
    UCP[UC Policy]
  end
  subgraph PM[PM/BA]
    UCD[Use Case]
    DCM[Data Contract]
  end
  subgraph ENG[Data Eng]
    DLT[DLT Pipeline]
    JOBS[Jobs]
  end
  subgraph AE[Analytics Eng]
    GOLD[Gold Semantic]
  end
  subgraph ML[ML Eng]
    FEAT[Feature Store]
    MSC[Model Card]
    SRV[Serving]
  end
  subgraph GOV[Governance]
    MASK[Masking/Grants]
  end
  subgraph OPS[Ops/SRE]
    MON[Monitoring]
    RBF[Rollback/Backfill]
    INC[Incidents]
  end
  subgraph FIN[FinOps]
    COST[Budgets]
  end
  subgraph REL[Release]
    CI[CI/CD]
  end

  UCD --> DCM --> ARCHDOC --> DELTA --> UCP --> DLT --> JOBS --> GOLD --> CI --> SRV
  GOLD --> MON
  SRV --> MON
  MON --> INC --> RBF
  COST --> CI
  UCP --- MASK
```""")

write(f"{BASE}/workflows/handoff-contracts.md", """# 交接契约（Handoff Contracts）

| From | To | Trigger | Input Files | Output Files | Acceptance |
|---|---|---|---|---|---|
| BA/Contract | Architect | Contract Locked | docs/data-contract.md | docs/delta-table-spec.md | 命名/口径一致 |
| Architect | Data Eng/Streaming | UC Policy Ready | docs/uc-catalog-policy.md | docs/dlt-design.md | DLT/Autoloader 跑通 |
| DE/AE | QA/Release | Gold DQ Passed | data/dq_rules.csv + 测试报告 | ci-cd/github-actions-databricks.yml | CI 通过 |
| ML | Serving/Obs | Model Staged | docs/model-card.md | docs/serving-config.md | 端点健康、SLO 告警 |
| FinOps/Obs | Platform | Monthly Bill | data/kpi.csv + data/cost_budgets.csv | 优化建议 | 成本回归目标 |
""")

# ---------- 3) templates/docs ----------
DOCS = {
 "lakehouse-architecture.md": "# Lakehouse Architecture（架构）\n- 域模型/表层级/权限/成本/可观测\n",
 "domain-data-map.md": "# Domain Data Map（域与数据地图）\n- 业务域→实体→指标\n",
 "data-contract.md": "# Data Contract（数据契约）\n- Schema/约束/SLA/SLO/隐私/变更\n",
 "delta-table-spec.md": "# Delta Table Spec（表规范）\n- 分区/约束/审计列/OPTIMIZE/ZORDER\n",
 "uc-catalog-policy.md": "# UC Catalog Policy（治理策略）\n- Catalog/Schema/Object/Grants\n",
 "data-classification-matrix.md": "# Data Classification（数据分级）\n- 公共/内部/机密/敏感\n",
 "pii-masking-design.md": "# PII Masking Design（隐私遮罩）\n- 列/行级/动态视图\n",
 "dlt-design.md": "# DLT Design（Delta Live Tables）\n- 依赖图/期望/检查点\n",
 "job-runbook.md": "# Job Runbook（运行手册）\n- 调度/重试/失败处置\n",
 "batch-pipeline-design.md": "# Batch Pipeline Design（批处理）\n- 源/变换/加载/回填\n",
 "streaming-autoloader-design.md": "# Streaming Autoloader（流式摄取）\n- 模式/幂等/窗口\n",
 "silver-to-gold-modeling.md": "# Silver→Gold Modeling（建模）\n- 维度/事实/度量/语义层\n",
 "feature-store-spec.md": "# Feature Store Spec（特征仓库）\n- 实体/特征/新鲜度/一致性\n",
 "ml-experiment-plan.md": "# ML Experiment Plan（实验计划）\n- 指标/分桶/回滚\n",
 "model-card.md": "# Model Card（模型卡）\n- 训练/指标/偏差/监控\n",
 "serving-config.md": "# Serving Config（服务配置）\n- 端点/资源/SLA\n",
 "ci-cd-guide.md": "# CI/CD Guide（发布指南）\n- 分支/流水线/审批/回滚\n",
 "tf-landing-zone-guide.md": "# Terraform Landing Zone（落地指南）\n- Provider/资源/策略\n",
 "cluster-policy.md": "# Cluster Policy（集群策略）\n- 实例/自动停止/标签\n",
 "finops-budget-policy.md": "# FinOps Budget Policy（成本策略）\n- 预算/上限/告警/优化\n",
 "observability-slo.md": "# Observability & SLO（可观测/SLO）\n- 指标/阈值/告警/值班\n",
 "rollback-backfill-playbook.md": "# Rollback & Backfill（回滚与回填）\n- 场景/脚本/验证\n",
 "kpi-dictionary.md": "# KPI Dictionary（指标）\n- 延迟/可用性/成本/质量\n",
 "risk-register.md": "# Risk Register（风险台账）\n| 风险 | 影响 | 概率 | 对策 | 负责人 |\n|---|---|---|---|---|\n",
 "postmortem-report.md": "# Postmortem（复盘）\n- 事故/根因/改进/跟踪\n",
 "runbook.md": "# Runbook（运行手册）\n- 值守/升级/回滚/审计\n",
}
for fn, content in DOCS.items():
    write(f"{BASE}/templates/docs/{fn}", content)

# ---------- 4) templates/code ----------
NOTEBOOKS = {
 "notebooks/ingestion_notebook.py": """# Databricks notebook source
from pyspark.sql import functions as F
def ingest(src_path, table_fullname):
    df = spark.read.format("json").load(src_path)
    df = df.withColumn("_ingest_time", F.current_timestamp())
    df.write.format("delta").mode("append").saveAsTable(table_fullname)
    return df.count()
""",
 "notebooks/silver_transform.sql": """-- Databricks SQL
CREATE OR REPLACE TABLE ${catalog}.${schema}.silver_sales AS
SELECT CAST(order_id AS STRING) AS order_id,
       customer_id,
       amount::DOUBLE AS amount,
       to_date(order_ts) AS order_date,
       current_timestamp() AS _etl_ts
FROM ${catalog}.${schema}.bronze_sales
WHERE amount IS NOT NULL;""",
 "notebooks/gold_mart.sql": """-- Databricks SQL
CREATE OR REPLACE TABLE ${catalog}.${schema}.gold_sales_daily AS
SELECT order_date, SUM(amount) AS revenue
FROM ${catalog}.${schema}.silver_sales
GROUP BY order_date;""",
 "notebooks/streaming_autoloader.py": """from pyspark.sql import functions as F
df = (spark.readStream.format("cloudFiles")
      .option("cloudFiles.format","json")
      .option("cloudFiles.inferColumnTypes","true")
      .load("${src_path}"))
df = df.withColumn("_ingest_time", F.current_timestamp())
(df.writeStream
    .format("delta")
    .option("checkpointLocation","${checkpoint}")
    .trigger(availableNow=True)
    .toTable("${catalog}.${schema}.bronze_stream"))
""",
 "notebooks/expectations_dq.py": """from pyspark.sql import functions as F
rules = [("not_null_order_id","order_id IS NOT NULL"),("amount_positive","amount > 0")]
df = spark.table("${catalog}.${schema}.silver_sales")
violations = [(name, df.filter(f"NOT ({expr})").count()) for name, expr in rules]
print(violations)
"""
}
for rel, content in NOTEBOOKS.items():
    write(f"{BASE}/templates/code/{rel}", content)

DLT = {
 "dlt/pipeline.py": '''import dlt
from pyspark.sql.functions import current_timestamp
@dlt.table
def bronze_sales():
    return (spark.read.format("json").load("${src_path}")
            .withColumn("_ingest_time", current_timestamp()))
@dlt.table
def silver_sales():
    return dlt.read("bronze_sales").withColumn("_etl_ts", current_timestamp())
''',
 "ml/experiment_notebook.py": """# Databricks notebook for ML experiment
import mlflow, uuid
mlflow.set_experiment("/Shared/${project}/exp")
with mlflow.start_run(run_name=f"exp-{uuid.uuid4().hex[:6]}"):
    mlflow.log_param("model","baseline"); mlflow.log_metric("accuracy", 0.9)
""",
 "ml/feature_engineering.py": """# Feature Store placeholder
# from databricks.feature_store import FeatureStoreClient
# fs = FeatureStoreClient()
""",
 "ml/serving_example.py": """def predict(request_json):
    return {"ok": True, "input": request_json}
"""
}
for rel, content in DLT.items():
    write(f"{BASE}/templates/code/{rel}", content)

# ---------- 5) IaC / CI-CD / policies / monitoring ----------
IAC = {
 "terraform/providers.tf": """terraform { required_providers { databricks = { source = "databricks/databricks" } } }
provider "databricks" { host = var.databricks_host  token = var.databricks_token }""",
 "terraform/workspace_objects.tf": """resource "databricks_repo" "this" { url = var.repo_url  path = "/Repos/${var.owner}/project" }""",
 "terraform/uc_catalogs.tf": """resource "databricks_catalog" "domain" { name = var.catalog  comment = "Domain catalog" }""",
 "terraform/cluster_policies.tf": """resource "databricks_cluster_policy" "std" { name = "std-policy"  definition = file("${path.module}/policy.json") }""",
}
for rel, content in IAC.items():
    write(f"{BASE}/templates/iac/{rel}", content)

CICD = {
 "github-actions-databricks.yml": """name: dbx-ci
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Lint
      run: echo "lint"
    - name: Deploy Notebooks
      run: |
        databricks repos update --path "/Repos/${OWNER}/project" --branch $GITHUB_REF_NAME
    - name: Run Tests
      run: echo "dq tests"
""",
 "databricks-cli-profile.example": """[DEFAULT]
host = https://<your-workspace>.cloud.databricks.com
token = dapiXXXXXXXXXXXXXXXX
"""
}
for rel, content in CICD.items():
    write(f"{BASE}/templates/ci-cd/{rel}", content)

POL = {
 "cluster_policy.json": json.dumps({
     "spark_version": {"type":"fixed","value":"13.3.x-scala2.12"},
     "num_workers": {"type":"range","minValue":1,"maxValue":10},
     "autoscale": {"type":"checkbox","value":True}
 }, indent=2),
 "uc_grants.sql": """-- Example UC grants
GRANT USAGE ON CATALOG ${catalog} TO `data_scientists`;
GRANT SELECT ON SCHEMA ${catalog}.${schema} TO `analysts`;""",
 "row_column_masking.sql": """-- Row/Column level masking example
CREATE OR REPLACE VIEW ${catalog}.${schema}.masked_customers AS
SELECT *, CASE WHEN is_member('pii_viewers') THEN email ELSE '***' END AS email_masked
FROM ${catalog}.${schema}.customers;"""
}
for rel, content in POL.items():
    write(f"{BASE}/templates/policies/{rel}", content)

MON = {
 "lakehouse-monitoring.yaml": """slo:
  - name: pipeline_latency
    objective: 99.0
    alert: "> 30m latency in last 1h"
  - name: serving_uptime
    objective: 99.5
    alert: "uptime < 99.5% daily"
""",
 "sql-alerts.md": "# SQL Alerts\n- 数据延迟/空表/错误率\n"
}
for rel, content in MON.items():
    write(f"{BASE}/templates/monitoring/{rel}", content)

# ---------- 6) templates/data (CSVs) ----------
DATA = {
 "data_contracts.csv": ["contract_id","domain","table","owner","sla_ms","pii_level","status","version"],
 "table_registry.csv": ["catalog","schema","table","owner","quality_tier","created_ts"],
 "lineage_owner_map.csv": ["upstream","downstream","owner","criticality"],
 "dq_rules.csv": ["table","column","rule_name","rule_expr","severity","owner"],
 "cost_budgets.csv": ["env","owner","budget_usd","month","status"],
 "jobs_schedule.csv": ["job_id","name","cron","owner","enabled"],
 "models_registry.csv": ["model_name","version","stage","owner","auc","f1"],
 "incidents.csv": ["incident_id","sev","start_ts","end_ts","owner","root_cause","status"],
 "audit_log.csv": ["ts","actor","action","resource","result"],
 "kpi.csv": ["metric","period_start","period_end","value","unit"],
}
for fn, headers in DATA.items():
    write_csv(f"{BASE}/templates/data/{fn}", headers)

# ---------- 7) checklists ----------
CHECKS = {
 "dor-dod.md": "# DoR / DoD（按阶段）\n- 合同：口径/SLA/SLO/隐私；DoD：data-contract 发布并获签\n- 架构：表/流/特征/权限；DoD：delta-spec + uc-policy 发布\n- 实现：DLT/Jobs 可复现；DoD：dlt-design + 集成测试通过\n- Gold：语义层与 DQ；DoD：DQ 报告全绿\n- ML/Serving：模型卡/监控；DoD：serving-config 生效\n- 发布/运营：CI/CD + 监控；DoD：actions 成功 + monitoring 生效\n",
 "naming-versioning.md": "# 命名与版本\n- `DBX_${ORG}_${DOMAIN}_${PROJECT}_${ENV}_${COMP}_${DOC}_vX.Y_YYYYMMDD`\n- 版本语义化递增；破坏性变更需变更单与回执\n",
 "data-contract-dq.md": "# 数据契约与质量\n- 契约字段/约束/期望；规则库 dq_rules.csv；失败升级\n",
 "delta-uc-bestpractices.md": "# Delta/UC 最佳实践\n- 审计列/OPTIMIZE/ZORDER/软删除/时间旅行；UC 精细授权\n",
 "security-privacy.md": "# 安全与隐私\n- PII 分级/列行级遮罩/访问日志/密钥\n",
 "finops-guardrails.md": "# FinOps 守护栏\n- 策略/规模上限/空闲回收/预算告警/成本标签\n",
 "observability-alerts.md": "# 可观测与告警\n- 指标/SLO/阈值/轮值；报警到事件\n",
 "release-change-control.md": "# 发布与变更控制\n- PR→Review→CI→Deploy→验证→回滚/回填→归档\n",
 "backfill-reprocessing.md": "# 回填与重放\n- 触发/脚本/核对/告警抑制/窗口\n",
 "anti-patterns.md": "# 反模式与对策\n- 绕过契约直接写表 → 禁止发布\n- Gold 与报表口径漂移 → 语义层门禁\n- 长跑作业无检查点 → 强制 checkpoint/水印\n- 开发与生产混用 → 强制工作区隔离\n- 无成本标签/策略 → FinOps 失败门\n- 无告警/无回滚 → SRE 拒绝上线\n",
}
for fn, content in CHECKS.items():
    write(f"{BASE}/checklists/{fn}", content)

# ---------- 8) delivery ----------
DELIVERY = {
 "bundle-rules.md": "# 打包与归档规则\n- 关键节点（Contract/Arch/DLT/Gold/Serving/Release）执行 *bundle：生成清单、校验哈希、版本快照\n- 文档/代码/数据分仓；审计日志同行\n",
 "merge-docs.md": "# 文档合并\n- 多版本保留 vX.Y 轨迹与差异说明\n- 输出 merge-report\n",
 "merge-data.md": "# 数据合并与对账（CSV/Delta）\n- 主键：catalog/schema/table + 日期窗口\n- 统一日期/数值/口径格式，生成校验报告\n",
}
for fn, content in DELIVERY.items():
    write(f"{BASE}/delivery/{fn}", content)

# ---------- 9) README ----------
write(f"{BASE}/README.md", "# BMAD-Method｜基于 Databricks 的系统开发（Lakehouse）RolePack\n- 18 角色：人格/任务/模板/编排/DoR/DoD\n- manifests：角色清单/能力矩阵/工作流索引\n- workflows：编排手册/泳道图/交接契约\n- templates：架构/契约/DLT/Jobs/BI/ML/UC/CI-CD/监控/FinOps 模板 + 代码 + CSV\n- checklists：质量门/Delta-UC/安全隐私/FinOps/可观测/变更/反模式\n- delivery：打包与合并规则\n")

# ---------- 10) ZIP ----------
ZIP_PATH = os.path.abspath("./bmad-databricks-rolepack_v1.0.zip")
with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(BASE):
        for file in files:
            full = os.path.join(root, file)
            z.write(full, os.path.relpath(full, os.path.dirname(BASE)))

print(f"✅ Generated: {ZIP_PATH}")
