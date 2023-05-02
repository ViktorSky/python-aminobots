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
from typing import Literal

__all__ = ('Membership',)


@dataclass(repr=False)
class Membership:
    """Represets the user membership."""
    json: dict

    @cached_property
    def autoRenew(self) -> bool:
        return self.json.get('isAutoRenew')

    @cached_property
    def createdTime(self) -> str:
        return self.json.get('createdTime')

    @cached_property
    def expiredTime(self) -> str:
        return self.json.get('expiredTime')

    @cached_property
    def modifiedTime(self) -> str:
        return self.json.get('modifiedTime')

    @cached_property
    def paymentType(self) -> Literal[1, 2, 3, 4, 5]:
        return self.json.get('paymentType')

    @cached_property
    def renewedTime(self) -> str:
        return self.json.get('renewedTime')

    @cached_property
    def status(self) -> Literal[0, 1]:
        return self.json.get('membershipStatus')

    @cached_property
    def userId(self) -> str:
        return self.json.get('uid')
