# scaffolding - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/scaffolding/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this scaffolding/starters (dbt/snowpark/streaming/bi)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="技术栈（dbt/Snowpark/Streaming/BI）">
<action>Work on 技术栈（dbt/snowpark/streaming/bi）</action>
<template-output section="stacks"/>
</step>

<step n="3" goal="代码生成器与参数">
<action>Work on 代码生成器与参数</action>
<template-output section="generators"/>
</step>

<step n="4" goal="示例与端到端验证">
<action>Work on 示例与端到端验证</action>
<template-output section="samples"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
