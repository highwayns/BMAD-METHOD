# secrets-keys - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/secrets-keys/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this secrets/keys (scopes/kms/rotation)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="KMS/Client-side/Server-side">
<action>Work on kms/client-side/server-side</action>
<template-output section="kms"/>
</step>

<step n="3" goal="轮换/过期/证据">
<action>Work on 轮换/过期/证据</action>
<template-output section="rotation"/>
</step>

<step n="4" goal="作用域与最小权限">
<action>Work on 作用域与最小权限</action>
<template-output section="scope"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
