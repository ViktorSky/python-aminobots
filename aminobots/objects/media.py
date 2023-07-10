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
from typing import Any, Optional, TYPE_CHECKING, Union
from pydantic import AnyUrl, Field
from pydantic.dataclasses import dataclass
from ..enums import MediaType

__all__ = ('Media',)


@dataclass
class Media:
    type: MediaType
    url: Union[AnyUrl, str]
    caption: Optional[str] = Field(default=None)
    id: Optional[str] = Field(default=None, max_length=3, min_length=3)
    if not TYPE_CHECKING:
        null0: Any = Field(default=None)
        null1: Optional[dict] = Field(default=None)

    def __getitem__(self, item: int) -> Union[MediaType, AnyUrl, str, None]:
        return [self.type, self.url, self.caption, self.id][item]

    def __repr__(self) -> str:
        return '{}({})'.format(
            type(self).__name__,
            ', '.join([
                'type=%d',
                'url=%r',
                'caption=%r',
                'id=%r'
            ]) % (
                self.type,
                self.url,
                self.caption,
                self.id
            )
        )
