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

from typing import (
    Any,
    Callable,
    Coroutine,
    overload,
    Optional,
    Type,
    Union,
    TYPE_CHECKING
)

import logging
import aiohttp

from .abc import ABCAmino
from .enums import Language
from .ws import WSClient
from .rtc import RTCClient
from .http import HTTPClient
from .utils import copy_all_docs, Device, suppress, MISSING
from . import enums, models, objects
from inspect import iscoroutinefunction
from functools import wraps


__all__ = ('Amino',)


DEFAULT_LOGGER = logging.getLogger('Amino')
DEFAULT_LOGGER.setLevel(logging.WARNING)
DEFAULT_HANDLER = logging.StreamHandler()
DEFAULT_HANDLER.setLevel(logging.WARNING)
DEFAULT_HANDLER.setFormatter(logging.Formatter(
    '%(asctime)s |:| %(levelname)s |:| %(name)s |:| %(message)s',
    '%Y-%m-%d %H:%M:%S'))
DEFAULT_LOGGER.addHandler(DEFAULT_HANDLER)


@copy_all_docs
class Amino(ABCAmino):
    """Represent the Amino client.

    Examples
    --------
    ```
    >>> amino = Amino()
    >>> response = amino.login(input('email:'), input('password:'))
    >>> if response.api.ok():
    ...     print(amino.user.nickname)
    ... else:
    ...     print(response.api.message)
    ```

    Parameters
    ----------
    device: Union[:class:`str`, :class:`Device`]
        NDC device. (default is `None`)
    proxy: :class:`str`
        Http or Https proxy. (default is `None`)
    language: :class:`Language`
        Content language for amino. (default is :attr:`Language.ENGLISH`)
    utc: `int`
        UTC timezone. (default is `0`)
    raiseExceptions: :class:`bool`
        Raise amino exceptions. (defualt is `True`)

    Attributes
    ----------
    account: :class:`Account`
        User account.
    auid: :class:`str`
        User auth id.
    device: :class:`Device`
        User device.
    http: :class:`HTTPClient`
        HTTP client for amino api.
    raiseExceptions: :class:`bool`
        Raise amino exceptions.
    rtc: :class:`RTCClient`
        RTC client for agora service.
    sid: Optional[:class:`str`]
        Amino session id. (token)
    secret: Optional[:class:`str`]
        Secret password encoded.
    user: :class:`UserProfile`
        User profile.
    utc: :class:`int`
        Timezone (UTC).
    ws: :class:`WSClient`
        Websocket client for amino.

    """
    account: objects.Account
    auid: Optional[str]
    device: Device
    http: HTTPClient
    language: Language
    logger: logging.Logger
    raiseExceptions: bool
    rtc: RTCClient
    sid: Optional[str]
    secret: Optional[str]
    timeout: Optional[int]
    user: objects.UserProfile
    utc: int
    ws: WSClient

    def __init__(
        self,
        device: Optional[Union[str, Device]] = None,
        proxy: Optional[str] = None,
        proxy_auth: aiohttp.BasicAuth = None,
        *,
        logger: logging.Logger = DEFAULT_LOGGER,
        language: Language = Language.ENGLISH,
        utc: int = 0,
        timeout: Optional[int] = None,
        raiseExceptions: bool = True,
    ) -> None:
        if not isinstance(device, Optional[Union[str, Device]]):
            raise TypeError('expected str, Device or None, not %r.' % type(device).__name__)
        if not isinstance(logger, logging.Logger):
            raise TypeError('expected Logger not %r.' % type(logger).__name__)
        if not isinstance(proxy, Optional[str]):
            raise TypeError('expected str not %r.' % type(proxy).__name__)
        if not isinstance(proxy_auth, Optional[aiohttp.BasicAuth]):
            raise TypeError('expected BasicAuth not %r.' % type(proxy_auth).__name__)
        if not isinstance(utc, int):
            raise TypeError('expected int not %r.' % type(utc).__name__)
        if utc not in range(-12, 15):
            raise ValueError('the utc must be between -12 and 14.')
        if not isinstance(language, Language):
            raise TypeError('expected str or Language not %r.' % type(language).__name__)
        if not isinstance(timeout, Optional[int]):
            raise TypeError('expected int not %r.' % type(timeout).__name__)
        self.ws = WSClient(self)
        self.http = HTTPClient(self)
        self.rtc = RTCClient(self)
        self.account = objects.Account(dict())
        self.user = objects.UserProfile(dict())
        self.device = Device(device) if device else Device()
        self.logger = logger
        self.proxy = proxy
        self.proxy_auth = proxy_auth
        self.utc = utc
        self.language = language
        self.timeout = timeout
        self.raiseExceptions = raiseExceptions
        self.auid = None
        self.secret = None
        self.sid = None

    @property
    def timezone(self) -> int:
        """Timezone for amino http parameters."""
        return self.utc * 60

    async def get_from_link(self, link: str) -> models.LinkResolution:
        return models.LinkResolution(await self.http.get('link-resolution', dict(q=link)))

    async def get_link_info(self, link: str) -> models.LinkIdentify:
        return models.LinkIdentify(await self.http.get('community/link-identify', dict(q=link)))

    async def get_user_info(self, id: str, cid: Optional[int] = None) -> models.UserInfo:
        return models.UserInfo(await self.http.get(f'user-profile/{id}', cid=cid))

    async def get_account_info(self) -> models.AccountInfo:
        return models.AccountInfo(await self.http.get('account'))

    async def get_community_info(self, id: int, /) -> models.CommunityInfo:
        params = dict(withInfluencerList=1, withTopicList='true', influencerListOrderStrategy='fansCount')
        return models.CommunityInfo(await self.http.get('community/info', params=params, scopeCid=id))

    async def joined_communities(self, start: int = 0, size: int = 25) -> models.JoinedCommunities:
        return models.JoinedCommunities(await self.http.get('community/joined', dict(v=1, start=start, size=size)))

    async def get_vip_users(self, cid: int) -> models.CommunityInfluencers:
        return models.CommunityInfluencers(await self.http.get('influencer', cid=cid))

    async def search_user(self, q: str, cid: Optional[int] = None) -> dict:
        """Deprecated api service."""
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('user-profile/search', params=params, cid=cid)

    async def search_community(self, q: str, language: str = 'en') -> models.SearchCommunity:
        return models.SearchCommunity(await self.http.get('community/search', dict(q=q, timezone=self.timezone, language=language)))

    async def login(
        self,
        email: str,
        password: str = MISSING,
        secret: str = MISSING
    ) -> models.Login:
        if not password and not secret:
            raise ValueError('Password or secret can\'t be empty.')
        response = models.Login(await self.http.post('/auth/login', dict(
            action="normal",
            clientType=enums.ClientType.MASTER.value,
            deviceID=self.device,
            email=email,
            secret=f"0 {password}" if password else secret,
            v=2
        )))
        if response.ok():
            self.auid = response.auid
            self.secret = response.secret
            self.sid = response.sid
            self.account.json.update(response.account.json)
            self.user.json.update(response.user.json)
        return response

    async def logout(self):
        self.auid = None
        self.secret = None
        self.sid = None
        self.account.json.clear()
        self.user.json.clear()


