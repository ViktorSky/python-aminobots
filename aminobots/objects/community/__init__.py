from typing import Optional

from ..object import Object
from .activeinfo import *
from .addedtopic import AddedTopic
from .advancedsettings import *
from .agent import *
from .configuration import *
from .extensions import *
from .promotionalmedia import *
from .themepack import *

__all__ = 'Community',


class Community(Object):
    json: dict

    @property
    def activeInfo(self) -> ActiveInfo:
        return ActiveInfo(self.json.get("activeInfo") or {})

    @property
    def addedTopic(self) -> AddedTopic:
        return AddedTopic(self.json.get("userAddedTopicList") or [])

    @property
    def advancedSettings(self) -> AdvancedSettings:
        return AdvancedSettings(self.json.get("advancedSettings") or {})

    @property
    def agent(self) -> Agent:
        return Agent(self.json.get("agent") or {})

    @property
    def aminoId(self) -> str:
        return self.json.get("endpoint")

    @property
    def configuration(self) -> Configuration:
        return Configuration(self.json.get("configuration") or {})

    @property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @property
    def description(self) -> Optional[str]:
        return self.json.get("content")

    @property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @property
    def heat(self) -> int:
        return self.json.get("communityHeat")

    @property
    def icon(self) -> str:
        return self.json.get("icon")

    @property
    def id(self) -> int:
        return self.json.get("ndcId")

    @property
    def isStandaloneAppDeprecated(self) -> bool:
        return self.json.get("isStandaloneAppDeprecated")

    @property
    def isStandaloneAppMonetizationEnabled(self) -> bool:
        return self.json.get("isStandaloneAppMonetizationEnabled")

    @property
    def joinType(self) -> int:
        return self.json.get("joinType")

    @property
    def keywords(self) -> Optional[str]:
        return self.json.get("keywords")

    @property
    def link(self) -> str:
        return self.json.get("link")

    @property
    def listedStatus(self) -> int:
        return self.json.get("listedStatus")

    @property
    def mediaList(self) -> list:
        return self.json.get("mediaList") or []

    @property
    def membersCount(self) -> int:
        return self.json.get("membersCount")

    @property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    @property
    def name(self) -> str:
        return self.json.get("name")

    @property
    def primaryLanguage(self) -> str:
        return self.json.get("primaryLanguage")

    @property
    def probationStatus(self) -> int:
        return self.json.get("probationStatus")

    @property
    def promotionalMedia(self) -> PromotionalMedia:
        return PromotionalMedia(self.json.get("promotionalMediaList") or [])

    @property
    def searchable(self) -> bool:
        return self.json.get("searchable")

    @property
    def status(self) -> int:
        return self.json.get("status")

    @property
    def tagline(self) -> str:
        return self.json.get("tagline")

    @property
    def themePack(self) -> ThemePack:
        return ThemePack(self.json.get("themePack") or {})

    @property
    def themePackColor(self) -> str:
        return self.themePack.color

    @property
    def themePackHash(self) -> str:
        return self.themePack.hash

    @property
    def themePackRevision(self) -> int:
        return self.themePack.revision

    @property
    def themePackUrl(self) -> str:
        return self.themePack.url

    @property
    def templateId(self) -> int:
        return self.json.get("templateId")

    @property
    def updatedTime(self) -> str:
        return self.json.get("updatedTime")
