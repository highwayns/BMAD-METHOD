# access-audit-analytics - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/access-audit-analytics/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this access & audit analytics (access history/policy)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Access History 模式/异常">
<action>Work on access history 模式/异常</action>
<template-output section="access"/>
</step>

<step n="3" goal="角色/策略变更与影响">
<action>Work on 角色/策略变更与影响</action>
<template-output section="rbac"/>
</step>

<step n="4" goal="证据与合规报表">
<action>Work on 证据与合规报表</action>
<template-output section="evidence"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
