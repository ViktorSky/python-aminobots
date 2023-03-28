from typing import Optional
from ..object import Object

__all__ = 'AvatarFrame',


class AvatarFrame(Object):
    json: dict

    @property
    def id(self) -> str:
        return self.json.get("frameId")

    @property
    def frameType(self) -> int:
        return self.json.get("frameType")

    @property
    def icon(self) -> str:
        return self.json.get("icon")

    @property
    def name(self) -> str:
        return self.json.get("name")

    @property
    def ownershipStatus(self) -> Optional[str]:
        return self.json.get("ownershipStatus")

    @property
    def status(self) -> int:
        return self.json.get("status")

    @property
    def version(self) -> int:
        return self.json.get("version")

    @property
    def url(self) -> str:
        return self.json.get("resourceUrl")
