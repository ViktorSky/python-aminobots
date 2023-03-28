from typing import List, Tuple
from ..object import Object

__all__ = 'LinkedPromotionalMediaList',


class LinkedPromotionalMediaList(Object):
    json: List[List[Tuple[int, str, None]]]

    @property
    def url(self) -> List[List[str]]:
        return [[[ml[1] if ml else None for ml in pm] for pm in pml] for pml in self.json]
