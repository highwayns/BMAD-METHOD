# freeze-window - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/freeze-window/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this freeze window (major events/blackouts)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="关键事件与窗口">
<action>Work on 关键事件与窗口</action>
<template-output section="events"/>
</step>

<step n="3" goal="例外审批/紧急变更">
<action>Work on 例外审批/紧急变更</action>
<template-output section="policy"/>
</step>

<step n="4" goal="回退与恢复计划">
<action>Work on 回退与恢复计划</action>
<template-output section="rollback"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
