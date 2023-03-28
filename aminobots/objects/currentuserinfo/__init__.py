from typing import Optional
from ..object import Object
from ..userprofile import UserProfile

__all__ = ('CurrentUserInfo',)


class CurrentUserInfo(Object):
    @property
    def bio(self) -> Optional[str]:
        return self.user.bio

    @property
    def consecutiveCheckInDays(self) -> int:
        return self.user.consecutiveCheckInDays

    @property
    def icon(self) -> str:
        return self.user.icon

    @property
    def id(self) -> str:
        return self.user.id

    @property
    def level(self) -> int:
        return self.user.level

    @property
    def nickname(self) -> str:
        return self.user.nickname

    @property
    def notificationsCount(self) -> int:
        return self.json.get('notificationsCount') or 0

    @property
    def reputation(self) -> int:
        return self.user.reputation

    @property
    def role(self) -> int:
        return self.user.role

    @property
    def user(self) -> UserProfile:
        return UserProfile(self.json.get('userProfile') or {})

    UserProfile.level
