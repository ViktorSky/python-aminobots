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
from typing import (
    Any,
    ClassVar,
    Optional,
    Protocol,
    Union,
    runtime_checkable
)
import logging
import yarl
from . import enums

__all__ = (
    'ABCAmino',
    'ABCACM',
    'ABCHTTPClient',
    'ABCRTCClient',
    'ABCWSClient',
    'Object',
)


@runtime_checkable
@dataclass(repr=False)
class Object(Protocol):
    json: Union[list, dict]


@runtime_checkable
class ABCAmino(Protocol):
    __slots__ = ()

    logger: logging.Logger
    http: 'ABCHTTPClient'
    rtc: 'ABCRTCClient'
    ws: 'ABCWSClient'

    async def get_from_link(self, link: str, /) -> Object:
        """Request link data.

        Parameters
        ----------
        link : :class:`str`
            Http amino url.
    
        Examples
        --------
        ```
        >>> link: str = input('amino link: ')
        >>> r = await amino.get_from_link(link)
        >>> list(r.json)
        ['api:duration', 'api:message', 'linkInfoV2', 'api:timestamp', 'api:statuscode']
        ```

        """
        raise NotImplementedError

    async def get_from_device(self, device: str, /) -> Object:
        """Get auid (user-id) from device.

        Parameters
        ----------
        device : :class:`str` | :class:`Device`
            The user device.

        """
        raise NotImplementedError

    async def get_link_info(self, link: str, /) -> Object:
        """Request link info. (only community links)

        Parameters
        ----------
        link : :class:`str`
            Http amino url.

        Examples
        --------
        ```
        >>> link: str = input('community link: ')
        >>> r = await amino.get_link_info(link)
        ```

        """
        raise NotImplementedError

    async def get_ads_info(self) -> Object:
        """Get account coins earned by ads.

        Examples
        --------
        ```
        >>> ads = await amino.get_ads_info()
        >>> print(ads.coinsEarned.weekly)
        ```

        """
        raise NotImplementedError

    async def get_user_info(self, id: str, /, cid: Optional[int] = ...) -> Object:
        """Request user profile.

        Parameters
        ----------
        id : :class:`str`
            User id.
        cid : :class:`int` | `None`
            Community id.

        Examples
        --------
        ```
        >>> user_link = input('user-link:')
        >>> info = await amino.get_from_link(user_link)
        >>> user = await amino.get_user_info(info.id)
        >>> print('nickname:', user.nickname)
        ```

        """
        raise NotImplementedError

    async def get_account_info(self) -> Object:
        """Request account info.

        Requirements
        ------------
        - Login

        Examples
        --------
        ```
        >>> info = await amino.get_account_info()
        >>> print(info.account.email)
        ```

        """
        raise NotImplementedError

    async def get_chat_info(self, id: str, /, cid: Optional[int] = ...) -> Object:
        """Get chat thread info.

        Parameters
        ----------
        id : :class:`str`
            Chat thread id.
        cid : :class:`int` | `None`
            Community id.

        """
        raise NotImplementedError

    async def get_chat_members(self, id: str, /, start: int = ..., size: int = ..., cid: Optional[int] = ...) -> Object:
        """Get members profiles in chat.

        Parameters
        ----------
        id : :class:`str`
            Chat thread id.
        start : :class:`int`
            Start index.
        size : :class:`int`
            Size of list of users. Max size is 100.
        cid : :class:`int` | `None`
            Community id.
        """
        raise NotImplementedError

    async def get_community_info(self, id: int, /) -> Object:
        """Request Community info.

        Parameters
        ----------
        id : :class:`int`
            Community id.

        Examples
        --------
        ```
        >>> community_link = input('community-link: ')
        >>> cid = await amino.get_from_link(community_link)
        >>> info = await amino.get_community_info(cid.id)
        >>> print('community name:', info.community.name)
        ```

        """
        raise NotImplementedError

    async def get_community_trending(self, cid: int, /) -> Object:
        """Get trending of community.

        Parameters
        ----------
        cid : :class:`int`
            Community id.

        Examples
        --------
        ```
        >>> trending = await amino.get_community_trending(communityId)
        ```

        """
        raise NotImplementedError

    async def get_wallet_info(self) -> Object:
        """Get account wallet.

        Requirements
        ------------
        - Login

        Examples
        --------
        ```
        >>> info = await amino.get_wallet_info()
        >>> print(info.wallet.totalCoins)
        ```

        """
        raise NotImplementedError

    async def get_wallet_history(self, start: int = ..., size: int = ...) -> Object:
        """Get account coin history.

        Requirements
        ------------
        - Login

        Parameters
        ----------
        start : :class:`int`
            The history index.
        size : :class:`int`
            The size of the history list. (max is 100)

        """
        raise NotImplementedError

    async def get_account_push_settings(self) -> Object:
        """Get account global push settings.

        Requirements
        ------------
        - Login

        Examples
        --------
        ```
        >>> push = await amino.get_account_push_settings()
        >>> print(push.settings.communityIds)
        ```

        """
        raise NotImplementedError

    async def get_push_settings(self, cid: int = ...) -> Object:
        """Get global/community push settings.

        Requirements
        ------------
        - Login

        Parameters
        ----------
        cid : :class:`int`
            The community id.

        """
        raise NotImplementedError

    async def set_push_settings(self, activities: bool, broadcasts: bool, cid: int = ...) -> Object:
        """Update the global/community push settings.

        Requirements
        ------------
        - Login

        Parameters
        ----------
        activities : :class:`bool`
            Enable members activities notifications.
        broadcasts : :class:`bool`
            Enable leaders broadcasts notifications.
        cid : :class:`int`
            The community id.

        Examples
        --------
        ```
        >>> await amino.set_push_settings(False, True, communityId)
        ```

        """
        raise NotImplementedError

    async def get_membership_info(self) -> Object:
        """Get account membership info.

        Requirements
        ------------
        - Login

        Examples
        --------
        ```
        >>> info = await amino.get_membership_info()
        >>> print(info.enabled)
        ```

        """
        raise NotImplementedError

    async def joined_chats(self, cid: int, start: int = ..., size: int = ...) -> Object:
        """Get global/community joined chats.

        Parameters
        ----------
        cid : :class:`int`
            Comminity id.
        start : :class:`int`
            Start index.
        size : :class:`int`
            Size of the list. Max size is 100.

        """
        raise NotImplementedError

    async def configure_membership(self, autoRenew: bool) -> Object:
        """Update the account membership.

        Requirements
        ------------
        - Login

        Parameters
        ----------
        autoRenew : :class:`bool`
            Auto renew the membership.

        """
        raise NotImplementedError

    async def joined_communities(self) -> Object:
        """Get list of joined communities.

        Parameters
        ----------
        start : :class:`int`
            Start index.
        size : :class:`int`
            Size of the list. Max size is 100.

        Examples
        --------
        ```
        >>> await amino.joined_communities()
        ```

        """
        raise NotImplementedError

    async def get_vip_users(self, cid: int, /) -> Object:
        """Get community influencers (vip users)

        Parameters
        ----------
        cid : :class:`int`
            Community id.

        """
        raise NotImplementedError

    async def search_user(self, q: str, /, cid: Optional[int] = ...) -> Object:
        """Search user. Match amino id or nickname.

        Parameters
        ----------
        q : :class:`str`
            Query string.
        cid : :class:`int` | `None`
            Community id.

        """
        raise NotImplementedError

    async def search_community(self, q: str, /, language: str = ...) -> Object:
        """Search community. Match amino-id, name.

        Parameters
        ----------
        q : :class:`str`
            Query string.
        language : :class:`Language`
            Search language filter.

        """
        raise NotImplementedError

    async def search_chat(self, q: str, /, cid: Optional[int] = ...) -> Object:
        """Search global/community chat.

        Parameters
        ----------
        q : :class:`str`
            Chat title, search key.
        cid : :class:`int`
            Community id.

        """
        raise NotImplementedError

    async def search_quiz(self, q: str, /, cid: Optional[int] = ...) -> Object:
        """Search quiz posts.

        Parameters
        ----------
        q : :class:`str`
            Quiz title, search key.
        cid : :class:`int` | `None`
            Community id.

        """
        raise NotImplementedError

    async def verify_password(self, password: str = ..., secret: str = ...) -> Object:
        """Verify the account password.

        Parameters
        ----------
        password : :class:`str` | `None`
            The account password.
        secret : :class:`str` | `None`
            The account encoded secret password.

        Examples
        --------
        ```
        >>> await amino.login_sid(os.environ['sid'])
        >>> check = await amino.verify_password('my-password')
        >>> check.api.message
        'OK.'
        ```

        """
        raise NotImplementedError

    async def login(
        self,
        email: str,
        password: Optional[str] = ...,
        secret: Optional[str] = ...
    ) -> Object:
        """Login in one account.

        Parameters
        ----------
        email : :class:`str`
            Email of the amino account.
        password : :class:`str` | `None`
            Password of the amino account.
        secret : :class:`str` | `None`
            Secret password encoded of the amino account.

        Examples
        --------
        ```
        >>> log = await amino.login(email='example@example.com', password='null-password')
        >>> log.account.email
        'example@example.com'
        ```

        """
        raise NotImplementedError

    async def login_phone(
        self,
        phone: str,
        password: str = ...,
        secret: str = ...
    ) -> Object:
        """Login in one account.

        Parameters
        ----------
        phone : :class:`str`
            Phone number of the amino account.
        password : :class:`str` | `None`
            Password of the amino account.
        secret : :class:`str` | `None`
            Secret password encoded of the amino account.

        Examples
        --------
        ```
        >>> amino.login_phone('+1 234234235', 'null-password')
        >>> print('my email is:', amino.account.email)
        ```

        """
        raise NotImplementedError

    async def from_sid(self):
        raise NotImplementedError


