from typing import List
from ..object import Object

__all__ = 'AddedTopic', 'Style'


class Style(Object):
    json: List[dict]

    @property
    def backgroundColor(self) -> List[str]:
        return [s.get("backgroundColor") for s in self.json]


class AddedTopic(Object):
    json: List[dict]

    @property
    def backgroundColor(self) -> List[str]:
        return self.style.backgroundColor

    @property
    def name(self) -> List[str]:
        return [at.get("name") for at in self.json]

    @property
    def style(self) -> Style:
        return Style([at.get("style") or {} for at in self.json])

    @property
    def topicId(self) -> List[int]:
        return [at.get("topicId") for at in self.json]
