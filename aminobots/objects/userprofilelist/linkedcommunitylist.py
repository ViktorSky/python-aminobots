from typing import List
from ..object import Object
from .linkedactiveinfolist import *
from .linkedaddedtopiclist import *
from .linkedagentlist import *
from .linkedpromotionalmedialist import *
from .linkedthemepacklist import *

__all__ = 'LinkedCommunityList',


class LinkedCommunityList(Object):
    json: List[List[dict]]

    @property
    def activeInfo(self) -> LinkedActiveInfoList:
        return LinkedActiveInfoList([[c.get("activeInfo") or {} for c in lcl] for lcl in self.json])

    @property
    def addedTopicList(self) -> LinkedAddedTopicList:
        return LinkedAddedTopicList([[c.get("userAddedTopicList") or {} for c in lcl] for lcl in self.json])

    @property
    def agent(self) -> LinkedAgentList:
        return LinkedAgentList([[c.get("agent") or {} for c in lcl] for lcl in self.json])

    @property
    def aminoId(self) -> List[List[str]]:
        return [[c.get("endpoint") for c in lcl] for lcl in self.json]

    @property
    def comId(self) -> List[List[int]]:
        return [[c.get("ndcId") for c in lcl] for lcl in self.json]

    @property
    def createdTime(self) -> List[List[str]]:
        return [[c.get("createdTime") for c in lcl] for lcl in self.json]

    @property
    def description(self) -> List[List[str]]:
        return [[c.get("tagline") for c in lcl] for lcl in self.json]

    @property
    def heat(self) -> List[List[int]]:
        return [[c.get("communityHeat") or 0 for c in lcl] for lcl in self.json]

    @property
    def icon(self) -> List[List[str]]:
        return [[c.get("icon") for c in lcl] for lcl in self.json]

    @property
    def joinType(self) -> List[List[int]]:
        return [[c.get("joinType") for c in lcl] for lcl in self.json]

    @property
    def link(self) -> List[List[str]]:
        return [[c.get("link") for c in lcl] for lcl in self.json]

    @property
    def listedStatus(self) -> List[List[int]]:
        return [[c.get("listedStatus") for c in lcl] for lcl in self.json]

    @property
    def membersCount(self) -> List[List[int]]:
        return [[c.get("membersCount") or 0 for c in lcl] for lcl in self.json]

    @property
    def modifiedTime(self) -> List[List[str]]:
        return [[c.get("modifiedTime") for c in lcl] for lcl in self.json]

    @property
    def name(self) -> List[List[str]]:
        return [[c.get("name") for c in lcl] for lcl in self.json]

    @property
    def probationStatus(self) -> List[List[int]]:
        return [[c.get("probationStatus") or 0 for c in lcl] for lcl in self.json]

    @property
    def promotionalMedia(self) -> LinkedPromotionalMediaList:
        return LinkedPromotionalMediaList([[c.get("promotionalMediaList") or [] for c in lcl] for lcl in self.json])

    @property
    def primaryLanguage(self) -> List[List[str]]:
        return [[c.get("primaryLanguage") for c in lcl] for lcl in self.json]

    @property
    def status(self) -> List[List[int]]:
        return [[c.get("status") or 0 for c in lcl] for lcl in self.json]

    @property
    def templateId(self) -> List[List[str]]:
        return [[c.get("templateId") for c in lcl] for lcl in self.json]

    @property
    def themePack(self) -> LinkedThemePackList:
        return LinkedThemePackList([[c.get("themePack") or {} for c in lcl] for lcl in self.json])

    @property
    def updatedTime(self) -> List[List[str]]:
        return [[c.get("updatedTime") for c in lcl] for lcl in self.json]
