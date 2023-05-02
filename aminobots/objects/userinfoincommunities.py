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
from . import userprofilelist
import dataclasses
import functools
import typing

__all__ = ('UserInfoInCommunities',)


@dataclasses.dataclass(repr=False)
class UserInfoInCommunities:
    """Represent the user profile in multiple communities.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    accountMembershipStatus: List[:class:`int`]
        Account membership status.
    avatarId: List[:class:`str`]
        User avatar frame ids.
    comId: List[:class:`int`]
        Community ids.
    followingStatus: List[:class:`int`]
        Following this user.
    icon: List[:class:`str`]
        Community user icon urls.
    id: List[:class:`str`]
        All user ids.
    isGlobal: List[:class:`bool`]
        Global or commmunity profile.
    level: List[Optional[:class:`int`]]
        All community user levels.
    membershipStatus: List[:class:`int`]
        Membership status.
    nickname: List[:class:`str`]
        Community user nicknames.
    nicknameVerified: List[:class:`bool`]
        Is nickname verified.
    profile: :class:`UserProfileList`
        All user profiles.
    reputation: List[:class:`int`]
        Community user reputation.
    role: List[:class:`int`]
        Community user role.
    status: List[:class:`int`]
        Profile status.

    """
    json: typing.Dict[str, typing.Dict[str, typing.Any]]

    @functools.cache
    def __getitem__(self, comId: int) -> userprofile.UserProfile:
        """User profile in one community."""
        profile = self.json[str(comId)]
        return userprofile.UserProfile(profile)

    @functools.cached_property
    def accountMembershipStatus(self) -> typing.List[int]:
        """Account membership status."""
        return self.profile.accountMembershipStatus

    @functools.cached_property
    def avatarId(self) -> typing.List[str]:
        """User avatar frame ids."""
        return self.profile.avatarId

    @functools.cached_property
    def comId(self) -> typing.List[int]:
        """Community ids."""
        return self.profile.comId

    @functools.cached_property
    def followersCount(self) -> typing.List[int]:
        """Community user followers count."""
        return self.profile.followersCount

    @functools.cached_property
    def followingsCount(self) -> typing.List[int]:
        """Community user followings count."""
        return self.profile.followingsCount

    @functools.cached_property
    def followingStatus(self) -> typing.List[int]:
        """Following this user."""
        return self.profile.followingStatus

    @functools.cached_property
    def icon(self) -> typing.List[str]:
        """Community user icon urls."""
        return self.profile.icon

    @functools.cached_property
    def id(self) -> typing.List[str]:
        """All user ids."""
        return self.profile.id

    @functools.cached_property
    def isGlobal(self) -> typing.List[bool]:
        """Global or commmunity profile."""
        return self.profile.isGlobal

    @functools.cached_property
    def level(self) -> typing.List[typing.Optional[int]]:
        """All community user level."""
        return self.profile.level

    @functools.cached_property
    def membershipStatus(self) -> typing.List[int]:
        """Membership status."""
        return self.profile.membershipStatus

    @functools.cached_property
    def nickname(self) -> typing.List[str]:
        """User nicknames."""
        return self.profile.nickname

    @functools.cached_property
    def nicknameVerified(self) -> typing.List[bool]:
        """Is nickname verified."""
        return self.profile.nicknameVerified

    @functools.cached_property
    def profile(self) -> userprofilelist.UserProfileList:
        """All user profiles."""
        return userprofilelist.UserProfileList([p.get('userProfile') or {} for p in self.json.values()])

    @functools.cached_property
    def reputation(self) -> typing.List[int]:
        """Community user reputation."""
        return self.profile.reputation

    @functools.cached_property
    def role(self) -> typing.List[int]:
        """Community user roles."""
        return self.profile.role

    @functools.cached_property
    def status(self) -> typing.List[int]:
        """Profile status."""
        return self.profile.status


{
    "124421795": {
        "userProfile": {
            #"status": 0,
            #"isNicknameVerified": False,
            #"uid": "d780e629-1ec7-4c56-9974-42c515ba56c6",
            #"level": 9,
            #"followingStatus": 0,
            #"accountMembershipStatus": 0,
            #"isGlobal": False,
            #"membershipStatus": 0,
            #"avatarFrameId": "14fbc07b-1662-4768-89d8-183f79727b41",
            #"reputation": 1159,
            #"role": 0,
            #"ndcId": 124421795,
            #"membersCount": 12,
            #"nickname": "Viktor",
            #"icon": "http:\/\/pm1.narvii.com\/8548\/fcf32917d3c212763e18dfe79fd95acbe3fbe86ar1-500-512v2_00.jpg"
        }
    }
}
