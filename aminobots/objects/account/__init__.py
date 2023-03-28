from typing import Literal, Optional

from ..object import Object
from ..communitylist import CommunityList

from .advancedsettings import *
from .deviceinfo import *
from .extensions import *
from .popupconfig import *

__all__ = 'Account',


class Account(Object):
    json: dict

    @property
    def activation(self) -> Literal[0, 1]:
        return self.json.get("activation")

    @property
    def adsEnabled(self) -> bool:
        return self.extensions.adsEnabled

    @property
    def adsFlags(self) -> int:
        return self.extensions.adsFlags

    @property
    def adsLevel(self) -> int:
        return self.extensions.adsLevel

    @property
    def advancedSettings(self) -> AdvancedSettings:
        return AdvancedSettings(self.json.get("advancedSettings", {}))

    @property
    def analyticsEnabled(self) -> int:
        return self.advancedSettings.analyticsEnabled

    @property
    def aminoId(self) -> str:
        return self.json.get("aminoId")

    @property
    def aminoIdEditable(self) -> bool:
        return self.json.get("aminoIdEditable")

    @property
    def appleId(self) -> Optional[str]:
        return self.json.get("appleID")

    @property
    def avatarFrameId(self) -> str:
        return self.extensions.avatarFrameId

    @property
    def contentLanguage(self) -> str:
        return self.extensions.contentLanguage

    @property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @property
    def deviceId(self) -> Optional[str]:
        return self.json.get("deviceID")

    @property
    def deviceInfo(self) -> DeviceInfo:
        return self.extensions.deviceInfo

    @property
    def email(self) -> Optional[str]:
        return self.json.get("email")

    @property
    def emailActivation(self) -> Literal[0, 1]:
        return self.json.get("emailActivation")

    @property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @property
    def facebookId(self) -> Optional[str]:
        return self.json.get("facebookID")

    @property
    def googleId(self) -> Optional[str]:
        return self.json.get("googleID")

    @property
    def icon(self) -> str:
        return self.json.get("icon")

    @property
    def linkedCommunity(self) -> CommunityList:
        return CommunityList(self.json.get("linkedCommunityList") or [])

    @property
    def mediaLabAdsMigrationAugust2020(self) -> bool:
        return self.extensions.mediaLabAdsMigrationAugust2020

    @property
    def membership(self):  # ...
        return self.json.get("membership")

    @property
    def mediaList(self):  # ...
        return self.json.get("mediaList")

    @property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    @property
    def nickname(self) -> str:
        return self.json.get("nickname")

    @property
    def phone(self) -> Optional[str]:
        return self.json.get("phoneNumber")

    @property
    def phoneActivation(self) -> Literal[0, 1]:
        return self.json.get("phoneNumberActivation")

    @property
    def popupConfig(self) -> PopupConfig:
        return self.extensions.popupConfig

    @property
    def role(self) -> int:
        return self.json.get("role")

    @property
    def securityLevel(self) -> int:  # (3,)
        return self.json.get("securityLevel")

    @property
    def status(self) -> Literal[0, 1]:
        return self.json.get("status")

    @property
    def twitterId(self) -> Optional[str]:
        return self.json.get("twitterID")

    @property
    def userId(self) -> str:
        return self.json.get("uid")

    @property
    def username(self) -> str:
        return self.json.get("username")

