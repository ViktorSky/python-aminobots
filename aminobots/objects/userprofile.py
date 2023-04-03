"""MIT License

Copyright (c) 2022 ViktorSky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from dataclasses import dataclass
from typing import List, Literal, Optional, Tuple
from .account import DeviceInfo
from .communitylist import CommunityList

__all__ = ('UserProfile',)


@dataclass(repr=False)
class BackgroundMedia:
    """Represent the user profile background.

    Attributes
    ----------
    json: List[:class:`list`]
        The raw API data.
    url: Optional[:class:`str`]
        background url.

    """
    json: List[Tuple[int, str, None, None, None, dict]]

    @property
    def url(self) -> Optional[str]:
        """Background url."""
        if self.json and any(self.json[0]):
            return self.json[0][1]


@dataclass(repr=False)
class Media:
    """Represent all media value in the user bio.

    Attributes
    ----------
    json: :class:`list`
        The raw API data.
    url: List[:class:`str`]
        media urls.

    """
    json: list

    @property
    def url(self) -> List[str]:
        return [m[1] if m else None for m in self.json]


@dataclass(repr=False)
class Style:
    """Represent the user profile style.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    background: :class:`BackroundMedia`
        Backround object.
    backroundColor: Optional[:class:`str`]
        Color hex code.
    backroundUrl: :class:`str`
        Backroun url.

    """
    json: dict

    @property
    def background(self) -> BackgroundMedia:
        """Backround object."""
        return BackgroundMedia(self.json.get("backgroundMediaList") or [])

    @property
    def backgroundColor(self) -> Optional[str]:
        """Color hex code."""
        return self.json.get("backgroundColor")

    @property
    def backgroundUrl(self) -> Optional[str]:
        """Backround url."""
        return self.background.url


@dataclass(repr=False)
class Extensions:
    """Represent the user profile extensions.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    acpDeeplink: Optional[:class:`str`]
        ...
    adsEnabled: Optional[:class:`bool`]
        ...
    adsFlags: :class:`int`
        ...
    background: :class:`BackroundMedia`
        Background object.
    backgroundUrl: :class:`str`
        Background url.
    creatorDeeplink: :class:`str`
        ...
    titles: Optional[List[:class:`dict`]]
        User custom titles.
    defaultBubbleId: Optional[:class:`str`]
        Bubble id.
    deviceInfo: :class:`DeviceInfo`
        Device info object.
    privilegeOfChatInviteRequest: :class:`int`
        ...
    privilegeOfChatRequest: :class:`int`
        ...
    privilegeOfCommentOnUserProfile: :class:`int`
        ...
    privilegeOfPublicChat: :class:`int`
        ...
    privilegeOfVideoChat: :class:`int`
        ...
    style: :class:`Style`
        ...
    tippingPermStatus: :class:`int`
        ...

    """
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
    def background(self) -> BackgroundMedia:
        """User background."""
        return self.style.background

    @property
    def backroundColor(self) -> Optional[str]:
        """Color hex code."""
        return self.style.backgroundColor

    @property
    def backgroundUrl(self) -> Optional[str]:
        return self.style.backgroundUrl

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


@dataclass(repr=False)
class AvatarFrame:
    """Represent the user avatar frame.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    id: :class:`str`
        Avatar frame id.
    icon: :class:`str`
        Avatar frame icon url.
    name: :class:`str`
        Avatar frame name.
    ownershipStatus: :class:`int`
        Ownership status.
    status: :class:`int`
        Avatar frame status.
    type: :class:`int`
        Avatar frame type.
    version: :class:`int`
        Avatar frame version.
    url: :class:`str`
        Avatar frame resource url. (zip)

    """
    json: dict

    @property
    def id(self) -> str:
        """Avatar frame id."""
        return self.json.get("frameId")

    @property
    def icon(self) -> str:
        """Avatar frame icon url."""
        return self.json.get("icon")

    @property
    def name(self) -> str:
        """Avatar frame name."""
        return self.json.get("name")

    @property
    def ownershipStatus(self) -> Optional[str]:
        """Ownership status."""
        return self.json.get("ownershipStatus")

    @property
    def status(self) -> int:
        """Avatar frame status."""
        return self.json.get("status")

    @property
    def type(self) -> int:
        """Avatar frame type."""
        return self.json.get("frameType")

    @property
    def version(self) -> int:
        """Avatar frame version."""
        return self.json.get("version")

    @property
    def url(self) -> str:
        """Avatar frame resource url. (zip)"""
        return self.json.get("resourceUrl")


@dataclass(repr=False)
class UserProfile:
    """Represent a user profile of Amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    acccountMembershipStatus: :class:`int`
        ...
    acpDeeplink: Optional[:class:`str`]
        ...
    adminLogCountIn7Days: Optional[:class:`int`]
        ...
    aminoId: :class:`str`
        ...
    avatar: :class:`AvatarFrame`
        Avatar Frame object.
    avatarId: :classs:`str`
        Avatar Frame id.
    background: :class:`BackgroundMedia`
        User background.
    backgroundColor: Optional[:class:`str`]
        Hex color string.
    bio: Optional[:class:`str`]
        User bio.
    blogsCount: :class:`int`
        User blogs count.
    comId: Optional[:class:`int`]
        Profile community id.
    commentsCount: :class:`int`
        Comments count.
    consecutiveCheckInDays: :class:`int`
        User Check-in days.
    createdTime: :class:`str`
        User community joined time.
    creatorDeeplink: Optional[:class:`str`]
        ...
    defaultBubbleId: Optional[:class:`str`]
        Default chat bubble id.
    deviceInfo: :class:`DeviceInfo`
        Device info.
    extensions: :class:`Extensions`
        User profile extensions.
    followersCount: :class:`int`
        Followers count.
    followingsCount: :class:`int`
        Followings count.
    followingStatus: Literal[`0`, `1`]
        ...
    icon: :class:`str`
        User icon url.
    id: :class:`str`
        User id.
    isGlobal: :class:`bool`
        Global or Community user profile.
    isnicknameVerified: :class:`bool`
        ...
    level: :class:`int`
        Community user level.
    linkedCommunities: :class:`CommunityList`
        Profile Linked communities
    media: :class:`Media`
        Profile media list.
    membershipStatus: :class:`int`
        Membership status.
    modifiedTime: :class:`str`
        Profile modified time.
    nickname::class:`str`
        User nickname.
    notifSubStatus: :class:`int`
        Notification Subscription Status.
    onlineStatus: :class:`int`
        Online status.
    postsCount: :class:`int`
        Posts count.
    privilegeOfChatInviteRequest: Optional[:class:`int`]
        Privilege of chat invite request.
    privilegeOfChatRequest: :class:`int`
        Privilege of chat request.
    privilegeOfCommentOnUserProfile: Optional[:class:`int`]
        Privilege of comment on user profile.
    privilegeOfPublicChat: Optional[:class:`int`]
        Privilege of public chat.
    privilegeOfVideoChat: :class:`int`
        Privilege of video chat.
    pushEnabled: :class:`bool`
        Push enabled.
    reputation:
        Community user reputation.
    role: :class:`int`
        Community user role.
    status: :class:`int`
        Account status.
    storiesCount: :class:`int`
        Stories count.
    style: :class:`Style`
        Profile style extension.
    tippingPermStatus: :class:`int`
        Tipping permission status.
    visitPrivacy: :class:`int`
        ...
    wikisCount: :class:`int`
        Wikis count.

    """
    json: dict

    @property
    def accountMembershipStatus(self) -> Literal[0, 1]:
        """Account Membership status."""
        return self.json.get("accountMembershipStatus")

    @property
    def acpDeeplink(self) -> Optional[str]:
        return self.extensions.acpDeeplink

    @property
    def adminLogCountIn7Days(self):
        return self.json.get("adminLogCountIn7Days")

    @property
    def aminoId(self) -> str:
        """Amino id."""
        return self.json.get("aminoId")

    # @property  # not found
    # def aminoIdEditable(self) -> bool:
        # return self.json.get("aminoIdEditable")

    @property
    def avatar(self) -> AvatarFrame:
        """Avatar Frame object."""
        return AvatarFrame(self.json.get("avatarFrame") or {})

    @property
    def avatarId(self):
        """Avatar frame id."""
        return self.json.get("avatarFrameId") or self.avatarFrame.id

    @property
    def background(self) -> BackgroundMedia:
        """User background."""
        return self.extensions.style.background

    @property
    def backgroundColor(self) -> Optional[str]:
        """Hex color string."""
        return self.extensions.style.backgroundColor

    @property
    def bio(self) -> Optional[str]:
        """User bio."""
        return self.json.get("content")

    @property
    def blogsCount(self) -> int:
        """Blogs count."""
        return self.json.get("blogsCount")

    @property
    def comId(self) -> Optional[int]:
        """Profile community id."""
        return self.json.get("ndcId") or None

    @property
    def commentsCount(self) -> int:
        return self.json.get("commentsCount") or 0

    @property
    def consecutiveCheckInDays(self) -> Optional[int]:
        return self.json.get("consecutiveCheckInDays")

    @property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @property
    def creatorDeeplink(self) -> Optional[str]:
        return self.extensions.creatorDeeplink

    @property
    def defaultBubbleId(self) -> Optional[str]:
        return self.extensions.defaultBubbleId

    @property
    def deviceInfo(self) -> DeviceInfo:
        return self.extensions.deviceInfo

    @property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @property
    def followersCount(self) -> int:
        return self.json.get("membersCount") or 0

    @property
    def followingCount(self) -> int:
        return self.json.get("joinedCount") or 0

    @property
    def followingStatus(self) -> Literal[0, 1]:
        return self.json.get("followingStatus")

    @property
    def icon(self) -> str:
        return self.json.get("icon")

    @property
    def id(self) -> str:
        return self.json.get("uid")

    @property
    def isGlobal(self) -> bool:
        return self.json.get("isGlobal")

    @property
    def isnicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @property
    def level(self) -> int:
        return self.json.get("level")

    @property
    def linkedCommunities(self) -> CommunityList:
        return CommunityList(self.json.get("linkedCommunityList") or {})

    @property
    def media(self) -> Media:
        return Media(self.json.get("mediaList") or [])

    @property
    def membershipStatus(self) -> Literal[0, 1]:
        return self.json.get("membershipStatus")

    @property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    # @property
    # def mood(self):
        # return self.json.get("mood")

    # @property
    # def moodSticker(self):  # ...
        # return self.json.get("moodSticker")

    @property
    def nickname(self) -> str:
        """Community user nickname."""
        return self.json.get("nickname")

    @property
    def notifSubStatus(self) -> Literal[0, 1]:
        """Notification Subscription Status."""
        return self.json.get("notificationSubscriptionStatus")

    @property
    def onlineStatus(self) -> int: # [2]
        """Online status."""
        return self.json.get("onlineStatus")

    @property
    def postsCount(self) -> int:
        """Post count."""
        return self.json.get("postsCount")

    @property
    def privilegeOfChatInviteRequest(self) -> Optional[int]:
        """Privilege of chat invite request."""
        return self.extensions.privilegeOfChatInviteRequest

    @property
    def privilegeOfChatRequest(self) -> int:
        """privilege of chat request."""
        return self.extensions.privilegeOfChatRequest

    @property
    def privilegeOfCommentOnUserProfile(self) -> Optional[int]:
        """Privilege of comment on user profile."""
        return self.extensions.privilegeOfCommentOnUserProfile

    @property
    def privilegeOfPublicChat(self) -> Optional[int]:
        """Privilege of public chat."""
        return self.extensions.privilegeOfPublicChat

    @property
    def privilegeOfVideoChat(self) -> Optional[int]:
        """Privilege of video chat."""
        return self.extensions.privilegeOfVideoChat

    @property
    def pushEnabled(self) -> bool:
        """Push enabled."""
        return self.json.get("pushEnabled")

    @property
    def reputation(self) -> int:
        """Community user reputation."""
        return self.json.get("reputation")

    @property
    def role(self) -> int:
        """Community user role."""
        return self.json.get("role")

    @property
    def status(self) -> Literal[0, 1]:
        """Account status."""
        return self.json.get("status")

    @property
    def storiesCount(self) -> int:
        """Stories count."""
        return self.json.get("storiesCount")

    @property
    def style(self):
        return self.extensions.style

    @property
    def tippingPermStatus(self) -> Optional[int]:
        """Tipping permission status."""
        return self.extensions.tippingPermStatus

    @property
    def visitPrivacy(self) -> Optional[int]:  # [1]
        return self.json.get("visitPrivacy")

    @property
    def wikisCount(self) -> int:
        """Wikis count."""
        return self.json.get("itemsCount")
