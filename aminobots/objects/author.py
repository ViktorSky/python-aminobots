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
from pydantic import BaseModel, HttpUrl, Field
from ..enums import (
    FollowingStatus,
    MembershipStatus,
    Role
)

__all__ = ('Author',)


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
        type: Optional[int]
        version: Optional[int]
        url: Optional[HttpUrl]


class Author(BaseModel):
    accountMembershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    comId: int = Field(alias='ndcId', title='Community ID', default=0)
    followersCount: int = Field(alias='membersCount', default=0)
    followingStatus: FollowingStatus = Field(default=FollowingStatus.NOT_FOLLOWING)
    frame: AvatarFrame = Field(alias='avatarFrame', default_factory=AvatarFrame)
    frameId: Optional[str] = Field(alias='avatarFrameId')
    icon: HttpUrl
    id: str = Field(alias='uid')
    isGlobal: bool = Field(default=True)
    isNicknameVerified: bool = Field(default=False)
    level: Optional[int]
    membershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    nickname: str
    reputation: Optional[int]
    role: Role = Field(default=Role.MEMBER)
    status: int = Field(default=0)

    if not TYPE_CHECKING:
        icon: Optional[HttpUrl]
        id: Optional[str]
        nickname: Optional[str]
