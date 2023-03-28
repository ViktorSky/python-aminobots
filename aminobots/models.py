from typing import List, Optional, Union
from dataclasses import dataclass
from .enums import ObjectType
from .abc import Object
from .utils import Date
from .objects import (
    Account,
    UserProfile,
    UserProfileList,
    LinkInfoV2,
    linkinfov2
)

__all__ = (
    'AccountInfo',
    'LinkResolution',
    'LinkIdentify',
    'Login',
    'UserInfo'
)


@dataclass(repr=False, slots=True)
class Api(Object):
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

    Attributes
    ----------
    duration: :class:`float`
        Duration of prossesing for the request.
    message: :class:`str`
        Message for the request.
    statuscode: :class:`int`
        Status Code of the request.
    timestamp: :class:`Date`
        The timestamp of the request.

    """

    @property
    def message(self) -> str:
        return self.json.get('api:message')

    @property
    def statuscode(self) -> int:
        return self.json.get('api:statuscode', 0)

    @property
    def duration(self) -> float:
        return float(self.json.get('api:duration', '0.0s').removesuffix('s'))

    @property
    def timestamp(self) -> Date:
        return Date(self.json.get('api:timestamp', str(Date())))


@dataclass(repr=False, slots=True)
class HTTPResponse(Object):
    @property
    def api(self) -> Api:
        return Api(self.json)


class AccountInfo(HTTPResponse):
    ...


class CommunityInfo(HTTPResponse):
    ...


class UserInfo(HTTPResponse):
    ...


class CommunityInfluencers(HTTPResponse):
    @property
    def user(self) -> UserProfileList:
        return UserProfileList(self.json.get('userProfileList') or {})

    @property
    def monthlyFee(self) -> List[int]:
        return self.user.influencer.monthlyFee

    @property
    def nickname(self) -> List[str]:
        return self.user.nickname

    @property
    def fansCount(self) -> List[int]:
        return self.user.influencer.fansCount

    @property
    def id(self) -> List[str]:
        return self.user.id


class LinkResolution(HTTPResponse):
    @property
    def comId(self) -> int:
        return self.linkInfoV2.linkInfo.comId or self.linkInfoV2.community.id

    @property
    def extensions(self) -> linkinfov2.Extensions:
        return self.linkInfoV2.extensions

    @property
    def id(self) -> Union[str, int]:
        return self.linkInfoV2.extensions.linkInfo.objectId

    @property
    def type(self) -> ObjectType:
        return ObjectType(self.linkInfoV2.linkInfo.objectType)

    @property
    def linkInfoV2(self) -> LinkInfoV2:
        return LinkInfoV2(self.json.get('linkInfoV2', {}))

    @property
    def path(self) -> str:
        return self.linkInfoV2.path

    @property
    def fullPath(self) -> Optional[str]:
        return self.linkInfoV2.linkInfo.fullPath

    @property
    def fullUrl(self) -> Optional[str]:
        return self.linkInfoV2.linkInfo.fullUrl

    @property
    def shortCode(self) -> Optional[str]:
        return self.linkInfoV2.linkInfo.shortCode

    @property
    def shortUrl(self) -> Optional[str]:
        return self.linkInfoV2.linkInfo.shortUrl


class LinkIdentify(HTTPResponse):
    ...


class Login(HTTPResponse):
    @property
    def account(self) -> Account:
        """Account data."""
        return Account(self.json.get('account', {}))

    @property
    def auid(self) -> str:
        """Authentication id."""
        return self.json.get('auid')

    @property
    def secret(self) -> str:
        """Encoded Password."""
        return self.json.get('secret')

    @property
    def sid(self) -> str:
        """Session token."""
        return self.json.get('sid')

    @property
    def user(self) -> UserProfile:
        """Global Profile data."""
        return UserProfile(self.json.get('userProfile', {}))
