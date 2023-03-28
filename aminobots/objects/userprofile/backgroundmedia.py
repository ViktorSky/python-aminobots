from typing import List, Optional, Tuple
from ..object import Object

__all__ = 'BackgroundMedia',


class BackgroundMedia(Object):
    json: List[Tuple[int, str, None, None, None, dict]]

    @property
    def url(self) -> Optional[str]:
        if self.json and any(self.json[0]):
            return self.json[0][1]
