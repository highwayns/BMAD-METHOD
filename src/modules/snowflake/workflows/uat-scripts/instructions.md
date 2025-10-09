# uat-scripts - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/uat-scripts/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this uat test scripts (ba-led uat)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="场景脚本（Given-When-Then）">
<action>Work on 场景脚本（given-when-then）</action>
<template-output section="scenarios"/>
</step>

<step n="3" goal="测试数据与期望输出">
<action>Work on 测试数据与期望输出</action>
<template-output section="data"/>
</step>

<step n="4" goal="验收与签字">
<action>Work on 验收与签字</action>
<template-output section="signoff"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
