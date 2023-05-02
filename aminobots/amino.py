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
import logging
from typing import Optional, Union

from .http import HTTPClient
from .ws import WSClient
from .rtc import RTCClient
from .abc import ABCAmino
from .enums import ClientType, Language, PaymentType, ValidationType, ValidationLevel
from .utils import copy_all_docs, Device, SID
from . import (
    models,
    objects,
    utils
)

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

    Parameters
    ----------
    device : Union[:class:`str`, :class:`Device`], optional
        The NDC device to use for the client. If `None`, a new device will be generated. 
    proxy : :class:`str`, optional
        The HTTP or HTTPS proxy to use for the client. If not specified, no proxy will be used.
    language : :class:`Language`, optional
        The content language to use for Amino. Default is :attr:`Language.ENGLISH`.
    utc : `int`, optional
        The UTC timezone offset for the client in hours. Default is `0`.
    raiseExceptions : :class:`bool`, optional
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
    >>> if response.api.ok():
    ...     print(amino.user.nickname)
    ... else:
    ...     print(response.api.message)

    Note: Before running this example, make sure to replace "email" and "password" with your actual Amino email and password.

    """
    #  instance vars
    http: HTTPClient
    rtc: RTCClient
    ws: WSClient
    account: objects.Account
    user: objects.UserProfile
    logger: logging.Logger

    #  changeable settings
    _device: Device
    timeout: Optional[int]
    utc: int
    language: Language
    proxy: Optional[str]
    raiseExceptions: bool

    #  session vars
    auid: Optional[str]
    _sid: Optional[SID]
    secret: Optional[str]

    @property
    def device(self) -> Device:
        """The device being used by the client."""
        return self._device

    @device.setter
    def device(self, value: Union[str, Device]) -> None:
        if not isinstance(value, Union[str, Device]):
            raise TypeError('expected str or Device, not %r.' % type(value).__name__)
        elif isinstance(value, str):
            value = Device(value)
        self._device = value

    @property
    def sid(self) -> SID:
        """The session ID for the Amino client."""
        return self._sid

    @sid.setter
    def sid(self, value: Union[str, SID, None]) -> None:
        if not isinstance(value, Union[str, SID, None]):
            raise TypeError('expected str, SID or None, not %r.' % type(value).__name__)
        elif isinstance(value, str):
            value = SID(value)
        self._sid = value

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
    ) -> None:
        if not isinstance(device, Optional[Union[str, Device]]):
            raise TypeError(
                'device argument must be a string or Device object, not %r.' % type(device).__name__)
        if not isinstance(logger, logging.Logger):
            raise TypeError(
                'logger argument must be a Logger object, not %r.' % type(logger).__name__)
        if not isinstance(proxy, Optional[str]):
            raise TypeError(
                'proxy argument must be a string, not %r.' % type(proxy).__name__)
        if not isinstance(utc, int):
            raise TypeError(
                'utc argument must be a integer not %r.' % type(utc).__name__)
        if utc not in range(-12, 15):
            raise ValueError('utc argument must be between -12 and 14.')
        if not isinstance(language, Language):
            raise TypeError(
                'language argument must be a Language object not %r.' % type(language).__name__)
        if not isinstance(timeout, Optional[int]):
            raise TypeError(
                'timeout argument must be a integer not %r.' % type(timeout).__name__)
        self.ws = WSClient(self)
        self.http = HTTPClient(self)
        self.rtc = RTCClient(self)
        self.account = objects.Account(dict())
        self.user = objects.UserProfile(dict())
        self.device = device or Device()
        self.logger = logger
        self.proxy = proxy
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

    async def update(self) -> None:
        """Update the amino object."""
        if self.sid:
            self.account = (await self.get_account_info()).account
            self.user = (await self.get_user_info(self.user.id or self.sid.objectId)).user
        else:
            self.account = objects.Account({})
            self.user = objects.UserProfile({})

    async def get_from_link(self, link: str, /) -> models.LinkResolution:
        return models.LinkResolution(await self.http.get('link-resolution', dict(q=link)))

    async def get_from_device(self, device: Union[str, Device], /) -> models.FromDevice:
        return models.FromDevice(await self.http.get('auid', dict(deviceId=device)))

    async def get_link_info(self, link: str, /) -> models.LinkIdentify:
        return models.LinkIdentify(await self.http.get('community/link-identify', dict(q=link)))

    async def get_ads_info(self) -> models.WalletAds:
        return models.WalletAds(await self.http.get('wallet/setting/ads')) # timezone

    async def get_user_info(self, id: str, /, cid: Optional[int] = None) -> models.UserInfo:
        return models.UserInfo(await self.http.get(f'user-profile/{id}', cid=cid))

    async def get_account_info(self) -> models.AccountInfo:
        return models.AccountInfo(await self.http.get('account'))

    async def get_chat_info(self, id: str, /, cid: Optional[int] = None) -> models.ChatInfo:
        return models.ChatInfo(await self.http.get(f'chat/thread/{id}', cid=cid))

    async def get_chat_members(self, id: str, /, start: int = 0, size: int = 25, cid: Optional[int] = None):
        return models.ChatMembers(await self.http.get(f'chat/thread/{id}/member', dict(start=start, size=size, type='default', cv='1.2'), cid=cid))

    async def get_community_info(self, id: int, /) -> models.CommunityInfo:
        return models.CommunityInfo(await self.http.get('community/info', dict(withInfluencerList=1, withTopicList='true', influencerListOrderStrategy='fansCount'), scopeCid=id))

    async def get_community_trending(self, cid: int, /):
        return await self.http.get('community/trending', cid=cid)

    async def get_wallet_info(self) -> models.WalletInfo:
        return models.WalletInfo(await self.http.get('wallet'), dict(force=True)) # timezone

    async def get_wallet_history(self, start: int = 0, size: int = 25) -> models.WalletHistory:
        return models.WalletHistory(await self.http.get('wallet/coin/history', dict(start=start, size=size)))

    async def get_account_push_settings(self) -> models.AllPushSettings:
        return models.AllPushSettings(await self.http.get('account/push-settings'))

    async def get_push_settings(self, cid: int = 0) -> models.PushNotification:
        return models.PushNotification(await self.http.get('user-profile/push', cid=cid))

    async def set_push_settings(self, activities: bool, broadcasts: bool, cid: int = 0) -> models.PushNotification:
        return models.PushNotification(await self.http.post('user-profile/push', dict(
            pushEnabled=bool(activities or broadcasts),
            pushExtensions=dict(
                **dict(communityBroadcastsEnabled=broadcasts) if broadcasts else {},
                **dict(communityActivitiesEnabled=activities) if activities else {},
                #systemEnabled=enable
            )
        ), cid=cid))

    async def get_membership_info(self) -> models.MembershipInfo:
        return models.MembershipInfo(await self.http.get('membership'))

    async def configure_membership(self, autoRenew: bool) -> models.MembershipConfig:
        return models.MembershipConfig(await self.http.post('membership/config', dict(
            paymentType=PaymentType.COIN.value,
            paymentContext=dict(
                isAutoRenew=autoRenew
            )
        )))

    async def joined_chats(self, cid: int = 0, start: int = 0, size: int = 25):
        return await self.http.get('chat/thread', dict(type='joined-me', start=start, size=size), cid=cid)

    async def joined_communities(self, start: int = 0, size: int = 25) -> models.JoinedCommunities:
        return models.JoinedCommunities(await self.http.get('community/joined', dict(v=1, start=start, size=size)))

    async def get_vip_users(self, cid: int, /) -> models.CommunityInfluencers:
        return models.CommunityInfluencers(await self.http.get('influencer', cid=cid))

    async def search_user(self, q: str, /, cid: Optional[int] = None) -> models.SearchUser:
        return models.SearchUser(await self.http.get('user-profile', dict(q=q, timezone=self.timezone, type='name'), cid=cid))

    async def search_community(self, q: str, /, language: Language = Language.ALL) -> models.SearchCommunity:
        return models.SearchCommunity(await self.http.get('community/search', dict(q=q, timezone=self.timezone, language=language.value)))

    async def search_chat(self, q: str, cid: Optional[int] = None):
        return await self.http.get('chat/thread/explore/search', dict(q=q, timezone=self.timezone), cid=cid)

    async def search_quiz(self, q: str, /, cid: Optional[int] = None) -> models.SearchQuiz:
        return models.SearchQuiz(await self.http.get('post/search', dict(q=q, timezone=self.timezone), cid=cid))

    async def login(self, email: str, password: str = None, secret: str = None) -> models.Login:
        if self.raiseExceptions and (not password and not secret):
            raise ValueError('Password or secret can\'t be empty.')
        response = models.Login(await self.http.post('auth/login', dict(
            clientType=ClientType.MASTER.value,
            action="normal",
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
            await self.update()
        return response

    async def login_phone(
        self,
        phone: str,
        password: Optional[str] = None,
        secret: Optional[str] = None
    ) -> models.Login:
        if self.raiseExceptions and (not password and not secret):
            raise ValueError('Password or secret can\'t be empty.')
        response = models.Login(await self.http.post('auth/login', dict(
            clientType=ClientType.MASTER.value,
            action="normal",
            phoneNumber=phone,
            secret=f"0 {password}" if password else secret,
            v=2
        )))
        if response.ok():
            self.auid = response.auid
            self.secret = response.secret
            self.sid = response.sid
            self.account.json.update(response.account.json)
            self.user.json.update(response.user.json)
            await self.update()
        return response

    async def login_sid(self, sid: Union[str, SID]) -> None:
        self.sid = sid
        account = await self.get_account_info()
        user = await self.get_user_info(self.sid.objectId)
        self.account.json.clear()
        self.user.json.clear()
        self.account.json.update(account.json)
        self.user.json.update(user.json)
        await self.update()

    async def logout(self):
        self.auid = None
        self.secret = None
        self.sid = None
        self.account.json.clear()
        self.user.json.clear()

    async def check_in(self, cid: int):
        return await self.http.post('check-in', dict(), cid=cid)

    async def play_lottery(self, cid: int):
        return await self.http.post('check-in/lottery', dict(), cid=cid)

    async def set_birthday(self, date: utils.Date):
        return await self.http.post('persona/profile/birthday', dict(birthday=date))

    async def check_register(self, email: Optional[str] = None, phone: Optional[str] = None):
        return await self.http.post('auth/register-check', dict(
            identity=email or phone,
            **dict(email=email) if email else dict(phoneNumber=phone)
        ))

    async def request_verify_code(self):
        return await self.http.post('', dict())

    async def verify(self, vcode: str, email: str = None, phone: str = None):
        return await self.http.post('auth/check-security-validation', dict(
            validationContext=dict(
                type=ValidationType.EMAIL.value if email else ValidationType.GLOBAL_SMS.value,
                identity=email or phone,
                level=ValidationLevel.IDENTITY.value if email else ValidationLevel.SECRET.value,
                data=dict(code=vcode)
            )
        ))

    async def verify_password(self, password: Optional[str] = None, secret: Optional[str] = None) -> models.VerifyPassword:
        return models.VerifyPassword(await self.http.post('auth/verify-password', dict(secret=f'0 {password}' if password else secret, deviceID=self.device)))

    async def activate_email(self, vcode: str, email: Optional[str] = None, phone: Optional[str] = None):
        return await self.http.post('activate-email', dict(
            level=ValidationLevel.IDENTITY.value,
            type=ValidationType.EMAIL.value if email else ValidationType.GLOBAL_SMS.value,
            identity=email if email else phone,
            data=dict(code=vcode)
        ))

    async def update_email(self, new_email: str, vcode: str, password: Optional[str] = None, secret: Optional[str] = None):
        return await self.http.post('auth/update-email', dict(
            newValidationContext=dict(
                secret=f'0 {password}' if password else secret,
                identity=new_email,
                data=dict(code=vcode),
                level=ValidationLevel.IDENTITY.value,
                type=ValidationType.EMAIL.value,
                deviceID=self.device
            ),
            oldValidationContext=dict(
                identity=self.account.email,
                level=ValidationLevel.IDENTITY.value,
                data=dict(code=vcode),
                type=ValidationType.EMAIL.value,
                deviceID=self.device
            )
        ))

    async def update_phone(self, phone: str, vcode: str, password: str, secret: str):
        return await self.http.post('auth/update-phone-number', dict(
            newValidationContext=dict(
                secret=f'0 {password}' if password else secret,
                identity=phone,
                data=dict(code=vcode),
                level=ValidationLevel.IDENTITY.value,
                type=ValidationType.GLOBAL_SMS.value,
                deviceID=self.device
            ),
            oldValidationContext=dict(
                identity=self.account.phone,
                data=dict(code=vcode),
                level=ValidationLevel.IDENTITY.value,
                type=ValidationType.GLOBAL_SMS.value,
                deviceID=self.device
            )
        ))

    async def delete_account(self, password: Optional[str] = None, secret: Optional[str] = None):
        return await self.http.post('account/delete-request', dict(secret=f'0 {password}' if password else secret))

    async def edit_profile(self, nickname: str = None, bio: str = None, medias: utils.MediaList = None):
        ...

    async def get_bussiness_history(self):
        return await self.http.get('wallet/business-coin/history')

    async def watch_ads(self):
        return await self.http.post('wallet/ads/video/start', dict(canWatchVideo=True))

    async def coupon(self):
        return await self.http.get('coupon/new-user-coupon')

    async def get_latest_payment(self):
        # com.narvii.wallet.j1.java (onStart)
        return await self.http.get('membership/latest-payment-context')

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

    async def pre_subscribe(self):
        # com.narvii.wallet.j1.java
        return await self.http.post('membership/product/pre-subscribe', dict(
            sku='purchase.skus',
            packageName=None,
            paymentType=PaymentType.ANDROID_SUBSCRIPTION.value
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

    async def fetch_topic_header(self, id: int, cid: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get(f'topic/{id}/metadata', params=params, cid=cid)

    async def fetch_community_collection_view(self, cid: int):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('community-collection/view', params=params, scopeCid=cid)


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

    async def fetch_story(self, q: str, cid: int = 0):
        return await self.http.get('feed/story', dict(q=q, timezone=self.timezone), cid=cid)


    async def recommend_story(self, cid: int):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/0/feed/story', params=params, cid=cid)

    async def fetch_bookmark_topics(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/persona/bookmarked-topics')

    async def fetch_topic_static(self, id: int, cid: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get(f'topic/{id}/feed/story/explore', params=params, cid=cid)

    async def fetch_topic_latest(self, id: int, cid: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get(f'topic/{id}/feed/story/latest', params=params, cid=cid)

    async def fetch_topic_popular(self, cid: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/popular', params=params, cid=cid)

    async def fetch_topic_popular_v2(self, cid: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/topic/.*/feed/story', params=params, cid=cid)

    async def fetch_topic_recommend(self, cid: int = 0):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('topic/.*/feed/story/recommendation', params=params, cid=cid)

    async def fetch_community_collection_com(self):
        params: dict = dict(timezone=self.timezone)
        return await self.http.get('/community-collection/.*/communities', params=params)

    async def fetch_featured_topic(self, cid: int = 0):
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
