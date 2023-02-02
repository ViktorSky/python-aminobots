from typing import List
from ..object import Object

__all__ = 'LinkedAgentList',


class LinkedAgentList(Object):
    json: List[List[dict]]

    @property
    def id(self) -> List[List[str]]:
        return [[a.get("uid") for a in ag] for ag in self.json]
