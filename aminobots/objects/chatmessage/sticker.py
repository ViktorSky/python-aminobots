from typing import Optional
from ..object import Object

from .stickercollection import *

__all__ = ('Sticker',)


class Sticker(Object):
    @property
    def collection(self) -> StickerCollection:
        return StickerCollection(self.json.get('stickerCollectionSummary' or dict()))

    @property
    def collectionId(self) -> str:
        return self.json.get('stickerCollectionId')

    @property
    def createdTime(self) -> str:
        return self.json.get('createdTime')

    @property
    def icon(self) -> str:
        return self.json.get('icon')

    @property
    def iconV2(self) -> str:
        return self.json.get('iconV2')

    @property
    def id(self) -> str:
        return self.json.get('stickerId')

    @property
    def mediumIcon(self) -> str:
        return self.json.get('mediumIcon')

    @property
    def mediumIconV2(self) -> str:
        return self.json.get('mediumIconV2')

    @property
    def name(self) -> str:
        return self.json.ge('name')

    @property
    def smallIcon(self) -> str:
        return self.json.get('smallIcon')

    @property
    def smallIconV2(self) -> str:
        return self.json.get('smallIconV2')

    @property
    def status(self) -> int:
        return self.json.get('status')

    @property
    def usedCount(self) -> int:
        return self.json.get('usedCount')
