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
from abc import ABCMeta, abstractmethod, abstractproperty
from typing import (
    Any,
    Iterable,
    Optional,
    Union
)
from logging import Logger
from .enums import Language
from .utils import Device, SID

__all__ = (
    'ABCAmino',
    'ABCACM',
    'ABCHTTPClient',
    'ABCRTCClient',
    'ABCWSClient'
)


class ABCAmino(metaclass=ABCMeta):
    __slots__ = ()

    def __dir__(self) -> Iterable[str]:
        return [attr for attr in object.__dir__(self) if not attr.startswith('_') or attr.startswith('__')]

    @property
    def auid(self) -> Optional[str]:
        """Account user ID"""
        return getattr(self, '_auid', None)

    @auid.setter
    def auid(self, value: Optional[str]) -> None:
        if not isinstance(value, Optional[str]):
            raise TypeError('auid must be a string, not %r' % type(value).__name__)
        setattr(self, '_auid', value)

    @property
    def device(self) -> Device:
        """The device being used by the client"""
        return getattr(self, '_device')

    @device.setter
    def device(self, value: Union[str, Device]) -> None:
        if not isinstance(value, (str, Device)):
            raise TypeError('device must be a string or Device object, not %r.' % type(value).__name__)
        setattr(self, '_device', Device(value) if isinstance(value, str) else value)

    @property
    def language(self) -> Language:
        """Http language"""
        return getattr(self, 'languages', Language.ENGLISH)

    @language.setter
    def language(self, value: Language) -> None:
        if value not in Language:
            raise TypeError('language must be a Language object not %r.' % type(value).__name__)
        elif value is Language.ALL:
            raise ValueError('can\'t set all languages, select one only.')
        setattr(self, '_language', value)

    @property
    def logger(self) -> Logger:
        """Instance logger"""
        return getattr(self, '_logger')

    @logger.setter
    def logger(self, value: Logger) -> None:
        if not isinstance(value, Logger):
            raise TypeError('logger must be a Logger object, not %r.' % type(value).__name__)
        setattr(self, '_logger', value)

    @property
    def proxy(self) -> Optional[str]:
        """Http proxy url"""
        return getattr(self, '_proxy', None)

    @proxy.setter
    def proxy(self, value: Optional[str]) -> None:
        if not isinstance(value, Optional[str]):
            raise TypeError('proxy must be a string, not %r' % type(value).__name__)
        setattr(self, '_proxy', value)

    @property
    def raiseExceptions(self) -> bool:
        """Raise api exceptions (APIError subclasses)"""
        return getattr(self, '_raiseExceptions', True)

    @raiseExceptions.setter
    def raiseExceptions(self, value: bool) -> None:
        setattr(self, '_raiseExceptions', bool(value))

    @property
    def secret(self) -> Optional[str]:
        """Account secret password. (encoded string)"""
        return getattr(self, '_secret', None)

    @secret.setter
    def secret(self, value: Optional[str]) -> None:
        if not isinstance(value, Optional[str]):
            raise TypeError('secret must be a string, not %r' % type(value).__name__)
        setattr(self, '_secret', value)

    @property
    def sid(self) -> Optional[SID]:
        """The session ID for the Amino client"""
        return getattr(self, '_sid', None)

    @sid.setter
    def sid(self, value: Union[str, SID, None]) -> None:
        if not isinstance(value, Union[str, SID, None]):
            raise TypeError('expected str, SID or None, not %r.' % type(value).__name__)
        setattr(self, '_sid', SID(value) if isinstance(value, str) else value)

    @property
    def timeout(self) -> Optional[str]:
        """Http request timeout"""
        return getattr(self, '_timeout', None)

    @timeout.setter
    def timeout(self, value: Optional[int]) -> None:
        if not isinstance(value, Optional[int]):
            raise TypeError('timeout must be a integer not %r.' % type(value).__name__)
        setattr(self, '_timeout', value)

    @property
    def utc(self) -> int:
        """User device timezone (UTC)"""
        return getattr(self, '_utc', 0)

    @utc.setter
    def utc(self, value: int):
        if not isinstance(value, int):
            raise TypeError('utc must be a integer not %r.' % type(value).__name__)
        if value not in range(-12, 15):
            raise ValueError('utc must be between -12 and 14.')
        setattr(self, '_utc', value)

    @abstractmethod
    async def get_from_link(self, link: Any) -> Any:
        """Request amino link data.

        Parameters
        ----------
        link : :class:`str`
            Http amino url.

        Returns
        -------
        LinkResolution
            path : `~aminobots.models.LinkResolution`

        """

    @abstractmethod
    async def get_from_device(self, device: Any) -> Any:
        """Request auid (user ID) from device.

        Parameters
        ----------
        device : :class:`str` | :class:`Device`
            The user device.

        Returns
        -------
        FromDevice
            path : `~aminobots.models.FromDevice`

        """

    @abstractmethod
    async def get_link_info(self, link: Any) -> Any:
        """Request link info. (Only community links)

        Parameters
        ----------
        link : :class:`str`
            Http amino community url.

        Returns
        -------
        LinkIdentify
            path : `~aminobots.models.LinkIdentify`

        """

    @abstractmethod
    async def get_ads_info(self) -> Any:
        """Request account coins earned by ads.

        Notes
        -----
        Requires login

        Returns
        -------
        WalletAds
            path : `~aminobots.models.WalletAds`

        """

    @abstractmethod
    async def get_user_info(self, id: Any, comId: Any = ...) -> Any:
        """Request user profile.

        Parameters
        ----------
        id : :class:`str`
            User ID.
        comId : :class:`int`, default=`0`
            Community ID. If not provided, global profile is returned

        Returns
        -------
        UserInfo
            path : `~aminobots.models.UserInfo`

        """

    @abstractmethod
    async def get_account_info(self) -> Any:
        """Request user account.

        Notes
        -----
        Requires login

        Returns
        -------
        AccountInfo
            path : `~aminobots.models.AccountInfo`

        """

    @abstractmethod
    async def get_chat_info(self, id: Any, comId: Any = ...) -> Any:
        """Request chat thread info.

        Parameters
        ----------
        id : :class:`str`
            Chat ID.
        comId : :class:`int`, default=`0`
            Community ID. If not provided, global chat is returned

        Returns
        -------
        ChatInfo
            path : `~aminobots.models.ChatInfo`

        """

    @abstractmethod
    async def get_chat_members(self, id: Any, start: Any = ..., size: Any = ..., comId: Any = ...) -> Any:
        """Request members profiles in a chat.

        Parameters
        ----------
        id : :class:`str`
            Chat ID.
        start : :class:`int`, default=`0`
            Start index.
        size : :class:`int`, default=`25`
            Size of list of users. Max size is `100`.
        comId : :class:`int`, default=`0`
            Community ID. If not provided, global chat members is returned

        Returns
        -------
        ChatMembers
            path : `~aminobots.models.ChatMembers`

        """

    @abstractmethod
    async def get_community_info(self, id: Any) -> Any:
        """Request community profile.

        Parameters
        ----------
        id : :class:`int`
            Community ID.

        Returns
        -------
        CommunityInfo
            path : `~aminobots.models.CommunityInfo`

        """


    async def get_community_trending(self, id: Any) -> Any:
        """Request trending of community.

        Parameters
        ----------
        id : :class:`int`
            Community ID.

        """

    @abstractmethod
    async def get_wallet_info(self) -> Any:
        """Request account wallet.

        Notes
        -----
        Requires login

        Returns
        -------
        WalletInfo
            path : `~aminobots.models.WalletInfo`

        """

    @abstractmethod
    async def get_wallet_history(self, start: Any = ..., size: Any = ...) -> Any:
        """Request account coin history.

        Notes
        -----
        Requires login

        Parameters
        ----------
        start : :class:`int`, default=`0`
            The history start index.
        size : :class:`int`, default=`25`
            The size of the history list. Max size is `100`.

        Returns
        -------
        WalletHistory
            path : `~aminobots.models.WalletHistory`

        """

    @abstractmethod
    async def get_account_push_settings(self) -> Any:
        """Request account push settings.

        Notes
        -----
        Requires login

        Returns
        -------
        AllPushSettings
            path : `~aminobots.models.AllPushSettings`

        """

    @abstractmethod
    async def get_push_settings(self, comId: Any = ...) -> Any:
        """Get global/community push settings.

        Notes
        -----
        Requires login

        Parameters
        ----------
        comId : :class:`int`, default=`0`
            Community ID. If not provided, global settings is returned

        Returns
        -------
        PushNotification
            path : `~aminobots.models.PushNotification`

        """

    @abstractmethod
    async def set_push_settings(self, activities: Any, broadcasts: Any, comId: Any = ...) -> Any:
        """Update the global/community push settings.

        Notes
        -----
        Requires login

        Parameters
        ----------
        activities : :class:`bool`
            Enable members activities notifications.
        broadcasts : :class:`bool`
            Enable leaders broadcasts notifications.
        comId : :class:`int`, defaul=`0`
            The Community ID. If not provided, global settings is updated.

        Returns
        -------
        PushNotification
            path : `~aminobots.models.PushNotification`

        """

    @abstractmethod
    async def get_membership_info(self) -> Any:
        """Request account membership info.

        Notes
        -----
        Requires login

        Returns
        -------
        MembershipInfo
            path : `~aminobots.models.MembershipInfo`

        """

    @abstractmethod
    async def configure_membership(self, autoRenew: Any) -> Any:
        """Update the account membership.

        Notes
        -----
        Requires login

        Parameters
        ----------
        autoRenew : :class:`bool`
            Auto renew the membership.

        Returns
        -------
        MembershipConfig
            path : `~aminobots.models.MembershipConfig`

        """

    @abstractmethod
    async def joined_chats(self, start: Any = ..., size: Any = ..., comId: Any = ...) -> Any:
        """Request global/community joined chats.

        Notes
        -----
        Requires login

        Parameters
        ----------
        start : :class:`int`, default=`0`
            Chat start index.
        size : :class:`int`, default=`0`
            Size of the list. Max size is `100`.
        comId : :class:`int`, defualt=`0`
            The Community ID. If not provided, global joined-chats is returned

        Returns
        -------
        JoinedChats
            path : `~aminobots.models.JoinedChats`

        """

    @abstractmethod
    async def joined_communities(self, start: Any = ..., size: Any = ...) -> Any:
        """Request joined communities.

        Notes
        -----
        Requires login

        Parameters
        ----------
        start : :class:`int`, default=`0`
            Community start index.
        size : :class:`int`, default=`25`
            Size of the list. Max size is `100`.

        Returns
        -------
        JoinedCommunities
            path : `~aminobots.models.JoinedCommunities`

        """

    @abstractmethod
    async def get_vip_users(self, comId: Any) -> Any:
        """Request community influencer profiles (vip user profiles)

        Parameters
        ----------
        comId : :class:`int`
            The community ID.

        Returns
        -------
        CommunityInfluencers
            path : `~aminobots.models.CommunityInfluencers`

        """

    @abstractmethod
    async def search_user(self, q: Any, comId: Any = ...) -> Any:
        """Search user. Match amino ID or nickname.

        Parameters
        ----------
        q : :class:`str`
            Query string.
        comId : :class:`int`, default=`0`
            The Community ID. If not provided, global user profile is searched.

        Returns
        -------
        SearchUser
            path : `~aminobots.models.SearchUser`

        """

    @abstractmethod
    async def search_community(self, q: Any, language: Any = ...) -> Any:
        """Search community. Match amino ID or name.

        Parameters
        ----------
        q : :class:`str`
            Query string.
        language : :class:`Language`, defualt=`Language.ALL`
            Search language filter.

        Returns
        -------
        SearchCommunity
            path : `~aminobots.models.SearchCommunity`

        """

    @abstractmethod
    async def search_chat(self, q: Any, pageToken: Any = ..., comId: Any = ...) -> Any:
        """Search global/community chat.

        Parameters
        ----------
        q : :class:`str`
            Chat title
        comId : :class:`int`, default=`0`
            The community ID. If not provided, global chat is searched.
        pageToken : :class:`str`, default=`None`
            Next page token or Previous page token.

        Returns
        -------
        SearchChat
            path : `~aminobots.models.SearchChat`

        """

    @abstractmethod
    async def search_quiz(self, q: Any, comId: Any = ...) -> Any:
        """Search quiz posts.

        Parameters
        ----------
        q : :class:`str`
            Quiz title, search key.
        comId : :class:`int`
            Community ID.

        Returns
        ------
        SearchQuiz
            path : `~aminobots.models.SearchQuiz`

        """

    @abstractmethod
    async def verify_password(self, password: Any = ..., secret: Any = ...) -> Any:
        """Verify the account password.

        Notes
        -----
        Requires login

        Parameters
        ----------
        password : :class:`str`, default=`None`
            The account password.
        secret : :class:`str`, default=`None`
            The account secret password.

        Raises
        ------
        IncorrectPassword
            If the password is incorrect.

        Returns
        -------
        VerifyPassword
            path : `~aminobots.models.VerifyPassword`

        """

    @abstractmethod
    async def login(self, email: Any, password: Any = ..., secret: Any = ...) -> Any:
        """Login in an account.

        Parameters
        ----------
        email : :class:`str`
            Email of the amino account.
        password : :class:`str`, default=`None`
            The account password.
        secret : :class:`str`, default=`None`
            The account secret password.

        Raises
        ------

        Returns
        -------
        Login
            path : `~aminobots.models.Login`

        """

    @abstractmethod
    async def login_phone(
        self,
        phone: str,
        password: str = ...,
        secret: str = ...
    ) -> Any:
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

    async def login_sid(self, sid: str) -> Any:
        """Login in one account.

        Parameters
        ----------
        sid : :class:`str` | :class:`SID`
            The session id (token).

        Examples
        --------
        ```
        >>> await amino.login_sid(os.environ.get('SID'))
        >>> print(amino.user.nickname)
        ```

        """
        raise NotImplementedError


