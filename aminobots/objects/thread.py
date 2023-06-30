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
from pydantic import BaseModel, HttpUrl, Field, Json
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from .author import Author
from .media import Media
from .style import Style
from ..enums import (
    ChannelType,
    ChatType,
    JoinType,
    Language,
    MediaType,
    MembershipStatus,
    MessageType,
    Role
)

__all__ = ('Thread',)


class AliasTopic(BaseModel):
    pass


class Tab(BaseModel):
    pass


class SubTopic(BaseModel):
    pass


class UserAddedTopic(BaseModel):
    advancedCommunityStatus: int
    advancedStatus: int
    aliasTopicList: List[AliasTopic] = Field(default_factory=list)
    chatStatus: bool
    contentPoolId: Language = Field(default=Language.ENGLISH) # lang
    coverImage: Optional[HttpUrl]
    id: int = Field(alias='topicId')
    increaseId: int
    isAlias: bool = Field(default=False)
    isLocked: bool = Field(default=False)
    isOfficial: bool = Field(default=False)
    mappingScore: int = Field(alias='objectMappingScore')
    name: str
    scopeCid: int = Field(alias='scope', title='Scope Community ID')
    status: int = Field(default=0)
    source: int
    storyId: int
    style: Style = Field(default_factory=Style)
    subTopicList: List[SubTopic] = Field(default_factory=list)
    tabList: List[Tab] = Field(default_factory=list)
    visibility: int

    if not TYPE_CHECKING:
        advancedCommunityStatus: Optional[int]
        advancedStatus: Optional[int]
        chatStatus: Optional[bool]
        id: Optional[int]
        increaseId: Optional[int]
        mappingScore: Optional[int]
        name: Optional[str]
        scopeCid: Optional[int]
        source: Optional[int]
        storyId: Optional[int]
        visibility: Optional[int]


class Member(BaseModel):
    icon: HttpUrl
    id: str = Field(alias='uid')
    membershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    nickname: str
    role: Role = Field(default=Role.MEMBER)
    status: int = Field(default=0)

    if not TYPE_CHECKING:
        icon: Optional[HttpUrl]
        id: Optional[str]
        nickname: Optional[str]


class TipOption(BaseModel):
    icon: HttpUrl
    value: int

    if not TYPE_CHECKING:
        icon: Optional[HttpUrl]
        value: Optional[int]


class TipInfo(BaseModel):
    maxCoins: int = Field(alias='tipMaxCoin')
    minCoins: int = Field(alias='tipMinCoin')
    optionList: List[TipOption] = Field(alias='tipOptionList', default_factory=list)
    tippable: bool = Field(default=False)
    tippedCoins: float = Field(default=0.0)
    tippersCount: int = Field(default=0)

    if not TYPE_CHECKING:
        maxCoins: Optional[int]
        minCoins: Optional[int]


class LastMessageSummary(BaseModel):
    authorId: str = Field(alias='uid')
    content: Optional[str]
    createdTime: datetime
    id: str = Field(alias='messageId')
    isHidden: bool = Field(default=False)
    media: Optional[HttpUrl] = Field(alias='mediaValue')
    mediaType: MediaType = Field(default=MediaType.TEXT)
    type: MessageType = Field(default=MessageType.TEXT)

    if not TYPE_CHECKING:
        authorId: Optional[str]
        createdTime: Optional[datetime]
        id: Optional[str]
        media: Optional[HttpUrl]


class Extensions(BaseModel):
    announcement: Optional[str]
    pinAnnouncement: bool = Field(default=False)
    backgroundMediaList: List[Media] = Field(alias='bm', default_factory=list)
    bannedIdList: List[str] = Field(alias='bannedMemberUidList', default_factory=list)
    channelCreatedTime: Optional[datetime] = Field(alias='channelTypeLastCreatedTime')
    channelId: Optional[str] = Field(alias='avchatId')
    channelJoinType: Optional[JoinType] = Field(alias='vvChatJoinType', default=JoinType.OPEN)
    channelMemberIdList: List[str] = Field(alias='avchatMemberUidList', default_factory=list)
    channelType: ChannelType = Field(default=ChannelType.TEXT)
    coHosts: List[str] = Field(alias='coHost', default_factory=list)
    creatorId: str = Field(alias='creatorUid')
    fansOnly: bool = Field(default=False)
    language: Language = Field(Language.ENGLISH)
    membersCanInvite: bool = Field(default=True)
    membersUpdateTime: int = Field(alias='lastMembersSummaryUpdateTime')
    screeningRoomHostId: Optional[str] = Field(alias='screeningRoomHostUid')
    viewOnly: bool = Field(default=False)
    visibility: int

    if not TYPE_CHECKING:
        creatorId: Optional[str]
        membersUpdateTime: Optional[int]
        visibility: Optional[int]


class Thread(BaseModel):
    addedTopicList: List[UserAddedTopic] = Field(alias='userAddedTopicList', default_factory=list)
    alertOption: int
    coHosts: List[str] = property(lambda self: self.extensions.coHosts)
    condition: int
    comId: int = Field(alias='ndcId', default=0)
    createdTime: datetime
    description: Optional[str] = Field(alias='content')
    host: Author = Field(default_factory=Author)
    hostId: str = Field(alias='uid')
    hostMembershipStatus: MembershipStatus = Field(alias='membershipStatus', default=MembershipStatus.NONE)
    extensions: Extensions = Field(default_factory=Extensions)
    icon: HttpUrl
    id: str = Field(alias='threadId')
    isPinned: bool = Field(default=False)
    keywords: Optional[str] # seprarated by ','
    lastMessage: LastMessageSummary = Field(alias='lastMessageSummary', default_factory=LastMessageSummary)
    lastReadTime: Optional[datetime]
    latestActivityTime: Optional[datetime]
    membersSummary: List[Member] = Field(default_factory=list)
    membersCount: int = Field(default=0)
    membersQuota: int
    modifiedTime: Optional[datetime]
    needHidden: bool = Field(default=False)
    publishToGlobal: int # [0, 1]
    status: int = Field(default=0)
    strategyInfo: Json
    tip: TipInfo = Field(alias='tipInfo', default_factory=TipInfo)
    title: str
    type: ChatType = Field(default=ChatType.PUBLIC)

    if not TYPE_CHECKING:
        alertOption: Optional[int]
        condition: Optional[int]
        comId: Optional[int]
        createdTime: Optional[datetime]
        hostId: Optional[str]
        icon: Optional[HttpUrl]
        id: Optional[str]
        membersQuota: Optional[int]
        publishToGlobal: Optional[int]
        strategyInfo: Optional[Json]
        title: Optional[str]
