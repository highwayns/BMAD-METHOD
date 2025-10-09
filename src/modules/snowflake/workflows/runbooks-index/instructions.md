# runbooks-index - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/runbooks-index/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this runbooks index (snowflake domains)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="域：仓库/查询/Tasks/DT/Snowpipe/Streaming/RBAC/复制/预算/数据">
<action>Work on 域：仓库/查询/tasks/dt/snowpipe/streaming/rbac/复制/预算/数据</action>
<template-output section="list"/>
</step>

<step n="3" goal="演练频率/负责人">
<action>Work on 演练频率/负责人</action>
<template-output section="drills"/>
</step>

<step n="4" goal="更新与审计">
<action>Work on 更新与审计</action>
<template-output section="updates"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
