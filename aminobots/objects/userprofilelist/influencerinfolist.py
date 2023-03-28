from typing import List
from ..object import Object
from ...utils import Date

__all__ = ('InfluencerInfoList',)


class InfluencerInfoList(Object):
    json: List[dict]

    @property
    def fansCount(self) -> List[int]:
        return [i.get('fansCount') for i in self.json]

    @property
    def createdTime(self) -> List[Date]:
        return [Date(i.get('createdTime')) for i in self.json]

    @property
    def pinned(self) -> List[bool]:
        return [i.get('pinned') for i in self.json]

    @property
    def monthlyFee(self) -> List[int]:
        return [i.get('monthlyFee') for i in self.json]
