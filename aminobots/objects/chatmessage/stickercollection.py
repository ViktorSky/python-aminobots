from ..object import Object

__all__ = ('StickerCollection',)


class StickerCollection(Object):

    @property
    def authorId(self) -> str:
        return self.json.get('uid')

    @property
    def banner(self) -> str:
        return self.json.get('bannerUrl')

    @property
    def createdTime(self) -> str:
        return self.json.get('createdTime')

    @property
    def icon(self) -> str:
        return self.json.get('icon')

    @property
    def id(self) -> str:
        return self.json.get('collectionId')

    @property
    def modifiedTime(self) -> str:
        return self.json.get('modifiedTime')

    @property
    def name(self) -> str:
        return self.json.get('name')

    @property
    def smallIcon(self) -> str:
        return self.json.get('smallIcon')

    @property
    def status(self) -> int:
        return self.json.get('status')

    @property
    def stickersCount(self) -> int:
        return self.json.get('stickersCount')

    @property
    def type(self) -> int:
        return self.json.get('collectionType')

    @property
    def usedCount(self) -> int:
        return self.json.get('usedCount')
