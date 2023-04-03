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

__all__ = ('Invitation',)

@dataclass(repr=False)
class InfluencerInfo:
    json: dict

    @property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @property
    def fansCount(self) -> int:
        return self.json.get("fansCount") or 0

    @property
    def isPinned(self) -> bool:
        return self.json.get("pinned") or False

    @property
    def monthlyFee(self) -> int:
        return self.json.get("monthlyFee") or 0


@dataclass(repr=False)
class Author:
    json: dict

    @property
    def accountMembershipStatus(self) -> int:
        return self.json.get("accountMembershipStatus")

    @property
    def comId(self) -> int:
        return self.json.get("ndcId")

    @property
    def followersCount(self) -> int:
        return self.json.get("membersCount")

    @property
    def followingStatus(self) -> int:
        return self.json.get("followingStatus")

    @property
    def icon(self) -> str:
        return self.json.get("icon")

    @property
    def id(self) -> str:
        return self.json.get("uid")

    @property
    def influencer(self) -> InfluencerInfo:
        return InfluencerInfo(self.json.get("influencerInfo") or {})

    @property
    def influencerCreatedTime(self) -> str:
        return self.influencer.createdTime

    @property
    def influencerFansCount(self) -> int:
        return self.influencer.fansCount

    @property
    def influencerMonthlyFee(self) -> int:
        return self.influencer.monthlyFee

    @property
    def isGlobalProfile(self) -> bool:
        return self.json.get("isGlobal")

    @property
    def isInfluencerPinned(self) -> bool:
        return self.influencer.isPinned

    @property
    def isNicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @property
    def level(self) -> int:
        return self.json.get("level")

    @property
    def membershipStatus(self) -> int:
        return self.json.get("membershipStatus")

    @property
    def nickname(self) -> str:
        return self.json.get("nickname")

    @property
    def reputation(self) -> int:
        return self.json.get("reputation")

    @property
    def role(self) -> int:
        return self.json.get("role")

    @property
    def status(self) -> int:
        return self.json.get("status")


@dataclass(repr=False)
class Invitation:
    json: dict

    @property
    def author(self) -> Author:
        return Author(self.json.get("author") or {})

    @property
    def authorId(self) -> str:
        return self.author.id

    @property
    def code(self) -> str:
        return self.json.get("inviteCode")

    @property
    def comId(self) -> int:
        return self.json.get("ndcId")

    @property
    def duration(self) -> int:
        return self.json.get("duration")

    @property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @property
    def id(self) -> str:
        return self.json.get("invitationId")

    @property
    def link(self) -> str:
        return self.json.get("link")

    @property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    @property
    def status(self) -> int:
        return self.json.get("status")
