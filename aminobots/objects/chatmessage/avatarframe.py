from ..object import Object

__all__ = ('AvatarFrame',)


class AvatarFrame(Object):

    @property
    def id(self) -> str:
        return self.json.get('frameId')

    @property
    def icon(self) -> str:
        return self.json.get('icon')

    @property
    def name(self) -> str:
        return self.json.get('name')

    @property
    def status(self) -> int:
        return self.json.get('status')

    @property
    def type(self) -> int:
        return self.json.get('frameType')

    @property
    def url(self) -> str:
        return self.json.get('resourceUrl')

    @property
    def version(self) -> int:
        return self.json.get('version')
