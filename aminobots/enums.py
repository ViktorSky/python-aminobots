__all__ = (
    'Action',
    'AdsLevel',
    'AlertEvent',
    'ClientType',
    'ChatEvent',
    'ChatType',
    'CommentSort',
    'Connection',
    'ContentType',
    'Encoding',
    'Event',
    'EventType',
    'Gender',
    'Language',
    'Media',
    'MessageType',
    'Notice',
    'NoticeAction',
    'NoticePenaltyType',
    'NoticeStatus',
    'ObjectType',
    'PaymentType',
    'Role',
    'ValidationTarget',
    'VerifyType'
)

import enum
# AuthType


class Enum(enum.Enum):
    def __str__(self):
        """return str(self)"""
        return self.value

    def __int__(self) -> int:
        """return int(self)"""
        return int(self.value)

    def __eq__(self, other) -> bool:
        """return self == other"""
        if isinstance(other, enum.Enum):
            return self.value == other.value
        else:
            return self.value == other

    def __ne__(self, other):
        """return self != other"""
        if isinstance(other, enum.Enum):
            return self.value != other.value
        else:
            return self.value != other

    def __le__(self, other) -> bool:
        """return self <= other"""
        if isinstance(other, enum.Enum):
            return self.value <= other.value
        else:
            return self.value <= other

    def __lt__(self, other) -> bool:
        """return self < other"""
        if isinstance(other, enum.Enum):
            return self.value < other.value
        else:
            return self.value < other

    def __ge__(self, other) -> bool:
        """return self >= other"""
        if isinstance(other, enum.Enum):
            return self.value >= other.value
        else:
            return self.value >= other

    def __gt__(self, other):
        """return self > other"""
        if isinstance(other, enum.Enum):
            return self.value > other.value
        else:
            return self.value > other

    def __add__(self, other):
        """return self + other"""
        if isinstance(other, enum.Enum):
            return self.value + other.value
        else:
            return self.value + other

    def __and__(self, other):
        """return self & other"""
        if isinstance(other, enum.Enum):
            return self.value and other.value
        else:
            return self.value and other

    def __or__(self, other):
        """return self | other"""
        if isinstance(other, enum.Enum):
            return self.value or other.value
        else:
            return self.value or other

    def __float__(self) -> float:
        """return float(self)"""
        return float(self.value)


class Action(Enum):
    LIVE_CATEGORY_TOPIC_CHAT = "users-chatting-public"
    LIVE_CATEGORY_TYPE_LIVE_CHATTING = "users-live-chatting-public"


class AdsLevel(Enum):
    LEVEL_0 = 0
    LEVEL_1 = 1
    LEVEL_2 = 2


class ClientType(Enum):
    MASTER = 100
    STANDALONE = 101
    ACM = 200
    STORY_EDITOR = 201


class CommentSort(Enum):
    NEWEST = 0
    OLDEST = 1
    TOP = 2


class Connection(Enum):
    CLOSE: str = "Close"
    KEEP_ALIVE: str = "Keep-Alive"
    UPGRADE: str = "Upgrade"


class ChatType(Enum):
    PM = 0
    PRIVATE = 1
    PUBLIC = 2


class ContentType(Enum):
    AAC = "audio/aac"
    MP3 = "audio/mp3"
    MP4 = "video/mp4"
    GIF = "image/gif"
    JPG = "image/jpg"
    MOV = "video/mov"
    PNG = "image/png"
    JPEG = "image/jpeg"
    WEBP = "image/webp"

    CSS        = "text/css"
    PLAIN      = "text/plain"
    HTML       = "text/html"
    JAVASCRIPT = "text/javascript"

    BINARY     = "application/octet-stream"
    JSON       = "application/json; charset=utf-8"
    MULTIPART  = "multipart/form-data"
    TEXT       = "text/plain; charset=utf-8"
    URL_FORM   = "application/x-www-form-urlencoded; charset=utf-8"


class Encoding(Enum):
    BROTLI   = "br"
    CHUNKED  = "chunked"
    DEFLATE  = "deflate"
    COMPRESS = "compress"
    IDENTITY = "identity"
    GZIP     = "gzip"


class AlertEvent(Enum):
    pass


