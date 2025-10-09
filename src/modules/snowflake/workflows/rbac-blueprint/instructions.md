# rbac-blueprint - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/rbac-blueprint/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this rbac architecture and role design</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="角色分层（平台/域/产品/临时）">
<action>Work on 角色分层（平台/域/产品/临时）</action>
<template-output section="hierarchy"/>
</step>

<step n="3" goal="授权矩阵（USAGE/OWNERSHIP/OPERATE 等）">
<action>Work on 授权矩阵（usage/ownership/operate 等）</action>
<template-output section="grants"/>
</step>

<step n="4" goal="申请/审批/撤销/过期策略（JIT/TTL）">
<action>Work on 申请/审批/撤销/过期策略（jit/ttl）</action>
<template-output section="procedures"/>
</step>

<step n="5" goal="服务角色与密钥范围">
<action>Work on 服务角色与密钥范围</action>
<template-output section="service_roles"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete undefined output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
