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
from typing import List, Literal, Optional, Tuple
from ujson import loads
from .userprofilelist import AuthorList as _AuthorList

__all__ = ('ThreadList',)


@dataclass(repr=False)
class AliasTopicList:
    json: List[List[List[dict]]]


@dataclass(repr=False)
class SubTopicList:
    json: List[List[dict]]


@dataclass(repr=False)
class TabList:
    json: List[List[dict]]


class AuthorList(_AuthorList):
    pass


@dataclass(repr=False)
class BackgroundMediaList:
    json: List[List[List[Tuple[int, str, None, None, None, dict]]]]

    @cached_property
    def types(self) -> List[List[Optional[str]]]:
        return [[bg[0][0] if (bg and bg[0]) else None for bg in bgs] for bgs in self.json]

    @cached_property
    def urls(self) -> List[List[Optional[str]]]:
        return [[bg[0][1] if (bg and bg[0]) else None for bg in bgs] for bgs in self.json]


@dataclass(repr=False)
class Style:
    json: List[List[dict]]

    @cached_property
    def backgrounds(self) -> BackgroundMediaList:
        return BackgroundMediaList([[s.get("backgroundMediaList") or [] for s in sl] for sl in self.json])

    @cached_property
    def backgroundUrls(self) -> List[List[Optional[str]]]:
        return self.backgrounds.urls


@dataclass(repr=False)
class AddedTopicList:
    json: List[List[dict]]


    @cached_property
    def advancedCommunityStatuses(self) -> List[List[int]]:
        return [[at.get('advancedCommunityStatus') for at in atl] for atl in self.json]

    @cached_property
    def advancedStatuses(self) -> List[List[int]]:
        return [[at.get('advancedStatus') for at in atl] for atl in self.json]

    @cached_property
    def aliasTopics(self) -> AliasTopicList:
        return AliasTopicList([[at.get('aliasTopicList') or [] for at in atl] for atl in self.json])

    @cached_property
    def areAliases(self) -> List[List[bool]]:
        return [[at.get('isAlias') for at in atl] for atl in self.json]

    @cached_property
    def areLocked(self) -> List[List[bool]]:
        return [[at.get('isLocked') for at in atl] for atl in self.json]

    @cached_property
    def areOfficial(self) -> List[List[bool]]:
        return [[at.get('isOfficial') for at in atl] for atl in self.json]

    @cached_property
    def chatsStatuses(self) -> List[List[int]]:
        return [[at.get('chatStatus') for at in atl] for atl in self.json]

    @cached_property
    def contentPoolIds(self) -> List[List[str]]:
        """Content language."""
        return [[at.get('contentPoolId') for at in atl] for atl in self.json]

    @cached_property
    def coverImages(self) -> List[List[str]]:
        return [[at.get('coverImage') for at in atl] for atl in self.json]

    @cached_property
    def ids(self) -> List[List[int]]:
        return [[at.get('topicId') for at in atl] for atl in self.json]

    @cached_property
    def increaseIds(self) -> List[List[int]]:
        return [[at.get('increaseId') for at in atl] for atl in self.json]

    @cached_property
    def mappingScores(self) -> List[List[int]]:
        return [[at.get('objectMappingScore') for at in atl] for atl in self.json]

    @cached_property
    def names(self) -> List[List[str]]:
        return [[at.get('name') for at in atl] for atl in self.json]

    @cached_property
    def scopes(self) -> List[List[int]]:
        return [[at.get('scope') for at in atl] for atl in self.json]

    @cached_property
    def statuses(self) -> List[List[int]]:
        return [[at.get('status') for at in atl] for atl in self.json]

    @cached_property
    def sources(self) -> List[List[int]]:
        return [[at.get('source') for at in atl] for atl in self.json]

    @cached_property
    def storyIds(self) -> List[List[int]]:
        return [[at.get('storyId') for at in atl] for atl in self.json]

    @cached_property
    def styles(self) -> Style:
        return Style([[at.get('style') or {} for at in atl] for atl in self.json])

    @cached_property
    def subTopics(self) -> SubTopicList:
        return SubTopicList([[at.get('subTopicList') or [] for at in atl] for atl in self.json])

    @cached_property
    def tab(self) -> TabList:
        return TabList([[at.get('tabList') or [] for at in atl] for atl in self.json])

    @cached_property
    def visibilities(self) -> List[List[int]]:
        return [[at.get('visibility') for at in atl] for atl in self.json]


