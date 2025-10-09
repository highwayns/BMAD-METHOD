# evaluation-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/evaluation-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this evaluation plan (metrics/thresholds)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="指标（分类/回归/排序/生成）">
<action>Work on 指标（分类/回归/排序/生成）</action>
<template-output section="metrics"/>
</step>

<step n="3" goal="阈值与业务容忍区">
<action>Work on 阈值与业务容忍区</action>
<template-output section="thresholds"/>
</step>

<step n="4" goal="泄漏/数据穿越/偏置检查">
<action>Work on 泄漏/数据穿越/偏置检查</action>
<template-output section="leakage"/>
</step>

<step n="5" goal="A/B 或离线→在线一致性验证">
<action>Work on a/b 或离线→在线一致性验证</action>
<template-output section="abtest"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
