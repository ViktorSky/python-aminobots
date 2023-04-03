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
from dataclasses import dataclass
from typing import List, Optional, Tuple

__all__ = ('UserProfileList',)


@dataclass(repr=False)
class AvatarFrameList:
    """Represent the users avatar frames.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    id: List[:class:`str`]
        Users avatar frame ids.
    icon: List[:class:`str`]
        Users avatar frame icon urls.
    name: List[:class:`str`]
        Users avatar frame names.
    ownershipStatus: List[Optional[:class:`str`]]
        Users avatar frame ownership stats.
    status: List[:class:`int`]
        Users avatar frame status.
    type: List[:class:`int`]
        Users avatar frame types.
    version: List[:class:`int`]
        Users avatar frame versions.
    url: List[:class:`str`]
        Users avatar frame resource urls. (zip)

    """
    json: List[dict]

    @property
    def id(self) -> List[str]:
        """Users avatar frame ids."""
        return [af.get("frameId") for af in self.json]

    @property
    def icon(self) -> List[str]:
        """Users avatar frame icon urls."""
        return [af.get("icon") for af in self.json]

    @property
    def name(self) -> List[str]:
        """Users avatar frame names."""
        return [af.get("name") for af in self.json]

    @property
    def ownershipStatus(self) -> List[Optional[str]]:
        """Users avatar frame ownership status."""
        return [af.get("ownershipStatus") for af in self.json]

    @property
    def status(self) -> List[int]:
        """Users avatar frame status."""
        return [af.get("status") for af in self.json]

    @property
    def type(self) -> List[int]:
        """Users avatar frame types."""
        return [af.get("frameType") for af in self.json]

    @property
    def version(self) -> List[int]:
        """Users avatar frame versions."""
        return [af.get("version") for af in self.json]

    @property
    def url(self) -> List[str]:
        """Users avatar frame resource urls. (zip)"""
        return [af.get("resourceUrl") for af in self.json]


@dataclass(repr=False)
class BackgroundMediaList:
    """Represent the users background media list.

    Attributes
    ----------
    json: List[List[List[:class:`int`, :class:`str`, `None`, `None`, `None`, :class:`dict`]]]
        The raw API data.
    url: List[Optional[:class:`str`]]
        Users baground urls.

    """
    json: List[List[Tuple[int, str, None, None, None, dict]]]

    @property
    def url(self) -> List[Optional[str]]:
        """Users background urls."""
        return [bg[0][1] if bg and any(bg[0]) else None for bg in self.json]


@dataclass(repr=False)
class DeviceInfoList:
    """Represent the users device info.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    lastClientType: List[:class:`int`]
        Users last device client types.

    """
    json: List[dict]

    @property
    def lastClientType(self) -> List[int]:
        """Users last device client types."""
        return [di.get("lastClientType") for di in self.json]


@dataclass(repr=False)
class StyleList:
    """Represent the users profile styles.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    background: :class:`BackgroundMediaList`
        Users backgrounds.
    backgroundUrl: List[Optional[:class:`str`]]
        Users background hex color codes.

    """
    json: List[dict]

    @property
    def background(self) -> BackgroundMediaList:
        """Users backgrounds."""
        return BackgroundMediaList([s.get("backgroundMediaList") or [] for s in self.json])

    @property
    def backgroundUrl(self) -> List[Optional[str]]:
        """Users background hex color codes."""
        return self.background.url


