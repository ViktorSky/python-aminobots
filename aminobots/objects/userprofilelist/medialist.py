from typing import Any, List
from ..object import Object

__all__ = 'MediaList',


class MediaList(Object):
    json: List[List[List[Any]]]

    @property
    def url(self) -> List[List[str]]:
        return [[m[1] if m else None for m in ml] for ml in self.json]
