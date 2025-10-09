# task-scheduler-ops - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/task-scheduler-ops/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this task scheduler operations (cron/dependencies)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Streams/Tasks/Dynamic Tables 拓扑">
<action>Work on streams/tasks/dynamic tables 拓扑</action>
<template-output section="topology"/>
</step>

<step n="3" goal="SLA/重试/死信/补偿">
<action>Work on sla/重试/死信/补偿</action>
<template-output section="sla"/>
</step>

<step n="4" goal="任务历史与失败分析">
<action>Work on 任务历史与失败分析</action>
<template-output section="history"/>
</step>

<step n="5" goal="回退与重算">
<action>Work on 回退与重算</action>
<template-output section="rollback"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
