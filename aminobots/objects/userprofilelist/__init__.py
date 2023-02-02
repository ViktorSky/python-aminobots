from typing import List, Optional
from ..object import Object
from .avatarframelist import *
from .extensionlist import *
from .linkedcommunitylist import *
from .medialist import *
from .stylelist import *

__all__ = 'UserProfileList',
# LinkedActiveInfoList

class UserProfileList(Object):
    json: List[dict]

    @property
    def accountMembershipStatus(self) -> List[int]:
        return [up.get("accountMembershipStatus") or 0 for up in self.json]

    @property
    def acpDeeplink(self) -> List[Optional[str]]:
        return self.extensions.acpDeeplink

    @property
    def adminLogCountIn7Days(self):
        return [up.get("adminLogCountIn7Days") for up in self.json]

    @property
    def aminoId(self) -> List[str]:
        return [up.get("aminoId") for up in self.json]

    @property
    def avatarFrame(self) -> AvatarFrameList:
        return AvatarFrameList([up.get("avatarFrame") or {} for up in self.json])

    @property
    def bio(self) -> List[Optional[str]]:
        return [up.get("content") or 0 for up in self.json]

    @property
    def blogsCount(self) -> List[int]:
        return [up.get("blogsCount") or 0 for up in self.json]

    @property
    def comId(self) -> List[Optional[int]]:
        return [up.get("ndcId") or None for up in self.json]

    @property
    def commentsCount(self) -> List[int]:
        return [up.get("commentsCount") or 0 for up in self.json]

    @property
    def consecutiveCheckInDays(self):
        return [up.get("consecutiveCheckInDays") for up in self.json]

    @property
    def createdTime(self) -> List[str]:
        return [up.get("createdTime") for up in self.json]

    @property
    def creatorDeeplink(self) -> Optional[str]:
        return self.extensions.creatorDeeplink

    @property
    def extensions(self) -> ExtensionList:
        return ExtensionList([up.get("extensions") or {} for up in self.json])

    @property
    def followersCount(self) -> List[int]:
        return [up.get("membersCount") for up in self.json]

    @property
    def followingCount(self) -> List[int]:
        return [up.get("joinedCount") for up in self.json]

    @property
    def followingStatus(self) -> List[int]:
        return [up.get("followingStatus") for up in self.json]

    @property
    def icon(self) -> List[str]:
        return [up.get("icon") for up in self.json]

    @property
    def isGlobalProfile(self) -> bool:
        return all(up.get("isGlobal") for up in self.json)

    @property
    def level(self) -> List[int]:
        return [up.get("level") or 0 for up in self.json]

    @property
    def linkedCommunities(self) -> LinkedCommunityList:
        return LinkedCommunityList([up.get("linkedCommunityList") or [] for up in self.json])

    @property
    def media(self) -> MediaList:
        return MediaList([up.get("mediaList") or [] for up in self.json])

    @property
    def membershipStatus(self) -> List[int]:
        return [up.get("membershipStatus") or 0 for up in self.json]

    @property
    def modifiedTime(self) -> List[str]:
        return [up.get("modifiedTime") for up in self.json]

    # @property
    # def mood(self):
        # return [up.get("mood") for up in self.json]


    # @property
    # def moodSticker(self):
        # return [up.get("moodSticker") for up in self.json]

    @property
    def nickname(self) -> List[str]:
        return [up.get("nickname") for up in self.json]

    @property
    def nicknameVerified(self) -> List[bool]:
        return [up.get("isNicknameVerified") for up in self.json]

    @property
    def notifSubStatus(self) -> List[int]:  # [0, 1]
        return [up.get("notificationSubscriptionStatus") for up in self.json]

    @property
    def onlineStatus(self) -> List[int]:
        return [up.get("onlineStatus") for up in self.json]

    @property
    def postsCount(self) -> List[int]:
        return [up.get("postsCount") or 0 for up in self.json]

    @property
    def privilegeOfChatRequest(self) -> List[int]:
        return self.extensions.privilegeOfChatRequest

    @property
    def pushEnabled(self) -> List[bool]:
        return [up.get("pushEnabled") for up in self.json]

    @property
    def reputation(self) -> List[int]:
        return [up.get("reputation") or 0 for up in self.json]

    @property
    def role(self) -> List[int]:
        return [up.get("role") for up in self.json]

    @property
    def status(self) -> List[int]:
        return [up.get("status") for up in self.json]

    @property
    def storiesCount(self) -> List[int]:
        return [up.get("storiesCount") or 0 for up in self.json]

    @property
    def style(self) -> StyleList:
        return self.extensions.style

    @property
    def userId(self) -> List[str]:
        return [up.get("uid") for up in self.json]

    @property
    def wikisCount(self) -> List[int]:
        return [up.get("itemsCount") for up in self.json]
