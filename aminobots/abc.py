from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Iterable,
    Optional,
    Protocol,
    Type,
    Union
)
from yarl import URL


__all__ = (
    'ABCAmino',
    'ABCACM',
    'ABCHTTPClient',
    'ABCRTCClient',
    'ABCWSClient',
    'Object',
)


@dataclass(repr=False)
class Object(Protocol):
    json: Union[list, dict]


class _ABC(Protocol):
    def __dir__(self) -> Iterable[str]:
        return (a for a in object.__dir__(self) if not a.startswith('_') or a.startswith('__'))

    def __bool__(self) -> bool:
        return True


class ABCAmino(_ABC, Protocol):
    __slots__ = ()

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
        ```

        Parameters
        ----------
        link: :class:`str`
            Http amino url.

        """
        raise NotImplementedError

    async def get_link_info(self, link: str) -> Object:
        """Request link info.

        Examples
        --------
        ```
        >>> link: str = input('amino link: ')
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
    ):
        """
        """
        raise NotImplementedError

    async def login_phone(self, phone, password):
        raise NotImplementedError

    async def from_sid(self):
        raise NotImplementedError


class ABCACM(_ABC, Protocol):
    __slots__ = ()


class ABCWSClient(_ABC, Protocol):
    __slots__ = ()


class ABCRTCClient(_ABC, Protocol):
    __slots__ = ()


class ABCHTTPClient(_ABC, Protocol):
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
        data: Optional[dict] = ...,
        *,
        cid: Optional[int] = ...,
        isglobal: bool = ...,
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
        data: :class:`Optional[dict]`
            The data for the request. Only for post method.
        cid: :class:`Optional[int]`
            Community id.
        isglobal: :class:`bool`
            Force global with community id.
        minify: :class:`bool`
            Data to json_minify.

        Raises
        ------
        HTTPException:
            Raise when any api exception occurs.
        Forbidden:
            Raise when 403 http error eccurs.

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
        url: str,
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

    async def put(
        self,
        url: str,
        *,
        params: dict = ...
    ) -> dict:
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

    async def delete(
        self,
        url: str,
        params: dict,
        **kwargs: Any
    ) -> dict:
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
