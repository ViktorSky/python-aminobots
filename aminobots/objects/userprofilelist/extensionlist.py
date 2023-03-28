from typing import List, Optional
from ..object import Object
from .backgroundmedialist import *
from .deviceinfolist import *
from .stylelist import *

__all__ = 'ExtensionList',


class ExtensionList(Object):
    json: List[dict]

    @property
    def acpDeeplink(self) -> List[Optional[str]]:
        return [e.get("acpDeeplink") for e in self.json]

    @property
    def adsEnabled(self) -> List[Optional[bool]]:
        return [e.get("adsEnabled") for e in self.json]

    @property
    def adsFlags(self) -> List[Optional[int]]:
        return self.json.get("adsFlags")

    @property
    def backgroundMedia(self) -> BackgroundMediaList:
        return self.style.backgroundMedia

    @property
    def backgroundUrl(self) -> List[Optional[str]]:
        return self.style.backgroundUrl

    @property
    def backgroundUrlList(self) -> List[List[str]]:
        return self.style.backgroundUrlList

    @property
    def creatorDeeplink(self) -> List[Optional[str]]:
        return [e.get("creatorDeeplink") for e in self.json]

    @property
    def customTitles(self):
        return [e.get("customTitles") for e in self.json]

    @property
    def defaultBubbleId(self) -> List[Optional[str]]:
        return [e.get("defaultBubbleId") for e in self.json]

    @property
    def deviceInfo(self) -> DeviceInfoList:
        return DeviceInfoList([e.get("deviceInfo") or {} for e in self.json])

    # @property
    # def disabledLevel(self):
    #     return [e.get("__disabledLevel__") for e in self.json]

    # @property
    # def disabledStatus(self):
    #     return [e.get("__disabledStatus__") for e in self.json]

    # @property
    # def disabledTime(self):
    #     return [e.get("__disabledTime__") for e in self.json]

    # @property
    # def isMemberOfTeamAmino(self) -> bool:
    #     return [e.get("isMemberOfTeamAmino") or False for e in self.json]

    @property
    def privilegeOfChatInviteRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatInviteRequest") for e in self.json]

    @property
    def privilegeOfChatRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatRequest") for e in self.json]

    @property
    def privilegeOfCommentOnUserProfile(self) -> List[Optional[int]]:
        return [e.get("privilegeOfCommentOnUserProfile") for e in self.json]

    @property
    def privilegeOfPublicChat(self) -> List[Optional[int]]:
        return [e.get("privilegeOfPublicChat") for e in self.json]

    @property
    def privilegeOfVideoChat(self) -> Optional[int]:
        return [e.get("privilegeOfVideoChat") for e in self.json]

    @property
    def style(self) -> StyleList:
        return StyleList([e.get("style") or {} for e in self.json])

    @property
    def tippingPermStatus(self) -> Optional[int]:
        return [e.get("tippingPermStatus") for e in self.json]
