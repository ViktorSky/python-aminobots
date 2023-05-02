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
from . import communitylist
import dataclasses
import functools
import typing

__all__ = ('Account',)


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def lastPopupTime(self) -> str:
        return self.json.get("lastPopupTime")

    @functools.cached_property
    def status(self) -> int:
        return self.json.get("status")


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def analyticsEnabled(self) -> int:
        return self.json.get("analyticsEnabled")


@dataclasses.dataclass(repr=False)
class DeviceInfo:
    """Represent the account device info.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    lastClientType: :class:`int`

    """
    json: dict

    @functools.cached_property
    def lastClientType(self) -> int:
        return self.json.get("lastClientType")


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def ads(self) -> Ads:
        return Ads(self.json.get("ads", {}))

    @functools.cached_property
    def adsStatus(self):
        return self.ads.status

    @functools.cached_property
    def lastAdsPopupTime(self):
        return self.ads.lastPopupTime


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def adsEnabled(self) -> bool:
        return self.json.get("adsEnabled")

    @functools.cached_property
    def adsFlags(self) -> int:
        return self.json.get("adsFlags")

    @functools.cached_property
    def adsLevel(self) -> int:
        return self.json.get("adsLevel")

    @functools.cached_property
    def avatarFrameId(self) -> str:
        return self.json.get("avatarFrameId")

    @functools.cached_property
    def contentLanguage(self) -> str:
        return self.json.get("contentLanguage")

    @functools.cached_property
    def deviceInfo(self) -> DeviceInfo:
        return DeviceInfo(self.json.get("deviceInfo", {}))

    @functools.cached_property
    def mediaLabAdsMigrationAugust2020(self) -> bool:
        return self.json.get("mediaLabAdsMigrationAugust2020")

    @functools.cached_property
    def popupConfig(self) -> PopupConfig:
        return PopupConfig(self.json.get("popupConfig", {}))


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def activation(self) -> typing.Literal[0, 1]:
        return self.json.get("activation")

    @functools.cached_property
    def adsEnabled(self) -> bool:
        return self.extensions.adsEnabled

    @functools.cached_property
    def advancedSettings(self) -> AdvancedSettings:
        return AdvancedSettings(self.json.get("advancedSettings", {}))

    @functools.cached_property
    def aminoId(self) -> str:
        return self.json.get("aminoId")

    @functools.cached_property
    def aminoIdEditable(self) -> bool:
        return self.json.get("aminoIdEditable")

    @functools.cached_property
    def appleId(self) -> typing.Optional[str]:
        return self.json.get("appleID")

    @functools.cached_property
    def avatarFrameId(self) -> str:
        return self.extensions.avatarFrameId

    @functools.cached_property
    def contentLanguage(self) -> str:
        return self.extensions.contentLanguage

    @functools.cached_property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @functools.cached_property
    def deviceId(self) -> typing.Optional[str]:
        return self.json.get("deviceID")

    @functools.cached_property
    def deviceInfo(self) -> DeviceInfo:
        return self.extensions.deviceInfo

    @functools.cached_property
    def email(self) -> typing.Optional[str]:
        return self.json.get("email")

    @functools.cached_property
    def emailActivation(self) -> typing.Literal[0, 1]:
        return self.json.get("emailActivation")

    @functools.cached_property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @functools.cached_property
    def facebookId(self) -> typing.Optional[str]:
        return self.json.get("facebookID")

    @functools.cached_property
    def googleId(self) -> typing.Optional[str]:
        return self.json.get("googleID")

    @functools.cached_property
    def icon(self) -> str:
        return self.json.get("icon")

    @functools.cached_property
    def linkedCommunity(self) -> communitylist.CommunityList:
        return communitylist.CommunityList(self.json.get("linkedCommunityList") or [])

    @functools.cached_property
    def mediaLabAdsMigrationAugust2020(self) -> bool:
        return self.extensions.mediaLabAdsMigrationAugust2020

    @functools.cached_property
    def membership(self):  # ...
        return self.json.get("membership")

    @functools.cached_property
    def mediaList(self):  # ...
        return self.json.get("mediaList")

    @functools.cached_property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    @functools.cached_property
    def nickname(self) -> str:
        return self.json.get("nickname")

    @functools.cached_property
    def phone(self) -> typing.Optional[str]:
        return self.json.get("phoneNumber")

    @functools.cached_property
    def phoneActivation(self) -> typing.Literal[0, 1]:
        return self.json.get("phoneNumberActivation")

    @functools.cached_property
    def popupConfig(self) -> PopupConfig:
        return self.extensions.popupConfig

    @functools.cached_property
    def role(self) -> int:
        return self.json.get("role")

    @functools.cached_property
    def securityLevel(self) -> int:  # (3,)
        return self.json.get("securityLevel")

    @functools.cached_property
    def status(self) -> typing.Literal[0, 1]:
        return self.json.get("status")

    @functools.cached_property
    def twitterId(self) -> typing.Optional[str]:
        return self.json.get("twitterID")

    @functools.cached_property
    def userId(self) -> str:
        return self.json.get("uid")

    @functools.cached_property
    def username(self) -> str:
        return self.json.get("username")
