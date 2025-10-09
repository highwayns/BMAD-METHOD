# snowpipe-cost - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/snowpipe-cost/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this snowpipe/snowpipe streaming cost plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="文件大小/批量/触发频率">
<action>Work on 文件大小/批量/触发频率</action>
<template-output section="pattern"/>
</step>

<step n="3" goal="连接器/并发/重试成本">
<action>Work on 连接器/并发/重试成本</action>
<template-output section="streaming"/>
</step>

<step n="4" goal="告警与限流">
<action>Work on 告警与限流</action>
<template-output section="alerts"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