@dataclass(repr=False)
class LastMessageSummary:
    json: List[dict]

    @cached_property
    def authorIds(self) -> List[str]:
        return [m.get('uid') for m in self.json]

    @cached_property
    def contents(self) -> List[Optional[str]]:
        return [m.get('content') for m in self.json]

    @cached_property
    def createdTimes(self) -> List[str]:
        return [m.get('createdTime') for m in self.json]

    @cached_property
    def ids(self) -> List[str]:
        return [m.get('messageId') for m in self.json]

    @cached_property
    def areHidden(self) -> List[bool]:
        return [m.get('isHidden') for m in self.json]

    @cached_property
    def medias(self) -> List[Optional[str]]:
        return [m.get('mediaValue') for m in self.json]

    @cached_property
    def mediaTypes(self) -> List[int]:
        return [m.get('mediaType') or 0 for m in self.json]

    @cached_property
    def types(self) -> List[int]:
        return [m.get('type') for m in self.json]


@dataclass(repr=False)
class BackgroundMedia:
    json: List[Tuple[int, str, Optional[str]]]

    @cached_property
    def types(self) -> List[int]:
        return [bm[0] if bm else None for bm in self.json]

    @cached_property
    def urls(self) -> List[str]:
        return [bm[1] if bm else None for bm in self.json]


@dataclass(repr=False)
class Extensions:
    json: List[dict]

    @cached_property
    def announcements(self) -> List[Optional[str]]:
        return [e.get('announcement') for e in self.json]

    @cached_property
    def announcementsPinned(self) -> List[bool]:
        return [e.get('pinAnnouncement') for e in self.json]

    @cached_property
    def backgrounds(self) -> BackgroundMedia:
        return BackgroundMedia(*[e.get('bm') or [] for e in self.json])

    @cached_property
    def bannedIds(self) -> List[List[str]]:
        """Banned member user id list."""
        return [e.get('bannedMemberUidList') or [] for e in self.json]

    @cached_property
    def channelCreatedTimes(self) -> List[Optional[str]]:
        return [e.get('channelTypeLastCreatedTime') for e in self.json]

    @cached_property
    def channelsIds(self) -> List[Optional[str]]:
        return [e.get('avchatId') for e in self.json]

    @cached_property
    def channelsJoinTypes(self) -> List[int]:
        return [e.get('vvChatJoinType') for e in self.json]

    @cached_property
    def channelsMembersIds(self) -> List[List[str]]:
        return [e.get('avchatMemberUidList') or [] for e in self.json]

    @cached_property
    def channelsTypes(self) -> List[int]:
        return [e.get('channelType') or 0 for e in self.json]

    @cached_property
    def coHosts(self) -> List[List[str]]:
        """User id list."""
        return [e.get('coHost') or [] for e in self.json]

    @cached_property
    def creatorIds(self) -> List[str]:
        return [e.get('creatorUid') for e in self.json]

    @cached_property
    def languages(self) -> List[str]:
        return [e.get('language') for e in self.json]

    @cached_property
    def lastMembersUpdateTimes(self) -> List[int]:
        return [e.get('lastMembersSummaryUpdateTime') for e in self.json]

    @cached_property
    def membersCanInvite(self) -> List[bool]:
        return [e.get('membersCanInvite') for e in self.json]

    @cached_property
    def onlyFans(self) -> List[bool]:
        return [e.get('fansOnly') for e in self.json]

    @cached_property
    def screeningRoomHostIds(self) -> List[str]:
        return [e.get('screeningRoomHostUid') for e in self.json]

    @cached_property
    def viewOnly(self) -> List[bool]:
        return [e.get('viewOnly') for e in self.json]

    @cached_property
    def visibilities(self) -> List[int]:
        return [e.get('visibility') for e in self.json]


@dataclass(repr=False)
class MembersSummary:
    json: List[List[dict]]

    @cached_property
    def icons(self) -> List[List[str]]:
        return [[m.get('icon') for m in ml] for ml in self.json]

    @cached_property
    def ids(self) -> List[List[str]]:
        return [[m.get('uid') for m in ml] for ml in self.json]

    @cached_property
    def membershipStatuses(self) -> List[List[int]]:
        return [[m.get('membershipStatus') for m in ml] for ml in self.json]

    @cached_property
    def nicknames(self) -> List[List[str]]:
        return [[m.get('nickname') for m in ml] for ml in self.json]

    @cached_property
    def roles(self) -> List[List[int]]:
        return [[m.get('role') for m in ml] for ml in self.json]

    @cached_property
    def statuses(self) -> List[List[int]]:
        return [[m.get('status') for m in ml] for ml in self.json]


@dataclass(repr=False)
class TipOptionList:
    json: List[List[dict]]

    @cached_property
    def icons(self) -> List[List[str]]:
        return [[o.get('icon') for o in ol] for ol in self.json]

    @cached_property
    def values(self) -> List[List[int]]:
        return [[o.get('value') for o in ol] for ol in self.json]


