from __future__ import annotations

from typing import (
    Any,
    Iterable,
    Optional,
    Union,
    TYPE_CHECKING
)

from .abc import ABCHTTPClient
from .errors import Forbidden, HTTPException
from .utils import (
    copy_doc,
    signature,
    Device
)

from urllib.parse import urljoin, quote
import json_minify
import aiohttp
import ujson
import time

if TYPE_CHECKING:
    from .amino import Amino


USER_AGENT = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/star2ltexx-user 7.1.; com.narvii.amino.master/3.4.33602)'
USER_AGENT = 'Apple iPhone12,1 iOS v15.5 Main/3.12.2'


class HTTPClient(ABCHTTPClient):

    _user_agent: str
    _amino: Amino

    @property
    def device(self) -> Device:
        return self._amino.device

    def __init__(self, client: Amino, **kwargs):
        self._amino = client
        if 'user_agent' in kwargs:
            self.user_agent = kwargs.pop('user_agent')

    @property
    def user_agent(self) -> str:
        """User-Agent value of http headers"""
        try:
            value = self._user_agent
        except AttributeError:
            value = self._user_agent = USER_AGENT
        finally:
            return value

    @user_agent.setter
    def user_agent(self, value: str):
        if not isinstance(value, str):
            raise TypeError('expected str not %r.' % value.__class__.__name__)
        self._user_agent = value

    @property
    def device(self) -> Device:
        """NDCDEVICEID value of http headers"""
        try:
            d = self._device
        except AttributeError:
            d = self._device = str(Device())
        finally:
            return Device(self._device)

    @device.setter
    def device(self, value: Union[str, Device]):
        if not isinstance(value, (str, Device)):
            raise TypeError('expected str not %r.' % value.__class__.__name__)
        self._device = str(value)

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
            'NDCDEVICEID': self.device,
            'HOST': self.BASE.host,
            'User-Agent': self.user_agent
        }
        if self._amino.sid:
            headers['NDCAUTH'] = f'sid={self._amino.sid}'
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
        cid: Optional[int] = None,
        scopeCid: int = 0,
        minify: bool = False
    ) -> dict:
        if not cid:
            ndc = 'g/s/'
        elif not isinstance(cid, int):
            raise TypeError('comId must be int not %r.' % cid.__class__.__name__)
        elif scopeCid:
            ndc = f'g/s-{scopeCid}/'
        else:
            ndc = f'x{cid}/s/'
        if isinstance(params, dict):
            if 'timezone' not in params:
                params['timezone'] = self._amino.timezone
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
                    if self._amino.raiseExceptions:
                        raise Forbidden(await response.text())
                    else:
                        json = dict()
                try:
                    json = dict(await response.json(loads=ujson.loads))
                except aiohttp.ContentTypeError:
                    json: str = await response.read()
                if not response.ok and self._amino.raiseExceptions:
                    raise HTTPException(response, json)
                else:
                    return json

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
    async def post(self, url: str, json: dict, **kwargs):
        return await self.request('POST', url=url, json=json, **kwargs)
