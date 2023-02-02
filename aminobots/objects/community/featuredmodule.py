from ..object import Object

__all__ = 'FeaturedModule',


class FeaturedModule(Object):
    json: dict

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def layout(self) -> int:
        return self.json.get("layout")

    @property
    def lockMember(self) -> bool:
        return self.json.get("lockMember")

    @property
    def memberEnabled(self) -> bool:
        return self.json.get("memberEnabled")

    @property
    def postEnabled(self) -> bool:
        return self.json.get("postEnabled")

    @property
    def publicChatEnabled(self) -> bool:
        return self.json.get("publicChatRoomEnabled")
