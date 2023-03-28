from typing import Optional
from ..object import Object

from .sticker import *

__all__ = ('Extensions',)


class Extensions(Object):

    @property
    def duration(self) -> Optional[float]:
        return self.json.get('duration')

    @property
    def originalStickerId(self) -> Optional[str]:
        return self.json.get('originalStickerId')

    @property
    def sticker(self) -> Sticker:
        return Sticker(self.json.get('sticker') or dict())
