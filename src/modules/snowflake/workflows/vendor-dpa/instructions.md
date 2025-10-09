# vendor-dpa - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/vendor-dpa/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this vendor/dpa register & assessments</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="供应商与数据流向">
<action>Work on 供应商与数据流向</action>
<template-output section="inventory"/>
</step>

<step n="3" goal="合同条款/子处理者">
<action>Work on 合同条款/子处理者</action>
<template-output section="clauses"/>
</step>

<step n="4" goal="安全/隐私评估与复核频率">
<action>Work on 安全/隐私评估与复核频率</action>
<template-output section="assessments"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
