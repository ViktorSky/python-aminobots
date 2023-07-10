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
from typing import (
    List,
    Iterator,
    Optional,
    Mapping,
    KeysView,
    ItemsView,
    TYPE_CHECKING,
    Union,
    ValuesView
)
from pydantic import BaseModel, Field, FileUrl, AnyUrl
from .mappingbase import MappingBase
from .media import Media

__all__ = ('PlaylistInThreadList',)


class Item(BaseModel):
    backgroundList: List[Media] = Field(alias='mediaList', default_factory=list)
    duration: float = Field(default=0.0)
    isDone: bool = Field(default=False)
    title: str
    type: int
    url: Union[FileUrl, AnyUrl]

    if not TYPE_CHECKING:
        title: Optional[str]
        type: Optional[int]
        url: Union[FileUrl, AnyUrl, None]


class PlayList(BaseModel):
    currentIndex: int = Field(alias='currentItemIndex')
    currentStatus: int = Field(alias='currentItemStatus')
    itemList: List[Item] = Field(alias='items', default_factory=list)

    if not TYPE_CHECKING:
        currentIndex: Optional[int]
        currentStatus: Optional[int]


class PlaylistInThreadList(MappingBase):
    __root__: Mapping[str, PlayList]

    def __iter__(self) -> Iterator[str]:
        return super().__iter__()

    def __getitem__(self, chatId: str) -> PlayList:
        return super().__getitem__(chatId)

    def get(self, chatId: str, default=None) -> Optional[PlayList]:
        return super().get(chatId, default)

    def keys(self) -> KeysView[str]:
        return super().keys()

    def values(self) -> ValuesView[PlayList]:
        return super().values()

    def items(self) -> ItemsView[str, PlayList]:
        return super().items()

    if not TYPE_CHECKING:
        __root__: Optional[Mapping[str, PlayList]] = Field(default_factory=dict)