class ChatEvent(Enum):
    TEXT_MESSAGE                = "1000:0:0"
    IMAGE_MESSAGE               = "1000:0:100"
    YOUTUBE_MESSAGE             = "1000:0:103"
    AUDIO_MESSAGE               = "1000:2:110"
    STICKER_MESSAGE             = "1000:3:113"

    VOICE_CHAT_NOT_ANSWERED     = "1000:52:0"
    VOICE_CHAT_CANCELLED        = "1000:53:0"
    VOICE_CHAT_DECLINED         = "1000:54:0"
    VOICE_CHAT_START            = "1000:107:0"
    VOICE_CHAT_END              = "1000:110:0"

    LIVE_STREAM_NOT_ANSWERED    = "1000:55:0"
    LIVE_STREAM_CANCELLED       = "1000:56:0"
    LIVE_STREAM_DECLINED        = "1000:57:0"
    LIVE_STREAM_START           = "1000:108:0"
    LIVE_STREAM_END             = "1000:111:0"

    AVATAR_CHAT_NOT_ANSWERED    = "1000:58:0"
    AVATAR_CHAT_CANCELLED       = "1000:59:0"
    AVATAR_CHAT_DECLINED        = "1000:60:0"
    AVATAR_CHAT_START           = "1000:109:0"
    AVATAR_CHAT_END             = "1000:112:0"

    SCREENING_ROOM_START        = "1000:114:0"
    SCREENING_ROOM_END          = "1000:115:0"

    DELETE_MESSAGE              = "1000:100:0"
    MODERATOR_DELETE_MESSAGE    = "1000:119:0"

    JOIN_CHAT                   = "1000:101:0"
    LEAVE_CHAT                  = "1000:102:0"

    START_CHAT                  = "1000:103:0"  # PM, PUBLIC, PRIVATE

    CHAT_TIP                    = "1000:120:0"

    LIVE_OPEN_TO_EVERYONE       = "1000:122:0"
    LIVE_APPROVAL_REQUIRED      = "1000:123:0"
    LIVE_INVITE_ONLY            = "1000:124:0"


class Event(Enum):
    ALERT   = AlertEvent
    CHAT    = ChatEvent


class EventType(Enum):
    ALERT   = 10
    CHAT    = 1000


class Gender(Enum):
    UNKNOWN     = 0
    MALE        = 1
    FEMALE      = 2
    NON_BINARY  = 255


class Language(Enum):
    ARABIC                  = 'ar'      # العربية
    CATALAN                 = 'ca'      # Català
    SIMPLIFIED_CHINESE      = 'zh-Hans' # 中文 (简体)
    TRADITIONAL_CHINESE     = 'zh-Hant' # 中文 (繁體)
    CROATIAN                = 'hr'      # Hrvatski
    CZECH                   = 'cs'      # Čeština
    DANISH                  = 'da'      # Dansk
    DUTCH                   = 'nl'      # Nederlands\
    ENGLISH                 = 'en'      # English
    AUSTRALIA_ENGLISH       = 'en-AU'   # English
    CANADA_ENGLISH          = 'en-CA'   # English
    GREAT_BRITAIN_ENGLISH   = 'en-GB'   # English
    INDIA_ENGLISH           = 'en-IN'   # English
    MEXICO_ENGLISH          = 'en-MX'   # English
    FINNISH                 = 'fi'      # suomi
    FRENCH                  = 'fr'      # Français
    CANADA_FRENCH           = 'fr-CA'   # Français
    GERMAN                  = 'de'      # Deutsch
    GREEK                   = 'el'      # Ελληνικά
    HEBREW                  = 'he'      # עברית
    HINDI                   = 'hi'      # हिन्दी
    HUNGARIAN               = 'hu'      # Magyar
    INDONESIAN              = 'id'      # Bahasa Indonesia
    ITALIAN                 = 'it'      # Italiano
    JAPANESE                = 'ja'      # 日本語
    KOREAN                  = 'ko'      # 한국어
    MALAY                   = 'ms'      # Bahasa Melayu
    NORWEGIAN               = 'nb'      # Norsk (bokmål)
    POLISH                  = 'pl'      # Polski
    PORTUGUESE              = 'pt'      # Português
    BRAZIL_PORTUGUESE       = 'pt-BR'   # Português
    ROMANIAN                = 'ro'      # Română
    RUSSIAN                 = 'ru'      # Русский
    SLOVAK                  = 'sk'      # Slovenčina
    SPANISH                 = 'es'      # Español
    MEXICO_SPANISH          = 'es-MX'   # Español
    SWEDISH                 = 'sv'      # Svenska
    THAI                    = 'th'      # ไทย
    TURKISH                 = 'tr'      # Türkçe
    UKRAINIAN               = 'uk'      # Українська
    VIETNAMESE              = 'vi'      # Tiếng Việt