@dataclass(repr=False)
class ExtensionList:
    """Represent the user profile list extensions.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    acpDeeplink: List[Optional[:class:`str`]]
        Users acp deep link.
    adsEnabled: List[Optional[:class:`bool`]]
        Users ads enabled.
    adsFlags: List[Optional[:class:`int`]]
        Users ads flags.
    backgroundMedia: :class:`BackgroundMediaList`
        Users background media list.
    backgroundUrl(self) -> List[Optional[str]]:
        return self.style.backgroundUrl

    @property
    def backgroundUrlList(self) -> List[List[str]]:
        return self.style.backgroundUrlList

    @property
    def creatorDeeplink(self) -> List[Optional[str]]:
        return [e.get("creatorDeeplink") for e in self.json]

    @property
    def customTitles(self):
        return [e.get("customTitles") for e in self.json]

    @property
    def defaultBubbleId(self) -> List[Optional[str]]:
        return [e.get("defaultBubbleId") for e in self.json]

    @property
    def deviceInfo(self) -> DeviceInfoList:
        return DeviceInfoList([e.get("deviceInfo") or {} for e in self.json])

    @property
    def disabledLevel(self):
        return [e.get("__disabledLevel__") for e in self.json]

    @property
    def disabledStatus(self):
        return [e.get("__disabledStatus__") for e in self.json]

    @property
    def disabledTime(self):
        return [e.get("__disabledTime__") for e in self.json]

    @property
    def isMemberOfTeamAmino(self) -> bool:
        return [e.get("isMemberOfTeamAmino") or False for e in self.json]

    @property
    def privilegeOfChatInviteRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatInviteRequest") for e in self.json]

    @property
    def privilegeOfChatRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatRequest") for e in self.json]

    @property
    def privilegeOfCommentOnUserProfile(self) -> List[Optional[int]]:
        return [e.get("privilegeOfCommentOnUserProfile") for e in self.json]

    @property
    def privilegeOfPublicChat(self) -> List[Optional[int]]:
        return [e.get("privilegeOfPublicChat") for e in self.json]

    @property
    def privilegeOfVideoChat(self) -> Optional[int]:
        return [e.get("privilegeOfVideoChat") for e in self.json]

    @property
    def style(self) -> StyleList:
        return StyleList([e.get("style") or {} for e in self.json])

    @property
    def tippingPermStatus(self) -> Optional[int]:

    """
    json: List[dict]

    @property
    def acpDeeplink(self) -> List[Optional[str]]:
        return [e.get("acpDeeplink") for e in self.json]

    @property
    def adsEnabled(self) -> List[Optional[bool]]:
        return [e.get("adsEnabled") for e in self.json]

    @property
    def adsFlags(self) -> List[Optional[int]]:
        return self.json.get("adsFlags")

    @property
    def background(self) -> BackgroundMediaList:
        return self.style.background

    @property
    def backgroundColor(self) -> List[Optional[str]]:
        return self.style.backgroundColor

    @property
    def creatorDeeplink(self) -> List[Optional[str]]:
        return [e.get("creatorDeeplink") for e in self.json]

    @property
    def customTitles(self):
        return [e.get("customTitles") for e in self.json]

    @property
    def defaultBubbleId(self) -> List[Optional[str]]:
        return [e.get("defaultBubbleId") for e in self.json]

    @property
    def deviceInfo(self) -> DeviceInfoList:
        return DeviceInfoList([e.get("deviceInfo") or {} for e in self.json])

    @property
    def disabledLevel(self):
        return [e.get("__disabledLevel__") for e in self.json]

    @property
    def disabledStatus(self):
        return [e.get("__disabledStatus__") for e in self.json]

    @property
    def disabledTime(self):
        return [e.get("__disabledTime__") for e in self.json]

    @property
    def isMemberOfTeamAmino(self) -> bool:
        return [e.get("isMemberOfTeamAmino") or False for e in self.json]

    @property
    def privilegeOfChatInviteRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatInviteRequest") for e in self.json]

    @property
    def privilegeOfChatRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatRequest") for e in self.json]

    @property
    def privilegeOfCommentOnUserProfile(self) -> List[Optional[int]]:
        return [e.get("privilegeOfCommentOnUserProfile") for e in self.json]

    @property
    def privilegeOfPublicChat(self) -> List[Optional[int]]:
        return [e.get("privilegeOfPublicChat") for e in self.json]

    @property
    def privilegeOfVideoChat(self) -> Optional[int]:
        return [e.get("privilegeOfVideoChat") for e in self.json]

    @property
    def style(self) -> StyleList:
        return StyleList([e.get("style") or {} for e in self.json])

    @property
    def tippingPermStatus(self) -> Optional[int]:
        return [e.get("tippingPermStatus") for e in self.json]


