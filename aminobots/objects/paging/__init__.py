from ..object import Object

__all__ = ('Paging',)


class Paging(Object):

    @property
    def nextPageToken(self) -> str:
        return self.json.get("nextPageToken")
