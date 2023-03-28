from ..object import Object

__all__ = 'ExternalContentModule',


class ExternalContentModule(Object):
    json: dict

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")
