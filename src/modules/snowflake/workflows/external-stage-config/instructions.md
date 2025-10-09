# external-stage-config - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/external-stage-config/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this external stage config (s3/gcs/azure)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="存储位置与命名（分区/层级）">
<action>Work on 存储位置与命名（分区/层级）</action>
<template-output section="locations"/>
</step>

<step n="3" goal="凭证/密钥/网络策略（私连/策略）">
<action>Work on 凭证/密钥/网络策略（私连/策略）</action>
<template-output section="credentials"/>
</step>

<step n="4" goal="保留/生命周期与清理">
<action>Work on 保留/生命周期与清理</action>
<template-output section="retention"/>
</step>

<step n="5" goal="加密/最小权限/审计">
<action>Work on 加密/最小权限/审计</action>
<template-output section="security"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
