# docsite-generation - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/docsite-generation/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this docsite generation (dbt docs/glossary)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="指标/维度词汇表">
<action>Work on 指标/维度词汇表</action>
<template-output section="glossary"/>
</step>

<step n="3" goal="模型血缘与可视化">
<action>Work on 模型血缘与可视化</action>
<template-output section="lineage"/>
</step>

<step n="4" goal="发布与访问控制">
<action>Work on 发布与访问控制</action>
<template-output section="publishing"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
