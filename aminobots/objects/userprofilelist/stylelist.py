from typing import List, Optional
from ..object import Object
from .backgroundmedialist import *

__all__ = 'StyleList',


class StyleList(Object):
    json: List[dict]

    @property
    def backgroundMedia(self) -> BackgroundMediaList:
        return BackgroundMediaList([s.get("backgroundMediaList") or [] for s in self.json])

    @property
    def backgroundUrl(self) -> List[Optional[str]]:
        return self.backgroundMedia.url
