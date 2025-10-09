# security-policy-change - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/security-policy-change/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this security policy change (rbac/tags/mask/row)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="范围/影响/依赖">
<action>Work on 范围/影响/依赖</action>
<template-output section="scope"/>
</step>

<step n="3" goal="回归/影子测试">
<action>Work on 回归/影子测试</action>
<template-output section="tests"/>
</step>

<step n="4" goal="审计与证据">
<action>Work on 审计与证据</action>
<template-output section="evidence"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
