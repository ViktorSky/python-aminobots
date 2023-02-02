from typing import Optional
from ..object import Object
from .backgroundmedia import *

__all__ = 'Style',


class Style(Object):
    json: dict

    @property
    def backgroundMedia(self) -> BackgroundMedia:
        return BackgroundMedia(self.json.get("backgroundMediaList") or [])

    @property
    def backgroundColor(self) -> Optional[str]:
        return self.json.get("backgroundColor")

    @property
    def backgroundUrl(self) -> Optional[str]:
        return self.backgroundMedia.url
