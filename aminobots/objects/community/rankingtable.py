from typing import List
from ..object import Object

__all__ = 'RankingTable',


class RankingTable(Object):
    json: List[dict]

    @property
    def id(self) -> List[str]:
        return [rtl.get("id") for rtl in self.json]

    @property
    def level(self) -> List[int]:
        return [rtl.get("level") for rtl in self.json]

    @property
    def reputation(self) -> List[int]:
        return [rtl.get("reputation") for rtl in self.json]

    @property
    def title(self) -> List[str]:
        return [rtl.get("title") for rtl in self.json]
