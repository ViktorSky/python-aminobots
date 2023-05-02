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
from . import userprofilelist
import dataclasses
import functools
import typing

__all__ = ('Community',)


@dataclasses.dataclass(repr=False)
class ActiveInfo:
    """Represent Activity info.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.

    """
    json: dict


@dataclasses.dataclass(repr=False)
class Style:
    """Represent the community style object.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    backgroundColor: List[:class:`str`]
        Topics background color.

    """
    json: typing.List[dict]

    @functools.cached_property
    def backgroundColor(self) -> typing.List[str]:
        """Topic background color."""
        return [s.get("backgroundColor") for s in self.json]


@dataclasses.dataclass(repr=False)
class AddedTopic:
    """Represent a list of added topic in community.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    backgroundColor: List[:class:`str`]
        Topic background color.
    name: List[:class:`str`]
        Topic name.
    style: :class:`Style`
        Added topic style object.
    topicId: List[:class:`int`]
        Topic id.

    """
    json: typing.List[dict]

    @functools.cached_property
    def backgroundColor(self) -> typing.List[str]:
        """Hex color code."""
        return self.style.backgroundColor

    @functools.cached_property
    def name(self) -> typing.List[str]:
        """Topic name."""
        return [at.get("name") for at in self.json]

    @functools.cached_property
    def style(self) -> Style:
        """Style object."""
        return Style([at.get("style") or {} for at in self.json])

    @functools.cached_property
    def topicId(self) -> typing.List[int]:
        """Topic id."""
        return [at.get("topicId") for at in self.json]


@dataclasses.dataclass(repr=False)
class FeedPageList:
    """Represent the community feed pages.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    status: List[:class:`int`]
        ...
    type: List[:class:`int`]

    """
    json: typing.List[dict]

    @functools.cached_property
    def status(self) -> typing.List[int]:
        return [fp.get("status") for fp in self.json]

    @functools.cached_property
    def type(self):
        return [fp.get("type") for fp in self.json]


@dataclasses.dataclass(repr=False)
class RankingTable:
    """Represent the community ranking table.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    id: List[:class:`str`]
        ...
    level: List[:class:`int`]
        ...
    reputation: List[:class:`int`]
        ...
    title: str[:class:`str`]
        ...

    """
    json: typing.List[dict]

    @functools.cached_property
    def id(self) -> typing.List[str]:
        return [rtl.get("id") for rtl in self.json]

    @functools.cached_property
    def level(self) -> typing.List[int]:
        return [rtl.get("level") for rtl in self.json]

    @functools.cached_property
    def reputation(self) -> typing.List[int]:
        return [rtl.get("reputation") for rtl in self.json]

    @functools.cached_property
    def title(self) -> typing.List[str]:
        return [rtl.get("title") for rtl in self.json]


@dataclasses.dataclass(repr=False)
class AdvancedSettings:
    """Represent the advanced settings of community.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    catalogEnabled: :class:`bool`
        ...
    defaultRankingTypeInLeaderboard: :class:`int`
        ...
    facebookAppIdList: :class:`list`
        ...
    feedPages: :class:`FeedPageList`
        ...
    frontPageLayout: :class:`int`
        ...
    hasPendingReviewRequest: :class:`bool`
        ...
    joinedBaselineCollectionIdList: :class:`list`
        ...
    leaderboardStyle: :class:`dict`
        ...
    pollMinFullBarVoteCount: :calss:`int`
        ...
    rankingTable: :class:`RankingTable`
        ...
    welcomeMessageEnabled: :class:`bool`
        ...
    welcomeMessage: :class:`str`
        ...

    """
    json: dict

    @functools.cached_property
    def catalogEnabled(self) -> typing.Optional[bool]:
        return self.json.get("catalogEnabled")

    @functools.cached_property
    def defaultRankingTypeInLeaderboard(self) -> int:
        return self.json.get("defaultRankingTypeInLeaderboard")

    @functools.cached_property
    def facebookAppIdList(self) -> list:
        return self.json.get("facebookAppIdList") or []

    @functools.cached_property
    def feedPages(self) -> FeedPageList:
        return FeedPageList(self.json.get("newsfeedPages") or [])

    @functools.cached_property
    def frontPageLayout(self) -> int:
        return self.json.get("frontPageLayout")

    @functools.cached_property
    def hasPendingReviewRequest(self) -> typing.Optional[bool]:
        return self.json.get("hasPendingReviewRequest")

    @functools.cached_property
    def joinedBaselineCollectionIdList(self) -> list:
        return self.json.get("joinedBaselineCollectionIdList") or []

    @functools.cached_property
    def leaderboardStyle(self) -> dict:  # ...
        return self.json.get("leaderboardStyle") or {}

    @functools.cached_property
    def pollMinFullBarVoteCount(self) -> int:
        return self.json.get("pollMinFullBarVoteCount")

    @functools.cached_property
    def rankingTable(self) -> RankingTable:
        return RankingTable(self.json.get("rankingTable") or [])

    @functools.cached_property
    def welcomeMessageEnabled(self) -> typing.Optional[bool]:
        return self.json.get("welcomeMessageEnabled")

    @functools.cached_property
    def welcomeMessage(self) -> typing.Optional[str]:
        return self.json.get("welcomeMessageText")





