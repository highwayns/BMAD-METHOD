# file-format-config - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/file-format-config/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this file format config (json/csv/parquet/avro)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="格式参数与示例（压缩/编码）">
<action>Work on 格式参数与示例（压缩/编码）</action>
<template-output section="formats"/>
</step>

<step n="3" goal="Schema 推断与变更">
<action>Work on schema 推断与变更</action>
<template-output section="schema_inference"/>
</step>

<step n="4" goal="错误处理与容错（ON_ERROR等）">
<action>Work on 错误处理与容错（on_error等）</action>
<template-output section="errors"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
