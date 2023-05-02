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
from typing import List, Optional

__all__ = ('CoinHistoryList',)


@dataclass(repr=False)
class ExtensionsData:
    json: List[dict]

    @cached_property
    def deepLinks(self) -> List[str]:
        return [ed.get('objectDeeplinkUrl') for ed in self.json]

    @cached_property
    def descriptions(self) -> List[str]:
        return [ed.get('description') for ed in self.json]

    @cached_property
    def icons(self) -> List[str]:
        return [ed.get('icon') for ed in self.json]

    @cached_property
    def subtitle(self) -> List[Optional[str]]:
        return [ed.get('subtitle') for ed in self.json]


@dataclass(repr=False)
class CoinHistoryList:
    json: List[dict]

    def __len__(self) -> int:
        return len(self.json)

    @cached_property
    def arePositive(self) -> List[bool]:
        return [ch.get('isPositive') for ch in self.json]

    @cached_property
    def changedCoins(self) -> List[int]:
        return [ch.get('changedCoins') for ch in self.json]

    @cached_property
    def changedCoinsFloat(self) -> List[float]:
        return [ch.get('changedCoinsFloat') for ch in self.json]

    @cached_property
    def createdTimes(self) -> List[str]:
        return [ch.get('createdTime') for ch in self.json]

    @cached_property
    def originsCoins(self) -> List[int]:
        return [ch.get('originCoins') for ch in self.json]

    @cached_property
    def originsCoinsFloat(self) -> List[int]:
        return [ch.get('originCoinsFloat') for ch in self.json]

    @cached_property
    def sourceTypes(self) -> List[int]:
        return [ch.get('sourceType') for ch in self.json]

    @cached_property
    def totalsCoins(self) -> List[int]:
        return [ch.get('totalCoins') for ch in self.json]

    @cached_property
    def totalsCoinsFloat(self) -> List[float]:
        return [ch.get('totalCoinsFloat') for ch in self.json]

    @cached_property
    def userId(self) -> List[str]:
        return [ch.get('uid') for ch in self.json]


[
        {
            #"originCoins": -150,
            #"isPositive": False,
            #"changedCoinsFloat": -150,
            #"sourceType": 1,
            #"totalCoins": 2310068,
            #"createdTime": "2023-04-27T14:38:06Z",
            "bonusCoinsFloat": None,
            #"originCoinsFloat": -150,
            "taxCoins": None,
            "bonusCoins": None,
            #"totalCoinsFloat": 2310068.072101,
            #"uid": "d780e629-1ec7-4c56-9974-42c515ba56c6",
            #"extData": {},
            "taxCoinsFloat": None,
            #"changedCoins": -150
        }
]