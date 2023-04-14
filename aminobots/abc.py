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
    Iterable,
    Optional,
    Protocol,
    runtime_checkable,
    Type,
    Union
)
from yarl import URL
import logging

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
    http: Type['ABCHTTPClient']
    rtc: Type['ABCRTCClient']
    ws: Type['ABCWSClient']

    async def get_from_link(self, link: str) -> Object:
        """Request link data.
    
        Examples
        --------
        ```
        >>> link: str = input('amino link: ')
        >>> r = await amino.get_from_link(link)
        >>> list(r.json)
        ['api:duration', 'api:message', 'linkInfoV2', 'api:timestamp', 'api:statuscode']
        ```

        Parameters
        ----------
        link: :class:`str`
            Http amino url.

        """
        raise NotImplementedError

    async def get_link_info(self, link: str) -> Object:
        """Request link info. (only community links)

        Examples
        --------
        ```
        >>> link: str = input('community link: ')
        >>> r = await amino.get_link_info(link)
        ```

        Parameters
        ----------
        link: :class:`str`
            Http amino url.

        """
        raise NotImplementedError

    async def get_user_info(self, id: str, *, cid: Optional[int] = ...) -> Object:
        """Request user profile.

        Examples
        --------
        ```
        >>> info = await amino.get_from_link(user_link)
        >>> user = await amino.get_user_info(info.id)
        ```

        Parameters
        ----------
        id: :class:`str`
            User id.
        cid: :class:`Optional[int]`
            Community id.

        """
        raise NotImplementedError

    async def get_account_info(self) -> Object:
        """Request account info.
    
        Examples
        --------
        ```
        >>> account = await amino.get_account_info()
        >>> print(account.email)
        ```

        """
        raise NotImplementedError

    async def get_community_info(self, id: int, /) -> Object:
        """Request Community info.

        Examples
        --------
        ```
        >>> cid = await amino.get_from_link(input('community-link: '))
        >>> cm_info = await amino.get_community_info(cid.id)
        ```

        Parameters
        ----------
        id: :class:`int`
            Community id.

        """
        raise NotImplementedError

    async def joined_communities(self) -> Object:
        """Get list of joined communities.

        Parameters
        ----------
        start: int
            start index.
        size: int
            size of the list. Max size is 100.

        """
        raise NotImplementedError

    async def get_vip_users(self, cid: int) -> Object:
        """Get community influencers (vip users)

        Parameters
        ----------
        cid: :class:`int`
            Community id.

        """
        raise NotImplementedError

    async def login(
        self,
        email: str,
        password: Optional[str] = ...,
        secret: Optional[str] = ...
    ) -> Object:
        """Login in one account.

        Examples
        --------
        >>> amino.login(email='example@example.com', password='null-password')
        <aminobots.models.Login object at 0x000001BB8BAE9640>

        Parameters
        ----------
        email: :class:`str`
            Email of the amino account.
        password: Optional[:class:`str`]
            Password of the amino account. (default is None)
        phone: :class:`str`
            Phone number of the amino account. (default is None)
        secret: Optional[:class:`str`]
            Secret password encoded of the amino account. (default is None)

        Returns
        -------
        aminobots.objects.Login:
            An object organize api response

        """
        raise NotImplementedError

    async def login_phone(
        self,
        phone: str,
        password: str = ...,
        secret: str = ...
    ) -> Object:
        """Login in one account.

        Examples
        --------
        ```
        >>> amino.login_phone('+595 983772712', 'null-password')
        <aminobots.models.Login object at 0x000002D0A50AC500>
        ```

        Parameters
        ----------
        phone
        password
        secret

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

    BASE: ClassVar[URL] = URL('https://service.narvii.com/api/v1/')

    async def headers(
        self,
        data: Optional[str] = None,
        content_type: Optional[str] = None
    ) -> dict:
        """Prepare the request header.

        Examples
        --------
        ```
        >>> data: str = ujson.dumps({})
        >>> headers: dict = await amino.prepare_headers(data=data)
        ```

        Parameters
        ---------
        data: :class:`Optional[str]`
            The http body string.
        content_type: :class:`Optional[str]`
            Content-Type value of header.

        Returns
        -------
        dict:
            The full http headers.

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

        Examples
        -------
        ```python
        >>> r: dict = await amino.request('GET', 'user-profile/', params=dict(size=5))
        ```

        Parameters
        ----------
        method: :class:`str`
            HTTP method.
        url: :class:`str`
            Resource path.
        params: :class:`Optional[dict]`
            Request parameters. Only for get method.
        json: :class:`Optional[dict]`
            The data for the request. Only for post method.
        cid: :class:`Optional[int]`
            Community id.
        scopeCid: :class:`int`
            Scope community id.
        minify: :class:`bool`
            Data to json_minify.

        Raises
        ------
        APIError:
            Raise when the api response status is not `0`.
        ClientError:
            Raise when the request status <= `400`.
        ServerError:
            Raise when the request status <= `500`.
        Forbidden:
            Raise when `403` http error eccurs.

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

        Examples
        --------
        ```
        >>> r: dict = await amino.get('user-profile', dict(size=5))
        >>> print(r.get('api:message'))
        ```

        Parameters
        ----------
        url: :class:`str`
            The resource path.
        params: :class:`Optional[dict]`
            Parameters of the request.
        kwargs: :class:`dict[str, Any]`
            cid: :class:`int`
            isglobal: :class:`bool`

        Raises
        ------
        HTTPException:
            Raise when api response is not :class:`0`.
        Forbidden:
            If 403 error eccurs.

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
        url: :class:`str`
            The resource path.
        json: :class:`dict`
            Dict data to send.
        kwargs: :class:`Dict[str, Any]`
            cid: :class:`int`
            isglobal: :class:`bool`
            minify: :class:`bool`

        Raises
        ------
        HTTPException:
            Raise when api response is not :class:`0`.
        Forbidden:
            If 403 error eccurs.

        """
        raise NotImplementedError

    async def put(self, url: str, *, params: Optional[dict] = ...) -> dict:
        """Make a PUT request to the amino api.

        Parameters
        ----------
        url: :class:`str`
            The resource path.
        params: :class:`dict`
            Parameters of the request.
        kwargs: :class:`Dict[str, Any]`
            cid: :class:`int`
                Community id.
            isglobal: :class:`bool`
                Community global.

        Raises
        ------
        HTTPException:
            Raise when api response is not :class:`0`.
        Forbidden:
            If 403 error eccurs.

        """
        raise NotImplementedError

    async def delete(self, url: str, params: dict, **kwargs: Any) -> dict:
        """Make a DELETE request to the amino api.

        Parameters
        ----------
        url: :class:`str`
            The resource path.
        params: :class:`dict`
            data to send.
        kwargs: :class:`Dict[str, Any]`
            cid: :class:`int`
                Community id.
            isglobal: :class:`bool`
                Community global.

        Raises
        ------
        HTTPException:
            Raise when api response is not :class:`0`.
        Forbidden:
            If 403 error eccurs.

        """
        raise NotImplementedError
