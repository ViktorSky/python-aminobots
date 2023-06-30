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
from typing import Any, List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import (
    BaseModel,
    EmailStr,
    HttpUrl,
    Field
)
from .community import Community
from ..enums import ClientType, Language, Role

__all__ = ('Account',)


class Ads(BaseModel):
    lastPopupTime: str
    status: int

    if not TYPE_CHECKING:
        lastPopupTime: Optional[str]
        status: Optional[int] = Field(default=0)


class AdvancedSettings(BaseModel):
    analyticsEnabled: int

    if not TYPE_CHECKING:
        analyticsEnabled: Optional[int] = Field(default=0)


class DeviceInfo(BaseModel):
    lastClientType: ClientType = Field(default=ClientType.MASTER)


class PopupConfig(BaseModel):
    ads: Ads = Field(default_factory=Ads)


class Extensions(BaseModel):
    adsEnabled: bool = Field(default=False)
    adsFlags: int = Field(default=0)
    adsLevel: Optional[int]
    contentLanguage: Language = Field(default=Language.ENGLISH)
    deviceInfo: DeviceInfo = Field(default_factory=DeviceInfo)
    frameId: Optional[str] = Field(alias='avatarFrameId')
    mediaLabAdsMigrationAugust2020: bool = Field(default=False)
    popupConfig: PopupConfig = Field(default_factory=PopupConfig)


class Account(BaseModel):
    activation: int = Field(default=0)
    adsEnabled: bool = property(lambda self: self.extensions.adsEnabled)
    advancedSettings: AdvancedSettings = Field(default_factory=AdvancedSettings)
    aminoId: str
    aminoIdEditable: bool = Field(default=False)
    appleId: Optional[str] = Field(alias='appleID')
    contentLanguage: str = property(lambda self: self.extensions.contentLanguage)
    createdTime: datetime
    deviceId: Optional[str] = Field(alias='deviceID')
    deviceInfo: DeviceInfo = property(lambda self: self.extensions.deviceInfo)
    email: Optional[EmailStr]
    emailActivation: int = Field(default=0)
    extensions: Extensions = Field(default_factory=Extensions)
    facebookId: Optional[str] = Field(alias='facebookID')
    frameId: Optional[str] = property(lambda self: self.extensions.frameId)
    googleId: Optional[str] = Field(alias='googleID')
    icon: Optional[HttpUrl]
    linkedCommunityList: list[Community] = Field(default_factory=list)
    mediaLabAdsMigrationAugust2020: bool = property(lambda self: self.extensions.mediaLabAdsMigrationAugust2020)
    membership: Any
    mediaList: Any
    modifiedTime: Optional[datetime]
    nickname: str
    phoneNumber: Optional[str]
    phoneNumberActivation: int = Field(default=0)
    popupConfig: PopupConfig = property(lambda self: self.extensions.popupConfig)
    role: Role = Field(default=Role.MEMBER)
    securityLevel: int = Field(default=0)
    status: int = Field(default=0)
    twitterId: Optional[str] = Field(alias='twitterID')
    userId: str = Field(alias='uid')
    username: str

    if not TYPE_CHECKING:
        aminoId: Optional[str]
        createdTime: Optional[datetime]
        nickname: Optional[str]
        userId: Optional[str]
        username: Optional[str]
