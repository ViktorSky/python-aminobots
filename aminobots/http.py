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
    ClassVar,
    Iterable,
    Optional,
    Union,
    TYPE_CHECKING
)
from .abc import ABCHTTPClient
from .utils import (
    copy_doc,
    signature,
    Device
)
from . import errors
from urllib.parse import urljoin, quote
from yarl import URL
import json_minify
import aiohttp
import asyncio
import ujson
import time

if TYPE_CHECKING:
    from .amino import Amino

__all__ = ('HTTPClient',)

CONNECTION_TRIES = 5
USER_AGENT = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/star2ltexx-user 7.1.; com.narvii.amino.master/3.4.33602)'
USER_AGENT = 'Apple iPhone12,1 iOS v15.5 Main/3.12.2'


class HTTPClient(ABCHTTPClient):
    """Represent the HTTP client for amino API.

    Parameters
    ----------
    amino: :class:`Amino`
        Amino object.
    user_agent: :class:`str`
        User-Agent header string.

    Attributes
    ----------
    amino: :class:`Amino`
        Amino client.
    user_agent: :class:`str`
        Header user agent.

    """
    #BASE: ClassVar[URL] = URL('https://service.narvii.com/api/v1/')

    def __init__(self, amino: Amino, /, **kwargs) -> None:
        self.amino: Amino = amino
        self.user_agent = kwargs.pop('user_agent', USER_AGENT)

    @copy_doc(ABCHTTPClient.headers)
    async def headers(
        self,
        data: Optional[str] = None,
        content_type: Optional[str] = None
    ) -> dict:
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
        if data:
            headers['NDC-MSG-SIG'] = signature(data)
            headers['Content-Lenght'] = str(len(data))
        if content_type:
            headers['Content-Type'] = content_type
        return headers

    @copy_doc(ABCHTTPClient.request)
    async def request(
        self,
        method: str,
        url: str,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        *,
        cid: int = 0,
        scopeCid: int = 0,
        minify: bool = False
    ) -> dict:
        if scopeCid:
            ndc = f'g/s-x{scopeCid}/'
        elif not cid:
            ndc = 'g/s/'
        else:
            ndc = f'x{cid}/s/'
        if isinstance(params, dict):
            if 'timezone' not in params:
                params['timezone'] = self.amino.timezone
            params = {k: str(v) for k, v in params.items()}
        else:
            params = None
            if not json:
                json = dict()
            if isinstance(json, dict):
                if 'timestamp' not in json:
                    json['timestamp'] = int(time.time() * 1000)
                json: str = ujson.dumps(json)
                if minify:
                    json = json_minify.json_minify(json)
        path = urljoin(ndc, url.removeprefix('/'))
        url = urljoin(self.BASE.human_repr(), path)
        headers = await self.headers(json)
        for tries in range(CONNECTION_TRIES -1, -1, -1):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.request(
                        method=method,
                        url=url,
                        params=params,
                        data=json,
                        headers=headers
                    ) as response:
                        json: dict
                        if response.status in [403]:
                            self.amino.logger.warning('http: %r %r params=%s data=%r returns %d status code.', method, url, params, json, response.status)
                            if self.amino.raiseExceptions:
                                raise errors.Forbidden(await response.text())
                            else:
                                json = dict()
                        self.amino.logger.debug('http: %r %r params=%s data=%r returns %d status code.', method, url, params, json, response.status)
                        try:
                            json = dict(await response.json(loads=ujson.loads))
                        except aiohttp.ContentTypeError:
                            json: str = await response.read()
                        if not response.ok and self.amino.raiseExceptions:
                            if response.status >= 500:
                                raise errors.ServerError("%d - %s" % (response.status, response.reason))
                            elif response.status >= 200:
                                raise errors.APIError(await response.json(loads=ujson.loads))
                            raise errors.ClientError(response, json)
                        else:
                            return json
            except aiohttp.ClientConnectionError as exc:
                self.amino.logger.warning('No connection. %d tries.', tries)
                await asyncio.sleep(1)
                if tries < 1:
                    raise ConnectionError(exc) from exc

    @copy_doc(ABCHTTPClient.get)
    async def get(self, url: str, params: dict = {}, **kwargs: Any) -> dict:
        return await self.request('GET', url=url, params=params, **kwargs)

    @copy_doc(ABCHTTPClient.put)
    async def put(self, url: str, params: dict = {}, **kwargs: Any) -> dict:
        return await self.request('PUT', url=url, params=params, **kwargs)

    @copy_doc(ABCHTTPClient.delete)
    async def delete(self, url: str, params: dict = {}, **kwargs: dict) -> dict:
        return await self.request('DELETE', url=url, params=params, **kwargs)

    @copy_doc(ABCHTTPClient.post)
    async def post(self, url: str, json: dict, **kwargs) -> dict:
        return await self.request('POST', url=url, json=json, **kwargs)