@dataclasses.dataclass(repr=False)
class Agent:
    """Represent a community user agent profile.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    accountMembershipStatus: :class:`int`
        ...
    comId: :class:`int`
        Community id.
    followersCount: :class:`int`
        User followers count.
    followingStatus: :class:`int`
        User following status.
    icon: :class:`str`
        User icon url.
    id: :class:`str`
        User id.
    isGlobal: :class:`bool`
        Is Global or community profile.
    level: :class:`int`
        Community user level.
    membershipStatus: :class:`int`
        User membership status.
    nickname: :class:`str`
        User nickname.
    nicknameVerified: :class:`bool`
        Nickname verified.
    reputation: :class:`int`
        Community user reputation.
    role: :class:`int`
        Community user role.
    status: :class:`int`
        User status.

    """
    json: dict

    @functools.cached_property
    def accountMembershipStatus(self) -> int:
        return self.json.get("accountMembershipStatus")

    @functools.cached_property
    def comId(self) -> typing.Optional[int]:
        """Community id."""
        return self.json.get("ndcId")

    @functools.cached_property
    def followersCount(self) -> int:
        """User followers count."""
        return self.json.get("membersCount")

    @functools.cached_property
    def followingStatus(self) -> int:
        """User following status."""
        return self.json.get("followingStatus")

    @functools.cached_property
    def icon(self) -> typing.Optional[str]:
        """User icon url."""
        return self.json.get("icon")

    @functools.cached_property
    def id(self) -> str:
        """User id."""
        return self.json.get("uid")

    @functools.cached_property
    def isGlobal(self) -> bool:
        """Is Global or Community profile"""
        return self.json.get("isGlobal")

    @functools.cached_property
    def level(self) -> int:
        """Community user level."""
        return self.json.get("level")

    @functools.cached_property
    def membershipStatus(self) -> int:
        """User membership status."""
        return self.json.get("membershipStatus")

    @functools.cached_property
    def nickname(self) -> str:
        """User nickname"""
        return self.json.get("nickname")

    @functools.cached_property
    def nicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @functools.cached_property
    def reputation(self) -> typing.Optional[int]:
        """Community user reputation."""
        return self.json.get("reputation") or 0

    @functools.cached_property
    def role(self) -> int:
        """Community user role."""
        return self.json.get("role") or 111

    @functools.cached_property
    def status(self) -> int:
        return self.json.get("status")


@dataclasses.dataclass(repr=False)
class Extensions:
    """Represent the community extensions.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.

    """
    json: dict

    @functools.cached_property
    def iTagIdList(self) -> typing.List[int]:
        return self.json.get('iTagIdList') or []


@dataclasses.dataclass(repr=False)
class HomeNavigationList:
    """Represent the home page navigation.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    id: List[:class:`str`]
        Navigation page id.
    isStartPage: Optional[:class:`bool`]
        ...

    """
    json: typing.List[dict]

    @functools.cached_property
    def id(self) -> typing.List[str]:
        """Navigation page id."""
        return [nl.get("id") for nl in self.json]

    @functools.cached_property
    def isStartPage(self) -> typing.List[typing.Optional[bool]]:
        """Is start page."""
        return [nl.get("isStartPage") for nl in self.json]


@dataclasses.dataclass(repr=False)
class HomePage:
    """Represent the home page configuration.

    json: :class:`dict`
        The raw API data.
    id: List[:class:`str`]
        Navigation page id.
    isStartPage: List[:class:`bool`]
        Is start page.
    navigation: :class:`HomeNavigationList`
        Home page navigation object.

    """
    json: dict

    @functools.cached_property
    def id(self) -> typing.List[str]:
        """Navigation page id."""
        return self.navigation.id

    @functools.cached_property
    def isStartPage(self) -> typing.List[typing.Optional[bool]]:
        """Is start page."""
        return self.navigation.isStartPage

    @functools.cached_property
    def navigation(self) -> HomeNavigationList:
        """Home page navigation."""
        return HomeNavigationList(self.json.get("navigation") or [])



@dataclasses.dataclass(repr=False)
class LeftSidePanelStyle:
    """Represent the Left side panel style.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    iconColor: :class:`str`
        Hex color code.

    """
    json: dict

    @functools.cached_property
    def iconColor(self) -> typing.Optional[str]:
        return self.json.get("iconColor")


@dataclasses.dataclass(repr=False)
class NavigationLevelList:
    """Represent a community navigation level.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    id: List[:class:`str`]
        ...

    """
    json: typing.List[dict]

    @functools.cached_property
    def id(self) -> typing.List[str]:
        return [ll.get("id") for ll in self.json]


@dataclasses.dataclass(repr=False)
class Navigation:
    """Represent the community left side panel navigation

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    level1: :class:`NavigationLevelList`
        ...
    level1Ids: List[:class:`str`]
        ...
    level2: :class:`NavigationLevelList`
        ...
    level2Ids: List[:class:`str`]
        ...

    """
    json: dict

    @functools.cached_property
    def level1(self) -> NavigationLevelList:
        return NavigationLevelList(self.json.get("level1") or [])

    @functools.cached_property
    def level1Ids(self) -> typing.List[str]:
        return self.level1.id

    @functools.cached_property
    def level2(self) -> NavigationLevelList:
        return NavigationLevelList(self.json.get("level2") or [])

    @functools.cached_property
    def level2Ids(self) -> typing.List[str]:
        return self.level2.id


