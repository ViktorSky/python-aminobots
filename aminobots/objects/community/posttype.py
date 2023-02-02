from ..object import Object
from .privilege import PrivilegeManager

__all__ = 'PostType',


class PostType(Object):
    json: dict

    @property
    def blog(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("blog") or {})

    @property
    def catalogEntry(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("catalogEntry") or {})

    @property
    def image(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("image") or {})

    @property
    def liveMode(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("liveMode") or {})

    @property
    def poll(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("poll") or {})

    @property
    def publicChat(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("publicChatRooms") or {})

    @property
    def question(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("question") or {})

    @property
    def quiz(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("quiz") or {})

    @property
    def screeningRoom(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("screeningRoom") or {})

    @property
    def story(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("story") or {})

    @property
    def webLink(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("webLink") or {})
