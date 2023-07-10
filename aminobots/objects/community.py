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
from typing import Optional, Literal, List, TYPE_CHECKING
from datetime import datetime
from pydantic.color import Color
from pydantic import (
    BaseModel,
    AnyUrl,
    Field
)
from .media import Media
from .author import Author
from .validators import (
    bool_validator,
    list_validator,
    obj_validator
)
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
    backgroundColor: Optional[str] = Field(default=None)


class UserAddedTopic(BaseModel):
    backgroundColor: Optional[str] = property(lambda self: self.style.backgroundColor) # type: ignore
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
    defaultRankingTypeInLeaderboard: int = Field(default=0)
    facebookAppIdList: List[str] = Field(default_factory=list)
    newsfeedPages: List[FeedPage] = Field(default_factory=list)
    frontPageLayout: int = Field(default=1)
    hasPendingReviewRequest: bool = Field(default=False)
    joinedBaselineCollectionIdList: List[str] = Field(default_factory=list)
    leaderboardStyle: Optional[LeaderboardStyle] = Field(default=None)
    pollMinFullBarVoteCount: int = Field(default=0)
    rankingTable: List[RankedMember] = Field(default_factory=list)
    welcomeMessageEnabled: Optional[bool] = Field(default=None) # updating
    welcomeMessageText: Optional[str] = Field(default=None)
    wikiEnabled: Optional[bool] = Field(alias='catalogEnabled', default=False)

    _list_validator = list_validator('facebookAppIdList')

    if not TYPE_CHECKING:
        facebookAppIdList: Optional[List[str]]
        defaultRankingTypeInLeaderboard: Optional[int]
        frontPageLayout: Optional[int]


class Agent(Author):
    pass


class Extensions(BaseModel):
    iTagIdList: List[int] = Field(default_factory=list)


class PageNavigation(BaseModel):
    id: str
    isStartPage: bool = Field(default=False)

    if not TYPE_CHECKING:
        id: Optional[str]


class HomePage(BaseModel):
    navigation: List[PageNavigation] = Field(default_factory=list)


class LeftSidePanelStyle(BaseModel):
    iconColor: Optional[Color] = Field(default=None)


class NavigationLevel(BaseModel):
    id: str

    if not TYPE_CHECKING:
        id: Optional[str]


class Navigation(BaseModel):
    level1: List[NavigationLevel] = Field(default_factory=list)
    level2: List[NavigationLevel] = Field(default_factory=list)


class LeftSidePanel(BaseModel):
    style: LeftSidePanelStyle = Field(default_factory=LeftSidePanelStyle)
    iconColor: Optional[str] = property(lambda self: self.style.iconColor) # type: ignore
    navigation: Navigation = Field(default_factory=Navigation)


class Appearance(BaseModel):
    homePage: HomePage = Field(default_factory=HomePage)
    leftSidePanel: LeftSidePanel = Field(default_factory=LeftSidePanel)


class WelcomeMessage(BaseModel):
    enabled: bool = Field(default=False)
    text: Optional[str] = Field(default=None)

    _bool_validator = bool_validator('enabled')

    if not TYPE_CHECKING:
        enabled: Optional[bool]


class General(BaseModel):
    accountMembershipEnabled: bool = Field(default=False)
    disableLiveLayerActive: bool = Field(default=False)
    disableLiveLayerVisible: bool = Field(default=False)
    facebookAppIdList: List[str] = Field(default_factory=list)
    hasPendingReviewRequest: bool = Field(default=False)
    invitePermission: int = Field(default=0)
    joinedBaselineCollectionIdList: List[str] = Field(default_factory=list)
    joinedTopicIdList: List[int] = Field(default_factory=list)
    onlyAllowOfficialTag: bool = Field(default=False)
    premiumFeatureEnabled: bool = Field(default=False)
    videoUploadPolicy: int = Field(default=0)
    welcomeMessage: WelcomeMessage = Field(default_factory=WelcomeMessage)

    _list_validator = list_validator('facebookAppIdList')

    if not TYPE_CHECKING:
        facebookAppIdList: Optional[List[str]]
        invitePermission: Optional[int]
        videoUploadPolicy: Optional[int]


class PostPermission(BaseModel):
    minLevel: Optional[int] = Field(default=None)
    type: int = Field(default=0) # (anyone, minlevel, onlystaff)

    if not TYPE_CHECKING:
        type: Optional[int]


class PostPrivilege(BaseModel):
    enabled: bool = Field(default=False)
    minLevel: int = property(lambda self: self.permission.minLevel) # type: ignore
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
    publicChatEnabled: bool = property(lambda self: self.publicChat.enabled) # type: ignore
    spamProtectionEnabled: bool = Field(default=False)


class ExternalContentModule(BaseModel):
    enabled: bool = Field(default=False)


