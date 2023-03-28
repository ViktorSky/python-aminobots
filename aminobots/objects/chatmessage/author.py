from ..object import Object

from .avatarframe import *

__all__ = ('Author',)


class Author(Object):

    @property
    def accountMembershipStatus(self) -> int:
        return self.json.get('accountMembershipStatus', 0)

    @property
    def avatarFrame(self) -> AvatarFrame:
        return AvatarFrame(self.json.get('avatarFrame') or dict())

    @property
    def icon(self) -> str:
        return self.json.get('icon')

    @property
    def id(self) -> str:
        return self.json.get('uid')

    @property
    def level(self) -> int:
        return self.json.get('level')

    @property
    def nickname(self) -> str:
        return self.json.get('nickname', 0)

    @property
    def reputation(self) -> int:
        return self.json.get('reputation', 0)

    @property
    def role(self) -> int:
        return self.json.get('role')

    @property
    def status(self) -> int:
        return self.json.get('status')
