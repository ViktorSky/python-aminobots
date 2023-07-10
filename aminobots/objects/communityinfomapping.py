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
    ItemsView,
    Iterator,
    KeysView,
    Optional,
    Mapping,
    Optional,
    ValuesView,
    TYPE_CHECKING
)
from pydantic import Field
from .mappingbase import MappingBase
from .community import Community

__all__ = ('CommunityInfoMapping',)


class CommunityInfoMapping(MappingBase):
    __root__: Mapping[int, Community]

    def __iter__(self) -> Iterator[int]:
        return super().__iter__()

    def __getitem__(self, comId: int) -> Community:
        return super().__getitem__(comId)

    def get(self, comId: int, default=None) -> Optional[Community]:
        return super().get(comId, default)

    def keys(self) -> KeysView[int]:
        return super().keys()

    def values(self) -> ValuesView[Community]:
        return super().values()

    def items(self) -> ItemsView[int, Community]:
        return super().items()

    if not TYPE_CHECKING:
        __root__: Optional[Mapping[int, Community]] = Field(default_factory=dict)
