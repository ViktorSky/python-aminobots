from typing import List, Optional
from ..object import Object

__all__ = 'HomeNavigationList', 'HomePage'


class HomeNavigationList(Object):
    json: List[dict]

    @property
    def id(self) -> List[str]:
        return [nl.get("id") for nl in self.json]

    @property
    def isStartPage(self) -> List[Optional[bool]]:
        return [nl.get("isStartPage") for nl in self.json]


class HomePage(Object):
    json: dict

    @property
    def id(self) -> List[str]:
        return self.navigation.id

    @property
    def isStartPage(self) -> List[Optional[bool]]:
        return self.navigation.isStartPage

    @property
    def navigation(self) -> HomeNavigationList:
        return HomeNavigationList(self.json.get("navigation") or [])

