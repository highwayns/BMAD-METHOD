# sos-acceleration - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/sos-acceleration/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this search optimization service (sos) acceleration</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="候选表/列与过滤模式">
<action>Work on 候选表/列与过滤模式</action>
<template-output section="candidates"/>
</step>

<step n="3" goal="维护策略与成本权衡">
<action>Work on 维护策略与成本权衡</action>
<template-output section="policies"/>
</step>

<step n="4" goal="效果评估（命中率/延迟）">
<action>Work on 效果评估（命中率/延迟）</action>
<template-output section="validation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