@dataclass(repr=False)
class tipCustomOption:
    json: List[dict]

    @cached_property
    def icons(self) -> List[str]:
        return [co.get('icon') for co in self.json]

    @cached_property
    def values(self) -> List[Optional[int]]:
        return [co.get('value') for co in self.json]


@dataclass(repr=False)
class TipInfo:
    json: List[dict]

    @cached_property
    def maxCoins(self) -> List[int]:
        return [t.get('tipMaxCoin') for t in self.json]

    @cached_property
    def minCoins(self) -> List[int]:
        return [t.get('tipMinCoin') for t in self.json]

    @cached_property
    def options(self) -> TipOptionList:
        return TipOptionList([t.get('tipOptionList') or [] for t in self.json])

    @cached_property
    def tippables(self) -> List[bool]:
        return [t.get('tippable') for t in self.json]

    @cached_property
    def tippedCoins(self) -> List[float]:
        return [t.get('tippedCoins') for t in self.json]

    @cached_property
    def tippers(self) -> List[int]:
        """Tippers members count."""
        return [t.get('tippersCount') for t in self.json]


@dataclass(repr=False)
class ThreadList:
    json: List[dict]

    @cached_property
    def addedTopics(self) -> AddedTopicList:
        return AddedTopicList([t.get('userAddedTopicList') or [] for t in self.json])

    @cached_property
    def alertOptions(self) -> List[int]:
        return [th.get('alertOption') for th in self.json]

    @cached_property
    def coHosts(self) -> List[List[str]]:
        """Chats users ids."""
        return self.extensions.coHosts

    @cached_property
    def conditions(self) -> List[int]:
        return [th.get('condition') for th in self.json]

    @cached_property
    def communityIds(self) -> List[int]:
        return [th.get('ndcId') for th in self.json]

    @cached_property
    def contents(self) -> List[str]:
        return [th.get('content') for th in self.json]

    @cached_property
    def createdTimea(self) -> List[Optional[str]]:
        return [th.get('createdTime') for th in self.json]

    @cached_property
    def hosts(self) -> AuthorList:
        return AuthorList([th.get('author') or {} for th in self.json])

    @cached_property
    def hostIds(self) -> List[str]:
        return [th.get('uid') for th in self.json]

    @cached_property
    def extensions(self) -> Extensions:
        return Extensions([th.get('extensions') or {} for th in self.json])

    @cached_property
    def icons(self) -> List[str]:
        return [th.get('icon') for th in self.json]

    @cached_property
    def ids(self) -> List[str]:
        return [th.get('threadId') for th in self.json]

    @cached_property
    def arePinned(self) -> List[bool]:
        return [th.get('isPinned') for th in self.json]

    @cached_property
    def keywords(self) -> List[Optional[str]]:
        return [th.get('keywords') for th in self.json]

    @cached_property
    def lastMessages(self) -> LastMessageSummary:
        return LastMessageSummary([th.get('lastMessageSummary') or {} for th in self.json])

    @cached_property
    def lastReadTimes(self) -> List[Optional[str]]:
        return [th.get('lastReadTime') for th in self.json]

    @cached_property
    def latestActivityTimes(self) -> List[str]:
        return [th.get('latestActivityTime') for th in self.json]

    @cached_property
    def members(self) -> MembersSummary:
        return MembersSummary([th.get('membersSummary') or [] for th in self.json])

    @cached_property
    def membersCounts(self) -> List[int]:
        return [th.get('membersCount') for th in self.json]

    @cached_property
    def membershipStatuses(self) -> List[int]:
        """Hosts membership status."""
        return [th.get('membershipStatus') for th in self.json]

    @cached_property
    def membersQuota(self) -> List[int]:
        return [th.get('membersQuota') for th in self.json]

    @cached_property
    def modifiedTimes(self) -> List[Optional[str]]:
        return [th.get('modifiedTime') for th in self.json]

    @cached_property
    def needsHidden(self) -> List[bool]:
        return [th.get('needHidden') for th in self.json]

    @cached_property
    def publishesToGlobal(self) -> List[Literal[0, 1]]:
        return [th.get('publishToGlobal') for th in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [th.get('status') for th in self.json]

    @cached_property
    def strategyInfos(self) -> List[dict]:
        return [loads(th.get('strategyInfo') or '{}') for th in self.json]

    @cached_property
    def tips(self) -> TipInfo:
        return TipInfo([th.get('tipInfo') or {} for th in self.json])

    @cached_property
    def titles(self) -> List[str]:
        return [th.get('title') for th in self.json]

    @cached_property
    def types(self) -> List[int]:
        """Chat types."""
        return [th.get('type') for th in self.json]
