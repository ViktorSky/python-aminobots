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
from typing import Optional, Literal, TYPE_CHECKING
from datetime import datetime
from pydantic.color import Color
from pydantic import (
    BaseModel,
    HttpUrl,
    Field,
)
from .media import Media
from .author import Author
from ..enums import (
    CommunityStatus,
    FollowingStatus,
    Language,
    MembershipStatus,
    Role,
    JoinType
)

__all__ = ('Community',)


class ActiveInfo(BaseModel):
    pass


class Style(BaseModel):
    backgroundColor: Optional[str]


class UserAddedTopic(BaseModel):
    backgroundColor: Optional[str] = property(lambda self: self.style.backgroundColor)
    name: str
    style: Style = Field(default_factory=Style)
    topicId: int

    if not TYPE_CHECKING:
        name: Optional[str]
        topicId: Optional[int]


class FeedPage(BaseModel):
    status: int
    type: int

    if not TYPE_CHECKING:
        status: Optional[int]
        type: Optional[int]


class LeaderboardStyle(BaseModel):
    pass


class RankedMember(BaseModel):
    id: str
    level: Optional[int]
    reputation: Optional[int]
    title: str

    if not TYPE_CHECKING:
        id: Optional[str]
        title: Optional[str]


class AdvancedSettings(BaseModel):
    defaultRankingTypeInLeaderboard: int
    facebookAppIdList: list[str] = Field(default_factory=list)
    newsfeedPages: list[FeedPage] = Field(default_factory=list)
    frontPageLayout: int
    hasPendingReviewRequest: bool = Field(default=False)
    joinedBaselineCollectionIdList: list[str] = Field(default_factory=list)
    leaderboardStyle: Optional[LeaderboardStyle]
    pollMinFullBarVoteCount: int = Field(default=0)
    rankingTable: list[RankedMember] = Field(default_factory=list)
    welcomeMessageEnabled: Optional[bool] # updating
    welcomeMessageText: Optional[str]
    wikiEnabled: Optional[bool] = Field(alias='catalogEnabled')

    if not TYPE_CHECKING:
        defaultRankingTypeInLeaderboard: Optional[int]
        frontPageLayout: Optional[int]


class Agent(BaseModel):
    accountMembershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    comId: int = Field(alias='ndcId', default=0, title='Community ID')
    followersCount: int = Field(alias='membersCount', default=0)
    followingStatus: FollowingStatus = Field(default=FollowingStatus.NOT_FOLLOWING)
    icon: Optional[HttpUrl]
    id: str = Field(alias='uid')
    isGlobal: bool
    isNicknameVerified: bool = Field(default=False)
    level: Optional[int]
    membershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    nickname: str
    reputation: Optional[int]
    role: Role = Field(default=Role.AGENT)
    status: int = Field(default=0)

    if not TYPE_CHECKING:
        id: Optional[str]
        isGlobal: Optional[bool]
        nickname: Optional[str]


class Extensions(BaseModel):
    iTagIdList: list[int] = Field(default_factory=list)


class PageNavigation(BaseModel):
    id: str
    isStartPage: bool = Field(default=False)

    if not TYPE_CHECKING:
        id: Optional[str]


class HomePage(BaseModel):
    navigation: list[PageNavigation] = Field(default_factory=list)


class LeftSidePanelStyle(BaseModel):
    iconColor: Optional[Color]


class NavigationLevel(BaseModel):
    id: str

    if not TYPE_CHECKING:
        id: Optional[str]


class Navigation(BaseModel):
    level1: list[NavigationLevel] = Field(default_factory=list)
    level2: list[NavigationLevel] = Field(default_factory=list)


class LeftSidePanel(BaseModel):
    style: LeftSidePanelStyle = Field(default_factory=LeftSidePanelStyle)
    iconColor: Optional[str] = property(lambda self: self.style.iconColor)
    navigation: Navigation = Field(default_factory=Navigation)


class Appearance(BaseModel):
    homePage: HomePage = Field(default_factory=HomePage)
    leftSidePanel: LeftSidePanel = Field(default_factory=LeftSidePanel)


class WelcomeMessage(BaseModel):
    enabled: bool
    text: Optional[str]

    if not TYPE_CHECKING:
        enabled: Optional[bool]


class General(BaseModel):
    accountMembershipEnabled: bool = Field(default=False)
    disableLiveLayerActive: bool = Field(default=False)
    disableLiveLayerVisible: bool = Field(default=False)
    facebookAppIdList: list[str] = Field(default_factory=list)
    hasPendingReviewRequest: bool = Field(default=False)
    invitePermission: int
    joinedBaselineCollectionIdList: list[str] = Field(default_factory=list)
    joinedTopicIdList: list[int] = Field(default_factory=list)
    onlyAllowOfficialTag: bool = Field(default=False)
    premiumFeatureEnabled: bool = Field(default=False)
    videoUploadPolicy: int
    welcomeMessage: WelcomeMessage = Field(default_factory=WelcomeMessage)

    if not TYPE_CHECKING:
        invitePermission: Optional[int]
        videoUploadPolicy: Optional[int]


