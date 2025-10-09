# flaky-tests - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/flaky-tests/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this flaky tests management (quarantine/heuristics)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="隔离与重试策略">
<action>Work on 隔离与重试策略</action>
<template-output section="quarantine"/>
</step>

<step n="3" goal="诊断启发式与记录">
<action>Work on 诊断启发式与记录</action>
<template-output section="heuristics"/>
</step>

<step n="4" goal="修复与退出标准">
<action>Work on 修复与退出标准</action>
<template-output section="fix"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
