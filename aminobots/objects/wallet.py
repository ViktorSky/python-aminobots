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
from typing import Optional, TYPE_CHECKING
from pydantic import BaseModel, Field

__all__ = ('Wallet',)


class AdsVideoStats(BaseModel):
    canEarnedCoins: bool = Field(default=False) # from int
    canNotWatchReason: Optional[int] = Field(alias='canNotWatchVideoReason')
    canWatch: bool = Field(alias='canWatchVideo', default=False)
    nextWatchInterval: int = Field(alias='nextWatchVideoInterval', default=0)
    watchedCount: int = Field(alias='watchedVideoCount', default=0)
    watchMaxCount: int = Field(alias='watchVideoMaxCount', default=0)


class Wallet(BaseModel):
    adsEnabled: bool = Field(default=False)
    adsFlags: int = Field(default=0)
    adsVideo: AdsVideoStats = Field(alias='adsVideoStats', default=AdsVideoStats)
    businessCoinsEnabled: bool = Field(default=False)
    totalBusinessCoins: Optional[int] = Field(default=0)
    totalBusinessCoinsFloat: Optional[float] = Field(default=0)
    totalCoins: int = Field(default=0)
    totalCoinsFloat: float = Field(default=0.0)

    if not TYPE_CHECKING:
        totalCoins: Optional[int]
        totalCoinsFloat: Optional[float]
