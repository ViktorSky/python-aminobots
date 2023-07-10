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
    Field,
    validator
)
from .community import Community
from ..enums import (
    Boolean,
    ClientType,
    Language,
    Role,
    Status
)

__all__ = ('Account',)


class Ads(BaseModel):
    lastPopupTime: datetime = Field(default=None)
    status: Boolean = Field(default=Boolean.FALSE)

    if not TYPE_CHECKING:
        lastPopupTime: Optional[datetime]


class AdvancedSettings(BaseModel):
    analyticsEnabled: Boolean = Field(default=Boolean.FALSE)


class DeviceInfo(BaseModel):
    lastClientType: ClientType = Field(default=ClientType.MASTER)


class PopupConfig(BaseModel):
    ads: Ads = Field(default_factory=Ads)


class Extensions(BaseModel):
    adsEnabled: bool = Field(default=False)
    adsFlags: int = Field(default=0)
    adsLevel: Optional[int] = Field(default=None)
    contentLanguage: Language = Field(default=Language.ENGLISH)
    deviceInfo: DeviceInfo = Field(default_factory=DeviceInfo)
    frameId: Optional[str] = Field(alias='avatarFrameId', default=None)
    mediaLabAdsMigrationAugust2020: bool = Field(default=False)
    popupConfig: PopupConfig = Field(default_factory=PopupConfig)


class Account(BaseModel):
    activation: Boolean = Field(default=Boolean.TRUE)
    advancedSettings: AdvancedSettings = Field(default_factory=AdvancedSettings) # type: ignore
    aminoId: str
    aminoIdEditable: bool = Field(default=False)
    appleId: Optional[str] = Field(alias='appleID')
    createdTime: datetime
    deviceId: Optional[str] = Field(alias='deviceID')
    email: Optional[EmailStr]
    emailActivation: Boolean = Field(default=Boolean.FALSE)
    extensions: Extensions = Field(default_factory=Extensions)
    facebookId: Optional[str] = Field(alias='facebookID')
    googleId: Optional[str] = Field(alias='googleID')
    icon: Optional[HttpUrl] = Field(default=None)
    mediaLabAdsMigrationAugust2020: bool = property(lambda self: self.extensions.mediaLabAdsMigrationAugust2020) # type: ignore
    mediaList: Any
    membership: Any
    modifiedTime: Optional[datetime]
    nickname: str
    phone: Optional[str] = Field(alias='phoneNumber', default=None)
    phoneActivation: Boolean = Field(alias='phoneNumberActivation', default=Boolean.FALSE)
    popupConfig: PopupConfig = property(lambda self: self.extensions.popupConfig) # type: ignore
    role: Role = Field(default=Role.MEMBER)
    securityLevel: int = Field(default=0)
    status: Status = Field(default=Status.OK)
    twitterId: Optional[str] = Field(alias='twitterID')
    userId: str = Field(alias='uid')
    username: Optional[str] = Field(default=None)

    if not TYPE_CHECKING:
        aminoId: Optional[str]
        createdTime: Optional[datetime]
        nickname: Optional[str]
        userId: Optional[str]
