# showback-chargeback - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/showback-chargeback/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this showback/chargeback operating model</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="分摊模型（仓库/项目/域）">
<action>Work on 分摊模型（仓库/项目/域）</action>
<template-output section="model"/>
</step>

<step n="3" goal="周期/对账/争议处理">
<action>Work on 周期/对账/争议处理</action>
<template-output section="workflows"/>
</step>

<step n="4" goal="签字与归档">
<action>Work on 签字与归档</action>
<template-output section="signoff"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
