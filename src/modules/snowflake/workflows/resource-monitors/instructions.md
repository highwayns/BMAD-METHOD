# resource-monitors - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/resource-monitors/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this resource monitors & guardrails</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="信用配额/阈值/动作">
<action>Work on 信用配额/阈值/动作</action>
<template-output section="monitors"/>
</step>

<step n="3" goal="告警路由/静默策略">
<action>Work on 告警路由/静默策略</action>
<template-output section="routing"/>
</step>

<step n="4" goal="演练与证据">
<action>Work on 演练与证据</action>
<template-output section="evidence"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
