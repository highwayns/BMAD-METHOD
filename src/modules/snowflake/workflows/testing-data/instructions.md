# testing-data - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/testing-data/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this test data strategy (synthetic/masked/snapshots)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="来源（快照/生成/脱敏）">
<action>Work on 来源（快照/生成/脱敏）</action>
<template-output section="sources"/>
</step>

<step n="3" goal="覆盖（边界/异常/性能）">
<action>Work on 覆盖（边界/异常/性能）</action>
<template-output section="coverage"/>
</step>

<step n="4" goal="生命周期与清理">
<action>Work on 生命周期与清理</action>
<template-output section="ops"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
