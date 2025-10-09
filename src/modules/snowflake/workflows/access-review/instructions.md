# access-review - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/access-review/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this periodic access review & re-certification</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="范围（角色/对象/策略/外部共享）">
<action>Work on 范围（角色/对象/策略/外部共享）</action>
<template-output section="scope"/>
</step>

<step n="3" goal="流程（提取→分发→签字→整改）">
<action>Work on 流程（提取→分发→签字→整改）</action>
<template-output section="workflow"/>
</step>

<step n="4" goal="自动化报表与触发">
<action>Work on 自动化报表与触发</action>
<template-output section="automation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
