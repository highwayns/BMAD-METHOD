# training-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/training-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this training plan (snowpark/compute/artifacts)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="环境/依赖/镜像与资源">
<action>Work on 环境/依赖/镜像与资源</action>
<template-output section="env"/>
</step>

<step n="3" goal="数据→特征→训练→评估流水线">
<action>Work on 数据→特征→训练→评估流水线</action>
<template-output section="pipeline"/>
</step>

<step n="4" goal="产物（模型/指标/日志）">
<action>Work on 产物（模型/指标/日志）</action>
<template-output section="artifacts"/>
</step>

<step n="5" goal="审批/合规/配额">
<action>Work on 审批/合规/配额</action>
<template-output section="governance"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
