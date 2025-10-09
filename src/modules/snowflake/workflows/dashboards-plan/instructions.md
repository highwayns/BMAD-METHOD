# dashboards-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dashboards-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dashboards plan (capacity/latency/errors/freshness/cost)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="布局与导航（总览→容量→性能→作业→质量→安全→成本）">
<action>Work on 布局与导航（总览→容量→性能→作业→质量→安全→成本）</action>
<template-output section="layout"/>
</step>

<step n="3" goal="数据源（Account Usage/Information Schema/自定义表）">
<action>Work on 数据源（account usage/information schema/自定义表）</action>
<template-output section="sources"/>
</step>

<step n="4" goal="KPI 与阈值/颜色/解释">
<action>Work on kpi 与阈值/颜色/解释</action>
<template-output section="kpis"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
