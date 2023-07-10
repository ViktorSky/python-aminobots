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
from typing import List, Optional, TYPE_CHECKING
from pydantic import BaseModel, HttpUrl, Field

__all__ = ('TipInfo',)


class TipOption(BaseModel):
    icon: Optional[HttpUrl] = Field(default=None)
    value: int = Field(default=None)

    if not TYPE_CHECKING:
        value: Optional[int]


class TipInfo(BaseModel):
    customOption: TipOption = Field(alias='tipCustomOption', default_factory=TipOption)
    maxCoins: int = Field(alias='tipMaxCoin', default=0)
    minCoins: int = Field(alias='tipMinCoin', default=0)
    optionList: List[TipOption] = Field(alias='tipOptionList', default_factory=list)
    tippable: bool = Field(default=False)
    tippedCoins: int = Field(default=0)
    tippersCount: int = Field(default=0)

    if not TYPE_CHECKING:
        maxCoins: Optional[int]
        minCoins: Optional[int]