@dataclasses.dataclass(repr=False)
class LeftSidePanel:
    """Represent the Left side panel

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    iconColor: :class:`str`
        Hex color code.
    navigation: :class:`Navigation`
        Naigation object.
    style: :class:`Style`
        Panel style.

    """
    json: dict

    @functools.cached_property
    def iconColor(self) -> typing.Optional[str]:
        """Panel icon color."""
        return self.style.iconColor

    @functools.cached_property
    def navigation(self) -> Navigation:
        """Panel navigation configuration."""
        return Navigation(self.json.get("navigation") or {})

    @functools.cached_property
    def style(self) -> LeftSidePanelStyle:
        """Panel style."""
        return LeftSidePanelStyle(self.json.get("style") or {})


@dataclasses.dataclass(repr=False)
class Appearance:
    """Represent the community appearance configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    homePage: :class:`HomePage`
        Homepage appearance configuration.
    leftSidePanel: :class:`LeftSidePanel`
        Left side panel configuation.

    """
    json: dict

    @functools.cached_property
    def homePage(self) -> HomePage:
        return HomePage(self.json.get("homePage") or {})

    @functools.cached_property
    def leftSidePanel(self) -> LeftSidePanel:
        return LeftSidePanel(self.json.get("leftSidePanel") or {})


@dataclasses.dataclass(repr=False)
class WelcomeMessage:
    """Represent the community welcome message configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    enabled: :class:`bool`
        Welcome message enabled.
    text: Optional[:class:`str`]
        Welcome message value.

    """
    json: dict

    @functools.cached_property
    def enabled(self) -> typing.Optional[bool]:
        """Welcome message enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def text(self) -> typing.Optional[str]:
        """Welcome message value."""
        return self.json.get("text")


@dataclasses.dataclass(repr=False)
class General:
    """Represent the community general configuration.

    Attributes
    ----------
    json
    accountMembershipEnabled: :class:`bool`
        ...
    disableLiveLayerActive: :class:`bool`
        ...
    disableLiveLayerVisible: :class:`bool`
        ...
    facebookAppIdList: List[:class:`str`]
        ...
    hasPendingReviewRequest: :class:`bool`
        ...
    invitePermission: :class:`int`
        ...
    joinedBaselineCollectionIdList: :class:`list`
        ...
    joinedTopicIdList: :class:`list`
        ...
    onlyAllowOfficialTag: :class:`bool`
        ...
    premiumFeatureEnabled :class:`bool`
        ...
    videoUploadPolicy: :class:`bool`
        ...
    welcomeMessage: :class:`WelcomeMessage`
        Community welcome message configuration.

    """
    json: dict

    @functools.cached_property
    def accountMembershipEnabled(self) -> bool:
        return self.json.get("accountMembershipEnabled")

    @functools.cached_property
    def disableLiveLayerActive(self) -> bool:
        return self.json.get("disableLiveLayerActive")

    @functools.cached_property
    def disableLiveLayerVisible(self) -> bool:
        return self.json.get("disableLiveLayerVisible")

    @functools.cached_property
    def facebookAppIdList(self) -> list:
        return self.json.get("facebookAppIdList") or []

    @functools.cached_property
    def hasPendingReviewRequest(self) -> bool:
        return self.json.get("hasPendingReviewRequest")

    @functools.cached_property
    def invitePermission(self) -> int:
        return self.json.get("invitePermission")

    @functools.cached_property
    def joinedBaselineCollectionIdList(self) -> list:
        return self.json.get("joinedBaselineCollectionIdList") or []

    @functools.cached_property
    def joinedTopicIdList(self):
        return self.json.get("joinedTopicIdList") or []

    @functools.cached_property
    def onlyAllowOfficialTag(self) -> bool:
        return self.json.get("onlyAllowOfficialTag")

    @functools.cached_property
    def premiumFeatureEnabled(self) -> bool:
        return self.json.get("premiumFeatureEnabled")

    @functools.cached_property
    def videoUploadPolicy(self) -> int:
        return self.json.get("videoUploadPolicy")

    @functools.cached_property
    def welcomeMessage(self) -> WelcomeMessage:
        return WelcomeMessage(self.json.get("welcomeMessage") or {})


@dataclasses.dataclass(repr=False)
class PostPermission:
    """Represent the community post privilege configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    minLevel: Optional[:class:`int`]
        Min user level.
    type: :class:`int`
        Posting permission.

    """
    json: dict

    @functools.cached_property
    def minLevel(self) -> typing.Optional[typing.Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]]:
        """Min user level."""
        return self.json.get("minLevel") or 0

    @functools.cached_property
    def type(self) -> int:
        """Posting permission. (anyone, minlevel, onlystaff)"""
        return self.json.get("type")


@dataclasses.dataclass(repr=False)
class PostPrivilege:
    """Represent the community post privilege.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    enabled: :class:`bool`
        Post type enabled.
    minLevel: Optional[:class:`int`]
        Min user level.
    permission: :class:`PostPermission`
        Posting permission.

    """
    json: dict

    @functools.cached_property
    def enabled(self) -> bool:
        """Post type enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def minLevel(self) -> int:
        """Min user level."""
        return self.permission.minLevel

    @functools.cached_property
    def permission(self) -> PostPermission:
        """Posting permission."""
        return PostPermission(self.json.get("privilege") or {})


