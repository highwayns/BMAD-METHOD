# row-access-policies - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/row-access-policies/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this row access policies (purpose/region/tenancy)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="谓词设计与性能">
<action>Work on 谓词设计与性能</action>
<template-output section="predicates"/>
</step>

<step n="3" goal="多租隔离（租户/区域/部门）">
<action>Work on 多租隔离（租户/区域/部门）</action>
<template-output section="tenancy"/>
</step>

<step n="4" goal="用途限定与数据契约挂钩">
<action>Work on 用途限定与数据契约挂钩</action>
<template-output section="purpose"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