class PostPermission(BaseModel):
    minLevel: Optional[int]
    type: int # (anyone, minlevel, onlystaff)

    if not TYPE_CHECKING:
        type: Optional[int]


class PostPrivilege(BaseModel):
    enabled: bool = Field(default=False)
    minLevel: int = property(lambda self: self.permission.minLevel)
    permission: PostPermission = Field(alias='privilege', default_factory=PostPermission)


class CatalogModule(BaseModel):
    curationEnabled: bool = Field(default=False)
    enabled: bool = Field(default=False)
    privilege: PostPrivilege = Field(default_factory=PostPrivilege)


class AvChat(BaseModel):
    audioEnabled: bool = Field(default=False)
    audio2Enabled: bool =  Field(default=False)
    screeningRoomEnabled: bool = Field(default=False)
    videoEnabled: bool = Field(default=False)


class ChatModule(BaseModel):
    avChat: AvChat = Field(default_factory=AvChat)
    enabled: bool = Field(default=False)
    publicChat: PostPrivilege = Field(default_factory=PostPrivilege)
    publicChatEnabled: bool = property(lambda self: self.publicChat.enabled)
    spamProtectionEnabled: bool = Field(default=False)


class ExternalContentModule(BaseModel):
    enabled: bool = Field(default=False)


class FeaturedModule(BaseModel):
    enabled: bool = Field(default=False)
    feedLayout: Literal[1, 2, 3, 4, 5, 6] = Field(alias='layout')
    lockMember: bool = Field(default=False)
    memberEnabled: bool = Field(default=False)
    postEnabled: bool = Field(default=False) # Feature posts
    publicChatEnabled: bool = Field(alias='publicChatRoomEnabled', default=False)

    if not TYPE_CHECKING:
        feedLayout: Optional[int]


class InfluencerModule(BaseModel):
    enabled: bool = Field(default=False)
    lock: bool = Field(default=False)
    maxMonthlyFee: int = Field(alias='maxVipMonthlyFee', default=0)
    maxVipNumbers: int = Field(default=0)
    minMonthlyFee: int = Field(alias='minVipMonthlyFee', default=0)


class TopicCategoriesModule(BaseModel):
    enabled: bool = Field(default=False)


class PostType(BaseModel):
    blog: PostPrivilege = Field(default_factory=PostPrivilege)
    image: PostPrivilege = Field(default_factory=PostPrivilege)
    liveMode: PostPrivilege = Field(default_factory=PostPrivilege)
    poll: PostPrivilege = Field(default_factory=PostPrivilege)
    publicChat: PostPrivilege = Field(alias='publicChatRooms', default_factory=PostPrivilege)
    question: PostPrivilege = Field(default_factory=PostPrivilege)
    quiz: PostPrivilege = Field(default_factory=PostPrivilege)
    screeningRoom: PostPrivilege = Field(default_factory=PostPrivilege)
    story: PostPrivilege = Field(default_factory=PostPrivilege)
    webLink: PostPrivilege = Field(default_factory=PostPrivilege)
    wikiEntry: PostPrivilege = Field(alias='catalogEntry', default_factory=PostPrivilege)


class PostModule(BaseModel):
    blog: PostPrivilege = property(lambda self: self.postType.blog)
    enabled: bool = Field(default=False)
    image: PostPrivilege = property(lambda self: self.postType.image)
    liveMode: PostPrivilege = property(lambda self: self.postType.liveMode)
    poll: PostPrivilege = property(lambda self: self.postType.poll)
    publicChatRooms: PostPrivilege = property(lambda self: self.postType.publicChat)
    question: PostPrivilege = property(lambda self: self.postType.question)
    postType: PostType = Field(default_factory=PostType)
    quiz: PostPrivilege = property(lambda self: self.postType.quiz)
    screeningRoom: PostPrivilege = property(lambda self: self.postType.screeningRoom)
    story: PostPrivilege = property(lambda self: self.postType.story)
    webLink: PostPrivilege = property(lambda self: self.postType.webLink)
    wikiEntry: PostPrivilege = property(lambda self: self.postType.wikiEntry)


class Leaderboard(BaseModel):
    enabled: bool
    id: str
    style: list
    type: int

    if not TYPE_CHECKING:
        enabled: Optional[bool]
        id: Optional[str]
        style: Optional[list]
        type: Optional[int]


