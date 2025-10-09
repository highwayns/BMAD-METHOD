# abac-tags-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/abac-tags-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this abac with tags (classification/cost/domain)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="标签分类法（机密性/合规/成本/域）">
<action>Work on 标签分类法（机密性/合规/成本/域）</action>
<template-output section="taxonomy"/>
</step>

<step n="3" goal="标签绑定策略（对象/列/行/角色）">
<action>Work on 标签绑定策略（对象/列/行/角色）</action>
<template-output section="bindings"/>
</step>

<step n="4" goal="自动化与漂移检测">
<action>Work on 自动化与漂移检测</action>
<template-output section="automation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
