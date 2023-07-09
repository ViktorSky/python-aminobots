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
from collections.abc import Iterable
import typing_extensions
import urllib.request
import urllib.parse
import dataclasses
import functools
import datetime
import typing
import ujson
import enum
import re

from . import utils

__all__ = (
    'YouTube',
)


class YTError:
    UNKNOWN = 2
    NOT_AVALIBLE = 14 # Content not available
    NO_STREAM = 15 # Could not get any stream
    NO_WEBSITE = 16 # Could not parse website
    RECAPTCHA = 17 # Re-Captcha
    NPE = 18 # Error NPE


# com.narvii.youtube.j
RESS = {"720p", "360p", "240p"}
DOWNLOAD_RESS = {"1080p", "720p", "480p", "360p", "240p"}
THUMBNAIL_RESS = {"720p", "360p", "240p", "144p"}
# headers
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"

DOMAINS = ['youtube.com', 'youtu.be', 'm.youtube.com']
YOUTUBE_DOMAIN = "youtube.com"
YOUTUBE_RESTRICTED_MODE_COOKIE = "PREF=f2=8000000"
YOUTUBE_RESTRICTED_MODE_COOKIE_KEY = "youtube_restricted_mode_key"
KEY = "AIzaSyD5IESlV65OGvVmDDmFvrCyHWMGzTUYXAI"
TIMEOUT = 30

REGEX_VIDEO_ID = re.compile('[A-Za-z0-9_-]{11}')
REGEX_QUERY = re.compile('((?:[A-z0-9._-~+%]+)=(?:[A-z0-9._-~+%]+))')

REGEX_YOUTUBE_LINK = re.compile('(http[s]?://(?:youtu.be|(?:(?:www.|m.)?youtube.com))/(?:(?:embed|watch)(?:[?v=/]+))?[A-Za-z0-9_-]{11})')
REGEX_AMINO_YT_LINK = re.compile('ytv://[A-Za-z0-9_-]{11}')
REGEX_LINK = re.compile('((?:(?:http[s]?://(?:youtu.be|(?:(?:www.|m.)+?youtube.com))/(?:(?:embed|watch)(?:[?v=/]+))?)|ytv://)[A-Za-z0-9_-]{11})')
# youtube links
REGEX_TIME = re.compile('t=((?:[0-9]+))')
REGEX_TIME_QUOTE = re.compile('t=(?:[0-9]+)')
REGEX_APP = re.compile('app=((?:[A-z]+))')
REGEX_APP_QUERY = re.compile('app=(?:[A-z]+)')
REGEX_FEATURE = re.compile('feature=((?:[A-z.]+))')
REGEX_FEATURE_QUERY = re.compile('feature=(?:[A-z.]+)')
REGEX_DISPLAY = re.compile('display=((?:[A-z]+))')
REGEX_DISPLAY_QUERY = re.compile('display=(?:[A-z]+)')
# embed links
REGEX_EMBED_TIME = re.compile('(?:amp;)?start=([0-9]+)')
REGEX_EMBED_TIME_QUERY = re.compile('(?:amp;)?start=[0-9]+')
REGEX_EMBED_CONTROL = re.compile('controls=([0]+)')
REGEX_EMBED_CONTROL_QUERY = re.compile('controls=[0]+')


class YTVideo:
    # com.narvii.youtube.i
    averageBitrate: int = -1
    mimeType: str
    resolution: str
    type: int
    url: str


@dataclasses.dataclass(repr=False, frozen=True)
class Result:
    json: dict

    @functools.cached_property
    def videoIds(self) -> typing.List[str]:
        ...