@dataclass(repr=False)
class InfluencerInfoList:
    """Represent the users vip infos.

    Attributes
    ----------
    json: List[:class:;`dict`]
        The raw API data.
    fansCount: List[:class:`int`]
        Users fans counts.
    createdTime: List[:class:`str`]
        Users vip created dates.
    pinned: List[:class:`bool`]
        Users pinned.
    monthlyFee: List[:class:`int`]
        Users monthly fee.

    """
    json: List[dict]

    @property
    def fansCount(self) -> List[int]:
        return [i.get('fansCount') for i in self.json]

    @property
    def createdTime(self) -> List[str]:
        """Users vip created dates."""
        return [i.get('createdTime') for i in self.json]

    @property
    def pinned(self) -> List[bool]:
        """Users pinned."""
        return [i.get('pinned') for i in self.json]

    @property
    def monthlyFee(self) -> List[int]:
        """Users monthly fee."""
        return [i.get('monthlyFee') for i in self.json]


@dataclass(repr=False)
class LinkedActiveInfoList:
    """Represent the linked communities active info.

    Attributes
    ----------
    json: List[List[:class:`dict`]]
        The raw API data.

    """
    json: List[List[dict]]


@dataclass(repr=False)
class LinkedBackgroundMediaList:
    """Represent the Linked communities topic background media list.

    Attributes
    ----------
    json: List[List[List[List[:class:`int`, :class:`str`, `None`, `None`, `None`, :class:`dict`]]]]
        The raw API data.
    url: List[List[List[:class:`str`]]]
        Linked communities background url list.

    """
    json: List[List[List[Tuple[int, str, None, None, None, dict]]]]

    @property
    def url(self) -> List[List[List[str]]]:
        """Linked communities background url list."""
        return [[bg[0][1] if bg and any(bg[0]) else None for bg in bgl] for bgl in self.json]


@dataclass(repr=False)
class LinkedStyleList:
    """Represent the topic style list.

    Attributes
    ----------
    json: List[List[List[:class:`dict`]]]
        The raw API data.
    background: :class:`LinkedBackgroundMediaList`
        Topic background list.
    backgroundColor: List[List[List[Optional[:class:`str`]]]]
        Topic background color list.

    """
    json: List[List[List[dict]]]

    @property
    def background(self) -> LinkedBackgroundMediaList:
        """Topic background list."""
        return LinkedBackgroundMediaList([[[s.get("backgroundMediaList") or [] for s in ls] for ls in lsl] for lsl in self.json])

    @property
    def backgroundColor(self) -> List[List[List[Optional[str]]]]:
        """Topic background color list."""
        return [[[s.get('backgroundColor')for s in ls]for ls in lsl]for lsl in self.json]


@dataclass(repr=False)
class LinkedAddedTopicList:
    """Represent the linked communities added topics.

    Attributes
    ----------
    json: List[List[List[:class:`dict`]]]
        The raw API data.
    background: :class:`BackgroundMediaList`
        Topics background list.
    backgroundColor: List[List[List[:class:`str`]]]
        Hex colors codes.
    name: List[List[List[:class:`str`]]]
        Topic names.
    style: :class:`LinkedStyleList`
        Topic style.
    id: List[List[List[:class:`int`]]]
        Topic ids.

    """
    json: List[List[List[dict]]]

    @property
    def background(self) -> BackgroundMediaList:
        """Topics background media list."""
        return self.style.background

    @property
    def backgroundColor(self) -> List[str]:
        """Topics background hex colors codes."""
        return self.style.backgroundColor

    @property
    def name(self) -> List[List[List[str]]]:
        """Topic names."""
        return [[[lt.get("name") for lt in lat] for lat in latl] for latl in self.json]

    @property
    def style(self) -> LinkedStyleList:
        """Topics styles."""
        return LinkedStyleList([[[lt.get("style") or {} for lt in lat] for lat in latl] for latl in self.json])

    @property
    def id(self) -> List[List[List[int]]]:
        """Topics ids."""
        return [[[lt.get("topicId") for lt in lat] for lat in latl] for latl in self.json]


