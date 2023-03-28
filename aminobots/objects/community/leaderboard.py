from typing import List, Optional
from ..object import Object

__all__ = 'Leaderboard',


class Leaderboard(Object):
    json: List[dict]

    @property
    def enabled(self) -> List[bool]:
        return [lb.get("enabled") for lb in self.json]

    @property
    def id(self) -> List[str]:
        return [lb.get("id") for lb in self.json]

    @property
    def style(self) -> List[Optional[str]]:
        return [lb.get("style") for lb in self.json]

    @property
    def type(self) -> List[int]:
        return [lb.get("type") for lb in self.json]
