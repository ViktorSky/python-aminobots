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
import aiohttp
import asyncio
import typing
import ujson
import yarl
import time

from . import (
    abc,
    enums,
    utils,
    errors
)

if typing.TYPE_CHECKING:
    from . import amino

__all__ = ('WSClient',)

CONNECTION_TRIES = 4


class Action:
    def __init__(self, ws: 'WSClient', json: dict) -> None:
        self.ws = ws
        self.json = json

    async def __aenter__(self):
        await self.ws.client.send_json({**self.json, 't': 306})

    async def __aexit__(self, *error):
        await self.ws.client.send_json({**self.json, 't': 303})


@utils.copy_all_docs
class WSClient(abc.ABCWSClient):
    BASE: typing.ClassVar[str] = 'wss://ws%d.narvii.com/'
    client: aiohttp.ClientWebSocketResponse
    reconnectTime: typing.ClassVar[int] = 120

    def __init__(self, amino: 'amino.Amino') -> None:
        self.client = None
        self.amino = amino

    def __dir__(self) -> typing.Iterable:
        return set(object.__dir__(self)) - {'amino'}

    @property
    def closed(self) -> bool:
        """Websocket closed."""
        return not (isinstance(self.client, aiohttp.ClientWebSocketResponse) and self.client.closed)

    @staticmethod
    async def get_token(sid: str) -> typing.Optional[str]:
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

    async def connect(self, token_url: typing.Optional[str] = None) -> None:
        session: aiohttp.ClientSession = None
        while self.amino.sid or token_url:
            params, headers = {}, {
                'NDCDEVICEID': self.amino.device,
                'NDCAUTH': self.amino.sid,
                'Content-Type': 'text/plain',
                'Host': 'aminoapps.com',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://aminoapps.com/partial/main-chat-window?ndcId=86797652&source=sidebar_community_list&action=click'
            }

            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            # 'accept': '*/*',
            # 'referer': 'https://aminoapps.com/partial/main-chat-window?ndcId=86797652&source=sidebar_community_list&action=click',
            # 'accept-language': 'en-US,en;q=0.9',

            if not token_url:
                timestamp = int(time.time() * 1000)
                data = f'{self.amino.device}|{timestamp}'
                headers.update({'NDC-MSG-SIG': utils.signature(data)})
                params.update(signbody=data)
            try:
                if not isinstance(session, aiohttp.ClientSession) or session.closed:
                    session = aiohttp.ClientSession()
                if not isinstance(self.client, aiohttp.ClientWebSocketResponse):
                    for tries in range(1, CONNECTION_TRIES + 1):
                        url = token_url or self.BASE % tries
                        headers.update(HOST=yarl.URL(url).host)
                        self.client = await session.ws_connect(
                            url, params=params,
                            headers=headers,
                            proxy=self.amino.proxy
                        )
                        break
                self.amino.logger.info('websocket connected.')
                while True:
                    msg = await self.client.receive()
                    #self.amino.logger.debug('ws receive: %r: %s' % (msg.type, msg.data))
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

    async def connect(self, token_url: typing.Optional[str] = None) -> None:
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
                headers.update({'NDC-MSG-SIG': utils.signature(data)})
                params.update(signbody=data)
            try:
                if not isinstance(session, aiohttp.ClientSession) or session.closed:
                    session = aiohttp.ClientSession()
                if not isinstance(self.client, aiohttp.ClientWebSocketResponse):
                    for tries in range(1, CONNECTION_TRIES + 1):
                        url = token_url or self.BASE % tries
                        headers.update(HOST=yarl.URL(url).host)
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

    async def connect_daemon(self, token_url: typing.Optional[str] = None) -> None:
        loop = asyncio.get_running_loop()
        loop.create_task(self.connect(token_url), name='connection-task')
        # wait the connection
        while self.closed:
            pass

    async def close(self, code: int = aiohttp.WSCloseCode.OK, message: bytes = b''):
        await self.client.close(code=code, message=message)

    async def send(self, data: typing.Union[str, dict]):
        data: str = ujson.dumps(data) if isinstance(data, dict) else data
        self.BASE

    async def on_ws_message(self, msg: aiohttp.WSMessage) -> None:
        import pprint
        pprint.pprint(msg.json(loads=ujson.loads))

    @utils.typechecker
    async def create_channel(self, comId: int, chatId: str, channelType: enums.ChannelType):
        await self.client.send_json({
            'o': {
                'ndcId': comId,
                'threadId': chatId,
                'joinRole': enums.ChannelJoinRole.OWNER.value,
                'id': '2154531'
            },
            't': 112
        })
        await self.client.send_json({
            'o': {
                'ndcId': comId,
                'threadId': chatId,
                'joinRole': enums.ChannelJoinRole.OWNER.value,
                'channelType': channelType.value,
                'id': '2154531'
            },
            't': 108
        })

    @utils.typechecker
    async def join_channel(self, comId: int, chatId: str, channelJoinRole: enums.ChannelJoinRole = enums.ChannelJoinRole.VIEWER):
        await self.client.send_json({
            'o': {
                'ndcId': comId,
                'threadId': chatId,
                'joinRole': channelJoinRole.value,
                'id': '72446'
            },
            't': 112
        })

    async def send_action(self, comId: int, chatId: str = None):
        ...

    async def start_voice_chat(self, comId: int, chatId: str):
        await self.create_channel(comId, chatId, enums.ChannelType.VOICE)

    async def end_voice_chat(self, comId: int, chatId: str):
        await self.join_channel(comId, chatId, enums.ChannelJoinRole.VIEWER)

    async def start_video_chat(self, comId: int, chatId: str):
        await self.create_channel(comId, chatId, enums.ChannelType.VIDEO)

    async def end_video_chat(self, comId: int, chatId: str):
        ...

    async def start_screening_room(self, comId: int, chatId: str):
        await self.create_channel(comId, chatId, enums.ChannelType.SCREENING_ROOM)

    async def end_screening_room(self, comId: int, chatId: str):
        ...

    async def typing(self):
        ...

    async def recording(self):
        ...

    async def browsing(self, comId: int):
        """"""
        await self.client.send_json({
            'o': {
                'ndcId': comId,
                'actions': ['Browsing'],
                'id': '82333',
                'target': f'ndc://x{comId}',
            },
            't': 304
        })

    async def visiting(self):
        ...

    async def reading(self):
        """Reading posts action."""
        ...
