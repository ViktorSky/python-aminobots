from typing import List, Optional, Tuple
from ..object import Object

__all__ = 'LinkedBackgroundMediaList',


class LinkedBackgroundMediaList(Object):
    json: List[List[List[Tuple[int, str, None, None, None, dict]]]]

    @property
    def url(self) -> List[List[Optional[str]]]:
        return [[bg[0][1] if bg and any(bg[0]) else None for bg in bgl] for bgl in self.json]