@runtime_checkable
class ABCACM(Protocol):
    ...


@runtime_checkable
class ABCWSClient(Protocol):
    ...


@runtime_checkable
class ABCRTCClient(Protocol):
    ...


@runtime_checkable
class ABCHTTPClient(Protocol):
    __slots__ = ()

    BASE: ClassVar[yarl.URL] = yarl.URL('https://service.narvii.com/api/v1/')

    async def headers(
        self,
        data: Optional[str] = None,
        content_type: Optional[str] = None
    ) -> dict:
        """Prepare the request header.

        Parameters
        ---------
        data : :class:`str` | `None`
            The http body string.
        content_type : :class:`str` | `None`
            Content-Type value of header.

        Returns
        -------
        dict
            The full http headers.

        Examples
        --------
        ```
        >>> data: str = ujson.dumps({})
        >>> headers: dict = await amino.prepare_headers(data)
        ```

        """
        raise NotImplementedError

    async def request(
        self,
        method: str,
        url: str,
        params: Optional[dict] = ...,
        json: Optional[dict] = ...,
        *,
        cid: Optional[int] = ...,
        scopeCid: int = ...,
        minify: bool = ...
    ) -> dict:
        """Make a request to the amino api.

        Parameters
        ----------
        method : :class:`str`
            HTTP method.
        url : :class:`str`
            Resource path.
        params : :class:`dict` | `None`
            Request parameters. Only for get method.
        json : :class:`dict` | `None`
            The data for the request. Only for post method.
        cid : :class:`int` | `None`
            Community id.
        scopeCid : :class:`int`
            Scope community id.
        minify : :class:`bool`
            Data to json_minify.

        Raises
        ------
        APIError
            Raise when the api response status is not `0`.
        ClientError
            Raise when the request status <= `400`.
        ServerError
            Raise when the request status <= `500`.
        Forbidden
            Raise when `403` http error eccurs.

        Examples
        -------
        ```
        >>> r: dict = await amino.request('GET', 'user-profile', params=dict(size=5))
        ```

        """
        raise NotImplementedError

    async def get(
        self,
        url: str,
        *,
        params: Optional[dict] = ...,
        **kwargs: ...
    ) -> dict:
        """Make a GET request to the amino api.

        Parameters
        ----------
        url : :class:`str`
            The resource path.
        params : :class:`dict` | `None`
            Parameters of the request.

        Raises
        ------
        HTTPException
            Raise when api response is not `0`.
        Forbidden
            If `403` error eccurs.

        Examples
        --------
        ```
        >>> r: dict = await amino.get('user-profile', dict(size=5))
        >>> r.get('api:message')
        'OK.'
        ```

        """
        raise NotImplementedError

    async def post(
        self,
        url: dict,
        *,
        json: dict,
        **kwargs: ...
    ) -> dict:
        """Make a POST request to the amino api.

        Parameters
        ----------
        url : :class:`str`
            The resource path.
        json : :class:`dict`
            Dict data to send.
        Raises
        ------
        HTTPException
            Raise when api response is not `0`.
        Forbidden
            If `403` error eccurs.

        """
        raise NotImplementedError

    async def put(self, url: str, /) -> dict:
        """Make a PUT request to the amino api.

        Parameters
        ----------
        url : :class:`str`
            The resource path.

        Raises
        ------
        HTTPException:
            Raise when api response is not :class:`0`.
        Forbidden:
            If `403` error eccurs.

        """
        raise NotImplementedError

    async def delete(self, url: str, **kwargs: Any) -> dict:
        """Make a DELETE request to the amino api.

        Parameters
        ----------
        url : :class:`str`
            The resource path.
        cid : :class:`int`
            Community id.

        Raises
        ------
        HTTPException
            Raise when api response is not :class:`0`.
        Forbidden
            If `403` error eccurs.

        """
        raise NotImplementedError
