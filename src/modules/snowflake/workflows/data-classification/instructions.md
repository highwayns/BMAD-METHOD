# data-classification - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/data-classification/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data classification and tagging strategy</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="数据清单（域/Owner/用途）">
<action>Work on 数据清单（域/owner/用途）</action>
<template-output section="inventory"/>
</step>

<step n="3" goal="标签与级别（PUBLIC/INTERNAL/CONFIDENTIAL/PII 等）">
<action>Work on 标签与级别（public/internal/confidential/pii 等）</action>
<template-output section="labels"/>
</step>

<step n="4" goal="保留/Time Travel/Fail-safe/Legal Hold">
<action>Work on 保留/time travel/fail-safe/legal hold</action>
<template-output section="retention"/>
</step>

<step n="5" goal="共享策略与禁止规则">
<action>Work on 共享策略与禁止规则</action>
<template-output section="sharing"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete undefined output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
