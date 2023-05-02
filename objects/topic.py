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
from typing import List, Optional

__all__ = ('Topic',)


@dataclass(repr=False)
class Style:
    json: dict

    @cached_property
    def backgroundColor(self) -> Optional[str]:
        return self.json.get('backgroundColor')

    @cached_property
    def backgroundImage(self) -> Optional[str]:
        return self.json.get('backgroundImage')


@dataclass(repr=False)
class TabList:
    json: List[dict]

    @cached_property
    def keys(self) -> List[str]:
        return [t.get('tabKey') for t in self.json]

    @cached_property
    def titles(self) -> List[str]:
        return [t.get('title') for t in self.json]


@dataclass(repr=False)
class SubTopicList:
    json: List[dict]


@dataclass(repr=False)
class AliasTopicList:
    json: List[dict]


@dataclass(repr=False)
class ActiveInfo:
    json: dict

    @cached_property
    def membersCount(self) -> int:
        return self.json.get('memberCount')


@dataclass(repr=False)
class Topic:
    json: dict

    @cached_property
    def activeInfo(self) -> ActiveInfo:
        return ActiveInfo(self.json.get('activeInfo') or {})

    @cached_property
    def advancedCommunityStatus(self) -> int:
        return self.json.get('advancedCommunityStatus')

    @cached_property
    def advancedStatus(self) -> int:
        return self.json.get('advancedStatus')

    @cached_property
    def aliasTopics(self) -> AliasTopicList:
        return AliasTopicList(self.json.get('aliasTopicList') or [])

    @cached_property
    def chatStatus(self) -> int:
        return self.json.get('chatStatus')

    @cached_property
    def contentPoolId(self) -> str:
        """Content language."""
        return self.json.get('contentPoolId')

    @cached_property
    def coverImage(self) -> Optional[str]:
        return self.json.get('coverImage')

    @cached_property
    def createdTime(self) -> int:
        return self.json.get('createdTime')

    @cached_property
    def id(self) -> int:
        return self.json.get('topicId')

    @cached_property
    def invalid(self) -> bool:
        return self.json.get('invalid')

    @cached_property
    def isAlias(self) -> bool:
        return self.json.get('isAlias')

    @cached_property
    def isBookmarked(self) -> bool:
        return self.json.get('isBookmarked')

    @cached_property
    def isLocked(self) -> bool:
        return self.json.get('isLocked')

    @cached_property
    def isOfficial(self) -> bool:
        return self.json.get('isOfficial')

    @cached_property
    def landingTab(self) -> str:
        return self.json.get('landingTab')

    @cached_property
    def name(self) -> str:
        return self.json.get('name')

    @cached_property
    def scope(self) -> int:
        return self.json.get('scope')

    @cached_property
    def status(self) -> int:
        return self.json.get('status')

    @cached_property
    def storyCount(self) -> int:
        return self.json.get('storyCount')

    @cached_property
    def storyId(self) -> Optional[str]:
        return self.json.get('storyId')

    @cached_property
    def style(self) -> Style:
        return Style(self.json.get('style') or {})

    @cached_property
    def subscriptionStatus(self) -> int:
        return self.json.get('subscriptionStatus')

    @cached_property
    def tabs(self) -> TabList:
        return TabList(self.json.get('tabList') or [])

    @cached_property
    def visibility(self) -> int:
        return self.json.get('visibility')
