from typing import List
from ..object import Object

__all__ = 'Media',


class Media(Object):
    json: list

    @property
    def url(self) -> List[str]:
        return [m[1] if m else None for m in self.json]
