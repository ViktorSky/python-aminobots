from typing import List
from ..object import Object

__all__ = 'FeedPageList',


class FeedPageList(Object):
    json: list

    @property
    def json(self) -> List[dict]:
        return sorted(self.json, key=lambda x: x.get("type"))

    @property
    def status(self) -> List[int]:
        return [fp.get("status") for fp in self.json]

    @property
    def type(self):
        return [fp.get("type") for fp in self.json]
