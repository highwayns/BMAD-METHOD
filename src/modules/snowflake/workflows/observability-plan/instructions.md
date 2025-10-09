# observability-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/observability-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this observability & alerting plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="数据源（Account Usage/Information Schema/自定义指标）">
<action>Work on 数据源（account usage/information schema/自定义指标）</action>
<template-output section="sources"/>
</step>

<step n="3" goal="仪表盘（容量/性能/成本/安全）">
<action>Work on 仪表盘（容量/性能/成本/安全）</action>
<template-output section="dashboards"/>
</step>

<step n="4" goal="告警阈值/路由/演练">
<action>Work on 告警阈值/路由/演练</action>
<template-output section="alerts"/>
</step>

<step n="5" goal="值班/排班与交接">
<action>Work on 值班/排班与交接</action>
<template-output section="oncall"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
