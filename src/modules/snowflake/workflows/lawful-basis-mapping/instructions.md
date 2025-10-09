# lawful-basis-mapping - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/lawful-basis-mapping/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this lawful basis mapping (gdpr/ccpa/pipl)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="合法基础（同意/合同/法定义务/重大利益/公共利益/正当利益）">
<action>Work on 合法基础（同意/合同/法定义务/重大利益/公共利益/正当利益）</action>
<template-output section="basis"/>
</step>

<step n="3" goal="平衡测试/必要性评估">
<action>Work on 平衡测试/必要性评估</action>
<template-output section="tests"/>
</step>

<step n="4" goal="证据与签字">
<action>Work on 证据与签字</action>
<template-output section="evidence"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
