from typing import List
from ..object import Object
from .linkedstylelist import *

__all__ = 'LinkedAddedTopicList',


class LinkedAddedTopicList(Object):
    json: List[List[List[dict]]]

    @property
    def backgroundColor(self) -> List[str]:
        return self.style.backgroundColor

    @property
    def name(self) -> List[List[List[str]]]:
        return [[[lt.get("name") for lt in lat] for lat in latl] for latl in self.json]

    @property
    def style(self) -> LinkedStyleList:
        return LinkedStyleList([[[lt.get("style") or {} for lt in lat] for lat in latl] for latl in self.json])

    @property
    def topicId(self) -> List[List[List[int]]]:
        return [[[lt.get("topicId") for lt in lat] for lat in latl] for latl in self.json]
