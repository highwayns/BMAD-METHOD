# replication-failover - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/replication-failover/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this replication & failover/failback</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="覆盖范围（数据库/账户/对象）">
<action>Work on 覆盖范围（数据库/账户/对象）</action>
<template-output section="scope"/>
</step>

<step n="3" goal="复制延迟与监控">
<action>Work on 复制延迟与监控</action>
<template-output section="lag"/>
</step>

<step n="4" goal="切换演练/验证/回退">
<action>Work on 切换演练/验证/回退</action>
<template-output section="exercises"/>
</step>

<step n="5" goal="权限/密钥/审计">
<action>Work on 权限/密钥/审计</action>
<template-output section="access"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
