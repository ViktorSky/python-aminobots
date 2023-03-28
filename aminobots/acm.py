from typing import Optional, Union
from .abc import ABCACM
from .utils import Device
from .http import HTTPClient
from .ws import WSClient

__all__ = ('ACM',)


class ACM(ABCACM):
    def __init__(
        self,
        device: Optional[Union[str, Device]] = None,
    ) -> None:
        self.http = HTTPClient(self)
        self.ws = WSClient(self)

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

