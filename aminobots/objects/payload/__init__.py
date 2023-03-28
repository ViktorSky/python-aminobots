from ..object import Object
from .aps import *

__all__ = ('Payload',)


class Payload(Object):

    @property
    def aps(self) -> Aps:
        return Aps(self.json.get('aps', dict()))

    @property
    def chatId(self) -> str:
        return self.json.get('tid')

    @property
    def comId(self) -> str:
        return self.json.get('ndcId')

    @property
    def createdTime(self) -> str:
        return self.json.get('ts')

    @property
    def id(self) -> str:
        return self.json.get('id')

    @property
    def isHidden(self) -> bool:
        return self.json.get('isHidden')

    @property
    def msgType(self) -> int:
        return self.json.get('msgType', 0)

    @property
    def notifType(self) -> int:
        return self.json.get('notifType', 0)
