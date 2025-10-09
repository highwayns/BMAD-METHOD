# network-policies - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/network-policies/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this network policies (allowlist/privatelink/proxy)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="IP/区域/代理与会话策略">
<action>Work on ip/区域/代理与会话策略</action>
<template-output section="policies"/>
</step>

<step n="3" goal="PrivateLink/私连与数据出境">
<action>Work on privatelink/私连与数据出境</action>
<template-output section="privatelink"/>
</step>

<step n="4" goal="姿态评估与例外">
<action>Work on 姿态评估与例外</action>
<template-output section="posture"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
