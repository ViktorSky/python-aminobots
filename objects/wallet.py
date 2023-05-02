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
from functools import cached_property
from typing import Optional

__all__ = ('Wallet',)


@dataclass(repr=False)
class AdsVideoStats:
    json: dict

    @cached_property
    def canEarnedCoins(self) -> int:
        """Coins that you earn by watching the video."""
        return self.json.get('canEarnedCoins')

    @cached_property
    def canNotWatchReason(self) -> Optional[int]:
        return self.json.get('canNotWatchVideoReason')

    @cached_property
    def canWatch(self) -> bool:
        return self.json.get('canWatchVideo')

    @cached_property
    def nextWatchInterval(self) -> int:
        """next video in seconds."""
        return self.json.get('nextWatchVideoInterval')

    @cached_property
    def watchedCount(self) -> int:
        return self.json.get('watchedVideoCount')

    @cached_property
    def watchMaxCount(self) -> int:
        return self.json.get('watchVideoMaxCount')


@dataclass(repr=False)
class Wallet:
    """Represents the user wallet info.

    Attributes
    ----------
    json : :class:`dict`
        The raw API data.
    adsEnabled : :class:`bool`
        Adversiments enabled.
    adsFlags : :class:`int`
        Adversiments flags.
    bussinessCoinsEnabled : :class:`bool`
        User bussiness coins enabled.
    totalBusinessCoins : :class:`int`
        User bussiness coins.
    totalBusinessCoinsFloat : :class:`float`
        User buusiness coins.
    totalCoins : :class:`int`
        User total coins.
    totalCoinsFloat : :class:`float`
        User total coins.
    video : :class:`AdsVideoStats`
        Adversiment video stats.

    """
    json: dict

    @cached_property
    def adsEnabled(self) -> bool:
        return self.json.get('adsEnabled')

    @cached_property
    def adsFlags(self) -> int:
        return self.json.get('adsFlags')

    @cached_property
    def businessCoinsEnabled(self) -> bool:
        return self.json.get('businessCoinsEnabled')

    @cached_property
    def totalBusinessCoins(self) -> int:
        return self.json.get('totalBusinessCoins')

    @cached_property
    def totalBusinessCoinsFloat(self) -> float:
        return self.json.get('totalBusinessCoinsFloat')

    @cached_property
    def totalCoins(self) -> int:
        return self.json.get('totalCoins')

    @cached_property
    def totalCoinsFloat(self) -> float:
        return self.json.get('totalCoinsFloat')

    @cached_property
    def video(self) -> AdsVideoStats:
        return AdsVideoStats(self.json.get('adsVideoStats') or {})
