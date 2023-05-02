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
from functools import cached_property
from dataclasses import dataclass
from typing import List, Literal, Optional, Tuple
from . import account
from . import communitylist



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

    @cached_property
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

    @cached_property
    def type(self) -> List[int]:
        return [m[0] if m else None for m in self.json]

    @cached_property
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

    @cached_property
    def background(self) -> BackgroundMedia:
        """Backround object."""
        return BackgroundMedia(self.json.get("backgroundMediaList") or [])

    @cached_property
    def backgroundColor(self) -> Optional[str]:
        """Color hex code."""
        return self.json.get("backgroundColor")

    @cached_property
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

    @cached_property
    def acpDeeplink(self) -> Optional[str]:
        return self.json.get("acpDeeplink")

    @cached_property
    def adsEnabled(self) -> Optional[bool]:
        return self.json.get("adsEnabled")

    @cached_property
    def adsFlags(self) -> Optional[int]:
        return self.json.get("adsFlags")

    @cached_property
    def background(self) -> BackgroundMedia:
        """User background."""
        return self.style.background

    @cached_property
    def backroundColor(self) -> Optional[str]:
        """Color hex code."""
        return self.style.backgroundColor

    @cached_property
    def backgroundUrl(self) -> Optional[str]:
        return self.style.backgroundUrl

    @cached_property
    def creatorDeeplink(self) -> Optional[str]:
        return self.json.get("creatorDeeplink")
        # https://aminoapps.page.link/6CTa

    @cached_property
    def customTitles(self):
        return self.json.get("customTitles")

    @cached_property
    def defaultBubbleId(self) -> Optional[str]:
        return self.json.get("defaultBubbleId")

    @cached_property
    def deviceInfo(self) -> account.DeviceInfo:
        return account.DeviceInfo(self.json.get("deviceInfo") or {})

    # @cached_property
    # def disabledLevel(self):
    #     return self.json.get("__disabledLevel__")

    # @cached_property
    # def disabledStatus(self):
    #     return self.json.get("__disabledStatus__")

    # @cached_property
    # def disabledTime(self):
    #     return self.json.get("__disabledTime__")

    # @cached_property
    # def isMemberOfTeamAmino(self) -> bool:
    #     return self.json.get("isMemberOfTeamAmino") or False

    @cached_property
    def privilegeOfChatInviteRequest(self) -> Optional[int]: # [1,]
        return self.json.get("privilegeOfChatInviteRequest")

    @cached_property
    def privilegeOfChatRequest(self) -> Optional[int]: # []
        return self.json.get("privilegeOfChatRequest")

    @cached_property
    def privilegeOfCommentOnUserProfile(self) -> Optional[int]: # [2, 3]
        return self.json.get("privilegeOfCommentOnUserProfile")

    @cached_property
    def privilegeOfPublicChat(self) -> Optional[Literal[0, 1]]:
        return self.json.get("privilegeOfPublicChat")

    @cached_property
    def privilegeOfVideoChat(self) -> Optional[int]: # [9,]
        return self.json.get("privilegeOfVideoChat")

    @cached_property
    def style(self) -> Style:
        return Style(self.json.get("style") or {})

    @cached_property
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

    @cached_property
    def id(self) -> str:
        """Avatar frame id."""
        return self.json.get("frameId")

    @cached_property
    def icon(self) -> str:
        """Avatar frame icon url."""
        return self.json.get("icon")

    @cached_property
    def name(self) -> str:
        """Avatar frame name."""
        return self.json.get("name")

    @cached_property
    def ownershipStatus(self) -> Optional[str]:
        """Ownership status."""
        return self.json.get("ownershipStatus")

    @cached_property
    def status(self) -> int:
        """Avatar frame status."""
        return self.json.get("status")

    @cached_property
    def type(self) -> int:
        """Avatar frame type."""
        return self.json.get("frameType")

    @cached_property
    def version(self) -> int:
        """Avatar frame version."""
        return self.json.get("version")

    @cached_property
    def url(self) -> str:
        """Avatar frame resource url. (zip)"""
        return self.json.get("resourceUrl")


