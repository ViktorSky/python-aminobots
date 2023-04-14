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

__all__ = ('Invitation',)

@dataclass(repr=False)
class InfluencerInfo:
    json: dict

    @cached_property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @cached_property
    def fansCount(self) -> int:
        return self.json.get("fansCount") or 0

    @cached_property
    def isPinned(self) -> bool:
        return self.json.get("pinned") or False

    @cached_property
    def monthlyFee(self) -> int:
        return self.json.get("monthlyFee") or 0


@dataclass(repr=False)
class Author:
    json: dict

    @cached_property
    def accountMembershipStatus(self) -> int:
        return self.json.get("accountMembershipStatus")

    @cached_property
    def comId(self) -> int:
        return self.json.get("ndcId")

    @cached_property
    def followersCount(self) -> int:
        return self.json.get("membersCount")

    @cached_property
    def followingStatus(self) -> int:
        return self.json.get("followingStatus")

    @cached_property
    def icon(self) -> str:
        return self.json.get("icon")

    @cached_property
    def id(self) -> str:
        return self.json.get("uid")

    @cached_property
    def influencer(self) -> InfluencerInfo:
        return InfluencerInfo(self.json.get("influencerInfo") or {})

    @cached_property
    def influencerCreatedTime(self) -> str:
        return self.influencer.createdTime

    @cached_property
    def influencerFansCount(self) -> int:
        return self.influencer.fansCount

    @cached_property
    def influencerMonthlyFee(self) -> int:
        return self.influencer.monthlyFee

    @cached_property
    def isGlobalProfile(self) -> bool:
        return self.json.get("isGlobal")

    @cached_property
    def isInfluencerPinned(self) -> bool:
        return self.influencer.isPinned

    @cached_property
    def isNicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @cached_property
    def level(self) -> int:
        return self.json.get("level")

    @cached_property
    def membershipStatus(self) -> int:
        return self.json.get("membershipStatus")

    @cached_property
    def nickname(self) -> str:
        return self.json.get("nickname")

    @cached_property
    def reputation(self) -> int:
        return self.json.get("reputation")

    @cached_property
    def role(self) -> int:
        return self.json.get("role")

    @cached_property
    def status(self) -> int:
        return self.json.get("status")


@dataclass(repr=False)
class Invitation:
    json: dict

    @cached_property
    def author(self) -> Author:
        return Author(self.json.get("author") or {})

    @cached_property
    def authorId(self) -> str:
        return self.author.id

    @cached_property
    def code(self) -> str:
        return self.json.get("inviteCode")

    @cached_property
    def comId(self) -> int:
        return self.json.get("ndcId")

    @cached_property
    def duration(self) -> int:
        return self.json.get("duration")

    @cached_property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @cached_property
    def id(self) -> str:
        return self.json.get("invitationId")

    @cached_property
    def link(self) -> str:
        return self.json.get("link")

    @cached_property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    @cached_property
    def status(self) -> int:
        return self.json.get("status")