@dataclasses.dataclass(repr=False)
class CatalogModule:
    """Represent the community wiki module configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    curationEnabled: :clas:`bool`
        Wiki curation enabled.
    enabled: :class:`bool`
        Catalog module enabled.
    Privilege: :class:`Privilege`
        Catalog Privilege.

    """
    json: dict

    @functools.cached_property
    def curationEnabled(self) -> bool:
        """Wiki curation enabled."""
        return self.json.get("curationEnabled")

    @functools.cached_property
    def enabled(self) -> bool:
        """Wiki enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def privilege(self):
        """Wiki privilege."""
        return PostPrivilege(self.json.get("privilege") or {})


@dataclasses.dataclass(repr=False)
class AvChat:
    """Represent a live chat configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    audioEnabled: :class:`bool`
        Voice chat enabled.
    audio2Enabled
        ...
    screeningRoomEnabled: :class:`bool`
        Screeningroom enabled.
    videoEnabled: :class:`bool`
        Stream chat enabled.

    """
    json: dict

    @functools.cached_property
    def audioEnabled(self) -> bool:
        return self.json.get("audioEnabled")

    @functools.cached_property
    def audio2Enabled(self) -> bool:
        return self.json.get("audio2Enabled")

    @functools.cached_property
    def screeningRoomEnabled(self) -> bool:
        return self.json.get("screeningRoomEnabled")

    @functools.cached_property
    def videoEnabled(self) -> bool:
        """Stream chat enabled."""
        return self.json.get("videoEnabled")


@dataclasses.dataclass(repr=False)
class ChatModule:
    """Represent the community chat module configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    avChat: :class:`AvChat`
        Live chat configuration.
    enabled: :clas:`bool`
        Chat module enabled.
    publicChat: :class:`PostPrivilege`
        Public chat Privileges.
    publicChatEnabled: :class:`bool`
        Public chat enabled.
    spamProtectionEnabled: :class:`bool`
        Chat text spam protection enabled.

    """
    json: dict

    @functools.cached_property
    def avChat(self) -> AvChat:
        """Live chat configuration."""
        return AvChat(self.json.get("avChat") or {})

    @functools.cached_property
    def enabled(self) -> bool:
        """Chat module enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def publicChat(self) -> PostPrivilege:
        """Public chat Privileges."""
        return PostPrivilege(self.json.get("publicChat") or {})

    @functools.cached_property
    def publicChatEnabled(self):
        """Public chat enabled."""
        return self.publicChat.enabled

    @functools.cached_property
    def spamProtectionEnabled(self) -> bool:
        """Chat text spam protection enabled."""
        return self.json.get("spamProtectionEnabled")


@dataclasses.dataclass(repr=False)
class ExternalContentModule:
    """Represent the community external content module.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    enabled: :class:`bool`
        External content enabled.

    """
    json: dict

    @functools.cached_property
    def enabled(self) -> bool:
        """External content enabled."""
        return self.json.get("enabled")


@dataclasses.dataclass(repr=False)
class FeaturedModule:
    """Represent community member featured module.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    enabled: :class:`bool`
        Featured module enabled.
    feedLayout: :class:`int`
        Featured feed layout.
    lockMember: :class:`bool`
        ...
    memberEnabled: :class:`bool`
        Feature members.
    postEnabled: :clas:`bool`
        Feature posts.
    publicChatEnabled: :class:`bool`
        Feature public chatrooms.

    """
    json: dict

    @functools.cached_property
    def enabled(self) -> bool:
        """Featured moduel enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def feedLayout(self) -> typing.Literal[1, 2, 3, 4, 5, 6]:
        """Feature feed layout."""
        return self.json.get("layout")

    @functools.cached_property
    def lockMember(self) -> bool:
        """..."""
        return self.json.get("lockMember")

    @functools.cached_property
    def memberEnabled(self) -> bool:
        """Feature members."""
        return self.json.get("memberEnabled")

    @functools.cached_property
    def postEnabled(self) -> bool:
        """Feature posts."""
        return self.json.get("postEnabled")

    @functools.cached_property
    def publicChatEnabled(self) -> bool:
        """Feature public chatrooms."""
        return self.json.get("publicChatRoomEnabled")


@dataclasses.dataclass(repr=False)
class InfluencerModule:
    """Represent the vip module of Amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    enabled: :class:`bool`
        Vip module enabled.
    lock: :class:`bool`
        ...
    maxMonthlyFee: :class:`int`
        Max monthly fee price.
    maxVipNumbers: :class:`int`
        Max vip member numbers.
    minMonthlyFee: :class:`int`
        Min monthly fee price.

    """
    json: dict

    @functools.cached_property
    def enabled(self) -> bool:
        """Vip module enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def lock(self) -> bool:
        """Locked module."""
        return self.json.get("lock")

    @functools.cached_property
    def maxMonthlyFee(self) -> int:
        """Max monthly fee price."""
        return self.json.get("maxVipMonthlyFee")

    @functools.cached_property
    def maxVipNumbers(self) -> int:
        """Max vip member numbers."""
        return self.json.get("maxVipNumbers")

    @functools.cached_property
    def minMonthlyFee(self) -> int:
        """Min monthly fee price."""
        return self.json.get("minVipMonthlyFee")


@dataclasses.dataclass(repr=False)
class TopicCategoriesModule:
    """Represent the community post categories module.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    enabled: :class:`bool`
        Post categories module enabled.

    """
    json: dict

    @functools.cached_property
    def enabled(self) -> bool:
        """Post categories module enabled."""
        return self.json.get("enabled")


