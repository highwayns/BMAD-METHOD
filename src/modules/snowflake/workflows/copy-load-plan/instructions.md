# copy-load-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/copy-load-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this copy load plan (batch/micro-batch)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="COPY 参数（并行/文件模式/验证）">
<action>Work on copy 参数（并行/文件模式/验证）</action>
<template-output section="copy_params"/>
</step>

<step n="3" goal="幂等/去重/断点续传">
<action>Work on 幂等/去重/断点续传</action>
<template-output section="idempotency"/>
</step>

<step n="4" goal="错误处理/隔离与重试">
<action>Work on 错误处理/隔离与重试</action>
<template-output section="error_handling"/>
</step>

<step n="5" goal="调度与回补">
<action>Work on 调度与回补</action>
<template-output section="scheduling"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
