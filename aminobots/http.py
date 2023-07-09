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
from __future__ import annotations
from typing import (
    Any,
    Dict,
    Final,
    NoReturn,
    Optional,
    TYPE_CHECKING,
    Union,
    cast
)
from urllib.parse import urljoin
from asyncio import sleep
from time import time
from enum import Enum
from aiohttp import ClientConnectionError, ClientSession
from ujson import dumps, loads, JSONDecodeError
from json_minify import json_minify
from yarl import URL
from .abc import ABCHTTPClient
from .utils import (
    copy_all_docs,
    signature
)
from .errors import (
    APIError,
    ClientError,
    ConnectionError,
    RedirectionError,
    ServerError,
    check_api_error,
    check_client_error,
    check_redirect_error,
    check_server_error
)
if TYPE_CHECKING:
    from .amino import Amino

__all__ = ('HTTPClient',)

CONNECTION_TRIES = 5
CONNECTION_SLEEP = 2
USER_AGENT = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/star2ltexx-user 7.1.; com.narvii.amino.master/3.4.33602)'
USER_AGENT = 'Apple iPhone12,1 iOS v15.5 Main/3.12.2'


def update_enum_data(json: dict) -> dict:
    """Convert all enums values to python native value."""
    return {k:v.value if isinstance(v, Enum) else update_enum_data(v)
            if isinstance(v, dict) else v for k,v in json.items()}


@copy_all_docs
class HTTPClient(ABCHTTPClient):
    """Represents the HTTP client for amino API.

    Parameters
    ----------
    amino : :class:`Amino`
        Amino object.
    user_agent : :class:`str`, optional
        User-Agent header string.

    Attributes
    ----------
    amino : :class:`Amino`
        Amino client.
    user_agent : :class:`str`
        Header user agent.

    """

    BASE: Final[URL] = URL('https://service.narvii.com/api/v1/')

    def __init__(self, amino: Amino, /, user_agent: Optional[str] = None) -> None:
        self.amino: Amino = amino
        self.user_agent: str = user_agent or USER_AGENT

    async def headers(
        self,
        data: Optional[str] = None,
        content_type: Optional[str] = None
    ) -> Dict[str, str]:
        headers = {
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'en-US',
            'Connection': 'Upgrade',
            'Content-Type': 'application/x-www-form-urlencoded',
            'NDCDEVICEID': self.amino.device,
            'HOST': self.BASE.host,
            'User-Agent': self.user_agent
        }
        if self.amino.sid:
            headers['NDCAUTH'] = f'sid={self.amino.sid}'
        if self.amino.auid:
            headers['AUID'] = self.amino.auid
        if data:
            headers['NDC-MSG-SIG'] = signature(data)
            headers['Content-Length'] = str(len(data))
        if content_type:
            headers['Content-Type'] = content_type
        return headers

    async def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        *,
        content_type: Optional[str] = None,
        comId: int = 0,
        scope: int = 0,
        minify: bool = False
    ) -> Union[Dict[str, Any], NoReturn]:
        body: Optional[str] = None
        if scope:
            ndc = f'g/s-x{scope}/'
        elif not comId:
            ndc = 'g/s/'
        else:
            ndc = f'x{comId}/s/'
        path = path.removeprefix('/')
        path = urljoin(ndc, path)
        url = urljoin(self.BASE.human_repr(), path)
        if isinstance(params, dict):
            params.update(update_enum_data(params))
            if 'timezone' not in params:
                params['timezone'] = self.amino.timezone
            params.update({k: str(v) for k, v in params.items()})
        if isinstance(json, dict):
            json.update(update_enum_data(json))
            if 'timestamp' not in json:
                json['timestamp'] = int(time() * 1000)
            if path.startswith('auth') or path.startswith('account'):
                if 'deviceID' not in json:
                    json['deviceID'] = self.amino.device
            body = dumps(json)
            if minify:
                body = cast(str, json_minify(json))
        headers = await self.headers(body, content_type)
        content: Union[Dict[str, Any], str] = {}
        for tries in range(CONNECTION_TRIES -1, -1, -1):
            try:
                async with ClientSession() as session:
                    async with session.request(
                        method=method,
                        url=url,
                        params=params,
                        data=body,
                        headers=headers,
                        proxy=self.amino.proxy
                    ) as response:
                        try:
                            content = loads(await response.read())
                        except JSONDecodeError:
                            content = await response.text()
                # logger message
                log: Dict[str, Any] = {
                    'client': 'http',
                    'method': method,
                    'path': path
                }
                if isinstance(content, dict) and content.get('api:statuscode') != 0:
                    # amino api exceptions
                    self.amino.logger.warning(dumps(log.setdefault('data', content)))
                    if self.amino.raiseExceptions:
                        raise check_api_error(content)
                elif isinstance(content, str):
                    # amino web exceptions
                    msg = '%d - %s' % (response.status, response.reason)
                    self.amino.logger.warning(dumps(log.setdefault('data', msg)))
                    if self.amino.raiseExceptions:
                        if response.status >= 500:
                            raise check_server_error(response.status, cast(str, response.reason))
                        elif response.status >= 400:
                            raise check_client_error(response.status, cast(str, response.reason))
                        elif response.status >= 300:
                            raise check_redirect_error(response.status, cast(str, response.reason))
                        else:
                            raise NotImplementedError(response.status, response.status)
                else:
                    break
            except ClientConnectionError as exc:
                self.amino.logger.warning(dumps({
                    'client': 'http',
                    'message': 'No connection. %d tries.' % tries
                }))
                await sleep(CONNECTION_SLEEP)
                if tries < 1:
                    raise ConnectionError(exc) from exc
            except (ServerError, ClientError, RedirectionError) as error:
                if tries > 1:
                    await sleep(1)
                    continue
                else:
                    raise error from None
        return cast(dict, content)

    async def get(self, path: str, params: dict = {}, comId: int = 0, scope: int = 0) -> Union[Dict[str, Any], NoReturn]:
        return await self.request('GET', path=path, params=params, comId=comId, scope=scope)

    async def post(self, path: str, json: dict, comId: int = 0, scope: int = 0, content_type: Optional[str] = None, minify: bool = False) -> Union[Dict[str, Any], NoReturn]:
        return await self.request('POST', path=path, json=json, comId=comId, scope=scope, content_type=content_type, minify=minify)

    async def put(self, path: str, **kwargs: Any) -> Union[Dict[str, Any], NoReturn]:
        return await self.request('PUT', path=path, **kwargs)

    async def delete(self, path: str, **kwargs: Any) -> Union[Dict[str, Any], NoReturn]:
        return await self.request('DELETE', path=path, **kwargs)