class FeaturedModule(BaseModel):
    enabled: bool = Field(default=False)
    feedLayout: Literal[1, 2, 3, 4, 5, 6] = Field(alias='layout', default=1)
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
    blog: PostPrivilege = property(lambda self: self.postType.blog) # type: ignore
    enabled: bool = Field(default=False)
    image: PostPrivilege = property(lambda self: self.postType.image) # type: ignore
    liveMode: PostPrivilege = property(lambda self: self.postType.liveMode) # type: ignore
    poll: PostPrivilege = property(lambda self: self.postType.poll) # type: ignore
    publicChatRooms: PostPrivilege = property(lambda self: self.postType.publicChat) # type: ignore
    question: PostPrivilege = property(lambda self: self.postType.question) # type: ignore
    postType: PostType = Field(default_factory=PostType)
    quiz: PostPrivilege = property(lambda self: self.postType.quiz) # type: ignore
    screeningRoom: PostPrivilege = property(lambda self: self.postType.screeningRoom) # type: ignore
    story: PostPrivilege = property(lambda self: self.postType.story) # type: ignore
    webLink: PostPrivilege = property(lambda self: self.postType.webLink) # type: ignore
    wikiEntry: PostPrivilege = property(lambda self: self.postType.wikiEntry) # type: ignore


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
    defaultLeaderboardType: int = Field(default=0)
    enabled: bool = Field(default=False)
    leaderboardList: List[Leaderboard] = Field(default_factory=list)
    leaderboardEnabled: bool = Field(default=False)
    rankingTable: List[RankedMember] = Field(default_factory=list)

    if not TYPE_CHECKING:
        defaultLeaderboardType: Optional[int]
        enabled: Optional[bool]


class SharedFolderModule(BaseModel):
    albumManage: PostPrivilege = Field(alias='albumManagePrivilege', default_factory=PostPrivilege)
    albumManageMinLevel: Optional[int] = property(lambda self: self.albumManage.minLevel) # type: ignore
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
    url: AnyUrl

    if not TYPE_CHECKING:
        id: Optional[str]
        url: Optional[AnyUrl]


class Page(BaseModel):
    customList: List[TabEntry] = Field(default_factory=list)
    defaultList: List[TabEntry] = Field(default_factory=list)


class Configuration(BaseModel):
    appearance: Appearance = Field(default_factory=Appearance)
    general: General = Field(default_factory=General)
    module: Module = Field(default_factory=Module)
    page: Page = Field(default_factory=Page)


class ThemePack(BaseModel):
    color: Color = Field(alias='themeColor', default=Color('#000000')) # hex color code
    hash: str = Field(alias='themePackHash', default=None)
    revision: int = Field(alias='themePackRevision', default=0)
    url: AnyUrl = Field(alias='themePackUrl', default=None) # resource url (zip)

    if not TYPE_CHECKING:
        color: Optional[Color]
        hash: Optional[str]
        revision: Optional[int]
        url: Optional[AnyUrl]


class Community(BaseModel):
    activeInfo: ActiveInfo = Field(default_factory=ActiveInfo)
    userAddedTopicList: List[UserAddedTopic] = Field(default_factory=list)
    advancedSettings: AdvancedSettings = Field(default_factory=AdvancedSettings)
    agent: Agent = Field(default_factory=Agent)
    aminoId: str = Field(alias='endpoint', default=None)
    configuration: Configuration = Field(default_factory=Configuration)
    createdTime: datetime = Field(default=None)
    description: Optional[str] = Field(alias='content', default=None)
    extensions: Extensions = Field(default_factory=Extensions)
    heat: float = Field(alias='communityHeat', default=0.0) # community activity bar
    icon: AnyUrl = Field(default=None)
    id: int = Field(alias='ndcId', default=0) # community id
    isStandaloneAppDeprecated: bool = Field(default=False)
    isStandaloneAppMonetizationEnabled: bool = Field(default=False)
    joinType: Optional[JoinType] = Field(default=JoinType.OPEN)
    keywords: Optional[str] = Field(default=None) # separated by ','
    link: AnyUrl = Field(default=None)
    listedStatus: int = Field(default=0)
    mediaList: List[Media] = Field(default_factory=list) # MediaList object
    membersCount: int = Field(default=0)
    modifiedTime: Optional[datetime] = Field(default=None)
    name: str = Field(default=None)
    primaryLanguage: Language = Field(default=Language.ENGLISH)
    probationStatus: int = Field(default=0)
    promotionalMediaList: List[Media] = Field(default_factory=list) # MediaList object
    searchable: bool = Field(default=False)
    status: CommunityStatus = Field(default=CommunityStatus.OK)
    tagline: str = Field(default=None)
    themePack: ThemePack = Field(default_factory=ThemePack)
    templateId: int = Field(default=0)
    updatedTime: Optional[datetime] = Field(default=None)
    vipList: List[Author] = Field(alias='influencerList', default_factory=list)

    _obj_validator = obj_validator(Extensions, 'extensions')
    _list_validator = list_validator('mediaList', 'userAddedTopicList', 'promotionalMediaList')

    if not TYPE_CHECKING:
        aminoId: Optional[str]
        createdTime: Optional[datetime]
        extensions: Optional[Extensions]
        icon: Optional[AnyUrl]
        id: Optional[int]
        link: Optional[AnyUrl]
        listedStatus: Optional[int]
        mediaList: Optional[List[Media]]
        membersCount: Optional[int]
        name: Optional[str]
        probationStatus: Optional[int]
        promotionalMediaList: Optional[List[Media]]
        tagline: Optional[str]
        templateId: Optional[int]
        userAddedTopicList: Optional[List[UserAddedTopic]]
