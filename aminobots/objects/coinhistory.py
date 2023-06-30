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
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from pydantic import BaseModel, HttpUrl, Field
from ..enums import SourceType

__all__ = ('CoinHistory',)


class Extensions(BaseModel):
    description: str
    icon: Optional[HttpUrl]
    objectDeeplinkUrl: HttpUrl
    subtitle: str

    if not TYPE_CHECKING:
        description: Optional[str]
        objectDeeplinkUrl: Optional[str]
        subtitle: Optional[str]


class CoinHistory(BaseModel):
    bonusCoins: Optional[int]
    bonusCoinsFloat: Optional[int]
    changedCoins: int = Field(default=0)
    changedCoinsFloat: float = Field(default=0.0)
    createdTime: datetime
    isPositive: bool
    originCoins: int = Field(default=0)
    originCoinsFloat: float = Field(default=0)
    sourceType: SourceType = Field(default=SourceType.ADS)
    taxCoins: Optional[int]
    taxCoinsFloat: Optional[float]
    totalCoins: int = Field(default=0)
    totalCoinsFloat: float = Field(default=0.0)
    userId: str = Field(alias='uid')

    if not TYPE_CHECKING:
        createdTime: Optional[datetime]
        isPositive: Optional[bool]
        userId: Optional[str]
