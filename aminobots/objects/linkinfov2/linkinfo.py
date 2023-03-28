from typing import Optional
from ..object import Object

__all__ = 'LinkInfo',


class LinkInfo(Object):
    json: dict

    @property
    def comId(self) -> int:
        return self.json.get("ndcId")

    @property
    def fullPath(self) -> Optional[str]:
        return self.json.get("fullPath")

    @property
    def fullUrl(self) -> Optional[str]:
        return self.json.get("shareURLFullPath")

    @property
    def objectId(self) -> str:
        return self.json.get("objectId")

    @property
    def objectType(self) -> int:
        return self.json.get("objectType")

    @property
    def shortCode(self) -> Optional[str]:
        return self.json.get("shortCode")

    @property
    def shortUrl(self) -> Optional[str]:
        return self.json.get("shareURLShortCode")

    @property
    def targetCode(self) -> int:
        return self.json.get("targetCode")
