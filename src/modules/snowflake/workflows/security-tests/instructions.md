# security-tests - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/security-tests/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this security tests (rbac/masking/row policy)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="角色与最小权限">
<action>Work on 角色与最小权限</action>
<template-output section="rbac"/>
</step>

<step n="3" goal="列掩码有效性">
<action>Work on 列掩码有效性</action>
<template-output section="masking"/>
</step>

<step n="4" goal="行访问策略（地域/租户/目的）">
<action>Work on 行访问策略（地域/租户/目的）</action>
<template-output section="row"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