@dataclass(repr=False)
class LinkedAgentList:
    """Represent the linked communities users agents.

    Attributes
    ----------
    json: List[List[:class:`dict`]]
        The raw API data.
    id: List[List[:class:`str`]]
        Linked communities users agents ids.

    """
    json: List[List[dict]]

    @property
    def id(self) -> List[List[str]]:
        """Linked communities users agents ids."""
        return [[a.get("uid") for a in ag] for ag in self.json]


@dataclass(repr=False)
class LinkedPromotionalMediaList:
    """Represent the linked communities promotional media list.

    Attributes
    ----------
    json: List[List[Tuple[:class:`int`, :class:`str`, `None`]]]
        The raw API data.
    url: List[List[:class:`str`]]
        Linked communities promotional media url.

    """
    json: List[List[Tuple[int, str, None]]]

    @property
    def url(self) -> List[List[str]]:
        """Linked communities promotional media url."""
        return [[ml[1] if ml else None for ml in pml] for pml in self.json]
        # return [[[ml[1] if ml else None for ml in pm] for pm in pml] for pml in self.json]

@dataclass(repr=False)
class LinkedThemePackList:
    """Represent the linked communities theme packs.

    Attributes
    ----------
    json: List[List[:class:`dict`]]
        The raw API data.
    color: List[List[:class:`str`]]
        Theme packs hex color codes.
    hash: List[List[:class:`str`]]
        Theme packs hashs.
    revision: List[List[:class:`int`]]
        Theme packs revisions.
    url: List[List[:class:`str`]]
        Theme packs urls.

    """
    json: List[List[dict]]

    @property
    def color(self) -> List[List[str]]:
        """Theme packs hex color codes."""
        return [[tp.get("themeColor") for tp in tpl] for tpl in self.json]

    @property
    def hash(self) -> List[List[str]]:
        """Theme packs hashs."""
        return [[tp.get("themePackHash") for tp in tpl] for tpl in self.json]

    @property
    def revision(self) -> List[List[int]]:
        """Theme packs revisions."""
        return [[tp.get("themePackRevision") for tp in tpl] for tpl in self.json]

    @property
    def url(self) -> List[List[str]]:
        """Theme packs urls."""
        return [[tp.get("themePackUrl") for tp in tpl] for tpl in self.json]


