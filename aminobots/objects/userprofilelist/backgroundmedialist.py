from typing import List, Optional, Tuple
from ..object import Object

__all__ = 'BackgroundMediaList',


class BackgroundMediaList(Object):
    json: List[List[Tuple[int, str, None, None, None, dict]]]

    @property
    def url(self) -> List[Optional[str]]:
        return [bg[0][1] if bg and any(bg[0]) else None for bg in self.json]

