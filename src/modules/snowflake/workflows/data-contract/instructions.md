# data-contract - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/data-contract/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data/feature/model contracts</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="训练/验证/线上数据集（Schema/分区/保留）">
<action>Work on 训练/验证/线上数据集（schema/分区/保留）</action>
<template-output section="datasets"/>
</step>

<step n="3" goal="特征定义（公式/口径/实体/时效）">
<action>Work on 特征定义（公式/口径/实体/时效）</action>
<template-output section="features"/>
</step>

<step n="4" goal="模型接口（输入/输出/约束）">
<action>Work on 模型接口（输入/输出/约束）</action>
<template-output section="models"/>
</step>

<step n="5" goal="SLI/SLO（准确/延迟/失败率/成本）">
<action>Work on sli/slo（准确/延迟/失败率/成本）</action>
<template-output section="slislos"/>
</step>

<step n="6" goal="隐私/用途限定/掩码/行列策略">
<action>Work on 隐私/用途限定/掩码/行列策略</action>
<template-output section="privacy"/>
</step>

<step n="7" goal="版本策略/兼容/弃用/回退">
<action>Work on 版本策略/兼容/弃用/回退</action>
<template-output section="versioning"/>
</step>

<step n="8" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
