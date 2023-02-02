from typing import List
from ..object import Object

__all__ = 'Navigation', 'NavigationLevelList'


class NavigationLevelList(Object):
    json: List[dict]

    @property
    def id(self) -> List[str]:
        return [ll.get("id") for ll in self.json]


class Navigation(Object):
    json: dict

    @property
    def level1(self) -> NavigationLevelList:
        return NavigationLevelList(self.json.get("level1") or [])

    @property
    def level1Ids(self) -> List[str]:
        return self.level1.id

    @property
    def level2(self) -> NavigationLevelList:
        return NavigationLevelList(self.json.get("level2") or [])

    @property
    def level2Ids(self) -> List[str]:
        return self.level2.id
