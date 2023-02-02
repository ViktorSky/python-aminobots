from ..object import Object
from .ads import *

__all__ = 'PopupConfig',


class PopupConfig(Object):
    json: dict

    @property
    def ads(self) -> Ads:
        return Ads(self.json.get("ads", {}))

    @property
    def lastAdsPopupTime(self):
        return self.ads.lastPopupTime

    @property
    def adsStatus(self):
        return self.ads.status
