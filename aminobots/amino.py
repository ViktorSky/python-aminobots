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
from typing import Dict, Optional, Union
from datetime import datetime
import logging
from pydantic import HttpUrl
from .abc import ABCAmino
from .enums import (
    ClientType,
    ConnectionStatus,
    Language,
    ObjectType,
    PaymentType,
    ValidationLevel,
    ValidationType
)
from .http import HTTPClient
from .rtc import RTCClient
from .ws import WSClient
from .utils import (
    Device,
    MediaList,
    SID,
    copy_all_docs,
    device_gen,
    typechecker
)
from .objects import (
    Account,
    UserProfile
)
from .models import (
    AccountInfo,
    AllPushSettings,
    ChatInfo,
    ChatMembers,
    CommunityInfluencers,
    CommunityInfo,
    FromDevice,
    JoinedChats,
    JoinedCommunities,
    LinkIdentify,
    LinkResolution,
    Login,
    MembershipConfig,
    MembershipInfo,
    PushNotification,
    SearchChat,
    SearchCommunity,
    SearchQuiz,
    SearchUser,
    UserInfo,
    VerifyPassword,
    WalletAds,
    WalletHistory,
    WalletInfo,
    parse_model
)

__all__ = ('Amino',)


DEFAULT_LOGGER = logging.getLogger(__name__)
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

    Parameters
    ----------
    device : :class:`str` | :class:`Device` | `None`
        The device being used by the client. If `None`, a new device will be generated. 
    proxy : :class:`str` | `None`
        The HTTP or HTTPS proxy to use for the client. If not specified, no proxy will be used.
    language : :class:`Language` | `None`
        The content language to use for Amino. Default is :attr:`Language.ENGLISH`.
    utc : `int` | `None`
        The UTC timezone offset for the client in hours. Default is `0`.
    raiseExceptions : :class:`bool` | `None`
        Whether to raise exceptions when errors occur. Default is `True`.

    Attributes
    ----------
    account : :class:`Account`
        The user's account information.
    auid : :class:`str`
        The user's id.
    device : :class:`Device`
        The device being used by the client.
    http : :class:`HTTPClient`
        The HTTP client for Amino API requests.
    raiseExceptions : :class:`bool`
        Whether to raise exceptions when errors occur.
    rtc : :class:`RTCClient`
        The RTC client for the Agora service.
    sid : Optional[:class:`str`]
        The session ID for the Amino client.
    secret : Optional[:class:`str`]
        The encoded secret password for the user.
    user : :class:`UserProfile`
        The user's profile information.
    utc : :class:`int`
        The UTC timezone offset for the client in hours.
    ws : :class:`WSClient`
        The WebSocket client for the Amino client.

    Examples
    --------
    This example demonstrates how to use the `Amino` class to log in to Amino and retrieve the user's nickname:

    >>> amino = Amino(raiseExceptions=False)
    >>> response = await amino.login(input('email:'), input('password:'))
    >>> if response.api.ok:
    ...     print(response.user.nickname)
    ... else:
    ...     print(response.api.message)

    """

    def __init__(
        self,
        device: Optional[Union[str, Device]] = None,
        proxy: Optional[str] = None,
        *,
        logger: logging.Logger = DEFAULT_LOGGER,
        language: Language = Language.ENGLISH,
        utc: int = 0,
        timeout: Optional[int] = None,
        raiseExceptions: bool = True,
        **kwargs
    ) -> None:
        self.http = HTTPClient(self, kwargs.pop('user_agent', None))
        self.rtc = RTCClient(self)
        self.ws = WSClient(self)
        self.account = Account.construct()
        self.user = UserProfile.construct()
        self.logger = logger
        self.device = device or device_gen()
        self.proxy = proxy
        self.utc = utc
        self.language = language
        self.timeout = timeout
        self.raiseExceptions = raiseExceptions

    @property
    def timezone(self) -> int:
        """Timezone for amino http parameters."""
        return self.utc * 60

    @property
    def authenticated(self) -> bool:
        """Check if the instance is authenticated in any acount."""
        return bool(self.sid)

    @typechecker
    async def update(self, user: Optional[UserProfile] = None, account: Optional[Account] = None) -> None:
        """Update the amino object."""
        if isinstance(user, UserProfile):
            self.user = user
        elif self.sid and not self.user.id:
            self.user = (await self.get_user_info(self.sid.objectId)).user
        if isinstance(account, Account):
            self.account = account
        elif self.sid and not self.account.aminoId:
            self.account = (await self.get_account_info()).account

    @typechecker
    async def get_from_link(self, link: Union[str, HttpUrl]) -> LinkResolution:
        return parse_model(LinkResolution, await self.http.get('link-resolution', dict(q=link)))

    @typechecker
    async def get_from_device(self, device: Union[str, Device]) -> FromDevice:
        return parse_model(FromDevice, await self.http.get('auid', dict(deviceId=device)))

    @typechecker
    async def get_link_info(self, link: str) -> LinkIdentify:
        return parse_model(LinkIdentify, await self.http.get('community/link-identify', dict(q=link)))

    async def get_ads_info(self) -> WalletAds:
        return parse_model(WalletAds, await self.http.get('wallet/setting/ads', dict(timezone=self.timezone)))

    @typechecker
    async def get_user_info(self, id: str, comId: int = 0) -> UserInfo:
        return parse_model(UserInfo, await self.http.get(f'user-profile/{id}', comId=comId))

    async def get_account_info(self) -> AccountInfo:
        return parse_model(AccountInfo, await self.http.get('account'))

    @typechecker
    async def get_chat_info(self, id: str, comId: int = 0) -> ChatInfo:
        return parse_model(ChatInfo, await self.http.get(f'chat/thread/{id}', comId=comId))

    @typechecker
    async def get_chat_members(self, id: str, start: int = 0, size: int = 25, comId: int = 0) -> ChatMembers:
        return parse_model(ChatMembers, await self.http.get(f'chat/thread/{id}/member',
            dict(start=start, size=size, type='default', cv='1.2'), comId=comId))

    @typechecker
    async def get_community_info(self, id: int) -> CommunityInfo:
        return parse_model(CommunityInfo, await self.http.get('community/info',
            dict(withInfluencerList=1, withTopicList='true', influencerListOrderStrategy='fansCount'), scope=id))

    @typechecker
    async def get_community_trending(self, id: int):
        return await self.http.get('community/trending', comId=id)

    async def get_wallet_info(self) -> WalletInfo:
        return parse_model(WalletInfo, await self.http.get('wallet', dict(force=True)))

    @typechecker
    async def get_wallet_history(self, start: int = 0, size: int = 25) -> WalletHistory:
        return parse_model(WalletHistory, await self.http.get('wallet/coin/history', dict(start=start, size=size)))

    @typechecker
    async def get_account_push_settings(self) -> AllPushSettings:
        return parse_model(AllPushSettings, await self.http.get('account/push-settings'))

    @typechecker
    async def get_push_settings(self, comId: int = 0) -> PushNotification:
        return parse_model(PushNotification, await self.http.get('user-profile/push', comId=comId))

    @typechecker
    async def set_push_settings(self, activities: Optional[bool], broadcasts: Optional[bool], comId: int = 0) -> PushNotification:
        pushExtensions: Dict[str, bool] = {}
        if activities is not None:
            pushExtensions["communityActivitiesEnabled"] = activities
        if broadcasts is not None:
            pushExtensions["communityBroadcastsEnabled"] = broadcasts
        return parse_model(PushNotification, await self.http.post('user-profile/push', dict(
            pushExtensions=pushExtensions, pushEnabled=bool(activities or broadcasts)), comId=comId))

    async def get_membership_info(self) -> MembershipInfo:
        return parse_model(MembershipInfo, await self.http.get('membership'))

    @typechecker
    async def configure_membership(self, autoRenew: bool) -> MembershipConfig:
        return parse_model(MembershipConfig, await self.http.post('membership/config', dict(
            paymentType=PaymentType.COIN, paymentContext=dict(isAutoRenew=autoRenew))))

    @typechecker
    async def joined_chats(self, start: int = 0, size: int = 25, comId: int = 0) -> JoinedChats:
        return parse_model(JoinedChats, await self.http.get('chat/thread', dict(type='joined-me', start=start, size=size), comId=comId))

    @typechecker
    async def joined_communities(self, start: int = 0, size: int = 25) -> JoinedCommunities:
        return parse_model(JoinedCommunities, await self.http.get('community/joined', dict(v=1, start=start, size=size)))

    @typechecker
    async def get_vip_users(self, comId: int) -> CommunityInfluencers:
        return parse_model(CommunityInfluencers, await self.http.get('influencer', comId=comId))

    @typechecker
    async def search_user(self, q: str, comId: int = 0) -> SearchUser:
        return parse_model(SearchUser, await self.http.get('user-profile', dict(q=q, timezone=self.timezone, type='name'), comId=comId))

    @typechecker
    async def search_community(self, q: str, language: Language = Language.ALL) -> SearchCommunity:
        return parse_model(SearchCommunity, await self.http.get('community/search', dict(q=q, timezone=self.timezone, language=language.value)))

    @typechecker
    async def search_chat(self, q: str, pageToken: Optional[str] = None, comId: int = 0) -> SearchChat:
        return parse_model(SearchChat, await self.http.get('chat/thread/explore/search',
            dict(q=q, timezone=self.timezone, pageToken=pageToken), comId=comId))

    @typechecker
    async def search_quiz(self, q: str, comId: int) -> SearchQuiz:
        return parse_model(SearchQuiz, await self.http.get('post/search', dict(q=q, timezone=self.timezone), comId=comId))

    @typechecker
    async def verify_password(self, password: Optional[str] = None, secret: Optional[str] = None) -> VerifyPassword:
        return parse_model(VerifyPassword, await self.http.post('auth/verify-password', dict(secret=f'0 {password}' if password else secret)))

    @typechecker
    async def login(self, email: str, password: Optional[str] = None, secret: Optional[str] = None) -> Login:
        if self.raiseExceptions and (not password and not secret):
            raise ValueError('Password or secret can\'t be empty.')
        response = parse_model(Login, await self.http.post('auth/login', dict(
            clientType=ClientType.MASTER,
            action="normal",
            email=email,
            secret=f"0 {password}" if password else secret,
            v=2
        )))
        if response.ok:
            self.auid = response.auid
            self.secret = response.secret
            self.sid = response.sid
            await self.update(response.user, response.account)
        return response

    @typechecker
    async def login_phone(
        self,
        phone: str,
        password: Optional[str] = None,
        secret: Optional[str] = None
    ) -> Login:
        if self.raiseExceptions and (not password and not secret):
            raise ValueError('Password or secret can\'t be empty.')
        response = parse_model(Login, await self.http.post('auth/login', dict(
            clientType=ClientType.MASTER,
            action="normal",
            phoneNumber=phone,
            secret=f"0 {password}" if password else secret,
            v=2
        )))
        if response.ok:
            self.auid = response.auid
            self.secret = response.secret
            self.sid = response.sid
            await self.update()
        return response

    @typechecker
    async def login_sid(self, sid: Union[str, SID]) -> None:
        self.sid = sid
        await self.update()

    async def logout(self):
        self.auid = self.secret = self.sid = None
        await self.update()

    @typechecker
    async def set_activity(self, status: ConnectionStatus):
        return await self.http.post(f'user-profile/{self.user.id}/online-status', dict(
            onlineStatus=status,
            duration=86400
        ))

    @typechecker
    async def compose_eligible_check(self, type: ObjectType, subType: Optional[ObjectType] = None):
        # com.narvii.util.j.java <public void `c`>
        return await self.http.post(f'user-profile/{self.user.id}/compose-eligible-check', dict(
            objectType=type,
            **dict(objectSubtype=subType) if subType else {}
        ))

    @typechecker
    async def check_in(self, comId: int):
        return await self.http.post('check-in', dict(), comId=comId)

    @typechecker
    async def play_lottery(self, comId: int):
        return await self.http.post('check-in/lottery', dict(), comId=comId)

    @typechecker
    async def set_birthday(self, date: datetime):
        return await self.http.post('persona/profile/birthday', dict(birthday=date))

    @typechecker
    async def check_register(self, email: Optional[str] = None, phone: Optional[str] = None):
        return await self.http.post('auth/register-check', dict(
            identity=email or phone,
            **dict(email=email) if email else dict(phoneNumber=phone)
        ))

    async def request_verify_code(self):
        return await self.http.post('', dict())

    @typechecker
    async def verify(self, vcode: str, email: Optional[str] = None, phone: Optional[str] = None):
        return await self.http.post('auth/check-security-validation', dict(
            validationContext=dict(
                type=ValidationType.EMAIL if email else ValidationType.GLOBAL_SMS,
                identity=email or phone,
                level=ValidationLevel.IDENTITY if email else ValidationLevel.SECRET,
                data=dict(code=vcode)
            )
        ))

    async def activate_email(self, vcode: str, email: Optional[str] = None, phone: Optional[str] = None):
        return await self.http.post('activate-email', dict(
            level=ValidationLevel.IDENTITY,
            type=ValidationType.EMAIL if email else ValidationType.GLOBAL_SMS,
            identity=email if email else phone,
            data=dict(code=vcode)
        ))

    async def update_email(self, new_email: str, vcode: str, password: Optional[str] = None, secret: Optional[str] = None):
        return await self.http.post('auth/update-email', dict(
            newValidationContext=dict(
                secret=f'0 {password}' if password else secret,
                identity=new_email,
                data=dict(code=vcode),
                level=ValidationLevel.IDENTITY,
                type=ValidationType.EMAIL,
                deviceID=self.device
            ),
            oldValidationContext=dict(
                identity=self.account.email,
                level=ValidationLevel.IDENTITY,
                data=dict(code=vcode),
                type=ValidationType.EMAIL,
                deviceID=self.device
            )
        ))

    async def update_phone(self, phone: str, vcode: str, password: str, secret: str):
        return await self.http.post('auth/update-phone-number', dict(
            newValidationContext=dict(
                secret=f'0 {password}' if password else secret,
                identity=phone,
                data=dict(code=vcode),
                level=ValidationLevel.IDENTITY,
                type=ValidationType.GLOBAL_SMS,
                deviceID=self.device
            ),
            oldValidationContext=dict(
                identity=self.account.phone,
                data=dict(code=vcode),
                level=ValidationLevel.IDENTITY,
                type=ValidationType.GLOBAL_SMS,
                deviceID=self.device
            )
        ))

    async def delete_account(self, password: Optional[str] = None, secret: Optional[str] = None):
        return await self.http.post('account/delete-request', dict(secret=f'0 {password}' if password else secret))

    async def edit_profile(self, nickname: Optional[str] = None, bio: Optional[str] = None, medias: Optional[MediaList] = None):
        ...

    async def get_bussiness_wallet_history(self):
        return await self.http.get('wallet/business-coin/history')

    async def watch_ads(self):
        return await self.http.post('wallet/ads/video/start', dict(canWatchVideo=True))

    async def coupon(self):
        return await self.http.get('coupon/new-user-coupon')

    async def get_latest_payment(self):
        # com.narvii.wallet.j1.java (onStart)
        return await self.http.get('membership/latest-payment-context')

    async def get_paid_log_info(self, paidOutId: str):
        return await self.http.get(f'wallet/paid-out-log/{paidOutId}', dict())

    async def get_paid_logs(self):
        # unsupported service
        return await self.http.post('wallet/paid-out-log', dict())

    async def get_paid_log(self, paidOutId: str):
        return await self.http.get(f'wallet/paid-out-log/{paidOutId}')

    async def buy_membership_by_coins(self, packName: str):
        # com.narvii.wallet.j1.java
        return await self.http.post('membership/product/v2', dict(
            paymentType=PaymentType.COIN.value,
            packageName=packName
        ))

    async def pre_subscribe(self, productId: str):
        # com.narvii.wallet.j1.java
        return await self.http.post('membership/product/pre-subscribe', dict(
            sku=productId,
            packageName='',
            paymentType=PaymentType.IOS_SUBSCRIPTION
        ))

    async def subscribe(self, packName: str):
        # com.narvii.wallet.j1.java
        return await self.http.post('membership/product/v2', dict(
            paymentType=PaymentType.ANDROID_SUBSCRIPTION.value,
            packageName=packName,
            packageVersion=2
        ))

    async def subscribe_product(self, pname: str, autoRenew: bool = True):
        # com.narvii.wallet.j1.java
        return await self.http.post('membership/product/subscribe', dict(
            sku=None,
            packageName=pname,
            paymentType=PaymentType.ANDROID_SUBSCRIPTION.value,
            paymentContext=dict(
                isAutoRenew=autoRenew
            ) # i0.d(hVar.d())
        ))

    async def purchase_master(self):
        # unsupported service
        return await self.http.post('wallet/product/master', dict(
            paymentType=PaymentType.ANDROID_PURCHASE.value
        ))

    async def fetch_topic_header(self, id: int, comId: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get(f'topic/{id}/metadata', params=params, comId=comId)

    async def fetch_community_collection_view(self, comId: int):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('community-collection/view', params=params, scope=comId)


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


class Amino2(Amino):

    async def recommend_community(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('community/suggested', params=params)

    async def fetch_story(self, q: str, comId: int = 0):
        return await self.http.get('feed/story', dict(q=q, timezone=self.timezone), comId)


    async def recommend_story(self, comId: int):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/0/feed/story', params=params, comId=comId)

    async def fetch_bookmark_topics(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/persona/bookmarked-topics')

    async def fetch_topic_static(self, id: int, comId: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get(f'topic/{id}/feed/story/explore', params=params, comId=comId)

    async def fetch_topic_latest(self, id: int, comId: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get(f'topic/{id}/feed/story/latest', params=params, comId=comId)

    async def fetch_topic_popular(self, comId: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/popular', params=params, comId=comId)

    async def fetch_topic_popular_v2(self, comId: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/.*/feed/story', params=params, comId=comId)

    async def fetch_topic_recommend(self, comId: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/recommendation', params=params, comId=comId)

    async def fetch_community_collection_com(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/community-collection/.*/communities', params=params)

    async def fetch_featured_topic(self, comId: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/featured-topics', params=params, comId=comId)

    async def fetch_story_in_community(self, comId: int):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/feed/story', params=params, comId=comId)

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
        return await self.http.post('community/join', json=data, comId=id)

    async def check_membership(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/membership', params=params)

    async def check_device_status(self, device: str):
        params: dict = dict(timezone=self.timezone, q=device, device=device)
        return await self.http.get('device', params=params)

    async def suggest_topic(self, comId: int):
        params: dict = dict(timezone=self.timezone)
        return self.http.get('topic/suggest-topics', params=params, comId=comId)

    async def get_chat_messages(self, id: str, pageToken: Optional[str] = None, size: int = 25, comId: int = 0) -> dict:
        """Get an list of chat messages.

        Parameters
        ----------
        id: str
            Chat id.
        pageToken: str
            the token to continue reading an page of messages.
        comId: Optional[int]
            Community id.
        start: int
            start index.
        size: int
            size of the list. Max size is 100
        """
        # param: start (find)
        params: dict = dict(v=2, pagingType='t',
                            pageToken=pageToken, size=size)
        return await self.http.get(f'chat/thread/{id}/message', params=params, comId=comId)

    async def get_blog_info(self, id: str, comId: int = 0) -> dict:
        """Get Blog Info

        Parameters
        ----------
        id: str
            Blog id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/blog/{id}', comId=comId)

    async def get_quiz_info(self, id: str, comId: int = 0) -> dict:
        """Get Quiz Info

        Parameters
        ----------
        id: str
            Blog id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/blog/{id}', comId=comId)

    async def get_wiki_info(self, id: str, comId: int = 0) -> dict:
        """Get Item Info

        Parameters
        ----------
        id: str
            Wiki id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/item/{id}', comId=comId)

    async def get_file_info(self, id: str, comId: int = 0) -> dict:
        """Get Shared File Info

        Parameters
        ----------
        id: str
            File id.
        cid: int
            Community id.
        """
        return await self.http.get(f'/shared-folder/files/{id}', comId=comId)

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
