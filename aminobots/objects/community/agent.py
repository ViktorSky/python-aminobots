from typing import Optional
from ..object import Object

__all__ = 'Agent',


class Agent(Object):
    json: dict

    @property
    def accountMembershipStatus(self) -> int:
        return self.json.get("accountMembershipStatus")

    @property
    def comId(self) -> Optional[int]:
        return self.json.get("ndcId")

    @property
    def followersCount(self) -> int:
        return self.json.get("membersCount")

    @property
    def followingStatus(self) -> int:
        return self.json.get("followingStatus")

    @property
    def icon(self) -> Optional[str]:
        return self.json.get("icon")

    @property
    def id(self) -> str:
        return self.json.get("uid")

    @property
    def isGlobalProfile(self) -> bool:
        return self.json.get("isGlobal")

    @property
    def level(self) -> int:
        return self.json.get("level")

    @property
    def membershipStatus(self) -> int:
        return self.json.get("membershipStatus")

    @property
    def nickname(self) -> Optional[str]:
        return self.json.get("nickname")

    @property
    def nicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @property
    def reputation(self) -> Optional[int]:
        return self.json.get("reputation") or 0

    @property
    def role(self) -> int:
        return self.json.get("role") or 111

    @property
    def status(self) -> int:
        return self.json.get("status")
