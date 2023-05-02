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
from . import userprofile
import dataclasses
import functools
import typing

__all__ = ('CurrentUserInfo',)


@dataclasses.dataclass(repr=False)
class CurrentUserInfo:
    """Represent the current user logged.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    bio: Optional[:class:`str`]
        User bio.
    consecutiveCheckInDays: :class:`int`
        User check-in days.
    icon: :class:`str`
        User icon url.
    id: :class:`str`
        User id.
    level: :class:`int`
        Community user level.
    nickname: :class:`str`
        User nickname.
    notificationsCount: :class:`int`
        Notifications count.
    reputation: :class:`int`
        Community user reputation.
    role: :class:`int`
        Community user role.
    user: :class:`UserProfile`
        User profile object.

    """
    json: dict

    @functools.cached_property
    def bio(self) -> typing.Optional[str]:
        """User bio."""
        return self.user.bio

    @functools.cached_property
    def consecutiveCheckInDays(self) -> int:
        """Check-in days."""
        return self.user.consecutiveCheckInDays

    @functools.cached_property
    def icon(self) -> str:
        """User icon url."""
        return self.user.icon

    @functools.cached_property
    def id(self) -> str:
        """User id."""
        return self.user.id

    @functools.cached_property
    def level(self) -> int:
        """Community user level."""
        return self.user.level

    @functools.cached_property
    def nickname(self) -> str:
        """User nickname."""
        return self.user.nickname

    @functools.cached_property
    def notificationsCount(self) -> int:
        """Notifications count."""
        return self.json.get('notificationsCount') or 0

    @functools.cached_property
    def reputation(self) -> int:
        """Community user reputation."""
        return self.user.reputation

    @functools.cached_property
    def role(self) -> int:
        """Community user role."""
        return self.user.role

    @functools.cached_property
    def user(self) -> userprofile.UserProfile:
        """User profile object."""
        return userprofile.UserProfile(self.json.get('userProfile') or {})
