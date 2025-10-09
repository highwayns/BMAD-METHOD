# qa-test-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/qa-test-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this qa master test plan (scope/risks/strategy)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="范围（对象/作业/接口/权限）">
<action>Work on 范围（对象/作业/接口/权限）</action>
<template-output section="scope"/>
</step>

<step n="3" goal="风险与缓解（数据/安全/性能/成本）">
<action>Work on 风险与缓解（数据/安全/性能/成本）</action>
<template-output section="risks"/>
</step>

<step n="4" goal="策略（契约/数据/场景/门禁/证据）">
<action>Work on 策略（契约/数据/场景/门禁/证据）</action>
<template-output section="strategy"/>
</step>

<step n="5" goal="角色与责任/日程">
<action>Work on 角色与责任/日程</action>
<template-output section="owners"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
