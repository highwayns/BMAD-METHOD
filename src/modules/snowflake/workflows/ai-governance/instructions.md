# ai-governance - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/ai-governance/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this ai governance (features/models/prompts)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="训练/评估数据合法性与偏差">
<action>Work on 训练/评估数据合法性与偏差</action>
<template-output section="dataset"/>
</step>

<step n="3" goal="特征/敏感属性与用途限定">
<action>Work on 特征/敏感属性与用途限定</action>
<template-output section="features"/>
</step>

<step n="4" goal="推理/日志/保留/删除">
<action>Work on 推理/日志/保留/删除</action>
<template-output section="serving"/>
</step>

<step n="5" goal="模型卡/风险/签字与发布">
<action>Work on 模型卡/风险/签字与发布</action>
<template-output section="risks"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
