# observability-slo - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/observability-slo/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this observability & slo (query/cost/latency/error)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="KPI/SLI（查询延迟/失败率/credits）">
<action>Work on kpi/sli（查询延迟/失败率/credits）</action>
<template-output section="kpis"/>
</step>

<step n="3" goal="仪表盘（Account Usage/Information Schema）">
<action>Work on 仪表盘（account usage/information schema）</action>
<template-output section="dashboards"/>
</step>

<step n="4" goal="告警与升级路径">
<action>Work on 告警与升级路径</action>
<template-output section="alerts"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
