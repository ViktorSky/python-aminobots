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
    ClassVar,
    Optional,
    TYPE_CHECKING,
    Union
)
from .abc import ABCWSClient
from .utils import signature, copy_all_docs
from . import errors
from yarl import URL

if TYPE_CHECKING:
    from .amino import Amino

import aiohttp
import asyncio
import ujson
import time

__all__ = ('WSClient',)
CONNECTION_TRIES = 4


@copy_all_docs
class WSClient(ABCWSClient):
    BASE: ClassVar[str] = 'wss://ws%d.narvii.com/'
    amino: Amino
    client: aiohttp.ClientWebSocketResponse
    reconnectTime: ClassVar[int] = 120

    def __init__(self, amino: Amino) -> None:
        self.amino = amino
        self.client = None

    @property
    def closed(self) -> bool:
        """Websocket closed."""
        return isinstance(self.client, aiohttp.ClientWebSocketResponse) and self.client.closed

    @staticmethod
    async def get_token(sid: str) -> Optional[str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                'https://aminoapps.com/api/chat/web-socket-url',
                headers=dict(cookie=f'sid={sid}')
            ) as response:
                try:
                    token = (await response.json())['result']['url']
                except (KeyError, ujson.JSONDecodeError):
                    token = None
                return token

    async def connect(self, token_url: Optional[str] = None) -> None:
        session: aiohttp.ClientSession = None
        while self.amino.sid or token_url:
            params, headers = {}, {
                'NDCDEVICEID': self.amino.device,
                'NDCAUTH': self.amino.sid,
                'Content-Type': 'text/plain'
            }
            if not token_url:
                timestamp = int(time.time() * 1000)
                data = f'{self.amino.device}|{timestamp}'
                headers.update({'NDC-MSG-SIG': signature(data)})
                params.update(signbody=data)
            try:
                if not isinstance(session, aiohttp.ClientSession) or session.closed:
                    session = aiohttp.ClientSession()
                if not isinstance(self.client, aiohttp.ClientWebSocketResponse):
                    for tries in range(1, CONNECTION_TRIES + 1):
                        url = token_url or self.BASE % tries
                        headers.update(HOST=URL(url).host)
                        self.client = await session.ws_connect(
                            url, params=params,
                            headers=headers,
                            proxy=self.amino.proxy
                        )
                        break
                self.amino.logger.info('websocket connected.')
                while True:
                    msg = await self.client.receive()
                    self.amino.logger.debug('ws receive: %r' % msg.type)
                    if msg.type == aiohttp.WSMsgType.CLOSED:
                        raise errors.WebSocketClosed
                        #if msg.type == aiohttp.WSMsgType.TEXT:
                    print(msg.type, msg.data)
                        #loop = asyncio.get_running_loop()
                        #loop.create_task(self.on_ws_message(msg))
            except aiohttp.WSServerHandshakeError:
                self.amino.logger.debug('websocket handshaking.')
                await asyncio.sleep(1)
                continue
            except errors.WebSocketClosed:
                self.amino.logger.info('websocket disconnected.')
                continue
            finally:
            #except asyncio.CancelledError:
                await session.close()
                await self.close()
                return

    async def connect(self, token_url: Optional[str] = None) -> None:
        session: aiohttp.ClientSession = None
        while self.amino.sid or token_url:
            params, headers = {}, {
                'NDCDEVICEID': self.amino.device,
                'NDCAUTH': self.amino.sid,
                'Content-Type': 'text/plain'
            }
            if not token_url:
                timestamp = int(time.time() * 1000)
                data = f'{self.amino.device}|{timestamp}'
                headers.update({'NDC-MSG-SIG': signature(data)})
                params.update(signbody=data)
            try:
                if not isinstance(session, aiohttp.ClientSession) or session.closed:
                    session = aiohttp.ClientSession()
                if not isinstance(self.client, aiohttp.ClientWebSocketResponse):
                    for tries in range(1, CONNECTION_TRIES + 1):
                        url = token_url or self.BASE % tries
                        headers.update(HOST=URL(url).host)
                        self.client = await session.ws_connect(
                            url, params=params,
                            headers=headers,
                            proxy=self.amino.proxy
                        )
                        break
                self.amino.logger.info('websocket connected.')
                while True:
                    msg = await self.client.receive()
                    self.amino.logger.debug('ws receive: %r' % msg.type)
                    if msg.type == aiohttp.WSMsgType.CLOSED:
                        raise errors.WebSocketClosed
                        #if msg.type == aiohttp.WSMsgType.TEXT:
                    print(msg.type, msg.data)
                        #loop = asyncio.get_running_loop()
                        #loop.create_task(self.on_ws_message(msg))
            except aiohttp.WSServerHandshakeError:
                self.amino.logger.debug('websocket handshaking.')
                await asyncio.sleep(1)
                continue
            except errors.WebSocketClosed:
                self.amino.logger.info('websocket disconnected. Reconnecting in 5 seconds...')
                await asyncio.sleep(5)  # wait for 5 minutes before trying to reconnect
                continue
            finally:
                await session.close()
                await self.close()
                return

    async def close(self, code: int = aiohttp.WSCloseCode.OK, message: bytes = b''):
        await self.client.close(code=code, message=message)

    async def send(self, data: Union[str, dict]):
        data: str = ujson.dumps(data) if isinstance(data, dict) else data
        self.BASE

    async def on_ws_message(self, msg: aiohttp.WSMessage) -> None:
        import pprint
        pprint.pprint(msg.json(loads=ujson.loads))

    async def typing(self):
        ...

    async def recording(self):
        ...

    async def browsing(self):
        ...

    async def visiting(self):
        ...

    async def reading(self):
        ...