@dataclass(repr=False)
class LinkedCommunityList:
    """Represent the users linked communities.

    Attributes
    ----------
    json: List[List[:class:`dict`]]
        The raw API data.
    activeInfo: :class:`LinkedActiveInfoList`
        Linked communities active info.
    addedTopic: :class:`LinkedAddedTopicList`
        Linked communities added topics.
    agent: :class:`LinkedAgentList`
        Linked communities users agents profiles.
    aminoId: List[List[:class:`str`]]
        Linked communities amino ids.
    comId: List[List[:class:`int`]]
        Linked communities ids.
    createdTime: List[List[:class:`str`]]
        Linked communities created dates.
    description: List[List[:class:`str`]]
        Linked communites descriptions.
    heat: List[List[:class:`int`]]
        Linked communities heats.
    icon: List[List[:class:`str`]]
        Linked communities icon urls.
    joinType: List[List[:class:`int`]]
        Linked communities join types.
    language: List[List[:class:`str`]]
        Linked communities languages.
    link: List[List[:class:`str`]]
        Linked communities links.
    listedStatus: List[List[:class:`int`]]
        Linked communities listed status.
    membersCount: List[List[:class:`int`]]
        Linked communities members counts.
    modifiedTime: List[List[:class:`str`]]
        Linked communities modified times.
    name: List[List[:class:`str`]]
        Linked communities names.
    probationStatus: List[List[:class:`int`]]
        Linked communities probation status.
    promotionalMedia: :class:`LinkedPromotionalMediaList`
        Linked communities promotional medias.
    status: List[List[:class:`int`]]
        Linked communities status.
    templateId: List[List[:class:`str`]]
        Linked communities template ids.
    themePack: :class:`LinkedThemePackList`
        Linked communities theme packs.
    updatedTime: List[List[:class:`str`]]
        Linked communities updated dates.

    """
    json: List[List[dict]]

    @property
    def activeInfo(self) -> LinkedActiveInfoList:
        """Linked communities active info."""
        return LinkedActiveInfoList([[c.get("activeInfo") or {} for c in lcl] for lcl in self.json])

    @property
    def addedTopic(self) -> LinkedAddedTopicList:
        """Linked communities added topics."""
        return LinkedAddedTopicList([[c.get("userAddedTopicList") or {} for c in lcl] for lcl in self.json])

    @property
    def agent(self) -> LinkedAgentList:
        """Linked communities users agents profiles."""
        return LinkedAgentList([[c.get("agent") or {} for c in lcl] for lcl in self.json])

    @property
    def aminoId(self) -> List[List[str]]:
        """Linked communities amino ids."""
        return [[c.get("endpoint") for c in lcl] for lcl in self.json]

    @property
    def comId(self) -> List[List[int]]:
        """Linked communities ids."""
        return [[c.get("ndcId") for c in lcl] for lcl in self.json]

    @property
    def createdTime(self) -> List[List[str]]:
        """Linked communities created dates."""
        return [[c.get("createdTime") for c in lcl] for lcl in self.json]

    @property
    def description(self) -> List[List[str]]:
        """Linked communites descriptions."""
        return [[c.get("tagline") for c in lcl] for lcl in self.json]

    @property
    def heat(self) -> List[List[int]]:
        """Linked communities heats."""
        return [[c.get("communityHeat") or 0 for c in lcl] for lcl in self.json]

    @property
    def icon(self) -> List[List[str]]:
        """Linked communites icon urls."""
        return [[c.get("icon") for c in lcl] for lcl in self.json]

    @property
    def joinType(self) -> List[List[int]]:
        """Linked communities join types."""
        return [[c.get("joinType") for c in lcl] for lcl in self.json]

    @property
    def primaryLanguage(self) -> List[List[str]]:
        """Linked communities languages."""
        return [[c.get("primaryLanguage") for c in lcl] for lcl in self.json]

    @property
    def link(self) -> List[List[str]]:
        """Linked communities links."""
        return [[c.get("link") for c in lcl] for lcl in self.json]

    @property
    def listedStatus(self) -> List[List[int]]:
        """Linked communities listed status."""
        return [[c.get("listedStatus") for c in lcl] for lcl in self.json]

    @property
    def membersCount(self) -> List[List[int]]:
        """Linked communities members counts."""
        return [[c.get("membersCount") or 0 for c in lcl] for lcl in self.json]

    @property
    def modifiedTime(self) -> List[List[str]]:
        """Linked communities modified times."""
        return [[c.get("modifiedTime") for c in lcl] for lcl in self.json]

    @property
    def name(self) -> List[List[str]]:
        """Linked communities names."""
        return [[c.get("name") for c in lcl] for lcl in self.json]

    @property
    def probationStatus(self) -> List[List[int]]:
        """Linked communities probation status."""
        return [[c.get("probationStatus") or 0 for c in lcl] for lcl in self.json]

    @property
    def promotionalMedia(self) -> LinkedPromotionalMediaList:
        """Linked communities promotional medias."""
        return LinkedPromotionalMediaList([[c.get("promotionalMediaList") or [] for c in lcl] for lcl in self.json])

    @property
    def status(self) -> List[List[int]]:
        """Linked communities status."""
        return [[c.get("status") or 0 for c in lcl] for lcl in self.json]

    @property
    def templateId(self) -> List[List[str]]:
        """Linked communities template ids."""
        return [[c.get("templateId") for c in lcl] for lcl in self.json]

    @property
    def themePack(self) -> LinkedThemePackList:
        """Linked communities theme packs."""
        return LinkedThemePackList([[c.get("themePack") or {} for c in lcl] for lcl in self.json])

    @property
    def updatedTime(self) -> List[List[str]]:
        """Linked communities updated dates."""
        return [[c.get("updatedTime") for c in lcl] for lcl in self.json]


