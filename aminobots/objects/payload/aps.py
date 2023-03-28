from ..object import Object

__all__ = ('Aps',)


class Aps(Object):

    @property
    def alert(self) -> str:
        return self.json.get('alert')

    @property
    def badge(self) -> int:
        return self.json.get('badge')

    @property
    def sound(self) -> str:
        return self.json.get('sound')
