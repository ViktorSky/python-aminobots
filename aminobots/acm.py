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

from typing import Optional, Union
from .abc import ABCACM
from .utils import Device, copy_all_docs
from .http import HTTPClient
from .ws import WSClient
from .enums import ClientType

__all__ = ('ACM',)


@copy_all_docs
class ACM(ABCACM):
    """Represent the Amino Community Manager app.

    Attributes
    ----------
    device: :class:`Device`
        NDC device id.
    http: :class:`HTTPClient`
        HTTP client for amino api.
    ws: :class:`WSClient`
        WS client for amino api.

    """
    def __init__(
        self,
        device: Optional[Union[str, Device]] = None,
        raiseExceptions: bool = True
    ) -> None:
        self.device = device
        self.http = HTTPClient(self)
        self.ws = WSClient(self)
        self.auid = None
        self.sid = None
        self.raiseExceptions: bool = raiseExceptions

    async def search(self, q: str, language='en', cid: Optional[int] = None):
        # exacted from 'com/narvii/community/d'
        return await self.http.post(
            'community/search', dict(
                q=q,
                language=language,
                competeKeyword=1
            ),
            cid=cid
        )

    async def affiliations(self):
        return await self.http.get('account/affiliations', dict(type='active'))

    async def login(
        self,
        email: str,
        password: str = None,
        secret: str = None
    ):
        data = dict(
            action="normal",
            clientType=ClientType.ACM.value,
            deviceID=self.device,
            email=email,
            secret=f"0 {password}" if password else secret,
            v=2
        )
        response = await self.http.post('auth/login', json=data)
        if isinstance(response.get('api:statuscode'), int) and not response['api:statuscode']:
            self.auid = response.get('auid')
            self.secret = response.get('secret')
            self.sid = response.get('sid')
            #self.account.json.update(response.get('account'))
            #self.user.json.update(response.get('userProfile'))
            #if self.socketEnabled:
            #    await self.ws.connect(daemon=True)
        return response

    async def change_welcome_message(self, cid: int, text: Optional[str] = None):
        # extracted from 'com/narvii/customize/text/m.java <void y>'
        return await self.http.post(
            'community/configuration', dict(
                path='general.welcomeMessage',
                value=dict(
                    enabled=True,
                    text=text
                )
            ), 
            cid=cid
        )

    async def settings(self, cid: int):
        # extracted from 'com/narvii/customize/text/l.java' <void j> (abstract)
        return await self.http.get('community/settings', cid=cid)

    async def primarySettings(self, cid: int, primaryLanguage: str):
        return await self.http.get('community/settings', dict(primatyLanguage=primaryLanguage), cid=cid)

    async def guideline(self, cid: int):
        return await self.http.get('community/guideline', cid=cid)

    async def suggest(self, cid: int, q: str, language: str = 'all'):
        return await self.http.get('topic/suggest-topics', dict(q=q, language=language), cid=cid)

    async def top_user(self, idList: list):
        return await self.http.post('community/settings', dict(
            userAddedTopicList=[{'topicId': 0, 'name': 'xd'}]
        ))

    async def managed(self, cid: int):
        return await self.http.get('community/managed')

