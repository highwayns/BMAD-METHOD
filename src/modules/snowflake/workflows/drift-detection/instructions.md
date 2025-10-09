# drift-detection - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/drift-detection/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this drift detection & remediation</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="对象/权限/策略/标签/预算">
<action>Work on 对象/权限/策略/标签/预算</action>
<template-output section="scope"/>
</step>

<step n="3" goal="信号（差异比对/违规变更）">
<action>Work on 信号（差异比对/违规变更）</action>
<template-output section="signals"/>
</step>

<step n="4" goal="自动修复/例外/归档">
<action>Work on 自动修复/例外/归档</action>
<template-output section="actions"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
