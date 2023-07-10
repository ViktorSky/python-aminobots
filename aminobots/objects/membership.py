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
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import BaseModel, Field
from ..enums import PaymentType, MembershipStatus

__all__ = ('Membership',)


class Membership(BaseModel):
    createdTime: datetime = Field(default=None)
    expiredTime: Optional[datetime] = Field(default=None)
    isAutoRenew: bool = Field(default=False)
    membershipStatus: MembershipStatus = Field(default=MembershipStatus.NONE)
    modifiedTime: Optional[datetime] = Field(default=None)
    paymentType: PaymentType = Field(default=PaymentType.COIN)
    renewedTime: Optional[datetime] = Field(default=None)
    userId: str = Field(alias='uid', default=None)

    if not TYPE_CHECKING:
        createdTime: Optional[datetime]
        userId: Optional[str]

    def __bool__(self) -> bool:
        return self.membershipStatus == MembershipStatus.AMINO_PLUS
