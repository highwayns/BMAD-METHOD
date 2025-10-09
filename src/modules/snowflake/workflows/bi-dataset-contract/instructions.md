# bi-dataset-contract - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/bi-dataset-contract/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this bi dataset contract (schema/slo/access)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Schema/字段约束/字典">
<action>Work on schema/字段约束/字典</action>
<template-output section="schema"/>
</step>

<step n="3" goal="SLI/SLO（延迟/正确性/可用性）">
<action>Work on sli/slo（延迟/正确性/可用性）</action>
<template-output section="slislos"/>
</step>

<step n="4" goal="权限/屏蔽/行列策略">
<action>Work on 权限/屏蔽/行列策略</action>
<template-output section="access"/>
</step>

<step n="5" goal="版本/兼容/弃用计划">
<action>Work on 版本/兼容/弃用计划</action>
<template-output section="change"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
