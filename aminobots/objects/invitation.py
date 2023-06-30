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
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field
from ..enums import MembershipStatus, Role, FollowingStatus

__all__ = ('Invitation',)


class InfluencerInfo(BaseModel):
    createdTime: datetime
    fansCount: int = Field(default=0)
    pinned: bool = Field(default=False) # alias: isPinned
    monthlyFee: int = Field(default=0)

    if not TYPE_CHECKING:
        createdTime: Optional[datetime]


class Author(BaseModel):
    accountMembershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    followingStatus: FollowingStatus = Field(default=FollowingStatus.NOT_FOLLOWING)
    icon: HttpUrl
    followersCount: int = Field(alias='membersCount', default=0)
    comId: int = Field(alias='ndcId')
    id: str = Field(alias='uid')
    isGlobal: bool = Field(default=False)
    isNicknameVerified: bool = Field(default=False)
    level: Optional[int]
    membershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    nickname: str
    reputation: Optional[int]
    role: Role = Field(default=Role.MEMBER)
    status: int = Field(default=0)
    vip: InfluencerInfo = Field(alias='influencerInfo', default_factory=InfluencerInfo)

    if not TYPE_CHECKING:
        icon: Optional[HttpUrl]
        comId: Optional[int]
        id: Optional[str]
        nickname: Optional[str]


class Invitation(BaseModel):
    author: Author = Field(default_factory=Author)
    comId: int = Field(alias='ndcId')
    createdTime: datetime
    duration: int
    inviteCode: str
    id: str = Field(alias='invitationId')
    link: HttpUrl
    modifiedTime: Optional[datetime]
    status: int = Field(default=0)

    if not TYPE_CHECKING:
        comId: Optional[int]
        createdTime: Optional[datetime]
        duration: Optional[int]
        inviteCode: Optional[str]
        id: Optional[str]
        link: Optional[HttpUrl]