@dataclass(repr=False)
class MediaList:
    """Represent the user profile list medias.

    Attributes
    ----------
    json: List[List[List[Tuple[:class:`int`, :class:`str`, `None`]]]]
        The raw API data.
    url: List[List[:class:`str`]]
        Users medias urls.

    """
    json: List[List[List[Tuple[int, str, None]]]]

    @property
    def url(self) -> List[List[str]]:
        """Users medias urls."""
        return [[m[1] if m else None for m in ml] for ml in self.json]


@dataclass(repr=False)
class UserProfileList:
    """Represent a list of user profiles.

    Attributes
    ----------
    json: List[:class:`dict`]
        The raw API data.
    accountMembershipStatus: List[:class:`int`]
        ...
    acpDeeplink: List[Optional[:class:`str`]]
        Users acp deep links.
    adminLogCountIn7Days: :class:`int`
        ...
    aminoId: List[:class:`str`]
        Amino ids
    avatar: :class:`AvatarFrameList`
        Avatar frames.
    bio: List[Optional[:class:`str`]]
        Users bios.
    blogsCount: List[:class:`int`]
        Users blogs counts.
    comId: List[Optional[:class:`int`]]
        Users community ids.
    commentsCount: List[:class:`int`]
        Users comments counts.
    consecutiveCheckInDays: List[Optional[:class:`int`]]
        Users check-in days.
    createdTime: List[:class:`str`]
        Users register dates.
    creatorDeeplink: List[Optional[:class:`str`]]
        Users creator deep links.
    extensions: :class:`ExtensionList`
        User profile list extensions.
    followersCount: List[:class:`int`]
        Users followers counts.
    followingCount: List[`int`]
        Users following counts.
    followingStatus: List[:class:`int`]
        Following status.
    id: List[:class:`str`]
        Users ids.
    icon: List[:class:`str`]
        Users icon urls.
    influencer: :class:`InfluencerInfoList`
        Users vip info.
    isGlobal: :class:`bool`
        ...
    level: List[:class:`int`]
        Users levels.
    linkedCommunities: :class:`LinkedCommunityList`
        Users linked communities.
    media: :class:`MediaList`
        Users medias.
    membershipStatus: List[:class:`int`]
        Users membership status.
    modifiedTime: List[:class:`str`]
        Users last modified dates.
    mood: ::``
        Users moods.
    moodSticker: ::``
        ...
    nickname: List[:class:`str`]
        Users nicknames.
    nicknameVerified: List[:class:`bool`]
        Users nickname verifieds.
    notifSubStatus: List[:class:`int`]
        Users notification subscription status.
    onlineStatus: List[:class:`int`]
        Users online status.
    postsCount: List[:class:`int`]
        Users posts counts.
    privilegeOfChatRequest: List[:class:`int`]
        Users privilege of chat requests.
    pushEnabled: List[:class:`bool`]
        Users push enabled.
    reputation: List[:class:`int`]
        Users reputation.
    role: List[:class:`int`]
        Community users role.
    status: List[:class:`int`]
        User status.
    storiesCount: List[:class:`int`]
        Users stories counts.
    style: :class:`StyleList`
        Users styles.
    wikisCount: List[:class:`int`]
        Users wikis counts.

    """
    json: List[dict]

    @property
    def accountMembershipStatus(self) -> List[int]:
        return [up.get("accountMembershipStatus") or 0 for up in self.json]

    @property
    def acpDeeplink(self) -> List[Optional[str]]:
        return self.extensions.acpDeeplink

    @property
    def adminLogCountIn7Days(self):
        return [up.get("adminLogCountIn7Days") for up in self.json]

    @property
    def aminoId(self) -> List[str]:
        return [up.get("aminoId") for up in self.json]

    @property
    def avatar(self) -> AvatarFrameList:
        return AvatarFrameList([up.get("avatarFrame") or {} for up in self.json])

    @property
    def bio(self) -> List[Optional[str]]:
        return [up.get("content") or 0 for up in self.json]

    @property
    def blogsCount(self) -> List[int]:
        return [up.get("blogsCount") or 0 for up in self.json]

    @property
    def comId(self) -> List[Optional[int]]:
        return [up.get("ndcId") or None for up in self.json]

    @property
    def commentsCount(self) -> List[int]:
        return [up.get("commentsCount") or 0 for up in self.json]

    @property
    def consecutiveCheckInDays(self):
        return [up.get("consecutiveCheckInDays") for up in self.json]

    @property
    def createdTime(self) -> List[str]:
        return [up.get("createdTime") for up in self.json]

    @property
    def creatorDeeplink(self) -> Optional[str]:
        return self.extensions.creatorDeeplink

    @property
    def extensions(self) -> ExtensionList:
        return ExtensionList([up.get("extensions") or {} for up in self.json])

    @property
    def followersCount(self) -> List[int]:
        return [up.get("membersCount") for up in self.json]

    @property
    def followingCount(self) -> List[int]:
        return [up.get("joinedCount") for up in self.json]

    @property
    def followingStatus(self) -> List[int]:
        return [up.get("followingStatus") for up in self.json]

    @property
    def id(self) -> List[str]:
        return [up.get("uid") for up in self.json]

    @property
    def icon(self) -> List[str]:
        return [up.get("icon") for up in self.json]

    @property
    def influencer(self) -> InfluencerInfoList:
        return InfluencerInfoList([i.get('influencerInfo') for i in self.json])

    @property
    def isGlobalProfile(self) -> bool:
        return all(up.get("isGlobal") for up in self.json)

    @property
    def level(self) -> List[int]:
        return [up.get("level") or 0 for up in self.json]

    @property
    def linkedCommunities(self) -> LinkedCommunityList:
        return LinkedCommunityList([up.get("linkedCommunityList") or [] for up in self.json])

    @property
    def media(self) -> MediaList:
        return MediaList([up.get("mediaList") or [] for up in self.json])

    @property
    def membershipStatus(self) -> List[int]:
        return [up.get("membershipStatus") or 0 for up in self.json]

    @property
    def modifiedTime(self) -> List[str]:
        return [up.get("modifiedTime") for up in self.json]

    @property
    def mood(self):
        return [up.get("mood") for up in self.json]

    @property
    def moodSticker(self):
        return [up.get("moodSticker") for up in self.json]

    @property
    def nickname(self) -> List[str]:
        return [up.get("nickname") for up in self.json]

    @property
    def nicknameVerified(self) -> List[bool]:
        return [up.get("isNicknameVerified") for up in self.json]

    @property
    def notifSubStatus(self) -> List[int]:  # [0, 1]
        return [up.get("notificationSubscriptionStatus") for up in self.json]

    @property
    def onlineStatus(self) -> List[int]:
        return [up.get("onlineStatus") for up in self.json]

    @property
    def postsCount(self) -> List[int]:
        return [up.get("postsCount") or 0 for up in self.json]

    @property
    def privilegeOfChatRequest(self) -> List[int]:
        return self.extensions.privilegeOfChatRequest

    @property
    def pushEnabled(self) -> List[bool]:
        return [up.get("pushEnabled") for up in self.json]

    @property
    def reputation(self) -> List[int]:
        return [up.get("reputation") or 0 for up in self.json]

    @property
    def role(self) -> List[int]:
        return [up.get("role") for up in self.json]

    @property
    def status(self) -> List[int]:
        return [up.get("status") for up in self.json]

    @property
    def storiesCount(self) -> List[int]:
        return [up.get("storiesCount") or 0 for up in self.json]

    @property
    def style(self) -> StyleList:
        return self.extensions.style

    @property
    def wikisCount(self) -> List[int]:
        return [up.get("itemsCount") for up in self.json]
