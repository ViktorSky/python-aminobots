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
    Any,
    ItemsView,
    Iterator,
    KeysView,
    Mapping,
    Optional,
    ValuesView
)
from pydantic import BaseModel, Field

__all__ = ('MappingBase',)


class MappingBase(BaseModel):
    __root__: Mapping = Field(default_factory=dict)

    def __iter__(self) -> Iterator:
        return iter(self.__root__)

    def __getitem__(self, item) -> Any:
        return self.__root__[item]

    def __len__(self) -> int:
        return len(self.__root__)

    def get(self, item, default=None) -> Optional[Any]:
        return self.__root__.get(item, default)

    def keys(self) -> KeysView:
        return self.__root__.keys()

    def values(self) -> ValuesView:
        return self.__root__.values()

    def items(self) -> ItemsView:
        return self.__root__.items()
