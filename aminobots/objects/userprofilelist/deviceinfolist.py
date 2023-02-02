from typing import List
from ..object import Object

__all__ = 'DeviceInfoList',


class DeviceInfoList(Object):
    json: List[dict]

    @property
    def lastClientType(self):
        return [di.get("lastClientType") for di in self.json]
