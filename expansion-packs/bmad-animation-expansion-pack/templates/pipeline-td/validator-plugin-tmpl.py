# template_id: pipeline-td/validator-plugin
# purpose: Validator 插件模板
class ValidatorPlugin:
    id = "name_rule"
    severity = "error"
    def check(self, context): ...
    def fix(self, context): ...
