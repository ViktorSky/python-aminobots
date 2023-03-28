from typing import List, Tuple
from .object import Object

__all__ = 'CommunityList',


class ActiveInfoList(Object):
    json: List[dict]


class StyleList(Object):
    json: List[List[dict]]

    @property
    def backgroundColor(self) -> List[List[str]]:
        return [[s.get("backgroundColor") for s in sl] for sl in self.json]


class AddedTopicList(Object):
    json: List[List[dict]]

    @property
    def backgroundColor(self) -> List[str]:
        return self.style.backgroundColor

    @property
    def name(self) -> List[List[str]]:
        return [[t.get("name") for t in at] for at in self.json]

    @property
    def style(self) -> StyleList:
        return StyleList([[t.get("style") or {} for t in at] for at in self.json])

    @property
    def topicId(self) -> List[List[int]]:
        return [[t.get("topicId") for t in at] for at in self.json]


class AgentList(Object):
    json: List[dict]

    @property
    def userId(self) -> List[str]:
        return [a.get("uid") for a in self.json]


class PromotionalMediaList(Object):
    json: List[List[Tuple[int, str, None]]]

    @property
    def url(self) -> List[List[str]]:
        return [[ml[1] if ml else None for ml in pm] for pm in self.json]


class ThemePackList(Object):
    json: List[dict]

    @property
    def color(self) -> List[str]:
        return [tp.get("themeColor") for tp in self.json]

    @property
    def hash(self) -> List[str]:
        return [tp.get("themePackHash") for tp in self.json]

    @property
    def revision(self) -> List[int]:
        return [tp.get("themePackRevision") for tp in self.json]

    @property
    def url(self) -> List[str]:
        return [tp.get("themePackUrl") for tp in self.json]


class CommunityList(Object):
    json: List[dict]

    @property
    def activeInfo(self) -> ActiveInfoList:
        return ActiveInfoList([c.get("activeInfo") or {} for c in self.json])

    @property
    def addedTopicList(self) -> AddedTopicList:
        return AddedTopicList([c.get("userAddedTopicList") or {} for c in self.json])

    @property
    def agent(self) -> AgentList:
        return AgentList([c.get("agent") or {} for c in self.json])

    @property
    def aminoId(self) -> List[str]:
        return [c.get("endpoint") for c in self.json]

    @property
    def comId(self) -> List[int]:
        return [c.get("ndcId") for c in self.json]

    @property
    def createdTime(self) -> List[str]:
        return [c.get("createdTime") for c in self.json]

    @property
    def description(self) -> List[str]:
        return [c.get("tagline") for c in self.json]

    @property
    def heat(self) -> List[int]:
        return [c.get("communityHeat") or 0 for c in self.json]

    @property
    def icon(self) -> List[str]:
        return [c.get("icon") for c in self.json]

    @property
    def joinType(self) -> List[int]:
        return [c.get("joinType") for c in self.json]

    @property
    def link(self) -> List[str]:
        return [c.get("link") for c in self.json]

    @property
    def listedStatus(self) -> List[int]:
        return [c.get("listedStatus") for c in self.json]

    @property
    def membersCount(self) -> List[int]:
        return [c.get("membersCount") or 0 for c in self.json]

    @property
    def modifiedTime(self) -> List[str]:
        return [c.get("modifiedTime") for c in self.json]

    @property
    def name(self) -> List[str]:
        return [c.get("name") for c in self.json]

    @property
    def probationStatus(self) -> List[int]:
        return [c.get("probationStatus") or 0 for c in self.json]

    @property
    def promotionalMedia(self) -> PromotionalMediaList:
        return PromotionalMediaList([c.get("promotionalMediaList") or [] for c in self.json])

    @property
    def primaryLanguage(self) -> List[str]:
        return [c.get("primaryLanguage") for c in self.json]

    @property
    def status(self) -> List[int]:
        return [c.get("status") or 0 for c in self.json]

    @property
    def templateId(self) -> List[str]:
        return [c.get("templateId") for c in self.json]

    @property
    def themePack(self) -> ThemePackList:
        return ThemePackList([c.get("themePack") or {} for c in self.json])

    @property
    def updatedTime(self) -> List[str]:
        return [c.get("updatedTime") for c in self.json]
