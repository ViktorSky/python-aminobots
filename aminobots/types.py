from typing import TypeVar, Dict, Type, TYPE_CHECKING
from typing_extensions import Self
from datetime import datetime, timedelta
import re

T = TypeVar('T') # var
S = TypeVar('S') # var 2
T_co = TypeVar('T_co', covariant=True) # covariant var

ACTION_PURCHASED_SUB_CHANGED = "com.narvii.action.PURCHASED_SUB_CHANGED"
REMOTE_AMINO_PLUS_PRICING = "android_amino_plus_pricing"

# checkMembershipAndPaymentResult
RENEW_IN_MASTER = 51
RENEW_IN_STANDALONE = 52
RENEW_IN_ANOTHER_GOOGLE_PLAY_ACCOUNT = 53
RENEW_IN_APPSTORE = 54

TITLE_PATTERN = re.compile("\\d+")
FALSE_REGEX = re.compile("^(0|false|f|no|n|off|)$", 2)
TRUE_REGEX = re.compile("^(1|true|t|yes|y|on)$", 2)
UUID_PATTERN = re.compile("([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})")

# D:\Desktop\alan\amino.dex\full.dex\sources\com\narvii\util

def error(code):
    if code == -3:
        return "SERVICE_TIMEOUT"
    if code == -2:
        return "FEATURE_NOT_SUPPORTED"
    if code == -1:
        return "SERVICE_DISCONNECTED"
    if code == 0:
         return "OK"
    if code == 1:
         return "USER_CANCELED"
    if code == 2:
         return "SERVICE_UNAVAILABLE"
    if code == 3:
         return "BILLING_UNAVAILABLE"
    if code == 4:
         return "ITEM_UNAVAILABLE"
    if code == 5:
         return "DEVELOPER_ERROR"
    if code == 6:
         return "ERROR"
    if code == 7:
         return "ITEM_ALREADY_OWNED"
    if code == 8:
         return "ITEM_NOT_OWNED"

class Package:
    AMINO = 'com.narvii.amino.master'
    ACM = 'com.narvii.amino.master'
    PLAY_STORE = 'com.android.vending'

class IBaseProduct:
    badge: str
    canAutoRenew: bool
    description: str
    dollarPrice: float
    icon: str
    numberOfCoins: int
    numberOfMonths: int # * 31
    price: int
    savePercent: int
    skuList: str
    suggested: bool
    title: str


class PaidOut:
    amount: float
    coins: float
    createdTime: str
    currencyCode: str
    paymentAccount: str
    paymentMethod: int
    transactionId: str

# D:\Desktop\alan\amino.dex\full.dex\sources\com\narvii\wallet


def apiTypeName(i: int) -> str:
        if (i == 4):
            return "blog/category"
        if (i == 106):
            return "shared-folder/folders/"
        if (i == 109):
            return "shared-folder/files"
        if (i == 114):
            return "sticker-collection"
        if (i == 116):
            return "chat/chat-bubble"
        if (i == 122):
            return "avatar-frame"
        if (i == 128):
            return "topic"
        if (i == 131):
            return "announcement"
        if (i == 12):
            return "chat/thread"
        if (i == 13):
            return "item/category"
        if (i == 15):
            return "item/submission"
        if (i == 16):
            return "community"
        if (i == 17):
            return "community/collection"


def objectTypeName(i: int) -> str:
        if (i == 4):
            return "blog-category"
        if (i == 13):
            return "item-category"

def seconds_text(seconds: int) -> str:
    if seconds < 300:
        return 'just a moment ago'
    elif seconds < 3600:
        return '%d minutes ago' % (seconds // 60)
    elif seconds < 5400:
        return 'about an hour ago'
    elif seconds < 86400:
        return '%d hours ago' % ((seconds + 1800) // 3600)
    elif seconds < 172800: # 48 hours
        return '1 day ago'
    elif seconds < 2592000: # 30 days
        return '%d days ago' % ((seconds + 43200) // 86400)
    else:
        weeks, r = divmod(seconds, 60*60*24*7)
        
        days, r = divmod(r, 60*60*24)
        if not days:
            days = 1
        hours, r = divmod(r, 60*60)
        delta = timedelta(
            weeks=weeks,
            days=days,
            hours=hours
        )
        dt = datetime.now() - delta
        return dt.strftime('%B %d, %Y')

# D:\Desktop\alan\amino.dex\full.dex\sources\com\narvii\util


