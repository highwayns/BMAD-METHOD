# template_id: pipeline-td/publisher-plugin
# purpose: Publisher 插件模板
class PublisherPlugin:
    family = "generic"
    version = 1
    def validate(self, context): ...
    def publish(self, context): ...
