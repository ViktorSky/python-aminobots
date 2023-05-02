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

__all__ = ('CouponMappingList',)


@dataclass(repr=False)
class Coupon:
    json: List[dict]

    @cached_property
    def createdTimes(self) -> List[str]:
        return [coupon.get('createdTime') for coupon in self.json]

    @cached_property
    def descriptions(self) -> List[str]:
        return [coupon.get('scopeDesc') for coupon in self.json]

    @cached_property
    def expiredTimes(self) -> List[Optional[int]]:
        return [coupon.get('expiredTime') for coupon in self.json]

    @cached_property
    def expiredTypes(self) -> List[int]:
        return [coupon.get('expiredType') for coupon in self.json]

    @cached_property
    def ids(self) -> List[str]:
        return [coupon.get('couponId') for coupon in self.json]

    @cached_property
    def modifiedTimes(self) -> List[str]:
        return [coupon.get('modifiedTime') for coupon in self.json]

    @cached_property
    def titles(self) -> List[str]:
        return [coupon.get('title') for coupon in self.json]

    @cached_property
    def types(self) -> List[int]:
        return [coupon.get('couponType') for coupon in self.json]

    @cached_property
    def values(self) -> List[int]:
        return [coupon.get('couponValue') for coupon in self.json]


@dataclass(repr=False)
class CouponMappingList:
    json: List[dict]

    @cached_property
    def couponMappingIds(self) -> List[str]:
        return [cm.get('couponMappingId') for cm in self.json]

    @cached_property
    def coupons(self) -> Coupon:
        return Coupon([cm.get('coupon') or {} for cm in self.json])

    @cached_property
    def createdTimes(self) -> List[str]:
        return [cm.get('createdTime') for cm in self.json]

    @cached_property
    def expiredTimes(self) -> List[Optional[str]]:
        return [cm.get('expiredTime') for cm in self.json]

    @cached_property
    def statuses(self) -> List[int]:
        return [cm.get('status') for cm in self.json]

    @cached_property
    def usedTimes(self) -> List[Optional[str]]:
        return [cm.get('usedTime') for cm in self.json]
