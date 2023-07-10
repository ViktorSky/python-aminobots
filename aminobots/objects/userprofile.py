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
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic.color import Color
from pydantic import BaseModel, HttpUrl, Field, validator
from .avatarframe import AvatarFrame
from .community import Community
from .media import Media
from .style import Style
from ..enums import (
    ChatRequestPermission,
    ClientType,
    CommentPermission,
    ConnectionStatus,
    FollowingStatus,
    MembershipStatus,
    Role
)

__all__ = ('UserProfile',)


class DeviceInfo(BaseModel):
    lastClientType: ClientType = Field(default=ClientType.MASTER)


class Extensions(BaseModel):
    acpDeeplink: Optional[str] = Field(default=None)
    adsEnabled: bool = Field(default=False)
    adsFlags: int = Field(default=0)
    backroundColor: Optional[Color] = property(lambda self: self.style.backgroundColor) # type: ignore
    backgroundMediaList: List[Media] = property(lambda self: self.style.backgroundMediaList) # type: ignore
    creatorDeeplink: Optional[HttpUrl] = Field(default=None) # example: https://aminoapps.page.link/6CTa
    customTitles: list = Field(default_factory=list)
    defaultBubbleId: Optional[str] = Field(default=None)
    deviceInfo: DeviceInfo = Field(default_factory=DeviceInfo)
    # disabledLevel: Any = Field(alias='__disabledLevel__')
    # disabledStatus: int = Field(alias='__disabledStatus__')
    # disabledTime: datetime = Field(alias='__disabledTime__')
    isMemberOfTeamAmino: bool = Field(default=False)
    chatInviteRequestPermission: ChatRequestPermission = Field(alias='privilegeOfChatInviteRequest', default=ChatRequestPermission.EVERYONE)
    chatRequestPermission: Optional[int] = Field(alias='privilegeOfChatRequest', default=None)
    commentPermission: CommentPermission = Field(alias='privilegeOfCommentOnUserProfile', default=CommentPermission.EVERYONE)
    privilegeOfPublicChat: Optional[int] = Field(default=None) # [0, 1]
    privilegeOfVideoChat: Optional[int] = Field(default=None) # [9]
    style: Style = Field(default_factory=Style)
    tippingPermStatus: Optional[int] = Field(default=None) # [0, 1]


class UserProfile(BaseModel):
    accountMembershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    acpDeeplink: Optional[str] = property(lambda self: self.extensions.acpDeeplink) # type: ignore
    adminLogCountIn7Days: bool = Field(default=False)
    aminoId: str = Field(default=None)
    aminoIdEditable: bool = Field(default=False)
    backgroundColor: Optional[Color] = property(lambda self: self.extensions.style.backgroundColor) # type: ignore
    backgroundMediaList: List[Media] = property(lambda self: self.extensions.style.backgroundMediaList) # type: ignore
    bio: Optional[str] = Field(alias='content', default=None)
    blogsCount: int = Field(default=0)
    comId: Optional[int] = Field(alias='ndcId', default=0)
    commentsCount: int = Field(default=0)
    consecutiveCheckInDays: Optional[int] = Field(default=0)
    createdTime: datetime = Field(default=None)
    creatorDeeplink: Optional[str] = property(lambda self: self.extensions.creatorDeeplink) # type: ignore
    defaultBubbleId: Optional[str] = property(lambda self: self.extensions.defaultBubbleId) # type: ignore
    deviceInfo: DeviceInfo = property(lambda self: self.extensions.deviceInfo) # type: ignore
    extensions: Optional[Extensions] = Field(default_factory=Extensions)
    followersCount: int = Field(alias='membersCount', default=0)
    followingsCount: int = Field(alias='joinedCount', default=0)
    frame: AvatarFrame = Field(alias='avatarFrame', default_factory=AvatarFrame)
    frameId: Optional[str] = Field(alias='avatarFrameId', default=None)
    followingStatus: FollowingStatus = Field(default=FollowingStatus.NOT_FOLLOWING)
    icon: HttpUrl = Field(default=None)
    id: str = Field(alias='uid', default=None)
    isGlobal: bool = Field(default=True)
    isNicknameVerified: bool = Field(default=False)
    level: Optional[int] = Field(default=None)
    linkedCommunityList: List[Community] = Field(default_factory=list)
    mediaList: Optional[List[Media]] = Field(default=None)
    membershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    modifiedTime: Optional[datetime]
    mood: str
    moodSticker: str
    nickname: str
    notifSubStatus: Optional[int] = Field(alias='notificationSubscriptionStatus') # [0, 1]
    onlineStatus: ConnectionStatus = Field(default=ConnectionStatus.OFFLINE)
    postsCount: int = Field(default=0)
    privilegeOfChatInviteRequest: Optional[int] = property(lambda self: self.extensions.privilegeOfChatInviteRequest) # type: ignore
    privilegeOfChatRequest: Optional[int] = property(lambda self: self.extensions.privilegeOfChatRequest) # type: ignore
    privilegeOfCommentOnUserProfile: Optional[int] = property(lambda self: self.extensions.privilegeOfCommentOnUserProfile) # type: ignore
    privilegeOfPublicChat: Optional[int] = property(lambda self: self.extensions.privilegeOfPublicChat) # type: ignore
    privilegeOfVideoChat: Optional[int] = property(lambda self: self.extensions.privilegeOfVideoChat) # type: ignore
    pushEnabled: bool = Field(default=False)
    reputation: Optional[int]
    role: Role = Field(default=Role.MEMBER)
    status: int = Field(default=0)
    storiesCount: int = Field(default=0)
    style: Style = property(lambda self: self.extensions.style) # type: ignore
    tippingPermStatus: Optional[int] = property(lambda self: self.extensions.tippingPermStatus) # type: ignore
    visitPrivacy: Optional[int]
    wikisCount: int = Field(alias='itemsCount', default=0)

    #_list_validator = validator('linkedCommunityList')(lambda value: [] if value is not None else value)
    #_int_validator = validator()(lambda value: 0 if value is not None else value)

    if not TYPE_CHECKING:
        aminoId: Optional[str]
        createdTime: Optional[datetime]
        icon: Optional[HttpUrl]
        id: Optional[str]
        mood: Optional[str]
        moodSticker: Optional[str]
        nickname: Optional[str]