@dataclass(repr=False)
class UserProfile:
    """Represent a user profile of Amino.

    Attributes
    ----------
    json : :class:`dict`
        The raw API data.
    acccountMembershipStatus : :class:`int`
        ...
    acpDeeplink : Optional[:class:`str`]
        ...
    adminLogCountIn7Days : Optional[:class:`int`]
        ...
    aminoId : :class:`str`
        ...
    background : :class:`BackgroundMedia`
        User background.
    backgroundColor : Optional[:class:`str`]
        Hex color string.
    bio : Optional[:class:`str`]
        User bio.
    blogsCount : :class:`int`
        User blogs count.
    communityId: Optional[:class:`int`]
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
    frame: :class:`AvatarFrame`
        Avatar Frame object.
    frameId: :classs:`str`
        Avatar Frame id.
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

    @cached_property
    def accountMembershipStatus(self) -> Literal[0, 1]:
        """Account Membership status."""
        return self.json.get("accountMembershipStatus")

    @cached_property
    def acpDeeplink(self) -> Optional[str]:
        return self.extensions.acpDeeplink

    @cached_property
    def adminLogCountIn7Days(self):
        return self.json.get("adminLogCountIn7Days")

    @cached_property
    def aminoId(self) -> str:
        """Amino id."""
        return self.json.get("aminoId")

    # @cached_property  # not found
    # def aminoIdEditable(self) -> bool:
        # return self.json.get("aminoIdEditable")

    @cached_property
    def frame(self) -> AvatarFrame:
        """Avatar Frame object."""
        return AvatarFrame(self.json.get("avatarFrame") or {})

    @cached_property
    def frameId(self):
        """Avatar frame id."""
        return self.json.get("avatarFrameId") or self.frame.id

    @cached_property
    def background(self) -> BackgroundMedia:
        """User background."""
        return self.extensions.style.background

    @cached_property
    def backgroundColor(self) -> Optional[str]:
        """Hex color string."""
        return self.extensions.style.backgroundColor

    @cached_property
    def bio(self) -> Optional[str]:
        """User bio."""
        return self.json.get("content")

    @cached_property
    def blogsCount(self) -> int:
        """Blogs count."""
        return self.json.get("blogsCount")

    @cached_property
    def communityId(self) -> Optional[int]:
        """Profile community id."""
        return self.json.get("ndcId") or None

    @cached_property
    def commentsCount(self) -> int:
        return self.json.get("commentsCount") or 0

    @cached_property
    def consecutiveCheckInDays(self) -> Optional[int]:
        return self.json.get("consecutiveCheckInDays")

    @cached_property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @cached_property
    def creatorDeeplink(self) -> Optional[str]:
        return self.extensions.creatorDeeplink

    @cached_property
    def defaultBubbleId(self) -> Optional[str]:
        return self.extensions.defaultBubbleId

    @cached_property
    def deviceInfo(self) -> account.DeviceInfo:
        return self.extensions.deviceInfo

    @cached_property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @cached_property
    def followersCount(self) -> int:
        return self.json.get("membersCount") or 0

    @cached_property
    def followingsCount(self) -> int:
        return self.json.get("joinedCount") or 0

    @cached_property
    def followingStatus(self) -> Literal[0, 1]:
        return self.json.get("followingStatus")

    @cached_property
    def icon(self) -> str:
        return self.json.get("icon")

    @cached_property
    def id(self) -> str:
        return self.json.get("uid")

    @cached_property
    def isGlobal(self) -> bool:
        return self.json.get("isGlobal")

    @cached_property
    def isnicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @cached_property
    def level(self) -> int:
        return self.json.get("level")

    @cached_property
    def linkedCommunities(self) -> communitylist.CommunityList:
        return communitylist.CommunityList(self.json.get("linkedCommunityList") or {})

    @cached_property
    def media(self) -> Media:
        return Media(self.json.get("mediaList") or [])

    @cached_property
    def membershipStatus(self) -> Literal[0, 1]:
        return self.json.get("membershipStatus")

    @cached_property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    # @cached_property
    # def mood(self):
        # return self.json.get("mood")

    # @cached_property
    # def moodSticker(self):  # ...
        # return self.json.get("moodSticker")

    @cached_property
    def nickname(self) -> str:
        """Community user nickname."""
        return self.json.get("nickname")

    @cached_property
    def notifSubStatus(self) -> Literal[0, 1]:
        """Notification Subscription Status."""
        return self.json.get("notificationSubscriptionStatus")

    @cached_property
    def onlineStatus(self) -> int: # [2]
        """Online status."""
        return self.json.get("onlineStatus")

    @cached_property
    def postsCount(self) -> int:
        """Post count."""
        return self.json.get("postsCount")

    @cached_property
    def privilegeOfChatInviteRequest(self) -> Optional[int]:
        """Privilege of chat invite request."""
        return self.extensions.privilegeOfChatInviteRequest

    @cached_property
    def privilegeOfChatRequest(self) -> int:
        """privilege of chat request."""
        return self.extensions.privilegeOfChatRequest

    @cached_property
    def privilegeOfCommentOnUserProfile(self) -> Optional[int]:
        """Privilege of comment on user profile."""
        return self.extensions.privilegeOfCommentOnUserProfile

    @cached_property
    def privilegeOfPublicChat(self) -> Optional[int]:
        """Privilege of public chat."""
        return self.extensions.privilegeOfPublicChat

    @cached_property
    def privilegeOfVideoChat(self) -> Optional[int]:
        """Privilege of video chat."""
        return self.extensions.privilegeOfVideoChat

    @cached_property
    def pushEnabled(self) -> bool:
        """Push enabled."""
        return self.json.get("pushEnabled")

    @cached_property
    def reputation(self) -> int:
        """Community user reputation."""
        return self.json.get("reputation")

    @cached_property
    def role(self) -> int:
        """Community user role."""
        return self.json.get("role")

    @cached_property
    def status(self) -> Literal[0, 1]:
        """Account status."""
        return self.json.get("status")

    @cached_property
    def storiesCount(self) -> int:
        """Stories count."""
        return self.json.get("storiesCount")

    @cached_property
    def style(self):
        return self.extensions.style

    @cached_property
    def tippingPermStatus(self) -> Optional[int]:
        """Tipping permission status."""
        return self.extensions.tippingPermStatus

    @cached_property
    def visitPrivacy(self) -> Optional[int]:  # [1]
        return self.json.get("visitPrivacy")

    @cached_property
    def wikisCount(self) -> int:
        """Wikis count."""
        return self.json.get("itemsCount")


@dataclass(repr=False)
class Author:
    json: dict

    @cached_property
    def accountMembershipStatus(self) -> int:
        return self.json.get('accountMembershipStatus')

    @cached_property
    def communityId(self) -> int:
        return self.json.get('ndcId')

    @cached_property
    def followersCount(self) -> int:
        return self.json.get('membersCount')

    @cached_property
    def followingStatus(self) -> int:
        return self.json.get('followingStatus')

    @cached_property
    def frame(self) -> AvatarFrame:
        return AvatarFrame(self.json.get('avatarFrame') or {})

    @cached_property
    def frameId(self) -> str:
        return self.json.get('avatarFrameId')

    @cached_property
    def icon(self) -> str:
        return self.json.get('icon')

    @cached_property
    def id(self) -> str:
        """User id."""
        return self.json.get('uid')

    @cached_property
    def isGlobal(self) -> bool:
        return self.json.get('isGlobal')

    @cached_property
    def level(self) -> int:
        return self.json.get('level')

    @cached_property
    def membershipStatus(self) -> int:
        return self.json.get('membershipStatus')

    @cached_property
    def nickname(self) -> str:
        return self.json.get('nickname')

    @cached_property
    def nicknameVerified(self) -> bool:
        return self.json.get('isNicknameVerified')

    @cached_property
    def reputation(self) -> int:
        return self.json.get('reputation')

    @cached_property
    def role(self) -> int:
        return self.json.get('role')

    @cached_property
    def status(self) -> int:
        return self.json.get('status')