class Media(Enum):
    TEXT    = 0
    IMAGE   = 100
    YOUTUBE = 103
    AUDIO   = 110
    STICKER = 113


class MessageType(Enum):
    TEXT                        = 0
    AUDIO                       = 2
    STICKER                     = 3

    VOICE_CHAT_NOT_ANSWERED     = 52
    VOICE_CHAT_CANCELLED        = 53
    VOICE_CHAT_DECLINED         = 54
    VOICE_CHAT_START            = 107
    VOICE_CHAT_END              = 110

    LIVE_STREAM_NOT_ANSWERED    = 55
    LIVE_STREAM_CANCELLED       = 56
    LIVE_STREAM_DECLINED        = 57
    LIVE_STREAM_START           = 108
    LIVE_STREAM_END             = 111

    AVATAR_CHAT_NOT_ANSWERED    = 58
    AVATAR_CHAT_CANCELLED       = 59
    AVATAR_CHAT_DECLINED        = 60
    AVATAR_CHAT_START           = 109
    AVATAR_CHAT_END             = 112

    SCREENING_ROOM_START        = 114
    SCREENING_ROOM_END          = 115

    DELETE                      = 100
    MODERATOR_DELETE            = 119

    JOIN_CHAT                   = 101
    LEAVE_CHAT                  = 102

    START_CHAT                  = 103

    CHAT_TIP                    = 120

    LIVE_OPEN_TO_EVERYONE       = 122
    LIVE_APPROVAL_REQUIRED      = 123
    LIVE_INVITE_ONLY            = 124


class Notice(Enum):
    NONE                    = 0
    PROMOTE_LEADER          = 1
    PROMOTE_CURATOR         = 2
    TRANSFER_AGENT          = 3
    STRIKE_USER             = 4
    COPYRIGHT_TAKE_DOWN     = 5
    NOTICE_USER             = 6
    WARN_USER               = 7
    GLOBAL_NOTICE_USER      = 8
    GLOBAL_WARN_USER        = 9
    GLOBAL_STRIKE_USER      = 10
    GLOBAL_SYSTEM_MESSAGE   = 11


class NoticeAction(Enum):
    NONE    = 0
    YES     = 1
    NO      = 2


class NoticePenaltyType(Enum):
    MUTE = 1
    NONE = 0


class NoticeStatus(Enum):
    NONE        = 0
    PENDING     = 1
    ACCEPTED    = 2
    DECLINED    = 3


class ObjectType(Enum):
    USER                = 0
    BLOG = QUIZ         = 1
    WIKI                = 2
    COMMENT             = 3
    BLOG_CATEGORY       = 4
    WIKI_CATEGOTY       = 5
    FEATURED_WIKI       = 6
    CHAT_MESSAGE        = 7

    REPUTATION_LOG      = 10
    POLL_OPTION         = 11
    CHAT                = 12

    COMMUNITY           = 16

    IMAGE               = 100
    MUSIC               = 101
    VIDEO               = 102
    YOUTUBE             = 103

    SHARED_FOLDER       = 106

    SHARED_FOLDER_FILE  = 109
    VOICE               = 110
    MODERATION_TASK     = 111
    SCREENSHOT          = 112
    STICKER             = 113
    STICKER_COLLECTION  = 114
    PROP                = 115
    CHAT_BUBBLE         = 116
    VIDEO_FILTER        = 117
    ORDER               = 118
    SHARE_REQUEST       = 119

    VV_CHAT             = 120
    P2A                 = 121
    SUBSCRIPTION        = 122
    AMINO_VIDEO         = 123


class PaymentType(Enum):
    COIN                    = 1
    IOS_PURCHASE            = 2
    IOS_SUBSCRIPTION        = 3
    ANDROID_PURCHASE        = 4
    ANDROID_SUBSCRIPTION    = 5


class Role(Enum):
    MEMBER      = 0
    LEADER      = 100
    CURATOR     = 101
    USER_AGENT  = 102


class ValidationTarget(Enum):
    DIGITS      = 3
    EMAIL       = 1
    GLOBAL_SMS  = 8


class VerifyType(Enum):
    RESET_PASSWORD      = 1
    FORGOT_PASSWORD     = 2
    CHANGE_PASSWORD     = 3
    SIGNUP              = 4
    ADD_IDENTITY        = 5
    UPDATE_IDENTITY     = 6
    VERIFY_NEW_IDENTITY = 7
    DELETE_ACCOUNT      = 8
