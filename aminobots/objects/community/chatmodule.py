from ..object import Object
from .privilege import PrivilegeManager

__all__ = 'AvChat', 'ChatModule'


class AvChat(Object):
    json: dict

    @property
    def audioEnabled(self) -> bool:
        return self.json.get("audioEnabled")

    @property
    def audio2Enabled(self) -> bool:
        return self.json.get("audio2Enabled")

    @property
    def screeningRoomEnabled(self) -> bool:
        return self.json.get("screeningRoomEnabled")

    @property
    def videoEnabled(self) -> bool:
        return self.json.get("videoEnabled")


class ChatModule(Object):
    json: dict

    @property
    def avChat(self) -> AvChat:
        return AvChat(self.json.get("avChat") or {})

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def publicChat(self) -> PrivilegeManager:
        return PrivilegeManager(self.json.get("publicChat") or {})

    @property
    def publicChatEnabled(self):
        return self.publicChat.enabled

    @property
    def spamProtectionEnabled(self) -> bool:
        return self.json.get("spamProtectionEnabled")
