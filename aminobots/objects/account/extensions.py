from ..object import Object
from .deviceinfo import *
from .popupconfig import *

__all__ = 'Extensions',


class Extensions(Object):
    json: dict

    @property
    def adsEnabled(self) -> bool:
        return self.json.get("adsEnabled")

    @property
    def adsFlags(self) -> int:
        return self.json.get("adsFlags")

    @property
    def adsLevel(self) -> int:
        return self.json.get("adsLevel")

    @property
    def avatarFrameId(self) -> str:
        return self.json.get("avatarFrameId")

    @property
    def contentLanguage(self) -> str:
        return self.json.get("contentLanguage")

    @property
    def deviceInfo(self) -> DeviceInfo:
        return DeviceInfo(self.json.get("deviceInfo", {}))

    @property
    def mediaLabAdsMigrationAugust2020(self) -> bool:
        return self.json.get("mediaLabAdsMigrationAugust2020")

    @property
    def popupConfig(self) -> PopupConfig:
        return PopupConfig(self.json.get("popupConfig", {}))