class Amino1:
    async def get_community(self, id: int):
        class CommunityService:
            ...
        return CommunityService()

    async def get_user(self, id: str):
        class UserService:
            ...
        return UserService()

    async def get_chat(self, id: str):
        class ChatService:
            ...
        return ChatService()

    async def get_blog(self, id: str):
        ...


class Amino2:

    async def get_trending_community(self, cid: int = None):
        return await self.http.get('/community/trending', cid=cid)

    async def search_post(self, q: str, cid: int):
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('/post/search', params=params, cid=cid)

    async def search_chat(self, q: str, cid: Optional[int] = None):
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('/chat/thread/explore/search', cid=cid)

    async def recommend_community(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('community/suggested', params=params)

    async def recommend_story(self, cid: int):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/0/feed/story', params=params, cid=cid)

    async def fetch_story(self, q: str, cid: int = None):
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('/feed/story', params=params, cid=cid)

    async def fetch_bookmark_topics(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/persona/bookmarked-topics')

    async def fetch_community_collection_view(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/community-collection/view', params=params)

    async def fetch_topic_header(self, cid: int = None):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/.*/metadata', params=params, cid=cid)

    async def fetch_topic_static(self, cid: int = None):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/explore', params=params, cid=cid)

    async def fetch_topic_latest(self, cid: int = None):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/latest', params=params, cid=cid)

    async def fetch_topic_popular(self, cid: int = None):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/popular', params=params, cid=cid)

    async def fetch_topic_popular_v2(self, cid: int = None):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/.*/feed/story', params=params, cid=cid)

    async def fetch_topic_recommend(self, cid: int = None):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/recommendation', params=params, cid=cid)

    async def fetch_community_collection_com(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/community-collection/.*/communities', params=params)

    async def fetch_featured_topic(self, cid: int = None):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/featured-topics', params=params, cid=cid)

    async def fetch_story_in_community(self, cid: int):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/feed/story', params=params, cid=cid)

    async def persona(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/persona/interest', params=params)

    async def get_content_language(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/client-config/content-language-settings', params=params)

    async def get_appearence_language(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/client-config/appearance-settings', params=params)

    async def join_community(self, id: int, invitation: Optional[str] = None):
        """Join in any community.

        Parameters
        ----------
        id: int
            Community id.
        invitation: str
            Invitation id.
        """
        data: dict = dict(invitationID=invitation) if invitation else dict()
        return await self.http.post('community/join', json=data, cid=id)

    async def check_membership(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/membership', params=params)

    async def check_device_status(self, device: str):
        params: dict = dict(timezone=self.timezone, q=device, device=device)
        return await self.http.get('device', params=params)

    async def suggest_topic(self, cid: int):
        params: dict = dict(timezone=self.timezone)
        return self.http.get('topic/suggest-topics', params=params, cid=cid)

    async def get_chat_info(self, id: str, cid: Optional[int] = None):
        """Get chat thread info

        Parameters
        ----------
        id: str
            Chat id (chat thread id).
        cid: int
            community id.
        """
        return await self.http.get(f'/chat/thread/{id}', cid=cid)

    async def get_joined_chats(self, cid: int, start: int = 0, size: int = 100) -> dict:
        """Get an list of joined chats.

        Parameters
        ----------
        cid: int
            Comminity id.
        start: int
            start index.
        size: int
            size of the list. Max size is 100.
        """
        params: dict = dict(type='joined', start=start, size=size)
        return await self.http.get('/chat/thread', params=params, cid=cid)

    async def get_chat_messages(self, id: str, pageToken: Optional[str] = None, size: int = 25, cid: Optional[int] = None) -> dict:
        """Get an list of chat messages.

        Parameters
        ----------
        id: str
            Chat id.
        pageToken: str
            the token to continue reading an page of messages.
        cid: Optional[int]
            Community id.
        start: int
            start index.
        size: int
            size of the list. Max size is 100
        """
        # param: start (find)
        params: dict = dict(v=2, pagingType='t',
                            pageToken=pageToken, size=size)
        return await self.http.get(f'chat/thread/{id}/message', params=params, cid=cid)

    async def get_chat_users(self, id: str, start: int = 0, size: int = 25, cid: Optional[int] = None) -> dict:
        """Get users in any chat

        Parameters
        ----------
        id: str
            Chat id. (chat thread id)
        start: int
            start index.
        size: int
            Size of list of users. Max size is 100.
        cid: Optional[int]
            Community id.
        """
        params: dict = dict(start=start, size=size, type='default', cv='1.2')
        return await self.http.get(f'chat/thread/{id}/member', params=params, cid=cid)

    async def get_blog_info(self, id: str, cid: Optional[int] = None) -> dict:
        """Get Blog Info

        Parameters
        ----------
        id: str
            Blog id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/blog/{id}', cid=cid)

    async def get_quiz_info(self, id: str, cid: Optional[int] = None) -> dict:
        """Get Quiz Info

        Parameters
        ----------
        id: str
            Blog id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/blog/{id}', cid=cid)

    async def get_wiki_info(self, id: str, cid: Optional[int] = None) -> dict:
        """Get Item Info

        Parameters
        ----------
        id: str
            Wiki id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/item/{id}', cid=cid)

    async def get_file_info(self, cid: Optional[int] = None) -> dict:
        """Get Shared File Info

        Parameters
        ----------
        id: str
            File id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/shared-folder/files/{id}', cid=cid)

    async def get_story_info(self):
        ...

    async def get_store_items(self):
        ...

    async def get_live_info(self):
        ...

    async def get_wallet_info(self):
        ...

    async def get_wallet_history(self):
        ...

    async def get_shared_folder(self):
        ...

    async def get_shared_folder_images(self):
        ...

    async def get_profile_comments(self):
        ...

    async def get_wiki_comments(self):
        ...

    async def get_blog_comments(self):
        ...

    async def get_quiz_comments(self):
        ...

    async def get_story_commments(self):
        ...

    async def get_post_supporters(self):
        ...

    async def get_chat_supporters(self):
        ...

    # all
    async def get_all_users(self, start: int = 0, size: int = 25):
        return await self.http.get('user-profile', dict(start=start, size=size))

    async def get_all_alerts(self):
        ...

    # others

    async def purchase(self):
        ...

    async def check_in(self):
        ...

    async def play_lottery(self):
        ...

    async def play_quiz(self):
        ...

    async def follow(self):
        ...

    async def unfollow(self):
        ...

    # post
    async def post_blog(self):
        ...

    async def post_wiki(self):
        ...

    async def post_quiz(self):
        ...

    async def post_image(self):
        ...

    async def post_question(self):
        ...

    async def post_poll(self):
        ...

    async def post_story(self):
        ...

    # live
    async def start_voice_chat(self):
        # members require approval to be a voice participant
        ...

    async def start_screening_room(self):
        ...

    async def start_live_stream(self):
        ...

    async def end_voice_chat(self):
        ...

    async def end_screening_room(self):
        ...

    async def end_live_stream(self):
        ...
