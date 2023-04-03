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
from typing import (
    Literal,
    Optional
)
from .communitylist import CommunityList

__all__ = ('Account',)


@dataclass(repr=False)
class Ads:
    """Respreset a account ads info.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    lastPopupTime: :class:`str`
        ...
    status: :class:`int`
        ...

    """
    json: dict

    @property
    def lastPopupTime(self) -> str:
        return self.json.get("lastPopupTime")

    @property
    def status(self) -> int:
        return self.json.get("status")


@dataclass(repr=False)
class AdvancedSettings:
    """Represent the account advanced settings.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    analytincsEnabled: Literal[`0`, `1`]
        ...

    """
    json: dict

    @property
    def analyticsEnabled(self) -> int:
        return self.json.get("analyticsEnabled")


@dataclass(repr=False)
class DeviceInfo:
    """Represent the account device info.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    lastClientType: :class:`int`

    """
    json: dict

    @property
    def lastClientType(self) -> int:
        return self.json.get("lastClientType")


@dataclass(repr=False)
class PopupConfig:
    """Represent the PopupConfig

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    ads: :class:`Ads`
        ...
    adsStatus: :class:`int`
        ...
    lastAdsPopupTime: :class:`str`
        ...

    """
    json: dict

    @property
    def ads(self) -> Ads:
        return Ads(self.json.get("ads", {}))

    @property
    def adsStatus(self):
        return self.ads.status

    @property
    def lastAdsPopupTime(self):
        return self.ads.lastPopupTime


@dataclass(repr=False)
class Extensions:
    """Represent account extensions.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    adsEnabled: :class:`bool`
        ...
    adsFlags: :class:`int`
        ...
    adsLevel: :class:`int`
        ...
    avatarFrameId: :class:`str`
        ...
    contentLanguage: :class:`str`
        ...
    deviceInfo: :class:`DeviceInfo`
        ...
    mediaLabAdsMigrationAugust2020: :class:`bool`
        ...
    popupConfig: :class:`PopupConfig`
        ...

    """
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


@dataclass(repr=False)
class Account:
    """Represent a user account in Amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    activation: Literal[:class:`0`, :class:`1`]
        ...
    adsEnabled: :class:`bool`
        ...
    advancedSettings: :class:`AdvancedSettings`
        ...
    aminoId: :class:`str`
        ...
    aminoIdEditable: :class:`bool`
        ...
    appleId: :class:`str`
        ...
    avatarFrameId: :class:`str`
        ...
    contentLanguage: :class:`str`
        ...
    createdTime: :class:`str`
        ...
    deviceId: :class:`str`
        ...
    deviceInfo: :class:`DeviceInfo`
        ...
    email: :class:`str`
        ...
    emailActivation: Literal[`0`, `1`]
        ...
    extensions: :class:`Extensions`
        ...
    facebookId: :class:`str`
        ...
    googleId: :class:`str`
        ...
    icon: :class:`str`
        ...
    linkedCommunity: :class:`CommunityList`
        ...
    mediaLabAdsMigrationAugust2020: :class:`bool`
        ...
    membership: ::``

    mediaList: ::``

    modifiedTime: :class:`str`
        ...
    nickname: :class:`str`
        ...
    phone: :class:`str`
        ...
    phoneActivation: Literal[`0`, `1`]
        ...
    popupConfig: :class:`PopupConfig`
        ...
    role: :class:`int`
        ...
    securityLevel: :class:`int`
        ...
    status: Literal[`0`, `1`]
        ...
    twitterId: :class:`str`
        ...
    userId: :class:`str`
        ...
    username: :class:`str`
        ...

    """

    json: dict

    @property
    def activation(self) -> Literal[0, 1]:
        return self.json.get("activation")

    @property
    def adsEnabled(self) -> bool:
        return self.extensions.adsEnabled

    @property
    def advancedSettings(self) -> AdvancedSettings:
        return AdvancedSettings(self.json.get("advancedSettings", {}))

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
