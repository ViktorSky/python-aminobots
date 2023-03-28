from typing import List
from ..object import Object

__all__ = 'LinkedThemePackList',


class LinkedThemePackList(Object):
    json: List[List[dict]]

    @property
    def color(self) -> List[List[str]]:
        return [[tp.get("themeColor") for tp in tpl] for tpl in self.json]

    @property
    def hash(self) -> List[List[str]]:
        return [[tp.get("themePackHash") for tp in tpl] for tpl in self.json]

    @property
    def revision(self) -> List[List[int]]:
        return [[tp.get("themePackRevision") for tp in tpl] for tpl in self.json]

    @property
    def url(self) -> List[List[str]]:
        return [[tp.get("themePackUrl") for tp in tpl] for tpl in self.json]
