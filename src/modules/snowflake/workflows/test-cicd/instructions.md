# test-cicd - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/test-cicd/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this test ci/cd (pipelines/artifacts/reports)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="流水线阶段（lint/test/contract/e2e）">
<action>Work on 流水线阶段（lint/test/contract/e2e）</action>
<template-output section="pipelines"/>
</step>

<step n="3" goal="工件（Junit/XML/证据包）">
<action>Work on 工件（junit/xml/证据包）</action>
<template-output section="artifacts"/>
</step>

<step n="4" goal="门禁/审批/回滚">
<action>Work on 门禁/审批/回滚</action>
<template-output section="governance"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