@dataclasses.dataclass(repr=False)
class Post:
    """Represent the post module post types.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    blog :class:`PostPrivilege`
        Blog posting privileges.
    image: :class:`PostPrivilege`
        Image posting privileges.
    liveMode: :class:`PostPrivilege`
        Live mode posting privileges.
    poll: :class:`PostPrivilege`
        Poll posting privileges.
    publicChat: :class:`PostPrivilege`
        Public chat posting privileges.
    question: :class:`PostPrivilege`
        Question posting privileges.
    quiz: :class:`PostPrivilege`
        Quiz posting privileges.
    screeningRoom: :class:`PostPrivilege`
        Screening room posting privileges.
    story: :class:`PostPrivilege`
        Story posting privileges.
    webLink: :class:`PostPrivilege`
        Web link posting privileges.
    wikiEntry: :class:`PostPrivilege`
        Wiki entry posting privileges.

    """
    json: dict

    @functools.cached_property
    def blog(self) -> PostPrivilege:
        """Blog posting privileges"""
        return PostPrivilege(self.json.get("blog") or {})

    @functools.cached_property
    def image(self) -> PostPrivilege:
        """Image posting privileges."""
        return PostPrivilege(self.json.get("image") or {})

    @functools.cached_property
    def liveMode(self) -> PostPrivilege:
        """Live mode posting privileges."""
        return PostPrivilege(self.json.get("liveMode") or {})

    @functools.cached_property
    def poll(self) -> PostPrivilege:
        """Poll posting privileges."""
        return PostPrivilege(self.json.get("poll") or {})

    @functools.cached_property
    def publicChat(self) -> PostPrivilege:
        """Public chat posting privileges."""
        return PostPrivilege(self.json.get("publicChatRooms") or {})

    @functools.cached_property
    def question(self) -> PostPrivilege:
        """Question posting privileges."""
        return PostPrivilege(self.json.get("question") or {})

    @functools.cached_property
    def quiz(self) -> PostPrivilege:
        """Quiz posting privileges."""
        return PostPrivilege(self.json.get("quiz") or {})

    @functools.cached_property
    def screeningRoom(self) -> PostPrivilege:
        """Screening room posting privileges."""
        return PostPrivilege(self.json.get("screeningRoom") or {})

    @functools.cached_property
    def story(self) -> PostPrivilege:
        """Story posting privileges."""
        return PostPrivilege(self.json.get("story") or {})

    @functools.cached_property
    def webLink(self) -> PostPrivilege:
        """Web link posting privileges."""
        return PostPrivilege(self.json.get("webLink") or {})

    @functools.cached_property
    def wikiEntry(self) -> PostPrivilege:
        """Wiki entry posting privileges."""
        return PostPrivilege(self.json.get("catalogEntry") or {})


