from typing import List, Tuple
from ..object import Object

__all__ = 'PromotionalMedia',


class PromotionalMedia(Object):
    json: List[Tuple[int, str, None]]

    @property
    def url(self) -> List[str]:
        return [m[1] if m else None for m in self.json]
