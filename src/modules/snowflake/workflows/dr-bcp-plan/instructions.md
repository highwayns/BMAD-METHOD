# dr-bcp-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dr-bcp-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dr & bcp plan (failover/exercises)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="复制/故障切换拓扑（数据库/Failover Group）">
<action>Work on 复制/故障切换拓扑（数据库/failover group）</action>
<template-output section="topology"/>
</step>

<step n="3" goal="RTO/RPO 目标与演练">
<action>Work on rto/rpo 目标与演练</action>
<template-output section="rto_rpo"/>
</step>

<step n="4" goal="演练脚本与回退">
<action>Work on 演练脚本与回退</action>
<template-output section="playbooks"/>
</step>

<step n="5" goal="通知与状态页">
<action>Work on 通知与状态页</action>
<template-output section="comms"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
