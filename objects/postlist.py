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
from typing import List, Tuple, Optional
from ujson import loads
from .userprofilelist import AuthorList
from ..enums import ObjectType

__all__ = ('PostList',)


@dataclass(repr=False)
class MediaList:
    json: List[List[Tuple[int, str, Optional[str], Optional[str]]]]

    @cached_property
    def captions(self) -> List[List[Optional[str]]]:
        return [[media[2] for media in medias] for medias in self.json]

    @cached_property
    def ids(self) -> List[List[Optional[str]]]:
        return [[media[3] for media in medias] for medias in self.json]

    @cached_property
    def types(self) -> List[List[int]]:
        return [[media[0] for media in medias] for medias in self.json]

    @cached_property
    def urls(self) -> List[List[str]]:
        return [[media[1] for media in medias] for medias in self.json]


@dataclass(repr=False)
class TipCustomOption:
    json: List[dict]
    
    @cached_property
    def icons(self) -> List[str]:
        return [custom.get('icon') for custom in self.json]

    @cached_property
    def values(self) -> List[Optional[int]]:
        return [custom.get('value') for custom in self.json]


@dataclass(repr=False)
class TipOptionList:
    json: List[List[dict]]

    @cached_property
    def icons(self) -> List[List[str]]:
        return [[option.get('icon') for option in options] for options in self.json]

    @cached_property
    def values(self) -> List[List[int]]:
        return [[option.get('value') for option in options] for options in self.json]


@dataclass(repr=False)
class TipInfo:
    json: List[dict]

    @cached_property
    def customOptions(self) -> TipCustomOption:
        return TipCustomOption([ti.get('tipCustomOption') or {} for ti in self.json])

    @cached_property
    def maxCoins(self) -> List[int]:
        return [ti.get('tipMaxCoin') for ti in self.json]

    @cached_property
    def minCoins(self) -> List[int]:
        return [ti.get('tipMinCoin') for ti in self.json]

    @cached_property
    def options(self) -> TipOptionList:
        return TipOptionList([ti.get('tipOptionList') or [] for ti in self.json])

    @cached_property
    def tippables(self) -> List[bool]:
        return [ti.get('tippable') for ti in self.json]

    @cached_property
    def tippedCoins(self) -> int:
        return [ti.get('tippedCoins') for ti in self.json]

    @cached_property
    def tippersCounts(self) -> List[int]:
        return [ti.get('tippersCount') for ti in self.json]


@dataclass(repr=False)
class HeadlineStyle:
    json: List[dict]

    @cached_property
    def displayTimeIndicator(self) -> List[bool]:
        return [hs.get('displayTimeIndicator') for hs in self.json]

    @cached_property
    def layouts(self) -> List[int]:
        return [hs.get('layout') for hs in self.json]


@dataclass(repr=False)
class BackgroundMediaList:
    json: List[List[Tuple[int, str, Optional[str]]]]

    @cached_property
    def types(self) -> List[str]:
        return [bm[0][0] if bm else None for bm in self.json]

    @cached_property
    def urls(self) -> List[str]:
        return [bm[0][1] if bm else None for bm in self.json]


@dataclass(repr=False)
class StyleList:
    json: List[dict]

    @cached_property
    def coverMediaIndexLists(self) -> List[int]:
        return [s.get('coverMediaIndexList') for s in self.json]

    @cached_property
    def backgrounds(self) -> BackgroundMediaList:
        return BackgroundMediaList([s.get('backgroundMediaList') or [] for s in self.json])

    @cached_property
    def backgroundsColors(self) -> List[Optional[str]]:
        return [s.get('backgroundColor') for s in self.json]


@dataclass(repr=False)
class PageSnippet:
    json: List[dict]

    @cached_property
    def bodies(self) -> List[str]:
        return [ps.get('body') for ps in self.json]

    @cached_property
    def deepLinks(self) -> List[Optional[str]]:
        return [ps.get('deepLink') for ps in self.json]

    @cached_property
    def links(self) -> List[str]:
        return [ps.get('link') for ps in self.json]

    @cached_property
    def medias(self) -> MediaList:
        return MediaList([ps.get('mediaList') or [] for ps in self.json])

    @cached_property
    def sources(self) -> List[str]:
        return [ps.get('source') for ps in self.json]

    @cached_property
    def titles(self) -> List[str]:
        return [ps.get('title') for ps in self.json]


@dataclass(repr=False)
class Extensions:
    json: List[dict]

    @cached_property
    def fansOnly(self) -> List[bool]:
        return [ex.get('fansOnly') for ex in self.json]

    @cached_property
    def featuredType(self) -> Optional[int]:
        return [ex.get('featuredType') for ex in self.json]

    @cached_property
    def headlineStyles(self) -> HeadlineStyle:
        return HeadlineStyle([ex.get('headlineStyle') or {} for ex in self.json])

    @cached_property
    def page(self) -> PageSnippet:
        return PageSnippet([ex.get('pageSnippet') or {} for ex in self.json])

    @cached_property
    def privilegeOfCommentOnPost(self) -> List[int]:
        return [ex.get('privilegeOfCommentOnPost') for ex in self.json]

    @cached_property
    def styles(self) -> StyleList:
        return StyleList([ex.get('style') for ex in self.json])


