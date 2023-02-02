from ..object import Object
from .catalogmodule import *
from .chatmodule import ChatModule
from .externalcontentmodule import *
from .featuredmodule import *
from .influencermodule import *
from .postmodule import *
from .rankingmodule import *
from .sharedfoldermodule import *
from .topiccategoriesmodule import *

__all__ = 'Module',


class Module(Object):
    json: dict

    @property
    def catalog(self) -> CatalogModule:
        return CatalogModule(self.json.get("catalog") or {})

    @property
    def chat(self) -> ChatModule:
        return ChatModule(self.json.get("chat") or {})

    @property
    def externalContent(self) -> ExternalContentModule:
        return ExternalContentModule(self.json.get("externalContent") or {})

    @property
    def externalContentEnabled(self) -> bool:
        return self.externalContent.enabled

    @property
    def featured(self) -> FeaturedModule:
        return FeaturedModule(self.json.get("featured") or {})

    @property
    def influencer(self) -> InfluencerModule:
        return InfluencerModule(self.json.get("influencer") or {})

    @property
    def post(self) -> PostModule:
        return PostModule(self.json.get("post") or {})

    @property
    def ranking(self) -> RankingModule:
        return RankingModule(self.json.get("ranking") or {})

    @property
    def sharedFolder(self) -> SharedFolderModule:
        return SharedFolderModule(self.json.get("sharedFolder") or {})

    @property
    def topicCategories(self) -> TopicCategoriesModule:
        return TopicCategoriesModule(self.json.get("topicCategories") or {})
