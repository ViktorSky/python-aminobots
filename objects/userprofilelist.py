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
from functools import cached_property
from typing import List, Optional, Tuple

__all__ = ('UserProfileList',)


@dataclass(repr=False)
class AvatarFrameList:
    """Represent the users avatar frames.

    Attributes
    ----------
    json : List[:class:`dict`]
        The raw API data.
    ids : List[:class:`str`]
        Users avatar frame ids.
    icons : List[:class:`str`]
        Users avatar frame icon urls.
    names : List[:class:`str`]
        Users avatar frame names.
    ownershipStatuses : List[Optional[:class:`str`]]
        Users avatar frame ownership stats.
    statuses : List[:class:`int`]
        Users avatar frame status.
    types : List[:class:`int`]
        Users avatar frame types.
    versions : List[:class:`int`]
        Users avatar frame versions.
    urls : List[:class:`str`]
        Users avatar frame resource urls. (zip)

    """
    json: List[dict]

    @cached_property
    def ids(self) -> List[str]:
        """Users avatar frame ids."""
        return [af.get("frameId") for af in self.json]

    @cached_property
    def icons(self) -> List[str]:
        """Users avatar frame icon urls."""
        return [af.get("icon") for af in self.json]

    @cached_property
    def names(self) -> List[str]:
        """Users avatar frame names."""
        return [af.get("name") for af in self.json]

    @cached_property
    def ownershipStatuses(self) -> List[Optional[str]]:
        """Users avatar frame ownership status."""
        return [af.get("ownershipStatus") for af in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        """Users avatar frame status."""
        return [af.get("status") for af in self.json]

    @cached_property
    def types(self) -> List[int]:
        """Users avatar frame types."""
        return [af.get("frameType") for af in self.json]

    @cached_property
    def versions(self) -> List[int]:
        """Users avatar frame versions."""
        return [af.get("version") for af in self.json]

    @cached_property
    def urls(self) -> List[str]:
        """Users avatar frame resource urls. (zip)"""
        return [af.get("resourceUrl") for af in self.json]


@dataclass(repr=False)
class BackgroundMediaList:
    """Represent the users background media list.

    Attributes
    ----------
    json : List[List[List[:class:`int`, :class:`str`, `None`, `None`, `None`, :class:`dict`]]]
        The raw API data.
    types : List[Optional[:class:`str`]]
        Users baground media types.
    urls : List[Optional[:class:`str`]]
        Users baground urls.

    """
    json: List[List[Tuple[int, str, None, None, None, dict]]]

    @cached_property
    def types(self) -> List[Optional[str]]:
        """Users background types."""
        return [bg[0][0] if (bg and bg[0]) else None for bg in self.json]

    @cached_property
    def urls(self) -> List[Optional[str]]:
        """Users background urls."""
        return [bg[0][1] if (bg and bg[0]) else None for bg in self.json]


@dataclass(repr=False)
class DeviceInfoList:
    """Represent the users device info.

    Attributes
    ----------
    json : List[:class:`dict`]
        The raw API data.
    lastClientTypes : List[:class:`int`]
        Users last device client types.

    """
    json: List[dict]

    @cached_property
    def lastClientTypes(self) -> List[int]:
        """Users last device client types."""
        return [di.get("lastClientType") for di in self.json]


@dataclass(repr=False)
class StyleList:
    """Represent the users profile styles.

    Attributes
    ----------
    json : List[:class:`dict`]
        The raw API data.
    backgrounds : :class:`BackgroundMediaList`
        Users backgrounds.
    backgroundUrls : List[Optional[:class:`str`]]
        Users background hex color codes.

    """
    json: List[dict]

    @cached_property
    def backgrounds(self) -> BackgroundMediaList:
        """Users backgrounds."""
        return BackgroundMediaList([s.get("backgroundMediaList") or [] for s in self.json])

    @cached_property
    def backgroundUrls(self) -> List[Optional[str]]:
        """Users background hex color codes."""
        return self.backgrounds.urls


@dataclass(repr=False)
class ExtensionList:
    """Represent the user profile list extensions."""
    json: List[dict]

    @cached_property
    def acpDeeplinks(self) -> List[Optional[str]]:
        return [e.get("acpDeeplink") for e in self.json]

    @cached_property
    def adsEnabled(self) -> List[Optional[bool]]:
        return [e.get("adsEnabled") for e in self.json]

    @cached_property
    def adsFlags(self) -> List[Optional[int]]:
        return self.json.get("adsFlags")

    @cached_property
    def backgrounds(self) -> BackgroundMediaList:
        return self.styles.backgrounds

    #@cached_property
    #def backgroundColors(self) -> List[Optional[str]]:
    #    return self.styles.backgroundsColors

    @cached_property
    def creatorDeeplinks(self) -> List[Optional[str]]:
        return [e.get("creatorDeeplink") for e in self.json]

    @cached_property
    def customTitles(self):
        return [e.get("customTitles") for e in self.json]

    @cached_property
    def defaultBubbleIds(self) -> List[Optional[str]]:
        return [e.get("defaultBubbleId") for e in self.json]

    @cached_property
    def deviceInfos(self) -> DeviceInfoList:
        return DeviceInfoList([e.get("deviceInfo") or {} for e in self.json])

    @cached_property
    def disabledLevels(self):
        return [e.get("__disabledLevel__") for e in self.json]

    @cached_property
    def disabledStatuses(self):
        return [e.get("__disabledStatus__") for e in self.json]

    @cached_property
    def disabledTimes(self):
        return [e.get("__disabledTime__") for e in self.json]

    @cached_property
    def privilegesOfChatInviteRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatInviteRequest") for e in self.json]

    @cached_property
    def privilegesOfChatRequest(self) -> List[Optional[int]]:
        return [e.get("privilegeOfChatRequest") for e in self.json]

    @cached_property
    def privilegesOfCommentOnUserProfile(self) -> List[Optional[int]]:
        return [e.get("privilegeOfCommentOnUserProfile") for e in self.json]

    @cached_property
    def privilegesOfPublicChat(self) -> List[Optional[int]]:
        return [e.get("privilegeOfPublicChat") for e in self.json]

    @cached_property
    def privilegesOfVideoChat(self) -> Optional[int]:
        return [e.get("privilegeOfVideoChat") for e in self.json]

    @cached_property
    def styles(self) -> StyleList:
        return StyleList([e.get("style") or {} for e in self.json])

    @cached_property
    def tippingPermStatuses(self) -> Optional[int]:
        return [e.get("tippingPermStatus") for e in self.json]


@dataclass(repr=False)
class InfluencerInfoList:
    """Represent the users vip infos.

    Attributes
    ----------
    json : List[:class:;`dict`]
        The raw API data.
    fans : List[:class:`int`]
        Users fans counts.
    createdTimes : List[:class:`str`]
        Users vip created dates.
    pinned: List[:class:`bool`]
        Users pinned.
    monthlyFees : List[:class:`int`]
        Users monthly fee.

    """
    json: List[dict]

    @cached_property
    def fans(self) -> List[int]:
        """Fans counts."""
        return [i.get('fansCount') for i in self.json]

    @cached_property
    def createdTimes(self) -> List[str]:
        """Users vip created dates."""
        return [i.get('createdTime') for i in self.json]

    @cached_property
    def pinned(self) -> List[bool]:
        """Users pinned."""
        return [i.get('pinned') for i in self.json]

    @cached_property
    def monthlyFees(self) -> List[int]:
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
    types : List[List[List[:class:`str`]]]
        Linked communities background type list.
    urls : List[List[List[:class:`str`]]]
        Linked communities background url list.

    """
    json: List[List[List[Tuple[int, str, None, None, None, dict]]]]


    @cached_property
    def types(self) -> List[List[List[int]]]:
        """Linked communities background url list."""
        return [[bg[0][0] if (bg and bg[0]) else None for bg in bgl] for bgl in self.json]

    @cached_property
    def urls(self) -> List[List[List[str]]]:
        """Linked communities background url list."""
        return [[bg[0][1] if (bg and bg[0]) else None for bg in bgl] for bgl in self.json]


@dataclass(repr=False)
class LinkedStyleList:
    """Represent the topic style list.

    Attributes
    ----------
    json: List[List[List[:class:`dict`]]]
        The raw API data.
    backgrounds : :class:`LinkedBackgroundMediaList`
        Topic background list.
    backgroundColors : List[List[List[Optional[:class:`str`]]]]
        Topic background color list.

    """
    json: List[List[List[dict]]]

    @cached_property
    def backgrounds(self) -> LinkedBackgroundMediaList:
        """Topic background list."""
        return LinkedBackgroundMediaList([[[s.get("backgroundMediaList") or [] for s in ls] for ls in lsl] for lsl in self.json])

    @cached_property
    def backgroundColors(self) -> List[List[List[Optional[str]]]]:
        """Topic background color list."""
        return [[[s.get('backgroundColor')for s in ls]for ls in lsl]for lsl in self.json]


@dataclass(repr=False)
class LinkedAddedTopicList:
    """Represent the linked communities added topics.

    Attributes
    ----------
    json: List[List[List[:class:`dict`]]]
        The raw API data.
    backgrounds : :class:`BackgroundMediaList`
        Topics background list.
    backgroundColors : List[List[List[:class:`str`]]]
        Hex colors codes.
    names : List[List[List[:class:`str`]]]
        Topic names.
    styles : :class:`LinkedStyleList`
        Topic style.
    ids : List[List[List[:class:`int`]]]
        Topic ids.

    """
    json: List[List[List[dict]]]

    @cached_property
    def backgrounds(self) -> BackgroundMediaList:
        """Topics background media list."""
        return self.styles.backgrounds

    @cached_property
    def backgroundColors(self) -> List[str]:
        """Topics background hex colors codes."""
        return self.styles.backgroundColors

    @cached_property
    def names(self) -> List[List[List[str]]]:
        """Topic names."""
        return [[[lt.get("name") for lt in lat] for lat in latl] for latl in self.json]

    @cached_property
    def styles(self) -> LinkedStyleList:
        """Topics styles."""
        return LinkedStyleList([[[lt.get("style") or {} for lt in lat] for lat in latl] for latl in self.json])

    @cached_property
    def ids(self) -> List[List[List[int]]]:
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

    @cached_property
    def ids(self) -> List[List[str]]:
        """Linked communities users agents ids."""
        return [[a.get("uid") for a in ag] for ag in self.json]


@dataclass(repr=False)
class LinkedPromotionalMediaList:
    """Represent the linked communities promotional media list.

    Attributes
    ----------
    json: List[List[Tuple[:class:`int`, :class:`str`, `None`]]]
        The raw API data.
    urls : List[List[:class:`str`]]
        Linked communities promotional media url.

    """
    json: List[List[Tuple[int, str, None]]]

    @cached_property
    def types(self) -> List[List[str]]:
        """Linked communities promotional media types."""
        return [[ml[0] if ml else None for ml in pml] for pml in self.json]

    @cached_property
    def urls(self) -> List[List[str]]:
        """Linked communities promotional media urls."""
        return [[ml[1] if ml else None for ml in pml] for pml in self.json]
        # return [[[ml[1] if ml else None for ml in pm] for pm in pml] for pml in self.json]

@dataclass(repr=False)
class LinkedThemePackList:
    """Represent the linked communities theme packs.

    Attributes
    ----------
    json : List[List[:class:`dict`]]
        The raw API data.
    colors : List[List[:class:`str`]]
        Theme packs hex color codes.
    hashs : List[List[:class:`str`]]
        Theme packs hashs.
    revisions : List[List[:class:`int`]]
        Theme packs revisions.
    urls : List[List[:class:`str`]]
        Theme packs urls.

    """
    json: List[List[dict]]

    @cached_property
    def colors(self) -> List[List[str]]:
        """Theme packs hex color codes."""
        return [[tp.get("themeColor") for tp in tpl] for tpl in self.json]

    @cached_property
    def hashs(self) -> List[List[str]]:
        """Theme packs hashs."""
        return [[tp.get("themePackHash") for tp in tpl] for tpl in self.json]

    @cached_property
    def revisions(self) -> List[List[int]]:
        """Theme packs revisions."""
        return [[tp.get("themePackRevision") for tp in tpl] for tpl in self.json]

    @cached_property
    def urls(self) -> List[List[str]]:
        """Theme packs urls."""
        return [[tp.get("themePackUrl") for tp in tpl] for tpl in self.json]


@dataclass(repr=False)
class LinkedCommunityList:
    """Represent the users linked communities.

    Attributes
    ----------
    json: List[List[:class:`dict`]]
        The raw API data.
    activeInfos : :class:`LinkedActiveInfoList`
        Linked communities active info.
    addedTopics : :class:`LinkedAddedTopicList`
        Linked communities added topics.
    agents : :class:`LinkedAgentList`
        Linked communities users agents profiles.
    aminoIds : List[List[:class:`str`]]
        Linked communities amino ids.
    communityIds : List[List[:class:`int`]]
        Linked communities ids.
    createdTimes : List[List[:class:`str`]]
        Linked communities created dates.
    descriptions : List[List[:class:`str`]]
        Linked communites descriptions.
    heats : List[List[:class:`int`]]
        Linked communities heats.
    icons : List[List[:class:`str`]]
        Linked communities icon urls.
    joinTypes : List[List[:class:`int`]]
        Linked communities join types.
    languages : List[List[:class:`str`]]
        Linked communities languages.
    links : List[List[:class:`str`]]
        Linked communities links.
    listedStatuses : List[List[:class:`int`]]
        Linked communities listed status.
    members : List[List[:class:`int`]]
        Linked communities members counts.
    modifiedTimes : List[List[:class:`str`]]
        Linked communities modified times.
    names : List[List[:class:`str`]]
        Linked communities names.
    probationStatuses : List[List[:class:`int`]]
        Linked communities probation status.
    promotionalMedias : :class:`LinkedPromotionalMediaList`
        Linked communities promotional medias.
    statuses : List[List[:class:`int`]]
        Linked communities status.
    templateIds : List[List[:class:`str`]]
        Linked communities template ids.
    themePacks : :class:`LinkedThemePackList`
        Linked communities theme packs.
    updatedTimes : List[List[:class:`str`]]
        Linked communities updated dates.

    """
    json: List[List[dict]]

    @cached_property
    def activeInfos(self) -> LinkedActiveInfoList:
        """Linked communities active info."""
        return LinkedActiveInfoList([[c.get("activeInfo") or {} for c in lcl] for lcl in self.json])

    @cached_property
    def addedTopics(self) -> LinkedAddedTopicList:
        """Linked communities added topics."""
        return LinkedAddedTopicList([[c.get("userAddedTopicList") or {} for c in lcl] for lcl in self.json])

    @cached_property
    def agents(self) -> LinkedAgentList:
        """Linked communities users agents profiles."""
        return LinkedAgentList([[c.get("agent") or {} for c in lcl] for lcl in self.json])

    @cached_property
    def aminoIds(self) -> List[List[str]]:
        """Linked communities amino ids."""
        return [[c.get("endpoint") for c in lcl] for lcl in self.json]

    @cached_property
    def communityIds(self) -> List[List[int]]:
        """Linked communities ids."""
        return [[c.get("ndcId") for c in lcl] for lcl in self.json]

    @cached_property
    def createdTimes(self) -> List[List[str]]:
        """Linked communities created dates."""
        return [[c.get("createdTime") for c in lcl] for lcl in self.json]

    @cached_property
    def descriptions(self) -> List[List[str]]:
        """Linked communites descriptions."""
        return [[c.get("tagline") for c in lcl] for lcl in self.json]

    @cached_property
    def heats(self) -> List[List[int]]:
        """Linked communities heats."""
        return [[c.get("communityHeat") or 0 for c in lcl] for lcl in self.json]

    @cached_property
    def icons(self) -> List[List[str]]:
        """Linked communites icon urls."""
        return [[c.get("icon") for c in lcl] for lcl in self.json]

    @cached_property
    def joinTypes(self) -> List[List[int]]:
        """Linked communities join types."""
        return [[c.get("joinType") for c in lcl] for lcl in self.json]

    @cached_property
    def primaryLanguages(self) -> List[List[str]]:
        """Linked communities languages."""
        return [[c.get("primaryLanguage") for c in lcl] for lcl in self.json]

    @cached_property
    def links(self) -> List[List[str]]:
        """Linked communities links."""
        return [[c.get("link") for c in lcl] for lcl in self.json]

    @cached_property
    def listedStatuses(self) -> List[List[int]]:
        """Linked communities listed status."""
        return [[c.get("listedStatus") for c in lcl] for lcl in self.json]

    @cached_property
    def members(self) -> List[List[int]]:
        """Linked communities members counts."""
        return [[c.get("membersCount") or 0 for c in lcl] for lcl in self.json]

    @cached_property
    def modifiedTimes(self) -> List[List[str]]:
        """Linked communities modified times."""
        return [[c.get("modifiedTime") for c in lcl] for lcl in self.json]

    @cached_property
    def names(self) -> List[List[str]]:
        """Linked communities names."""
        return [[c.get("name") for c in lcl] for lcl in self.json]

    @cached_property
    def probationStatuses(self) -> List[List[int]]:
        """Linked communities probation status."""
        return [[c.get("probationStatus") or 0 for c in lcl] for lcl in self.json]

    @cached_property
    def promotionalMedias(self) -> LinkedPromotionalMediaList:
        """Linked communities promotional medias."""
        return LinkedPromotionalMediaList([[c.get("promotionalMediaList") or [] for c in lcl] for lcl in self.json])

    @cached_property
    def statuses(self) -> List[List[int]]:
        """Linked communities status."""
        return [[c.get("status") or 0 for c in lcl] for lcl in self.json]

    @cached_property
    def templateIds(self) -> List[List[str]]:
        """Linked communities template ids."""
        return [[c.get("templateId") for c in lcl] for lcl in self.json]

    @cached_property
    def themePacks(self) -> LinkedThemePackList:
        """Linked communities theme packs."""
        return LinkedThemePackList([[c.get("themePack") or {} for c in lcl] for lcl in self.json])

    @cached_property
    def updatedTimes(self) -> List[List[str]]:
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

    @cached_property
    def types(self) -> List[List[int]]:
        return [[m[0] if m else None for m in ml] for ml in self.json]

    @cached_property
    def urls(self) -> List[List[str]]:
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
    followingsCount: List[`int`]
        Users following counts.
    followingStatus: List[:class:`int`]
        Following status.
    frame: :class:`AvatarFrameList`
        Avatar frames.
    frameId: List[:class:`str`]
        User avatar frame ids.
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

    @cached_property
    def accountMembershipStatuses(self) -> List[int]:
        return [up.get("accountMembershipStatus") or 0 for up in self.json]

    @cached_property
    def acpDeeplinks(self) -> List[Optional[str]]:
        return self.extensions.acpDeeplinks

    @cached_property
    def adminLogCountIn7Days(self):
        return [up.get("adminLogCountIn7Days") for up in self.json]

    @cached_property
    def aminoIds(self) -> List[str]:
        return [up.get("aminoId") for up in self.json]

    @cached_property
    def areGlobal(self) -> List[bool]:
        return [up.get("isGlobal") for up in self.json]

    @cached_property
    def bios(self) -> List[Optional[str]]:
        return [up.get("content") or 0 for up in self.json]

    @cached_property
    def blogs(self) -> List[int]:
        return [up.get("blogsCount") or 0 for up in self.json]

    @cached_property
    def comunityIds(self) -> List[Optional[int]]:
        return [up.get("ndcId") or None for up in self.json]

    @cached_property
    def comments(self) -> List[int]:
        """Comments counts."""
        return [up.get("commentsCount") or 0 for up in self.json]

    @cached_property
    def consecutiveCheckInDays(self):
        return [up.get("consecutiveCheckInDays") for up in self.json]

    @cached_property
    def createdTimes(self) -> List[str]:
        return [up.get("createdTime") for up in self.json]

    @cached_property
    def creatorDeeplinks(self) -> Optional[str]:
        return self.extensions.creatorDeeplinks

    @cached_property
    def extensions(self) -> ExtensionList:
        return ExtensionList([up.get("extensions") or {} for up in self.json])

    @cached_property
    def followers(self) -> List[int]:
        return [up.get("membersCount") for up in self.json]

    @cached_property
    def followings(self) -> List[int]:
        return [up.get("joinedCount") for up in self.json]

    @cached_property
    def followingsStatus(self) -> List[int]:
        return [up.get("followingStatus") for up in self.json]

    @cached_property
    def frames(self) -> AvatarFrameList:
        return AvatarFrameList([up.get("avatarFrame") or {} for up in self.json])

    @cached_property
    def frameIds(self) -> List[str]:
        """User avatar frame ids."""
        return [up.get('avatarFrameId') for up in self.json] or self.frames.ids

    @cached_property
    def ids(self) -> List[str]:
        return [up.get("uid") for up in self.json]

    @cached_property
    def icons(self) -> List[str]:
        return [up.get("icon") for up in self.json]

    @cached_property
    def influencers(self) -> InfluencerInfoList:
        return InfluencerInfoList([i.get('influencerInfo') for i in self.json])

    @cached_property
    def levels(self) -> List[int]:
        return [up.get("level") or 0 for up in self.json]

    @cached_property
    def linkedCommunities(self) -> LinkedCommunityList:
        return LinkedCommunityList([up.get("linkedCommunityList") or [] for up in self.json])

    @cached_property
    def medias(self) -> MediaList:
        return MediaList([up.get("mediaList") or [] for up in self.json])

    @cached_property
    def membershipStatuses(self) -> List[int]:
        return [up.get("membershipStatus") or 0 for up in self.json]

    @cached_property
    def modifiedTimes(self) -> List[str]:
        return [up.get("modifiedTime") for up in self.json]

    @cached_property
    def moods(self):
        return [up.get("mood") for up in self.json]

    @cached_property
    def moodStickers(self):
        return [up.get("moodSticker") for up in self.json]

    @cached_property
    def nicknames(self) -> List[str]:
        return [up.get("nickname") for up in self.json]

    @cached_property
    def nicknamesVerified(self) -> List[bool]:
        return [up.get("isNicknameVerified") for up in self.json]

    @cached_property
    def notifSubStatuses(self) -> List[int]:  # [0, 1]
        return [up.get("notificationSubscriptionStatus") for up in self.json]

    @cached_property
    def onlineStatuses(self) -> List[int]:
        return [up.get("onlineStatus") for up in self.json]

    @cached_property
    def posts(self) -> List[int]:
        return [up.get("postsCount") or 0 for up in self.json]

    @cached_property
    def privilegesOfChatRequest(self) -> List[int]:
        return self.extensions.privilegesOfChatRequest

    @cached_property
    def pushEnabled(self) -> List[bool]:
        return [up.get("pushEnabled") for up in self.json]

    @cached_property
    def reputations(self) -> List[int]:
        return [up.get("reputation") or 0 for up in self.json]

    @cached_property
    def roles(self) -> List[int]:
        return [up.get("role") for up in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [up.get("status") for up in self.json]

    @cached_property
    def stories(self) -> List[int]:
        return [up.get("storiesCount") or 0 for up in self.json]

    @cached_property
    def styles(self) -> StyleList:
        return self.extensions.styles

    @cached_property
    def wikis(self) -> List[int]:
        return [up.get("itemsCount") for up in self.json]


@dataclass(repr=False)
class AuthorList:
    json: List[dict]

    @cached_property
    def accountMembershipStatuses(self) -> List[int]:
        return [author.get('accountMembershipStatus') for author in self.json]

    @cached_property
    def areGlobal(self) -> List[bool]:
        return [author.get('isGlobal') for author in self.json]

    @cached_property
    def communityIds(self) -> List[int]:
        return [author.get('ndcId') for author in self.json]

    @cached_property
    def followers(self) -> List[int]:
        return [author.get('membersCount') for author in self.json]

    @cached_property
    def followingStatuses(self) -> List[int]:
        return [author.get('followingStatus') for author in self.json]

    @cached_property
    def frames(self) -> AvatarFrameList:
        return AvatarFrameList([author.get('avatarFrame') or {} for author in self.json])

    @cached_property
    def frameIds(self) -> List[str]:
        return [author.get('avatarFrameId') for author in self.json] or self.frames.ids

    @cached_property
    def icons(self) -> List[str]:
        return [author.get('icon') for author in self.json]

    @cached_property
    def ids(self) -> List[str]:
        """User ids."""
        return [author.get('uid') for author in self.json]

    @cached_property
    def levels(self) -> List[int]:
        return [author.get('level') for author in self.json]

    @cached_property
    def membershipStatuses(self) -> List[int]:
        return [author.get('membershipStatus') for author in self.json]

    @cached_property
    def nicknames(self) -> List[str]:
        return [author.get('nickname') for author in self.json]

    @cached_property
    def nicknameVerified(self) -> List[bool]:
        return [author.get('isNicknameVerified') for author in self.json]

    @cached_property
    def reputations(self) -> List[int]:
        return [author.get('reputation') for author in self.json]

    @cached_property
    def roles(self) -> List[int]:
        return [author.get('role') for author in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [author.get('status') for author in self.json]
