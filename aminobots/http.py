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
    Final,
    Optional,
    TYPE_CHECKING
)
from .abc import ABCHTTPClient
from .utils import (
    copy_all_docs,
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
    amino: Final[Amino]
    user_agent: Final[str]

    def __init__(self, amino: Amino, /, user_agent: str = USER_AGENT) -> None:
        self.amino: Amino = amino
        self.user_agent: str = user_agent

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
            headers['Content-Length'] = str(len(data))
        if content_type:
            headers['Content-Type'] = content_type
        return headers

    async def request(
        self,
        method: str,
        path: str,
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
        path = path.removeprefix('/')
        if isinstance(params, dict):
            if 'timezone' not in params:
                params['timezone'] = self.amino.timezone
            params = {k: str(v) for k, v in params.items()}
        if isinstance(json, dict):
            if 'timestamp' not in json:
                json['timestamp'] = int(time.time() * 1000)
            if path.startswith('auth') or path.startswith('account'):
                if 'deviceID' not in json:
                    json['deviceID'] = self.amino.device
            json: str = ujson.dumps(json)
        if minify and isinstance(json, str):
            json = json_minify.json_minify(json)
        path = urljoin(ndc, path)
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
                        if response.status in [403]:
                            self.amino.logger.warning('http: %r %r params=%s data=%r returns %d status code.', method, url, params, json, response.status)
                            if self.amino.raiseExceptions:
                                raise errors.Forbidden(await response.text())
                            else:
                                json = dict()
                        self.amino.logger.debug('http: %r %r params=%s data=%r returns %d status code.', method, url, params, json, response.status)
                        try:
                            json: dict = ujson.loads(await response.text())
                        except ujson.JSONDecodeError:
                            json: str = await response.read()
                        if isinstance(json, dict) and json.get('api:statuscode') != 0 and self.amino.raiseExceptions:
                            raise errors.check_api_error(json)
                        elif not isinstance(json, dict):
                            if self.amino.raiseExceptions:
                                if response.status >= 500:
                                    raise errors.ServerError(response.status, response.reason)
                                elif response.status >= 400:
                                    raise errors.ClientError(response.status, response.reason)
                                elif response.status >= 300:
                                    raise errors.RediretionError(response.status, response.reason)    
                                else:
                                    raise errors.ClientError(response, json)
                            json = dict()
                        return json
            except aiohttp.ClientConnectionError as exc:
                self.amino.logger.warning('No connection. %d tries.', tries)
                await asyncio.sleep(1)
                if tries < 1:
                    raise ConnectionError(exc) from exc

    async def get(self, path: str, params: dict = {}, **kwargs: Any) -> dict:
        return await self.request('GET', path=path, params=params, **kwargs)

    async def put(self, path: str, **kwargs: Any) -> dict:
        return await self.request('PUT', path=path, **kwargs)

    async def delete(self, path: str, **kwargs: dict) -> dict:
        return await self.request('DELETE', path=path, **kwargs)

    async def post(self, path: str, json: dict, **kwargs) -> dict:
        return await self.request('POST', path=path, json=json, **kwargs)
