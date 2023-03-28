from ..others import Object

__all__ = ("Style", "jsonExample")


class Style(Object):
    json: dict

    @property
    def backgroundColor(self) -> str:
        return self.json.get("backgroundColor")


jsonExample = {
    "backgroundColor": "#FF6262"
}
