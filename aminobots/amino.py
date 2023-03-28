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

from .abc import ABCAmino
from .enums import Language
from .ws import WSClient
from .rtc import RTCClient
from .http import HTTPClient
from .utils import copy_doc, Device, suppress
from .models import (
    AccountInfo,
    CommunityInfo,
    CommunityInfluencers,
    LinkIdentify,
    LinkResolution,
    Login,
    UserInfo
)
from .objects import (
    Account,
    UserProfile,
    Object
)
from inspect import iscoroutinefunction
from functools import wraps


__all__ = ('Amino',)


class Amino(ABCAmino):

    account: Account
    auid: Optional[str]
    device: Device
    http: HTTPClient
    raiseExceptions: bool
    rtc: RTCClient
    sid: Optional[str]
    secret: Optional[str]
    socketEnabled: bool
    user: UserProfile
    utc: int
    ws: WSClient

    def __init__(
        self,
        device: Optional[Union[str, Device]] = None,
        proxy: Optional[str] = None,
        *,
        language: Union[Language, str] = Language.ENGLISH,
        utc: int = 0,
        raiseExceptions: bool = True,
        socketEnabled: bool = True
    ) -> None:
        self.ws = WSClient(self)
        self.http = HTTPClient(self)
        self.rtc = RTCClient(self)
        self.account = Account(dict())
        self.user = UserProfile(dict())
        # proxy = options.get('proxy')
        # proxy_auth = options.get('proxy_auth')
        if not isinstance(device, Optional[Union[str, Device]]):
            raise TypeError('expected str, Device or None, not %r.' % type(device).__name__)
        self.device = Device(device) if device else Device()
        self.raiseExceptions = bool(raiseExceptions)
        self.socketEnabled = bool(socketEnabled)
        if not isinstance(utc, int):
            raise TypeError('expected int not %r.' % type(utc).__name__)
        elif utc not in range(-12, 15):
            raise ValueError('the utc must be between -12 and 14.')
        if not isinstance(language, (Language, str)):
            raise TypeError('expected str or Language not %r.' % type(language).__name__)
        self.utc = utc or 0
        self.auid = None
        self.secret = None
        self.sid = None

    @property
    def timezone(self) -> int:
        """Timezone for amino http parameters."""
        return self.utc * 60

    @copy_doc(ABCAmino.get_from_link)
    async def get_from_link(self, link: str) -> LinkResolution:
        return LinkResolution(await self.http.get('link-resolution', dict(q=link)))

    @copy_doc(ABCAmino.get_link_info)
    async def get_link_info(self, link: str) -> LinkIdentify:
        return LinkResolution(await self.http.get('community/link-identify', dict(q=link)))

    @copy_doc(ABCAmino.get_user_info)
    async def get_user_info(self, id: str, cid: Optional[int] = None) -> UserInfo:
        params = dict(withInfluencerInfo=1, withInfluencerList=1, influencerInfo='true')
        return UserInfo(await self.http.get(f'user-profile/{id}', params, cid=cid))

    @copy_doc(ABCAmino.get_account_info)
    async def get_account_info(self) -> AccountInfo:
        return AccountInfo(await self.http.get('account'))

    @copy_doc(ABCAmino.get_community_info)
    async def get_community_info(self, id: int, /) -> CommunityInfo:
        params = dict(withInfluencerList=1, withTopicList='true', influencerListOrderStrategy='fansCount')
        return CommunityInfo(await self.http.get('/community/info', params=params, scopeCid=id))

    @copy_doc(ABCAmino.joined_communities)
    async def joined_communities(self, start: int = 0, size: int = 25) -> dict:
        params = dict(v=1, start=start, size=size)
        return await self.http.get('/community/joined', params=params)

    @copy_doc(ABCAmino.get_vip_users)
    async def get_vip_users(self, cid: int) -> CommunityInfluencers:
        return CommunityInfluencers(await self.http.get('influencer', cid=cid))

    async def get_trending_community(self, cid: int = None):
        return await self.http.get('/community/trending', cid=cid)

    async def search_community(self, q: str):
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('/community/search', params=params)

    async def search_post(self, q: str, cid: int):
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('/post/search', params=params, cid=cid)

    async def search_chat(self, q: str, cid: Optional[int] = None):
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('/chat/thread/explore/search', cid=cid)

    async def search_user(self, q: str, cid: Optional[int] = None):
        params: dict = dict(q=q, timezone=self.timezone)
        return await self.http.get('/user-profile/search', params=params, cid=cid)

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
    async def login(
        self,
        email: str = None,
        password: str = None,
        phone: str = None,
        secret: str = None,
        clientType: int = 100
    ):
        """Login in one account.

        Parameters
        ----------
        email : str, optional
            email of the amino account. (default is None)
        password : str, optional
            password of the amino account. (default is None)
        phone : str, optional
            phone number of the amino account. (default is None)
        secret : str, optinal
            secret password encripted of the amino account. (default is None)
        clientType : int, optional
            client type of the user. (default is 100)

        Returns
        -------
        dict
            native api response
        aminobots.objects.Login
            an object organize api response

        Examples
        --------
        >>> amino.login(email='example@example.com', password='password123')
        <Login object at 0x000001BB8BAE9640>

        """
        data = dict(action="normal", clientType=clientType, deviceID=self.device,
                    email=email, secret=f"0 {password}" if password else secret, v=2)
        if phone is not None:
            data.update(phoneNumber=phone)
            data.pop("email")
        response = await self.http.post('/auth/login', json=data)
        if isinstance(response.get('api:statuscode'), int) and not response['api:statuscode']:
            self.auid = response.get('auid')
            self.secret = response.get('secret')
            self.sid = response.get('sid')
            self.account.json.update(response.get('account'))
            self.user.json.update(response.get('userProfile'))
            if self.socketEnabled:
                await self.ws.connect(daemon=True)
        return response

    async def logout(self):
        ...

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
