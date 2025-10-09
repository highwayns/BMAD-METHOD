# monitoring-drift - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/monitoring-drift/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this monitoring & drift detection</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="监控指标（数据分布/KS/PSI/延迟/失败）">
<action>Work on 监控指标（数据分布/ks/psi/延迟/失败）</action>
<template-output section="metrics"/>
</step>

<step n="3" goal="仪表盘（Account Usage/Information Schema/自定义表）">
<action>Work on 仪表盘（account usage/information schema/自定义表）</action>
<template-output section="dashboards"/>
</step>

<step n="4" goal="告警阈值/路由/升级路径">
<action>Work on 告警阈值/路由/升级路径</action>
<template-output section="alerts"/>
</step>

<step n="5" goal="再训练触发/审批流程">
<action>Work on 再训练触发/审批流程</action>
<template-output section="triggers"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