class ABCACM(metaclass=ABCMeta):
    ...


class ABCWSClient(metaclass=ABCMeta):
    ...


class ABCRTCClient(metaclass=ABCMeta):
    ...


class ABCHTTPClient(metaclass=ABCMeta):

    @abstractmethod
    async def headers(
        self,
        data: Any = ...,
        content_type: Any = ...
    ) -> Any:
        """Prepare the request header.

        Parameters
        ----------
        data : :class:`str` | `None`
            The http body string.
        content_type : :class:`str` | `None`
            Content-Type value of header.

        Examples
        --------
        >>> data = ujson.dumps({})
        >>> headers = await amino.prepare_headers(data)

        Returns
        -------
        dict
            The full HTTP headers.

        """

    @abstractmethod
    async def request(
        self,
        method: Any,
        path: Any,
        params: Any = ...,
        json: Any = ...,
        *,
        comId: Any = ...,
        scope: Any = ...,
        minify: Any = ...
    ) -> Any:
        """Make a request to the amino api.

        Parameters
        ----------
        method : :class:`str`
            HTTP method.
        path : :class:`str`
            Resource path url.
        params : :class:`dict` | `None`
            Request parameters. Only for get method.
        json : :class:`dict` | `None`
            The data for the request. Only for post method.
        comId : :class:`int`
            Community ID/Global request
        scope : :class:`int`
            Scope community ID.
        minify : :class:`bool`
            Json minify the data.

        Raises
        ------
        APIError
            Raised when the api response status is not `0`.
        ServerError
            Raise when the request status <= `500`.
        ClientError
            Raised when the request status <= `400`.
        RedirectionError
            Raised when the request status <= `300`.

        Examples
        --------
        >>> await amino.request('GET', 'user-profile', params=dict(size=5))

        Returns
        -------
        dict
            The API response data

        """

    @abstractmethod
    async def get(
        self,
        path: Any,
        params: Any = ...,
        comId: Any = ...,
        scope: Any = ...
    ) -> Any:
        """Make a GET request to the amino api.

        Parameters
        ----------
        url : :class:`str`
            The resource path.
        params : :class:`dict` | `None`
            Parameters of the request.
        comId : :class:`int`
            Community ID/Global.
        scope : :class:`int`
            Scope Community ID.

        Raises
        ------
        APIError
            Raised when the api response status is not `0`.
        ServerError
            Raise when the request status <= `500`.
        ClientError
            Raised when the request status <= `400`.
        RedirectionError
            Raised when the request status <= `300`.

        Returns
        -------
        dict
            The API response data

        See also
        --------
        - :func:`HTTPClient.request`

        """

    @abstractmethod
    async def post(
        self,
        path: Any,
        json: Any,
        comId: Any = ...,
        scope: Any = ...,
        content_type: Any = ...,
        minify: Any = ...
    ) -> Any:
        """Make a POST request to the amino api.

        Parameters
        ----------
        url : :class:`str`
            The resource path.
        json : :class:`dict`
            Dict data to send.
        comId : :class:`int`
            Community ID/Global.
        scope : :class:`int`
            Scope Community ID.
        content_type : :class:`str` | `None`
            The content type for HTTP headers.
        minify : :class:`bool`
            Json minify the data.

        Raises
        ------
        APIError
            Raised when the api response status is not `0`.
        ServerError
            Raise when the request status <= `500`.
        ClientError
            Raised when the request status <= `400`.
        RedirectionError
            Raised when the request status <= `300`.

        Returns
        -------
        dict
            The API response data

        See also
        --------
        - :func:`HTTPClient.request`

        """
