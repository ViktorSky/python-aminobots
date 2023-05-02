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
import dataclasses
import functools

__all__ = ('Invitation',)


@dataclasses.dataclass(repr=False)
class InfluencerInfo:
    json: dict

    @functools.cached_property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @functools.cached_property
    def fansCount(self) -> int:
        return self.json.get("fansCount") or 0

    @functools.cached_property
    def isPinned(self) -> bool:
        return self.json.get("pinned") or False

    @functools.cached_property
    def monthlyFee(self) -> int:
        return self.json.get("monthlyFee") or 0


@dataclasses.dataclass(repr=False)
class Author:
    json: dict

    @functools.cached_property
    def accountMembershipStatus(self) -> int:
        return self.json.get("accountMembershipStatus")

    @functools.cached_property
    def comId(self) -> int:
        return self.json.get("ndcId")

    @functools.cached_property
    def followersCount(self) -> int:
        return self.json.get("membersCount")

    @functools.cached_property
    def followingStatus(self) -> int:
        return self.json.get("followingStatus")

    @functools.cached_property
    def icon(self) -> str:
        return self.json.get("icon")

    @functools.cached_property
    def id(self) -> str:
        return self.json.get("uid")

    @functools.cached_property
    def influencer(self) -> InfluencerInfo:
        return InfluencerInfo(self.json.get("influencerInfo") or {})

    @functools.cached_property
    def influencerCreatedTime(self) -> str:
        return self.influencer.createdTime

    @functools.cached_property
    def influencerFansCount(self) -> int:
        return self.influencer.fansCount

    @functools.cached_property
    def influencerMonthlyFee(self) -> int:
        return self.influencer.monthlyFee

    @functools.cached_property
    def isGlobalProfile(self) -> bool:
        return self.json.get("isGlobal")

    @functools.cached_property
    def isInfluencerPinned(self) -> bool:
        return self.influencer.isPinned

    @functools.cached_property
    def isNicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @functools.cached_property
    def level(self) -> int:
        return self.json.get("level")

    @functools.cached_property
    def membershipStatus(self) -> int:
        return self.json.get("membershipStatus")

    @functools.cached_property
    def nickname(self) -> str:
        return self.json.get("nickname")

    @functools.cached_property
    def reputation(self) -> int:
        return self.json.get("reputation")

    @functools.cached_property
    def role(self) -> int:
        return self.json.get("role")

    @functools.cached_property
    def status(self) -> int:
        return self.json.get("status")


@dataclasses.dataclass(repr=False)
class Invitation:
    json: dict

    @functools.cached_property
    def author(self) -> Author:
        return Author(self.json.get("author") or {})

    @functools.cached_property
    def authorId(self) -> str:
        return self.author.id

    @functools.cached_property
    def code(self) -> str:
        return self.json.get("inviteCode")

    @functools.cached_property
    def comId(self) -> int:
        return self.json.get("ndcId")

    @functools.cached_property
    def duration(self) -> int:
        return self.json.get("duration")

    @functools.cached_property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @functools.cached_property
    def id(self) -> str:
        return self.json.get("invitationId")

    @functools.cached_property
    def link(self) -> str:
        return self.json.get("link")

    @functools.cached_property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    @functools.cached_property
    def status(self) -> int:
        return self.json.get("status")
