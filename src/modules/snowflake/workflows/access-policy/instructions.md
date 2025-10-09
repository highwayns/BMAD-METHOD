# access-policy - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/access-policy/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this access policy & privacy contract</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="数据分类与标签">
<action>Work on 数据分类与标签</action>
<template-output section="classification"/>
</step>

<step n="3" goal="行/列访问策略与动态屏蔽">
<action>Work on 行/列访问策略与动态屏蔽</action>
<template-output section="row_col"/>
</step>

<step n="4" goal="用途限定与再分发">
<action>Work on 用途限定与再分发</action>
<template-output section="usage"/>
</step>

<step n="5" goal="审计留痕与保留">
<action>Work on 审计留痕与保留</action>
<template-output section="audit"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
