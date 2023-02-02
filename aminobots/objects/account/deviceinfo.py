from ..object import Object

__all__ = 'DeviceInfo',


class DeviceInfo(Object):
    json: dict

    @property
    def lastClientType(self):
        return self.json.get("lastClientType")