class YTLink:
    __slots__ = ('val', '__dict__')

    @property
    def raw(self) -> str:
        return self.val

    class App(enum.Enum):
        DESKTOP = 'desktop'
        MOBILE = 'mobile'

    class Display(enum.Enum):
        POPUP = 'popup'

    class Feature(enum.Enum):
        SHARE = 'share'
        YOUTU_BE = 'youtu.be'

    def __repr__(self) -> str:
        params = dict()
        if self.time:
            params['t'] = self.time
        return utils.build_url(f'https://www.youtube.com/watch?v={self.videoId}', **params)

    def __dir__(self) -> Iterable[str]:
        return set(object.__dir__(self)) - {'val', '__slots__'}

    def __new__(cls, link: str) -> typing_extensions.Self:
        self = super().__new__(cls)
        if not typing.TYPE_CHECKING:
            self.val = link
        return self

    @functools.cached_property
    def videoId(self) -> str:
        result = REGEX_VIDEO_ID.search(self.raw)
        return '' if not result else result.group()

    @functools.cached_property
    def embed(self) -> str:
        params = dict()
        if self.time:
            params['start'] = self.time
        return utils.build_url(f'https://www.youtube.com/embed/{self.videoId}', **params)

    @functools.cached_property
    def embed_ep(self) -> str:
        """Embed with enchanced privacy mode."""
        params = dict()
        if self.time:
            params['start'] = self.time
        return utils.build_url(f'https://www.youtube-nocookie.com/embed/{self.videoId}', **params)

    @functools.cached_property
    def time(self) -> typing.Optional[int]:
        result = REGEX_TIME.search(self.raw) or REGEX_EMBED_TIME.search(self.raw)
        return result if not result else int(result.group())

    @functools.cached_property
    def app(self) -> typing.Optional[str]:
        result = REGEX_APP.search(self.raw)
        return result if not result else result.group()

    @functools.cached_property
    def feature(self) -> typing.Optional[str]:
        result = REGEX_FEATURE.search(self.raw)
        return result if not result else result.group()

    @functools.cached_property
    def display(self) -> typing.Optional[str]:
        result = REGEX_DISPLAY.search(self.raw)
        return result if not result else result.group()

    @utils.typechecker
    def with_embed(
        self,
        title: str = 'YouTube video player',
        width: int = 560,
        height: int = 315,
        ep: bool = False,
        controls: bool = True,
        frameborder: bool = False
    ) -> str:
        """Embed video maker

        Parameters
        ----------
        title : :class:`str`
            Title for the embed video.
        width : :class:`int`
            Width size for the frameborder. (html)
        height : :class:`int`
            Height size for the frameborder. (html)
        ep : :class:`bool`
            Enable privacy enhanced mode. (cookie)
        controls : :class:`bool`
            Show player controls.
        frameborder : :class:`bool`
            Show player frameborder.

        """
        return  '<iframe ' + ' '.join(f'{k}="{v}"' for k,v in dict(
            title=title, width=width, height=height, frameborder=frameborder.real,
            src=utils.build_url(self.embed_ep if ep else self.embed, controls=controls.real),
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        ).items()) + ' allowfullscreen></iframe>'

    @utils.typechecker
    def with_time(self, time: datetime.timedelta, /) -> typing_extensions.Self:
        """Add start time to video.

        Parameters
        ----------
        time : :class:`timedelta`
            The start time of the video.

        Examples
        --------
        ```
        >>> url = link.with_time(datetime.timedelta(seconds=24))
        ```

        """
        seconds = int(time.total_seconds())
        if time.total_seconds() < 0:
            raise ValueError('The time must be possitive.')
        return type(self)(utils.build_url(self.raw, t=seconds))

    @utils.typechecker
    def with_app(self, app: App, /) -> typing_extensions.Self:
        return type(self)(utils.build_url(self.raw, app=app.value))

    @utils.typechecker
    def with_feature(self, feature: Feature, /) -> typing_extensions.Self:
        return type(self)(utils.build_url(self.raw, feature=feature.value))

    @utils.typechecker
    def with_display(self, display: Display, /) -> typing_extensions.Self:
        return type(self)(utils.build_url(self.raw, display=display.value))


class YouTube:
    ndcId: int
    objectId: str
    objectType: int
    videoId: str
    eventOrigin: str

    errorCode: int
    message: str

    def __repr__(self) -> str:
        return "ytv://" + self.videoId

    def headers(self):
        return {
            'User-Agent': USER_AGENT,
            'Accept-Language': 'en-GB;q=0.9',
            'Cookie': self.url
        }

    @property
    def url(self) -> str:
        return 'https://www.youtube.com/watch?v=' + self.videoId

    @staticmethod
    def image(videoId: str, /) -> str:
        return "http://i.ytimg.com/vi/" + videoId + "/default.jpg"

    @staticmethod
    def image_hd(videoId: str) -> str:
        return "http://i.ytimg.com/vi/" + videoId + "/hqdefault.jpg"

    def search(self, q: str) -> dict:
        query = urllib.parse.quote(q).replace('%20', '+')
        url = "https://www.youtube.com/results?search_query=" + query + "&page=&utm_source=opensearch"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Accept": "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US"
        }
        text = urllib.request.urlopen(urllib.request.Request(url, None, headers)).read().decode('utf-8')
        return ujson.loads(re.findall(r'({"responseContext".+[^"]*});(?:[\r\n ]+)?</script>', text, re.DOTALL)[0])

    def todict(self):
        return {
            "videoId": self.videoId,
            "parserVersion": 11,
            "code": self.errorCode,
            "message": self.message,
            "ndcId": self.ndcId,
            "objectId": self.objectId,
            "objectType": self.objectType,
            "eventOrigin": self.eventOrigin
        }

    #def api(self, videoId):
    #    "https://www.googleapis.com/youtube/v3/videos?id=" + videoId + "&key=" + n() + "&part=snippet,contentDetails"