@dataclasses.dataclass(repr=False)
class PostModule:
    """Represent the community posts module.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    blog: :class:`PostPrivilege`
        Blog posts.
    enabled: :class:`bool`
        Post module enabled.
    image: :class:`PostPrivilege`
        Image posts.
    liveMode: :class:`PostPrivilege`
        Live mode posts.
    poll: :class:`PostPrivilege`
        Poll posts.
    publicChat: :class:`PostPrivilege`
        Public chat posts.
    question: :class:`PostPrivilege`
        Question posts.
    postType: :class:`PostType`
        Post types.
    quiz: :class:`PostPrivilege`
        Quiz posts.
    screeningRoom: :class:`PostPrivilege`
        Screening room posts.
    story: :class:`PostPrivilege`
        Story posts.
    webLink: :class:`PostPrivilege`
        Web link posts.
    wikiEntry: :class:`PostPrivilege`
        Wiki posts.

    """
    json: dict

    @functools.cached_property
    def blog(self) -> PostPrivilege:
        """Blog posts."""
        return self.postType.blog

    @functools.cached_property
    def enabled(self) -> bool:
        """Post module enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def image(self) -> PostPrivilege:
        """Image posts."""
        return self.postType.image

    @functools.cached_property
    def liveMode(self) -> PostPrivilege:
        """Live mode posts."""
        return self.postType.liveMode

    @functools.cached_property
    def poll(self) -> PostPrivilege:
        """Poll posts."""
        return self.postType.poll

    @functools.cached_property
    def publicChat(self) -> PostPrivilege:
        """Public chat posts."""
        return self.postType.publicChat

    @functools.cached_property
    def question(self) -> PostPrivilege:
        """Question posts."""
        return self.postType.question

    @functools.cached_property
    def postType(self) -> Post:
        """Post types."""
        return Post(self.json.get("postType") or {})

    @functools.cached_property
    def quiz(self) -> PostPrivilege:
        """Quiz posts."""
        return self.postType.quiz

    @functools.cached_property
    def screeningRoom(self) -> PostPrivilege:
        """Screening room posts."""
        return self.postType.screeningRoom

    @functools.cached_property
    def story(self) -> PostPrivilege:
        """Story posts."""
        return self.postType.story

    @functools.cached_property
    def webLink(self) -> PostPrivilege:
        """Web link posts."""
        return self.postType.webLink

    @functools.cached_property
    def wikiEntry(self) -> PostPrivilege:
        """Wiki entry posts."""
        return self.postType.wikiEntry


@dataclasses.dataclass(repr=False)
class Leaderboard:
    """Represent the community leaderboard.

    Attributes
    ----------
    json: List[:class:`dict`]
    enabled: List[:class:`bool`]
        ...
    id: List[:class:`str`]
        ...
    style: List[Optional[:class:`str`]]
        ...
    type: List[:class:`int`]
        ...

    """
    json: typing.List[dict]

    @functools.cached_property
    def enabled(self) -> typing.List[bool]:
        return [lb.get("enabled") for lb in self.json]

    @functools.cached_property
    def id(self) -> typing.List[str]:
        return [lb.get("id") for lb in self.json]

    @functools.cached_property
    def style(self) -> typing.List[typing.Optional[str]]:
        return [lb.get("style") for lb in self.json]

    @functools.cached_property
    def type(self) -> typing.List[int]:
        return [lb.get("type") for lb in self.json]


@dataclasses.dataclass(repr=False)
class RankingModule:
    """Represent the community member ranking module.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    defaultLeaderboardType: :class:`int`
        
    enabled: :class:`bool`
        Member ranking module enabled.
    leaderboard: :class:`Leaderboard`
        Community leaderboard.
    leaderboardEnabled: :class:`bool`
        Community leaderboard enabled.
    rankingTable: :class:`RankingTable`
        Community ranking table.

    """
    json: dict

    @functools.cached_property
    def defaultLeaderboardType(self) -> int:
        return self.json.get("defaultLeaderboardType")

    @functools.cached_property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @functools.cached_property
    def leaderboard(self) -> Leaderboard:
        return Leaderboard(self.json.get("leaderboardList") or [])

    @functools.cached_property
    def leaderboardEnabled(self) -> bool:
        return self.json.get("leaderboardEnabled")

    @functools.cached_property
    def rankingTable(self) -> RankingTable:
        return RankingTable(self.json.get("rankingTable") or [])


@dataclasses.dataclass(repr=False)
class SharedFolderModule:
    """Represent the community shared folder module.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    albumManage: :class:`Privilege`
        Album manage privilege.
    albumManageMinLevel: Optional[:class:`int`]
        Minimum user level manage albums.
    enabled: :class:`bool`
        Shared folder module enabled.
    upload: :class:`Privilege`
        Uploading privilege.

    """
    json: dict

    @functools.cached_property
    def albumManage(self) -> PostPrivilege:
        """Album manage privilege."""
        return PostPrivilege(self.json.get("albumManagePrivilege") or {})

    @functools.cached_property
    def albumManageMinLevel(self) -> typing.Optional[int]:
        """Minimum user level for manage albums"""
        return self.albumManage.minLevel

    @functools.cached_property
    def enabled(self) -> bool:
        """Shared folder module enabled."""
        return self.json.get("enabled")

    @functools.cached_property
    def upload(self) -> PostPrivilege:
        """Uploading privilege."""
        return PostPrivilege(self.json.get("uploadPrivilege") or {})


@dataclasses.dataclass(repr=False)
class Module:
    """Represent the community module configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    chat: :class:`ChatModule`
        Community chat module.
    externalContent: :class:`ExternalContentModule`
        Community external content.
    featured: :class:`FeaturedModule`
        Community featured module.
    vip: :class:`InfluencerModule`
        Community vip module.
    postCategories: :class:`TopicCategoriesModule`
        Community post categories module.
    posts: :class:`PostModule`
        Community post module.
    ranking: :class:`RankingModule`
        Community member ranking module.
    sharedFolder: :class:`SharedFolderModule`
        Community Shared folder module.
    wiki: :class:`CatalogModule`
        Community wiki module.

    """
    json: dict

    @functools.cached_property
    def chat(self) -> ChatModule:
        """Community chat module."""
        return ChatModule(self.json.get("chat") or {})

    @functools.cached_property
    def externalContent(self) -> ExternalContentModule:
        """Community external content module."""
        return ExternalContentModule(self.json.get("externalContent") or {})

    @functools.cached_property
    def featured(self) -> FeaturedModule:
        """Community featured module."""
        return FeaturedModule(self.json.get("featured") or {})

    @functools.cached_property
    def vip(self) -> InfluencerModule:
        """Communiry vip module."""
        return InfluencerModule(self.json.get("influencer") or {})

    @functools.cached_property
    def postCategories(self) -> TopicCategoriesModule:
        """Community post categories module."""
        return TopicCategoriesModule(self.json.get("topicCategories") or {})

    @functools.cached_property
    def posts(self) -> PostModule:
        """Community post module."""
        return PostModule(self.json.get("post") or {})

    @functools.cached_property
    def ranking(self) -> RankingModule:
        """Community member ranking module."""
        return RankingModule(self.json.get("ranking") or {})

    @functools.cached_property
    def sharedFolder(self) -> SharedFolderModule:
        """Community shared folder module."""
        return SharedFolderModule(self.json.get("sharedFolder") or {})

    @functools.cached_property
    def wiki(self) -> CatalogModule:
        """Community wiki module."""
        return CatalogModule(self.json.get("catalog") or {})


@dataclasses.dataclass(repr=False)
class CustomPage:
    """Represent the community custom pages.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    alias: List[Optional[:class:`str`]]
        Pages aliases.
    id: List[:class:`str`]
        Pages ids.
    url: List[:class:`str`]
        Pages urls.

    """
    json: typing.List[dict]

    @functools.cached_property
    def alias(self) -> typing.List[typing.Optional[str]]:
        """Pages aliases."""
        return [cl.get("alias") for cl in self.json]

    @functools.cached_property
    def id(self) -> typing.List[str]:
        """Pages ids."""
        return [cl.get("id") for cl in self.json]

    @functools.cached_property
    def url(self) -> typing.List[str]:
        """Pages urls."""
        return [cl.get("url") for cl in self.json]


@dataclasses.dataclass(repr=False)
class DefaultPage(CustomPage):
    """Represent the community default page.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    alias: List[Optional[:class:`str`]]
        Pages aliases.
    id: List[:class:`str`]
        Pages ids.
    url: List[:class:`str`]
        Pages urls.

    """


@dataclasses.dataclass(repr=False)
class Page:
    """Represent the community page configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    custom: :class:`CustomPage`
        Community custom pages.
    default: :class:`DefaultPage`
        Community default pages.

    """
    json: dict

    @functools.cached_property
    def custom(self) -> CustomPage:
        """Community custom pages."""
        return CustomPage(self.json.get("customList") or [])

    @functools.cached_property
    def default(self) -> DefaultPage:
        """Community default pages."""
        return DefaultPage(self.json.get("defaultList") or [])


@dataclasses.dataclass(repr=False)
class Configuration:
    """Represent the community configuration.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    appearance: :class:`Appearance`
        Community appearance configuration.
    general: :class:`General`
        Communirt general configuration.
    module: :class:`Module`
        Community module configuration.
    page: :class:`Page`
        Community page configuration.

    """
    json: dict

    @functools.cached_property
    def appearance(self) -> Appearance:
        """Community appearance configuration."""
        return Appearance(self.json.get("appearance") or {})

    @functools.cached_property
    def general(self) -> General:
        """Communirt general configuration."""
        return General(self.json.get("general") or {})

    @functools.cached_property
    def module(self) -> Module:
        """Community module configuration."""
        return Module(self.json.get("module") or {})

    @functools.cached_property
    def page(self) -> Page:
        """Community page configuration."""
        return Page(self.json.get("page") or {})


@dataclasses.dataclass(repr=False)
class PromotionalMedia:
    """Represent the community promotional media.

    Attributes
    ----------
    json: List[List[:class:`int`, :class:`str`, `None`]]
        The raw API data.
    url: List[:class:`str`]
        Promotional media urls.

    """
    json: typing.List[typing.Tuple[int, str, None]]

    @functools.cached_property
    def url(self) -> typing.List[str]:
        """Promotional media urls."""
        return [m[1] if m else None for m in self.json]


@dataclasses.dataclass(repr=False)
class ThemePack:
    """Represent the community theme pack.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    color: :class:`str`
        Hex color code.
    hash: :class:`str`
        Theme pack hash.
    revision: :class:`int`
        Theme pack revision.
    url: :class:`str`
        Theme pack resource url. (zip)

    """
    json: dict

    @functools.cached_property
    def color(self) -> str:
        """Hex color code."""
        return self.json.get("themeColor")

    @functools.cached_property
    def hash(self) -> str:
        """Theme pack hash."""
        return self.json.get("themePackHash")

    @functools.cached_property
    def revision(self) -> int:
        """Theme pack revision."""
        return self.json.get("themePackRevision")

    @functools.cached_property
    def url(self) -> str:
        """Theme pack resource url. (zip)"""
        return self.json.get("themePackUrl")


@dataclasses.dataclass(repr=False)
class MediaList:
    """Represent the media list.

    Attributes
    ----------
    json: List[Tuple[:class:`int`, :class`str`, `None`, :class:`str`]]
        The raw API data.
    id: List[:class:`str`]
        Media identifiers.
    type: List[:class:`int`]
        Media types.
    url: List[:class:`str`]
        Media urls.

    """
    json: typing.List[typing.Tuple[int, str, None, str]]

    @functools.cached_property
    def id(self) -> typing.List[str]:
        """Media identifiers."""
        return [m[3] if len(m) > 3 else None for m in self.json]

    @functools.cached_property
    def type(self) -> typing.List[int]:
        """Media types."""
        return [m[0] for m in self.json]

    @functools.cached_property
    def url(self) -> typing.List[str]:
        """Media urls."""
        return [m[1] for m in self.json]

    @functools.cached_property
    def null(self) -> list:
        """Unknow value. (comming soon)"""
        return [m[2] for m in self.json]


@dataclasses.dataclass(repr=False)
class Community:
    """Represent a community of amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    activeInfo: :class:`ActiveInfo`
        Community active info.
    addedTopic: :class:`AddedTopic`
        Community added topics.
    advancedSettings: :class:`AdvancedSettings`
        Community advanced settings.
    agent: :class:`Agent`
        Community user agent profile.
    aminoId: :class:`str`
        Community amino id.
    configuration: :class:`Configuration`
        Community configuration.
    createdTime: :class:`str`
        Community created date.
    description: :class:`str`
        Community description.
    extensions: :class:`Extensions`
        Community extensions.
    heat: :class:`int`
        ...
    icon: :class:`str`
        Community icon url.
    id: :class:`int`
        Community id.
    isStandaloneAppDeprecated: :class:`bool`
        Is tandalone app deprecated.
    isStandaloneAppMonetizationEnabled: :bool:`bool`
        Is standalone app monetization enabled.
    joinType: :class:`int`
        Community join type.
    keywords: Optional[:class:`str`]
        Community search keywords.
    link: :class:`str`
        Community link.
    listedStatus: :class:`int`
        Community listed status.
    media: :class:`MediaList`
        Community media list.
    membersCount: :class:`int`
        Community members count.
    modifiedTime: :class:`str`
        Community last modified date.
    name: :class:`str`
        Community name.
    primaryLanguage: :class:`str`
        Community language.
    probationStatus: :class:`int`
        Community probation status.
    promotionalMedia: :class:`PromotionalMedia`
        Community promotional media.
    searchable: :class:`bool`
        Searchable community.
    status: :class:`int`
        Community status.
    tagline: :class:`str`
        Community tagline.
    themePack: :class:`ThemePack`
        Community theme pack.
    templateId: :class:`int`
        Community template id.
    updatedTime: :class:`str`
        Community updated date.
    vips: :class:`UserProfileList`
        Community vip users.

    """
    json: dict

    @functools.cached_property
    def activeInfo(self) -> ActiveInfo:
        """Community active info."""
        return ActiveInfo(self.json.get("activeInfo") or {})

    @functools.cached_property
    def addedTopic(self) -> AddedTopic:
        """Community added topics."""
        return AddedTopic(self.json.get("userAddedTopicList") or [])

    @functools.cached_property
    def advancedSettings(self) -> AdvancedSettings:
        """Community advanced settings."""
        return AdvancedSettings(self.json.get("advancedSettings") or {})

    @functools.cached_property
    def agent(self) -> Agent:
        """Community user agent profile."""
        return Agent(self.json.get("agent") or {})

    @functools.cached_property
    def aminoId(self) -> str:
        """Community amino id."""
        return self.json.get("endpoint")

    @functools.cached_property
    def configuration(self) -> Configuration:
        """Community configuration."""
        return Configuration(self.json.get("configuration") or {})

    @functools.cached_property
    def createdTime(self) -> str:
        """Community created date."""
        return self.json.get("createdTime")

    @functools.cached_property
    def description(self) -> typing.Optional[str]:
        """Community description."""
        return self.json.get("content")

    @functools.cached_property
    def extensions(self) -> Extensions:
        """Community extensions."""
        return Extensions(self.json.get("extensions") or {})

    @functools.cached_property
    def heat(self) -> float:
        """Community heat."""
        return self.json.get("communityHeat") or 0.0

    @functools.cached_property
    def icon(self) -> str:
        """Community icon url."""
        return self.json.get("icon")

    @functools.cached_property
    def id(self) -> int:
        """Community id."""
        return self.json.get("ndcId")

    @functools.cached_property
    def isStandaloneAppDeprecated(self) -> bool:
        """Is standalone app deprecated."""
        return self.json.get("isStandaloneAppDeprecated")

    @functools.cached_property
    def isStandaloneAppMonetizationEnabled(self) -> bool:
        """Is standalone app monetization enabled."""
        return self.json.get("isStandaloneAppMonetizationEnabled")

    @functools.cached_property
    def joinType(self) -> int:
        """Community join type."""
        return self.json.get("joinType")

    @functools.cached_property
    def keywords(self) -> typing.Optional[str]:
        """Community search keywords. (separated by ',')"""
        return self.json.get("keywords")

    @functools.cached_property
    def link(self) -> str:
        """Community link."""
        return self.json.get("link")

    @functools.cached_property
    def listedStatus(self) -> int:
        """Community listed status."""
        return self.json.get("listedStatus")

    @functools.cached_property
    def media(self) -> MediaList:
        """Community media list."""
        return MediaList(self.json.get("mediaList") or [])

    @functools.cached_property
    def membersCount(self) -> int:
        """Community members count."""
        return self.json.get("membersCount")

    @functools.cached_property
    def modifiedTime(self) -> str:
        """Community last modified date."""
        return self.json.get("modifiedTime")

    @functools.cached_property
    def name(self) -> str:
        """Community name."""
        return self.json.get("name")

    @functools.cached_property
    def primaryLanguage(self) -> str:
        """Community language."""
        return self.json.get("primaryLanguage")

    @functools.cached_property
    def probationStatus(self) -> int:
        """Community probation status."""
        return self.json.get("probationStatus")

    @functools.cached_property
    def promotionalMedia(self) -> PromotionalMedia:
        """Community promotional media."""
        return PromotionalMedia(self.json.get("promotionalMediaList") or [])

    @functools.cached_property
    def searchable(self) -> bool:
        """Searchable community."""
        return self.json.get("searchable")

    @functools.cached_property
    def status(self) -> int:
        """Community status."""
        return self.json.get("status")

    @functools.cached_property
    def tagline(self) -> str:
        """Community tagline."""
        return self.json.get("tagline")

    @functools.cached_property
    def themePack(self) -> ThemePack:
        """Community theme pack."""
        return ThemePack(self.json.get("themePack") or {})

    @functools.cached_property
    def templateId(self) -> int:
        """Community template id."""
        return self.json.get("templateId")

    @functools.cached_property
    def updatedTime(self) -> str:
        """Community updated date."""
        return self.json.get("updatedTime")

    @functools.cached_property
    def vips(self) -> userprofilelist.UserProfileList:
        """Community vip users."""
        return userprofilelist.UserProfileList(self.json.get('influencerList') or [])
