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
import dataclasses
import functools
import typing

__all__ = ('CommunityList',)


@dataclasses.dataclass(repr=False)
class ActiveInfoList:
    json: typing.List[dict]


@dataclasses.dataclass(repr=False)
class StyleList:
    json: typing.List[typing.List[dict]]

    @functools.cached_property
    def backgroundColor(self) -> typing.List[typing.List[str]]:
        return [[s.get("backgroundColor") for s in sl] for sl in self.json]


@dataclasses.dataclass(repr=False)
class AddedTopicList:
    json: typing.List[typing.List[dict]]

    @functools.cached_property
    def backgroundColor(self) -> typing.List[str]:
        return self.style.backgroundColor

    @functools.cached_property
    def name(self) -> typing.List[typing.List[str]]:
        return [[t.get("name") for t in at] for at in self.json]

    @functools.cached_property
    def style(self) -> StyleList:
        return StyleList([[t.get("style") or {} for t in at] for at in self.json])

    @functools.cached_property
    def topicId(self) -> typing.List[typing.List[int]]:
        return [[t.get("topicId") for t in at] for at in self.json]


@dataclasses.dataclass(repr=False)
class AgentList:
    json: typing.List[dict]

    @functools.cached_property
    def userId(self) -> typing.List[str]:
        return [a.get("uid") for a in self.json]


@dataclasses.dataclass(repr=False)
class PromotionalMediaList:
    json: typing.List[typing.List[typing.Tuple[int, str, None]]]

    @functools.cached_property
    def url(self) -> typing.List[typing.List[str]]:
        return [[ml[1] if ml else None for ml in pm] for pm in self.json]


@dataclasses.dataclass(repr=False)
class ThemePackList:
    json: typing.List[dict]

    @functools.cached_property
    def color(self) -> typing.List[str]:
        return [tp.get("themeColor") for tp in self.json]

    @functools.cached_property
    def hash(self) -> typing.List[str]:
        return [tp.get("themePackHash") for tp in self.json]

    @functools.cached_property
    def revision(self) -> typing.List[int]:
        return [tp.get("themePackRevision") for tp in self.json]

    @functools.cached_property
    def url(self) -> typing.List[str]:
        return [tp.get("themePackUrl") for tp in self.json]


@dataclasses.dataclass(repr=False)
class CommunityList:
    json: typing.List[dict]

    @functools.cached_property
    def activeInfo(self) -> ActiveInfoList:
        return ActiveInfoList([c.get("activeInfo") or {} for c in self.json])

    @functools.cached_property
    def addedTopicList(self) -> AddedTopicList:
        return AddedTopicList([c.get("userAddedTopicList") or {} for c in self.json])

    @functools.cached_property
    def agent(self) -> AgentList:
        return AgentList([c.get("agent") or {} for c in self.json])

    @functools.cached_property
    def aminoId(self) -> typing.List[str]:
        return [c.get("endpoint") for c in self.json]

    @functools.cached_property
    def ids(self) -> typing.List[int]:
        """Communities ids."""
        return [c.get("ndcId") for c in self.json]

    @functools.cached_property
    def createdTime(self) -> typing.List[str]:
        return [c.get("createdTime") for c in self.json]

    @functools.cached_property
    def description(self) -> typing.List[str]:
        return [c.get("tagline") for c in self.json]

    @functools.cached_property
    def heat(self) -> typing.List[int]:
        return [c.get("communityHeat") or 0 for c in self.json]

    @functools.cached_property
    def icon(self) -> typing.List[str]:
        return [c.get("icon") for c in self.json]

    @functools.cached_property
    def joinType(self) -> typing.List[int]:
        return [c.get("joinType") for c in self.json]

    @functools.cached_property
    def link(self) -> typing.List[str]:
        return [c.get("link") for c in self.json]

    @functools.cached_property
    def listedStatus(self) -> typing.List[int]:
        return [c.get("listedStatus") for c in self.json]

    @functools.cached_property
    def membersCount(self) -> typing.List[int]:
        return [c.get("membersCount") or 0 for c in self.json]

    @functools.cached_property
    def modifiedTime(self) -> typing.List[str]:
        return [c.get("modifiedTime") for c in self.json]

    @functools.cached_property
    def name(self) -> typing.List[str]:
        return [c.get("name") for c in self.json]

    @functools.cached_property
    def probationStatus(self) -> typing.List[int]:
        return [c.get("probationStatus") or 0 for c in self.json]

    @functools.cached_property
    def promotionalMedia(self) -> PromotionalMediaList:
        return PromotionalMediaList([c.get("promotionalMediaList") or [] for c in self.json])

    @functools.cached_property
    def primaryLanguage(self) -> typing.List[str]:
        return [c.get("primaryLanguage") for c in self.json]

    @functools.cached_property
    def status(self) -> typing.List[int]:
        return [c.get("status") or 0 for c in self.json]

    @functools.cached_property
    def templateId(self) -> typing.List[str]:
        return [c.get("templateId") for c in self.json]

    @functools.cached_property
    def themePack(self) -> ThemePackList:
        return ThemePackList([c.get("themePack") or {} for c in self.json])

    @functools.cached_property
    def updatedTime(self) -> typing.List[str]:
        return [c.get("updatedTime") for c in self.json]
