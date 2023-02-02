from typing import Optional, List, Literal, Union
from ..object import Object
from ..account import DeviceInfo
from .backgroundmedia import *
from .style import Style

__all__ = 'Extensions',


class Extensions(Object):
    json: dict

    @property
    def acpDeeplink(self) -> Optional[str]:
        return self.json.get("acpDeeplink")

    @property
    def adsEnabled(self) -> Optional[bool]:
        return self.json.get("adsEnabled")

    @property
    def adsFlags(self) -> Optional[int]:
        return self.json.get("adsFlags")

    @property
    def backgroundMedia(self) -> BackgroundMedia:
        return self.style.backgroundMedia

    @property
    def backgroundUrl(self) -> Optional[str]:
        return self.style.backgroundUrl

    @property
    def backgroundUrlList(self) -> Union[List[str], list]:
        return self.style.backgroundUrlList

    @property
    def creatorDeeplink(self) -> Optional[str]:
        return self.json.get("creatorDeeplink")
        # https://aminoapps.page.link/6CTa

    @property
    def customTitles(self):
        return self.json.get("customTitles")

    @property
    def defaultBubbleId(self) -> Optional[str]:
        return self.json.get("defaultBubbleId")

    @property
    def deviceInfo(self) -> DeviceInfo:
        return DeviceInfo(self.json.get("deviceInfo") or {})

    # @property
    # def disabledLevel(self):
    #     return self.json.get("__disabledLevel__")

    # @property
    # def disabledStatus(self):
    #     return self.json.get("__disabledStatus__")

    # @property
    # def disabledTime(self):
    #     return self.json.get("__disabledTime__")

    # @property
    # def isMemberOfTeamAmino(self) -> bool:
    #     return self.json.get("isMemberOfTeamAmino") or False

    @property
    def privilegeOfChatInviteRequest(self) -> Optional[int]: # [1,]
        return self.json.get("privilegeOfChatInviteRequest")

    @property
    def privilegeOfChatRequest(self) -> Optional[int]: # []
        return self.json.get("privilegeOfChatRequest")

    @property
    def privilegeOfCommentOnUserProfile(self) -> Optional[int]: # [2, 3]
        return self.json.get("privilegeOfCommentOnUserProfile")

    @property
    def privilegeOfPublicChat(self) -> Optional[Literal[0, 1]]:
        return self.json.get("privilegeOfPublicChat")

    @property
    def privilegeOfVideoChat(self) -> Optional[int]: # [9,]
        return self.json.get("privilegeOfVideoChat")

    @property
    def style(self) -> Style:
        return Style(self.json.get("style") or {})

    @property
    def tippingPermStatus(self) -> Optional[Literal[0, 1]]:
        return self.json.get("tippingPermStatus")