@dataclass(repr=False)
class RefObject:
    json: List[dict]

    @cached_property
    def authors(self) -> AuthorList:
        return AuthorList([ro.get('author') or {} for ro in self.json])

    @cached_property
    def commentsCount(self) -> List[int]:
        return [ro.get('commentsCount') for ro in self.json]

    @cached_property
    def communityId(self) -> List[int]:
        return [ro.get('ndcId') for ro in self.json]

    @cached_property
    def contents(self) -> List[str]:
        return [ro.get('content') for ro in self.json]

    @cached_property
    def contentsRatings(self) -> List[int]:
        return [ro.get('contentRating') for ro in self.json]

    @cached_property
    def createdTime(self) -> List[str]:
        return [ro.get('createdTime') for ro in self.json]

    @cached_property
    def endTime(self) -> List[Optional[str]]:
        return [ro.get('endTime') for ro in self.json]

    @cached_property
    def globalCommentsCounts(self) -> List[int]:
        return [ro.get('globalCommentsCount') for ro in self.json]

    @cached_property
    def globalVotesCounts(self) -> List[int]:
        return [ro.get('globalVotesCount') for ro in self.json]

    @cached_property
    def globalVotedValues(self) -> List[int]:
        return [ro.get('globalVotedValue') for ro in self.json]

    @cached_property
    def guestVotesCounts(self) -> List[int]:
        return [ro.get('guestVotesCount') for ro in self.json]

    @cached_property
    def ids(self) -> List[str]:
        return [ro.get('blogId') for ro in self.json]

    @cached_property
    def medias(self) -> MediaList:
        return MediaList([ro.get('mediaList') or [] for ro in self.json])

    @cached_property
    def modifiedTimes(self) -> List[str]:
        return [ro.get('modifiedTime') for ro in self.json]

    @cached_property
    def needHidden(self) -> List[bool]:
        """< PLURALIZE >"""
        return [ro.get('needHidden') for ro in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [ro.get('status') for ro in self.json]

    @cached_property
    def styles(self) -> List[int]:
        return [ro.get('style') for ro in self.json]

    @cached_property
    def types(self) -> List[int]:
        """Object types."""
        return [ro.get('type') for ro in self.json]

    @cached_property
    def votedValue(self) -> List[int]:
        return [ro.get('votedValue') for ro in self.json]

    @cached_property
    def tip(self) -> TipInfo:
        return TipInfo([ro.get('tipInfo') or {} for ro in self.json])

    @cached_property
    def title(self) -> List[str]:
        return [ro.get('title') for ro in self.json]

    @cached_property
    def totalPollVoteCounts(self) -> List[int]:
        return [ro.get('totalPollVoteCount') for ro in self.json]

    @cached_property
    def totalQuizPlayCounts(self) -> List[int]:
        return [ro.get('totalQuizPlayCount') for ro in self.json]

    @cached_property
    def keywords(self) -> List[str]:
        return [ro.get('keywords') for ro in self.json]

    @cached_property
    def viewCounts(self) -> List[int]:
        return [ro.get('viewCount') for ro in self.json]

    @cached_property
    def votesCount(self) -> List[int]:
        return [ro.get('votesCount') for ro in self.json]

    @cached_property
    def widgetDisplayIntervals(self) -> Optional[float]:
        return [ro.get('widgetDisplayInterval') for ro in self.json]


@dataclass(repr=False)
class PostList:
    json: List[dict]

    @cached_property
    def authors(self) -> AuthorList:
        return AuthorList([post.get('author') or {} for post in self.json])

    @cached_property
    def commentsCounts(self) -> List[int]:
        return [post.get('commentsCount') for post in self.json]

    @cached_property
    def communityIds(self) -> List[int]:
        return [post.get('ndcId') for post in self.json]

    @cached_property
    def contents(self) -> List[str]:
        return [post.get('content') for post in self.json]

    @cached_property
    def createdTimes(self) -> List[str]:
        return [post.get('createdTime') for post in self.json]

    @cached_property
    def globalCommentsCounts(self) -> List[int]:
        return [post.get('globalCommentsCount') for post in self.json]

    @cached_property
    def globalVotedValues(self) -> List[int]:
        return [post.get('globalVotedValue') for post in self.json]

    @cached_property
    def globalVotesCounts(self) -> List[int]:
        return [post.get('globalVotesCount') for post in self.json]

    @cached_property
    def medias(self) -> MediaList:
        return MediaList([post.get('mediaList') for post in self.json])

    @cached_property
    def refObject(self) -> RefObject:
        """Reference object."""
        return RefObject([post.get('refObject') or {} for post in self.json])

    @cached_property
    def refObjectIds(self) -> List[str]:
        return [post.get('refObjectId') for post in self.json]

    @cached_property
    def refObjectSubtypes(self) -> List[int]:
        return [post.get('refObjectSubtype') for post in self.json]

    @cached_property
    def refObjectTypes(self) -> List[ObjectType]:
        return [ObjectType(post.get('refObjectType') or 1) for post in self.json]

    @cached_property
    def scores(self) -> List[float]:
        return [post.get('score') for post in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [post.get('status') for post in self.json]

    @cached_property
    def strategyInfo(self) -> List[dict]:
        return [loads(post['strategyInfo']) if post.get('strategyInfo') else {} for post in self.json]

    @cached_property
    def titles(self) -> List[str]:
        return [post.get('title') for post in self.json]

    @cached_property
    def votesCounts(self) -> List[int]:
        return [post.get('votesCount') for post in self.json]

    @cached_property
    def votedValues(self) -> List[int]:
        return [post.get('votedValue') for post in self.json]
