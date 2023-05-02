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

__all__ = ('Paging',)


@dataclass(repr=False)
class Paging:
    """Represent a Paging of Amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    nextPageToken: :class:`str`
        Next Page token.

    """

    json: dict

    @cached_property
    def nextPageToken(self) -> str:
        """Next page token."""
        return self.json.get("nextPageToken")

    @cached_property
    def prevPageToken(self) -> Optional[str]:
        """Previous page token."""
        return self.json.get("prevPageToken")
