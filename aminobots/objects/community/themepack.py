from ..object import Object

__all__ = 'ThemePack',


class ThemePack(Object):
    json: dict

    @property
    def color(self) -> str:
        return self.json.get("themeColor")

    @property
    def hash(self) -> str:
        return self.json.get("themePackHash")

    @property
    def revision(self) -> int:
        return self.json.get("themePackRevision")

    @property
    def url(self) -> str:
        return self.json.get("themePackUrl")
