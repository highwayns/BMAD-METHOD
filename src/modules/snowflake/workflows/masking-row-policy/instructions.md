# masking-row-policy - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/masking-row-policy/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this masking & row access policies</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="掩码模式与上下文化规则">
<action>Work on 掩码模式与上下文化规则</action>
<template-output section="masking"/>
</step>

<step n="3" goal="行策略（地域/租户/目的）">
<action>Work on 行策略（地域/租户/目的）</action>
<template-output section="row_policy"/>
</step>

<step n="4" goal="性能/缓存与例外">
<action>Work on 性能/缓存与例外</action>
<template-output section="performance"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