class RankingModule(BaseModel):
    defaultLeaderboardType: int
    enabled: bool
    leaderboardList: list[Leaderboard] = Field(default_factory=list)
    leaderboardEnabled: bool = Field(default=False)
    rankingTable: list[RankedMember] = Field(default_factory=list)

    if not TYPE_CHECKING:
        defaultLeaderboardType: Optional[int]
        enabled: Optional[bool]


class SharedFolderModule(BaseModel):
    albumManage: PostPrivilege = Field(alias='albumManagePrivilege', default_factory=PostPrivilege)
    albumManageMinLevel: Optional[int] = property(lambda self: self.albumManage.minLevel)
    enabled: bool = Field(default=False)
    upload: PostPrivilege = Field(alias='uploadPrivilege', default_factory=PostPrivilege)


class Module(BaseModel):
    chat: ChatModule = Field(default_factory=ChatModule)
    externalContent: ExternalContentModule = Field(default_factory=ExternalContentModule)
    featured: FeaturedModule = Field(default_factory=FeaturedModule)
    postCategories: TopicCategoriesModule = Field(alias='topicCategories', default_factory=TopicCategoriesModule)
    posts: PostModule = Field(alias='post', default_factory=PostModule)
    memberRanking: RankingModule = Field(alias='ranking', default_factory=RankingModule)
    sharedFolder: SharedFolderModule = Field(default_factory=SharedFolderModule)
    vip: InfluencerModule = Field(alias='influencer', default_factory=InfluencerModule)
    wiki: CatalogModule = Field(alias='catalog', default_factory=CatalogModule)


class TabEntry(BaseModel):
    alias: Optional[str]
    id: str
    url: HttpUrl

    if not TYPE_CHECKING:
        id: Optional[str]
        url: Optional[HttpUrl]


class Page(BaseModel):
    customList: list[TabEntry] = Field(default_factory=list)
    defaultList: list[TabEntry] = Field(default_factory=list)


class Configuration(BaseModel):
    appearance: Appearance = Field(default_factory=Appearance)
    general: General = Field(default_factory=General)
    module: Module = Field(default_factory=Module)
    page: Page = Field(default_factory=Page)


class ThemePack(BaseModel):
    color: Color = Field(alias='themeColor') # hex color code
    hash: str = Field(alias='themePackHash')
    revision: int = Field(alias='themePackRevision')
    url: HttpUrl = Field(alias='themePackUrl') # resource url (zip)

    if not TYPE_CHECKING:
        color: Optional[Color]
        hash: Optional[str]
        revision: Optional[int]
        url: Optional[HttpUrl]


class Community(BaseModel):
    activeInfo: ActiveInfo = Field(default_factory=ActiveInfo)
    userAddedTopicList: list[UserAddedTopic] = Field(default_factory=list)
    advancedSettings: AdvancedSettings = Field(default_factory=AdvancedSettings)
    agent: Agent = Field(default_factory=Agent)
    aminoId: str = Field(alias='endpoint')
    configuration: Configuration = Field(default_factory=Configuration)
    createdTime: datetime
    description: str = Field(alias='content')
    extensions: Extensions = Field(default_factory=Extensions)
    heat: float = Field(alias='communityHeat', default=0.0) # community activity bar
    icon: HttpUrl
    id: int = Field(alias='ndcId') # community id
    isStandaloneAppDeprecated: bool = Field(default=False)
    isStandaloneAppMonetizationEnabled: bool = Field(default=False)
    joinType: JoinType = Field(default=JoinType.OPEN)
    keywords: Optional[str] # separated by ','
    link: HttpUrl
    listedStatus: int
    mediaList: list[Media] = Field(default_factory=list) # MediaList object
    membersCount: int
    modifiedTime: Optional[datetime]
    name: str
    primaryLanguage: Language = Field(default=Language.ENGLISH)
    probationStatus: int
    promotionalMediaList: list[Media] = Field(default_factory=list) # MediaList object
    searchable: bool = Field(default=False)
    status: CommunityStatus = Field(default=CommunityStatus.OK)
    tagline: str
    themePack: ThemePack = Field(default_factory=ThemePack)
    templateId: int
    updatedTime: Optional[datetime]
    vipList: list[Author] = Field(alias='influencerList', default_factory=list)

    if not TYPE_CHECKING:
        aminoId: Optional[str]
        createdTime: Optional[datetime]
        description: Optional[str]
        icon: Optional[HttpUrl]
        id: Optional[int]
        link: Optional[HttpUrl]
        listedStatus: Optional[int]
        membersCount: Optional[int]
        name: Optional[str]
        probationStatus: Optional[int]
        tagline: Optional[str]
        templateId: Optional[int]
