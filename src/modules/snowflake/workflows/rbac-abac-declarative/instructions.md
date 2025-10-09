# rbac-abac-declarative - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/rbac-abac-declarative/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this declarative rbac/abac</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="角色/标签分类法">
<action>Work on 角色/标签分类法</action>
<template-output section="taxonomy"/>
</step>

<step n="3" goal="授权矩阵与最小权限">
<action>Work on 授权矩阵与最小权限</action>
<template-output section="grants"/>
</step>

<step n="4" goal="GitOps 应用/回滚与验证">
<action>Work on gitops 应用/回滚与验证</action>
<template-output section="pipelines"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
