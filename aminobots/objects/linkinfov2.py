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
from typing import Optional, TYPE_CHECKING, Any
from pydantic import BaseModel, Field
from .community import Community
from .currentuserinfo import CurrentUserInfo
from .invitation import Invitation
from ..enums import ObjectType

__all__ = ('LinkInfoV2',)


class LinkInfo(BaseModel):
    comId: int = Field(alias='ndcId')
    fullPath: Optional[str]
    objectId: str
    objectType: ObjectType = Field(default=ObjectType.USER)
    shareURLFullPath: Optional[str]
    shareURLShortCode: Optional[str]
    shortCode: Optional[str]
    targetCode: Optional[int]

    if not TYPE_CHECKING:
        comId: Optional[int]
        objectId: Optional[str]


class Extensions(BaseModel):
    comId: int = property(lambda self: self.linkInfo.comId or self.community.id)
    community: Optional[Community] = Field(default_factory=Community)
    currentUser: Optional[CurrentUserInfo] = Field(alias='currentUserInfo', default_factory=CurrentUserInfo)
    invitation: Invitation = Field(default_factory=Invitation)
    invitationId: Optional[str]
    linkInfo: LinkInfo = Field(default_factory=LinkInfo)
    isCurrentUserJoined: bool = Field(default=False)


class LinkInfoV2(BaseModel):
    community: Optional[Community] = Field(default_factory=Community)
    extensions: Extensions = Field(default_factory=Extensions)
    invitation: Optional[Invitation] = Field(default_factory=Invitation)
    linkInfo: LinkInfo = Field(default_factory=LinkInfo)
    path: str = Field(title='NDC path')

    if not TYPE_CHECKING:
        path: Optional[str]
