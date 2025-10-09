# ml-release - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/ml-release/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this ml release (registry/serving/monitoring)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="模型注册/签字">
<action>Work on 模型注册/签字</action>
<template-output section="registry"/>
</step>

<step n="3" goal="部署/回退与灰度">
<action>Work on 部署/回退与灰度</action>
<template-output section="serving"/>
</step>

<step n="4" goal="漂移/告警/再训练接口">
<action>Work on 漂移/告警/再训练接口</action>
<template-output section="monitoring"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
