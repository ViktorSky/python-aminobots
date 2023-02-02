from typing import List, Optional
from ..object import Object

__all__ = 'CustomPage', 'DefaultPage', 'PageModule'


class CustomPage(Object):
    json: List[dict]

    @property
    def alias(self) -> List[Optional[str]]:
        return [cl.get("alias") for cl in self.json]

    @property
    def id(self) -> List[str]:
        return [cl.get("id") for cl in self.json]

    @property
    def url(self) -> List[str]:
        return [cl.get("url") for cl in self.json]


class DefaultPage(Object):
    json: List[dict]

    @property
    def alias(self) -> List[Optional[str]]:
        return [dl.get("alias") for dl in self.json]

    @property
    def id(self) -> List[Optional[str]]:
        return [dl.get("id") for dl in self.json]

    @property
    def url(self) -> List[str]:
        return [dl.get("url") for dl in self.json]


class PageModule(Object):
    json: dict

    @property
    def custom(self) -> CustomPage:
        return CustomPage(self.json.get("customList") or [])

    @property
    def default(self) -> DefaultPage:
        return DefaultPage(self.json.get("defaultList") or [])
