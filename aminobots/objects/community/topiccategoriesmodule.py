from ..object import Object

__all__ = 'TopicCategoriesModule',


class TopicCategoriesModule(Object):
    json: dict

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")
