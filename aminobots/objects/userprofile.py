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
from pydantic import BaseModel, HttpUrl, Field
from .community import Community
from .media import Media
from .style import Style
from ..enums import (
    ClientType,
    ConnectionStatus,
    FollowingStatus,
    MembershipStatus,
    Role
)

__all__ = ('UserProfile',)


class DeviceInfo(BaseModel):
    lastClientType: ClientType = Field(default=ClientType.MASTER)


class Extensions(BaseModel):
    acpDeeplink: Optional[str]
    adsEnabled: bool = Field(default=False)
    adsFlags: int = Field(default=0)
    backroundColor: Optional[Color] = property(lambda self: self.style.backgroundColor)
    backgroundMediaList: List[Media] = property(lambda self: self.style.backgroundMediaList)
    creatorDeeplink: Optional[HttpUrl] # example: https://aminoapps.page.link/6CTa
    customTitles: list = Field(default_factory=list)
    defaultBubbleId: Optional[str]
    deviceInfo: DeviceInfo = Field(default_factory=DeviceInfo)
    # disabledLevel: Any = Field(alias='__disabledLevel__')
    # disabledStatus: int = Field(alias='__disabledStatus__')
    # disabledTime: datetime = Field(alias='__disabledTime__')
    isMemberOfTeamAmino: bool = Field(default=False)
    privilegeOfChatInviteRequest: Optional[int]
    privilegeOfChatRequest: Optional[int]
    privilegeOfCommentOnUserProfile: Optional[int] # [2, 3]
    privilegeOfPublicChat: Optional[int] # [0, 1]
    privilegeOfVideoChat: Optional[int] # [9]
    style: Style = Field(default_factory=Style)
    tippingPermStatus: Optional[int] # [0, 1]


class AvatarFrame(BaseModel):
    id: str = Field(alias='frameId')
    icon: HttpUrl
    name: str
    ownershipStatus: Optional[str]
    status: int = Field(default=0)
    type: int = Field(alias='frameType')
    version: int
    url: HttpUrl = Field(alias='resourceUrl')

    if not TYPE_CHECKING:
        id: Optional[str]
        icon: Optional[HttpUrl]
        name: Optional[str]
        ownershipStatus: Optional[str]
        type: Optional[int]
        version: Optional[int]
        url: Optional[HttpUrl]


class UserProfile(BaseModel):
    accountMembershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    acpDeeplink: Optional[str] = property(lambda self: self.extensions.acpDeeplink)
    adminLogCountIn7Days: bool = Field(default=False)
    aminoId: str
    aminoIdEditable: bool = Field(default=False)
    frame: AvatarFrame = Field(alias='avatarFrame', default_factory=AvatarFrame)
    frameId: Optional[str] = Field(alias='avatarFrameId')
    backgroundColor: Optional[Color] = property(lambda self: self.extensions.style.backgroundColor)
    backgroundMediaList: List[Media] = property(lambda self: self.extensions.style.backgroundMediaList)
    bio: Optional[str] = Field(alias='content')
    blogsCount: int = Field(default=0)
    comId: Optional[int] = Field(alias='ndcId', default=0)
    commentsCount: int = Field(default=0)
    consecutiveCheckInDays: Optional[int] = Field(default=0)
    createdTime: datetime
    creatorDeeplink: Optional[str] = property(lambda self: self.extensions.creatorDeeplink)
    defaultBubbleId: Optional[str] = property(lambda self: self.extensions.defaultBubbleId)
    deviceInfo: DeviceInfo = property(lambda self: self.extensions.deviceInfo)
    extensions: Extensions = Field(default_factory=Extensions)
    followersCount: int = Field(alias='membersCount', default=0)
    followingsCount: int = Field(alias='joinedCount', default=0)
    followingStatus: FollowingStatus = Field(default=FollowingStatus.NOT_FOLLOWING)
    icon: HttpUrl
    id: str = Field(alias='uid')
    isGlobal: bool = Field(default=True)
    isNicknameVerified: bool = Field(default=False)
    level: Optional[int]
    linkedCommunityList: List[Community] = Field(default_factory=list)
    mediaList: List[Media] = Field(default_factory=list)
    membershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    modifiedTime: Optional[datetime]
    mood: str
    moodSticker: str
    nickname: str
    notifSubStatus: Optional[int] = Field(alias='notificationSubscriptionStatus') # [0, 1]
    onlineStatus: ConnectionStatus = Field(default=ConnectionStatus.OFFLINE)
    postsCount: int = Field(default=0)
    privilegeOfChatInviteRequest: Optional[int] = property(lambda self: self.extensions.privilegeOfChatInviteRequest)
    privilegeOfChatRequest: Optional[int] = property(lambda self: self.extensions.privilegeOfChatRequest)
    privilegeOfCommentOnUserProfile: Optional[int] = property(lambda self: self.extensions.privilegeOfCommentOnUserProfile)
    privilegeOfPublicChat: Optional[int] = property(lambda self: self.extensions.privilegeOfPublicChat)
    privilegeOfVideoChat: Optional[int] = property(lambda self: self.extensions.privilegeOfVideoChat)
    pushEnabled: bool = Field(default=False)
    reputation: Optional[int]
    role: Role = Field(default=Role.MEMBER)
    status: int = Field(default=0)
    storiesCount: int = Field(default=0)
    style: Style = property(lambda self: self.extensions.style)
    tippingPermStatus: Optional[int] = property(lambda self: self.extensions.tippingPermStatus)
    visitPrivacy: Optional[int]
    wikisCount: int = Field(alias='itemsCount', default=0)

    if not TYPE_CHECKING:
        aminoId: Optional[str]
        createdTime: Optional[datetime]
        icon: Optional[HttpUrl]
        id: Optional[str]
        mood: Optional[str]
        moodSticker: Optional[str]
        nickname: Optional[str]
