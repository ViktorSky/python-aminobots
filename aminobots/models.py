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

from typing import Optional, Union
from dataclasses import dataclass
from functools import cached_property
from .utils import Date
from .enums import ObjectType
from . import objects

__all__ = (
    'AccountInfo',
    'AllPushSettings'
    'Api',
    'ChatInfo',
    'ChatMembers',
    'CommunityInfluencers',
    'CommunityInfo',
    'FromDevice',
    'HTTPResponse',
    'JoinedCommunities',
    'LinkResolution',
    'LinkIdentify',
    'Login',
    'MembershipConfig',
    'MembershipInfo',
    'PushNotification',
    'SearchCommunity',
    'SearchQuiz',
    'SearchUser',
    'UserInfo',
    'VerifyPassword',
    'Wallet',
    'WalletAds',
    'WalletHistory'
)


@dataclass(repr=False)
class Api:
    """Represent the amino api response.

    Examples
    --------
    ```
    >>> api = Api({
    ...     'api:message': 'OK.',
    ...     'api:statuscode': 0,
    ...     'api:duration': '0.0s',
    ...     'api:timestamp': str(Date()),
    ... })
    >>> api.duration
    0.0
    ```

    Parameters
    ----------
    json: :class:`dict`
        The raw API data.

    Attributes
    ----------
    duration: :class:`float`
        Duration of prossesing for the request.
    message: :class:`str`
        Request message.
    statuscode: :class:`int`
        Status Code of the request.
    timestamp: :class:`Date`
        The timestamp of the request.

    """
    json: dict

    @cached_property
    def duration(self) -> float:
        """Duration of prossesing for the request."""
        return float(self.json.get('api:duration', '0.0s').removesuffix('s'))

    @cached_property
    def message(self) -> str:
        """Request message."""
        return self.json.get('api:message')

    @cached_property
    def statuscode(self) -> int:
        """Status Code of the request."""
        return self.json.get('api:statuscode', 0)

    @cached_property
    def timestamp(self) -> Date:
        """The timestamp of the request."""
        return Date(self.json.get('api:timestamp', str(Date())))


@dataclass(repr=False)
class HTTPResponse:
    """Represent the HTTPClient response base.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    api: :class:`Api`
        Api request info.

    """
    json: dict

    @cached_property
    def api(self) -> Api:
        """Api request info."""
        return Api(self.json)

    def ok(self) -> bool:
        """Check if the response has statuscode `0`."""
        return self.api.statuscode == 0


class FromDevice(HTTPResponse):
    @cached_property
    def auid(self) -> str:
        """Amino user id."""
        return self.json.get('auid')


class AccountInfo(HTTPResponse):
    @cached_property
    def account(self) -> objects.Account:
        """Account object."""
        return objects.Account(self.json.get('account') or {})


class CommunityInfo(HTTPResponse):
    @cached_property
    def community(self) -> objects.Community:
        """Community object."""
        return objects.Community(self.json.get('community') or {})


class UserInfo(HTTPResponse):
    """Represents a user profile.

    Attributes
    ----------
    json : :class:`dict`
        The raw API data.
    user : :class:`UserProfile`
        User profile.

    """
    @cached_property
    def user(self) -> objects.UserProfile:
        """User profile."""
        return objects.UserProfile(self.json.get('userProfile') or {})


class ChatInfo(HTTPResponse):
    """Represents a chat thread response.

    Attributes
    ----------
    json : :class:`dict`
        The raw API data.
    chat : :class:`Thread`
        Chat thread info.

    """
    @cached_property
    def chat(self) -> objects.Thread:
        return objects.Thread(self.json.get('thread') or {})


class CommunityInfluencers(HTTPResponse):
    @cached_property
    def user(self) -> objects.UserProfileList:
        return objects.UserProfileList(self.json.get('userProfileList') or {})


class LinkResolution(HTTPResponse):
    @cached_property
    def comId(self) -> int:
        """Community id."""
        return self.linkInfoV2.linkInfo.comId or self.linkInfoV2.community.id

    @cached_property
    def extensions(self) -> objects.linkinfov2.Extensions:
        """Link extensions."""
        return self.linkInfoV2.extensions

    @cached_property
    def id(self) -> Union[str, int]:
        """Object id."""
        return self.linkInfoV2.extensions.linkInfo.objectId

    @cached_property
    def type(self) -> ObjectType:
        """Object type."""
        return ObjectType(self.linkInfoV2.linkInfo.objectType)

    @cached_property
    def linkInfoV2(self) -> objects.LinkInfoV2:
        """LinkInfoV2 object."""
        return objects.LinkInfoV2(self.json.get('linkInfoV2', {}))

    @cached_property
    def path(self) -> str:
        """NDC path."""
        return self.linkInfoV2.path

    @cached_property
    def fullPath(self) -> Optional[str]:
        """Web path."""
        return self.linkInfoV2.linkInfo.fullPath

    @cached_property
    def fullUrl(self) -> Optional[str]:
        """Full path url."""
        return self.linkInfoV2.linkInfo.fullUrl

    @cached_property
    def shortCode(self) -> Optional[str]:
        """Short code url."""
        return self.linkInfoV2.linkInfo.shortCode

    @cached_property
    def shortUrl(self) -> Optional[str]:
        """Short url."""
        return self.linkInfoV2.linkInfo.shortUrl


