from ..object import Object

__all__ = 'AdvancedSettings',


class AdvancedSettings(Object):
    json: dict

    @property
    def analyticsEnabled(self) -> int:
        return self.json.get("analyticsEnabled")
