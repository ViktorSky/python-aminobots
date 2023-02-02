from typing import List, Optional
from ..object import Object
from .linkedbackgroundmedialist import *

__all__ = 'LinkedStyleList',


class LinkedStyleList(Object):
    json: List[List[List[dict]]]

    @property
    def backgroundMedia(self) -> LinkedBackgroundMediaList:
        return LinkedBackgroundMediaList([[[s.get("backgroundMediaList") or [] for s in ls] for ls in lsl] for lsl in self.json])

    @property
    def backgroundColor(self) -> List[List[Optional[str]]]:
        return [[[s.get('backgroundColor')for s in ls]for ls in lsl]for lsl in self.json]

    @property
    def backgroundUrl(self) -> List[List[Optional[str]]]:
        return self.backgroundMedia.url