class LinkIdentify(HTTPResponse):
    @cached_property
    def community(self) -> objects.Community:
        """Community info."""
        return objects.Community(self.json.get('community') or {})

    @cached_property
    def invitation(self) -> objects.Invitation:
        """Community invitation info."""
        return objects.Invitation(self.json.get('invitation'))

    @cached_property
    def invitationId(self) -> Optional[str]:
        """Community invitation id."""
        return self.json.get('invitationId')

    @cached_property
    def path(self) -> str:
        """NDC path."""
        return self.json.get('path')


class ChatMembers(HTTPResponse):
    @cached_property
    def members(self) -> objects.MemberList:
        return objects.MemberList(self.json.get('memberList') or [])


class PushNotification(HTTPResponse):
    @cached_property
    def enabled(self) -> bool:
        """Push enabled."""
        return self.json.get('pushEnabled')

    @cached_property
    def extensions(self) -> objects.PushExtensions:
        """Global/Community notification config."""
        return objects.PushExtensions(self.json.get('pushExtensions') or {})


class MembershipInfo(HTTPResponse):
    @cached_property
    def enabled(self) -> bool:
        """Account membership enabled."""
        return self.json.get('accountMembershipEnabled')

    @cached_property
    def hasAnyAppleSubscription(self) -> bool:
        return self.json.get('hasAnyAppleSubscription')

    @cached_property
    def hasAnyAndroidSubscription(self) -> bool:
        return self.json.get('hasAnyAndroidSubscription')

    @cached_property
    def premiumEnabled(self) -> bool:
        return self.json.get('premiumFeatureEnabled')

    @cached_property
    def membership(self) -> objects.Membership:
        """User account membership object."""
        return objects.Membership(self.json.get('membership') or {})


class MembershipConfig(HTTPResponse):
    @cached_property
    def membership(self) -> objects.Membership:
        """User account membership."""
        return objects.Membership(self.json.get('membership') or {})


class WalletAds(HTTPResponse):
    @cached_property
    def coinsEarned(self) -> objects.CoinsEarnedByAds:
        return objects.CoinsEarnedByAds(self.json.get('coinsEarnedByAds') or {})

    @cached_property
    def estimatedCoinsEarned(self) -> float:
        return self.json.get('estimatedCoinsEarnedByAds')


class WalletInfo(HTTPResponse):
    @cached_property
    def wallet(self) -> objects.Wallet:
        return objects.Wallet(self.json.get('wallet') or {})


class WalletHistory(HTTPResponse):
    @cached_property
    def history(self) -> objects.CoinHistoryList:
        """Coin history list."""
        return objects.CoinHistoryList(self.json.get('coinHistoryList') or [])


class AllPushSettings(HTTPResponse):
    @cached_property
    def settings(self) -> objects.PushSettings:
        """Represents the push settings for all joined communities."""
        return objects.PushSettings(self.json.get('pushSettings') or [])


class VerifyPassword(HTTPResponse):
    pass


class Login(HTTPResponse):
    @cached_property
    def account(self) -> objects.Account:
        """Account data."""
        return objects.Account(self.json.get('account', {}))

    @cached_property
    def auid(self) -> str:
        """Authentication id."""
        return self.json.get('auid')

    @cached_property
    def secret(self) -> str:
        """Encoded Password."""
        return self.json.get('secret')

    @cached_property
    def sid(self) -> str:
        """Session token."""
        return self.json.get('sid')

    @cached_property
    def user(self) -> objects.UserProfile:
        """Global Profile data."""
        return objects.UserProfile(self.json.get('userProfile', {}))


class JoinedCommunities(HTTPResponse):
    @cached_property
    def communities(self) -> objects.CommunityList:
        """CommunityList object."""
        return objects.CommunityList(self.json.get('communityList'))

    @cached_property
    def showStoreBadge(self) -> bool:
        """Show user store badge."""
        return self.json.get('showStoreBadge')

    @cached_property
    def user(self) -> objects.UserInfoInCommunities:
        """User profile in communities."""
        return objects.UserInfoInCommunities(self.json.get('userInfoInCommunities') or {})


class SearchCommunity(HTTPResponse):
    @cached_property
    def communities(self) -> objects.CommunityList:
        """Community list object."""
        return objects.CommunityList(self.json.get('communityList') or [])

    @cached_property
    def endpointMatchedCommunity(self) -> dict:
        return self.json.get('endpointMatchedCommunity') or {}

    @cached_property
    def userInfoInJoinedCommunities(self) -> dict:
        return self.json.get('userInfoInJoinedCommunities', {})

    @cached_property
    def userJoinedCommunityList(self) -> list:
        return self.json.get('userJoinedCommunityList') or []


class SearchQuiz(HTTPResponse):
    @cached_property
    def communities(self) -> objects.CommunityInfoMapping:
        return objects.CommunityInfoMapping(self.json.get('communityInfoMapping') or {})

    @cached_property
    def paging(self) -> objects.Paging:
        return objects.Paging(self.json.get('paging') or {})

    @cached_property
    def posts(self):
        return objects.PostList(self.json.get('postList') or [])

    @cached_property
    def numberOfJoinedCommunities(self) -> int:
        return self.json.get('numberOfJoinedCommunities') or 0


class SearchUser(HTTPResponse):
    @cached_property
    def user(self) -> objects.UserProfileList:
        return objects.UserProfileList(self.json.get('userProfileList') or [])

    @cached_property
    def usersCount(self) -> int:
        return self.json.get('userProfileCount') or 0
