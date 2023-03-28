from ..object import Object

__all__ = 'Ads',


class Ads(Object):
    json: dict

    @property
    def lastPopupTime(self) -> str:
        return self.json.get("lastPopupTime")

    @property
    def status(self) -> int:
        return self.json.get("status")
