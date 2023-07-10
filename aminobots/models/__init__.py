"""
aminobots.models
-----------------

Response models for the Amino API.

:copyright: (c) 2023 ViktorSky
:license: MIT, see LICENSE for more details.

"""
from typing import Any, Dict, Type,TypeVar
from .accountinfo import AccountInfo
from .allpushsettings import AllPushSettings
from .chatinfo import ChatInfo
from .chatmembers import ChatMembers
from .communityinfluencers import CommunityInfluencers
from .communityinfo import CommunityInfo
from .fromdevice import FromDevice
from .joinedchats import JoinedChats
from .joinedcommunities import JoinedCommunities
from .linkidentify import LinkIdentify
from .linkresolution import LinkResolution
from .login import Login
from .membershipconfig import MembershipConfig
from .membershipinfo import MembershipInfo
from .model import Model
from .pushnotification import PushNotification
from .searchchat import SearchChat
from .searchcommunity import SearchCommunity
from .searchquiz import SearchQuiz
from .searchuser import SearchUser
from .userinfo import UserInfo
from .verifypassword import VerifyPassword
from .walletads import WalletAds
from .wallethistory import WalletHistory
from .walletinfo import WalletInfo
from ..objects import Api as _Api

__all__ = (
    'AccountInfo',
    'AllPushSettings',
    'ChatInfo',
    'ChatMembers',
    'CommunityInfluencers',
    'CommunityInfo',
    'FromDevice',
    'JoinedChats',
    'JoinedCommunities',
    'LinkIdentify',
    'LinkResolution',
    'Login',
    'MembershipConfig',
    'MembershipInfo',
    'Model',
    'PushNotification',
    'SearchCommunity',
    'SearchQuiz',
    'SearchUser',
    'UserInfo',
    'VerifyPassword',
    'WalletAds',
    'WalletHistory',
    'WalletInfo',
    'parse_model'
)

M = TypeVar('M', bound=Model)

def parse_model(cls: Type[M], data: Dict[str, Any]) -> M:
    kwargs = {k: v for k, v in data.items() if not k.startswith('api:')}
    api_data = {k: v for k, v in data.items() if k.startswith('api:')}
    if api_data:
        kwargs.update(api=_Api(**api_data))
    return cls(**kwargs)
