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
from .userprofile import Author
from .userprofilelist import StyleList as _StyleList

__all__ = ('Thread',)

class Style(_StyleList):
    """Represents community chat topics styles.

    Attributes
    ----------
    json : List[:class:`dict`]
        The raw API data.
    background : :class:`BackgroundMediaList`
        Users backgrounds.
    backgroundUrl : List[Optional[:class:`str`]]
        Users background hex color codes.

    """


@dataclass(repr=False)
class AliasTopicList:
    json: list


@dataclass(repr=False)
class TabList:
    json: list


@dataclass(repr=False)
class SubTopicList:
    json: list


@dataclass(repr=False)
class UserAddedTopicList:
    json: List[dict]

    @cached_property
    def advancedCommunityStatus(self) -> List[int]:
        return [at.get('advancedCommunityStatus') for at in self.json]

    @cached_property
    def advancedStatus(self) -> List[int]:
        return [at.get('advancedStatus') for at in self.json]

    @cached_property
    def aliasTopic(self) -> AliasTopicList:
        return AliasTopicList([at.get('aliasTopicList') or [] for at in self.json])

    @cached_property
    def areAliases(self) -> List[bool]:
        return [at.get('isAlias') for at in self.json]

    @cached_property
    def areLocked(self) -> List[bool]:
        return [at.get('isLocked') for at in self.json]

    @cached_property
    def areOfficial(self) -> List[bool]:
        return [at.get('isOfficial') for at in self.json]

    @cached_property
    def chatsStatuses(self) -> List[int]:
        return [at.get('chatStatus') for at in self.json]

    @cached_property
    def contentPoolId(self) -> List[str]:
        """Content language"""
        return [at.get('contentPoolId') for at in self.json]

    @cached_property
    def coverImage(self) -> List[str]:
        return [at.get('coverImage') for at in self.json]

    @cached_property
    def ids(self) -> List[int]:
        return [at.get('topicId') for at in self.json]

    @cached_property
    def increaseIds(self) -> List[int]:
        return [at.get('increaseId') for at in self.json]

    @cached_property
    def mappingScore(self) -> List[int]:
        return [at.get('objectMappingScore') for at in self.json]

    @cached_property
    def names(self) -> List[str]:
        return [at.get('name') for at in self.json]

    @cached_property
    def scope(self) -> List[int]:
        return [at.get('scope') for at in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [at.get('status') for at in self.json]

    @cached_property
    def source(self) -> List[int]:
        return [at.get('source') for at in self.json]

    @cached_property
    def storyIds(self) -> List[int]:
        return [at.get('storyId') for at in self.json]

    @cached_property
    def styles(self) -> Style:
        return Style([at.get('style') or {} for at in self.json])

    @cached_property
    def subTopic(self) -> SubTopicList:
        return SubTopicList([at.get('subTopicList') or [] for at in self.json])

    @cached_property
    def tab(self) -> TabList:
        return TabList([at.get('tabList') or [] for at in self.json])

    @cached_property
    def visibilities(self) -> List[int]:
        return [at.get('visibility') for at in self.json]


@dataclass(repr=False)
class MembersSummary:
    json: List[dict]

    def __len__(self) -> int:
        return len(self.json)

    @cached_property
    def icons(self) -> List[str]:
        return [m.get('icon') for m in self.json]

    @cached_property
    def ids(self) -> List[str]:
        return [m.get('uid') for m in self.json]

    @cached_property
    def membershipStatuses(self) -> List[int]:
        return [m.get('membershipStatus') for m in self.json]

    @cached_property
    def nicknames(self) -> List[str]:
        return [m.get('nickname') for m in self.json]

    @cached_property
    def roles(self) -> List[int]:
        return [m.get('role') for m in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [m.get('status') for m in self.json]


@dataclass(repr=False)
class TipOptionList:
    json: List[dict]

    @cached_property
    def icons(self) -> List[str]:
        return [opt.get('icon') for opt in self.json]

    @cached_property
    def values(self) -> List[int]:
        return [opt.get('value') for opt in self.json]


@dataclass(repr=False)
class tipCustomOption:
    json: dict

    @cached_property
    def icon(self) -> str:
        return self.json.get('icon')

    @cached_property
    def value(self) -> Optional[int]:
        return self.json.get('value')

@dataclass(repr=False)
class TipInfo:
    json: dict

    @cached_property
    def maxCoins(self) -> int:
        return self.json.get('tipMaxCoin')

    @cached_property
    def minCoins(self) -> int:
        return self.json.get('tipMinCoin')

    @cached_property
    def options(self) -> TipOptionList:
        return TipOptionList(self.json.get('tipOptionList') or [])

    @cached_property
    def tippable(self) -> bool:
        return self.json.get('tippable')

    @cached_property
    def tippedCoins(self) -> float:
        return self.json.get('tippedCoins')

    @cached_property
    def tippersCount(self) -> int:
        """Tippers members count."""
        return self.json.get('tippersCount')

@dataclass(repr=False)
class LastMessageSummary:
    json: dict

    @cached_property
    def authorId(self) -> str:
        return self.json.get('uid')

    @cached_property
    def content(self) -> Optional[str]:
        return self.json.get('content')

    @cached_property
    def createdTime(self) -> str:
        return self.json.get('createdTime')

    @cached_property
    def id(self) -> str:
        return self.json.get('messageId')

    @cached_property
    def isHidden(self) -> bool:
        return self.json.get('isHidden')

    @cached_property
    def media(self) -> Optional[str]:
        return self.json.get('mediaValue')

    @cached_property
    def mediaType(self) -> int:
        return self.json.get('mediaType') or 0

    @cached_property
    def type(self) -> int:
        return self.json.get('type')


@dataclass(repr=False)
class ScreeningRoomPermission:
    json: dict

    @cached_property
    def action(self) -> int:
        return self.json.get('action')

    @cached_property
    def userIds(self) -> List[str]:
        return self.json.get('uidList') or []


@dataclass(repr=False)
class BackgroundMedia:
    json: Tuple[int, str, Optional[str]]

    @cached_property
    def type(self) -> int:
        return self.json[0] if self.json else None

    @cached_property
    def url(self) -> str:
        return self.json[1] if self.json else None


@dataclass(repr=False)
class Extensions:
    json: dict

    @cached_property
    def announcement(self) -> Optional[str]:
        return self.json.get('announcement')

    @cached_property
    def announcementPinned(self) -> bool:
        return self.json.get('pinAnnouncement')

    @cached_property
    def background(self) -> BackgroundMedia:
        return BackgroundMedia(*self.json.get('bm') or [])

    @cached_property
    def bannedIds(self) -> List[str]:
        """Banned member user id list."""
        return self.json.get('bannedMemberUidList') or []

    @cached_property
    def channelCreatedTime(self) -> Optional[str]:
        return self.json.get('channelTypeLastCreatedTime')

    @cached_property
    def channelId(self) -> Optional[str]:
        return self.json.get('avchatId')

    @cached_property
    def channelJoinType(self) -> int:
        return self.json.get('vvChatJoinType')

    @cached_property
    def channelMembersIds(self) -> List[str]:
        return self.json.get('avchatMemberUidList') or []

    @cached_property
    def channelType(self) -> int:
        return self.json.get('channelType') or 0

    @cached_property
    def coHosts(self) -> List[str]:
        """User id list."""
        return self.json.get('coHost') or []

    @cached_property
    def creatorId(self) -> str:
        return self.json.get('creatorUid')

    @cached_property
    def language(self) -> str:
        return self.json.get('language')

    @cached_property
    def lastMembersUpdateTime(self) -> int:
        return self.json.get('lastMembersSummaryUpdateTime')

    @cached_property
    def membersCanInvite(self) -> bool:
        return self.json.get('membersCanInvite')

    @cached_property
    def onlyFans(self) -> bool:
        return self.json.get('fansOnly')

    @cached_property
    def screeningRoomHostId(self) -> str:
        # d780e629-1ec7-4c56-9974-42c515ba56c6
        return self.json.get('screeningRoomHostUid')

    @cached_property
    def viewOnly(self) -> bool:
        return self.json.get('viewOnly')

    @cached_property
    def visibility(self) -> int:
        return self.json.get('visibility')


@dataclass(repr=False)
class Thread:
    json: dict

    @cached_property
    def addedTopics(self) -> UserAddedTopicList:
        return UserAddedTopicList(self.json.get('userAddedTopicList') or [])

    @cached_property
    def alertOption(self) -> int:
        return self.json.get('alertOption')

    @cached_property
    def coHosts(self) -> List[str]:
        """Users ids."""
        return self.extensions.coHosts

    @cached_property
    def condition(self) -> int:
        return self.json.get('condition')

    @cached_property
    def communityId(self) -> int:
        return self.json.get('ndcId')

    @cached_property
    def content(self) -> str:
        return self.json.get('content')

    @cached_property
    def createdTime(self) -> Optional[str]:
        return self.json.get('createdTime')

    @cached_property
    def host(self) -> Author:
        """Basic user profile."""
        return Author(self.json.get('author') or {})

    @cached_property
    def hostId(self) -> str:
        """User id."""
        return self.json.get('uid')

    @cached_property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get('extensions') or {})

    @cached_property
    def icon(self) -> str:
        return self.json.get('icon')

    @cached_property
    def id(self) -> str:
        return self.json.get('threadId')

    @cached_property
    def isPinned(self) -> bool:
        return self.json.get('isPinned')

    @cached_property
    def keywords(self) -> Optional[str]:
        """Example: 'amino,role,offtopic'"""
        return self.json.get('keywords')

    @cached_property
    def lastMessage(self) -> LastMessageSummary:
        return LastMessageSummary(self.json.get('lastMessageSummary') or {})

    @cached_property
    def lastReadTime(self) -> Optional[str]:
        return self.json.get('lastReadTime')

    @cached_property
    def latestActivityTime(self) -> str:
        return self.json.get('latestActivityTime')

    @cached_property
    def members(self) -> MembersSummary:
        return MembersSummary(self.json.get('membersSummary') or [])

    @cached_property
    def membersCount(self) -> int:
        return self.json.get('membersCount')

    @cached_property
    def membershipStatus(self) -> int:
        """Host membership status."""
        return self.json.get('membershipStatus')

    @cached_property
    def membersQuota(self) -> int:
        return self.json.get('membersQuota')

    @cached_property
    def modifiedTime(self) -> Optional[str]:
        return self.json.get('modifiedTime')

    @cached_property
    def needHidden(self) -> bool:
        return self.json.get('needHidden')

    @cached_property
    def publishToGlobal(self) -> Literal[0, 1]:
        return self.json.get('publishToGlobal')

    @cached_property
    def status(self) -> int:
        return self.json.get('status')

    @cached_property
    def strategyInfo(self) -> dict:
        return loads(self.json.get('strategyInfo') or '{}')

    @cached_property
    def tip(self) -> TipInfo:
        return TipInfo(self.json.get('tipInfo') or {})

    @cached_property
    def title(self) -> str:
        return self.json.get('title')

    @cached_property
    def type(self) -> int:
        """Chat type."""
        return self.json.get('type')
