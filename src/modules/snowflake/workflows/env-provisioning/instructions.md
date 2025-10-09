# env-provisioning - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/env-provisioning/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this env provisioning (sandbox/preview/staging/prod)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="拓扑（账号/区域/云）">
<action>Work on 拓扑（账号/区域/云）</action>
<template-output section="topologies"/>
</step>

<step n="3" goal="IaC 蓝图（DB/Schema/Warehouse/Policy）">
<action>Work on iac 蓝图（db/schema/warehouse/policy）</action>
<template-output section="blueprints"/>
</step>

<step n="4" goal="推进策略（数据/对象/权限）">
<action>Work on 推进策略（数据/对象/权限）</action>
<template-output section="promotion"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
