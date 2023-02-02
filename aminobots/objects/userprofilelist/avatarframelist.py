from typing import List, Optional
from ..object import Object

__all__ = 'AvatarFrameList',


class AvatarFrameList(Object):
    json: List[dict]

    @property
    def frameId(self) -> List[str]:
        return [af.get("frameId") for af in self.json]

    @property
    def frameType(self) -> List[int]:
        return [af.get("frameType") for af in self.json]

    @property
    def icon(self) -> List[str]:
        return [af.get("icon") for af in self.json]

    @property
    def name(self) -> List[str]:
        return [af.get("name") for af in self.json]

    @property
    def ownershipStatus(self) -> List[Optional[str]]:
        return [af.get("ownershipStatus") for af in self.json]

    @property
    def status(self) -> List[int]:
        return [af.get("status") for af in self.json]

    @property
    def version(self) -> List[int]:
        return [af.get("version") for af in self.json]

    @property
    def url(self) -> List[str]:
        return [af.get("resourceUrl") for af in self.json]
