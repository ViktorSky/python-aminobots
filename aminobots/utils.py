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
import typing_extensions
import collections.abc
import urllib.parse
import dataclasses
import functools
import warnings
import datetime
import inspect
import hashlib
import typing
import base64
import ujson
import hmac
import time
import re
import os

from . import enums


__all__ = (
    'active_time',
    'build_url',
    'copy_doc',
    'copy_all_docs',
    'Device',
    'device_gen',
    'find_urls',
    'Link',
    'match_arguments',
    'Media',
    'MediaList',
    'MISSING',
    'parse_annotations',
    'parse_time',
    'SID',
    'signature',
    'suppress',
    'typechecker',
)

PREFIX = '19'
DEVKEY = 'E7309ECC0953C6FA60005B2765F99DBBC965C8E9'
SIGKEY = 'DFA5ED192DDA6E88A12FE12130DC6206B1251E44'

FMT_TIME = '%Y-%m-%dT%H:%M:%SZ'


if not typing.TYPE_CHECKING:
    class _Missing:
        __slots__ = ()

        def __eq__(self, o: object) -> bool:
            return False

        def __bool__(self) -> bool:
            return False

        def __repr__(self) -> str:
            return '...'

        def __hash__(self) -> int:
            return 0
    MISSING = _Missing()
else:
    MISSING: typing.Any = object()


def itersplit(array: collections.abc.Sequence, groups: int) -> typing.List[collections.abc.Sequence]:
    """Split iterables into a specific number of groups.

    Examples
    --------
    ```
    >>> my_list = tuple(range(17))
    >>> itersplit(my_list, groups=5)
    [(0, 5, 10, 15), (1, 6, 11, 16), (2, 7, 12), (3, 8, 13), (4, 9, 14)]
    ```
    """
    return [array[i::groups] for i in range(groups)]


@typing.overload
def parse_time(timestamp: None, /) -> None:
    ...

@typing.overload
def parse_time(timestamp: str, /) -> datetime.datetime:
    ...

@typing.overload
def parse_time(timestamp: typing.Optional[str], /) -> typing.Optional[datetime.datetime]:
    ...

def parse_time(timestamp: typing.Optional[str], /) -> typing.Optional[datetime.datetime]:
    """Convert API timestamp string to :class:`datetime.datetime` object."""
    if isinstance(timestamp, str) and timestamp:
        return datetime.datetime.strptime(timestamp, FMT_TIME)


class suppress:
    """Basic contextlib.suppress compatible with async/await"""

    __slots__ = ('exc_type', '__dict__')

    def __init__(self, exc_type) -> None:
        if not typing.TYPE_CHECKING:
            self.exc_type = exc_type

    def __enter__(self) -> None:
        pass

    async def __aenter__(self) -> None:
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exc_type is exc_type \
            or issubclass(exc_type, self.exc_type)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self.exc_type is exc_type \
            or issubclass(exc_type, self.exc_type)


class SID(str):
    """Represents the session ID of the user.

    Parameters
    ----------
    sid : :class:`str`
        The user sid string.

    Attributes
    ----------
    version : int
    key : str
    ip_address
    objectId
    objectType
    prefix: str
    timestamp
    clientType

    """

    json: dict
    key: str
    prefix: str
    version: int
    null: typing.Any
    objectId: str
    objectType = int
    ip_address: str
    timestamp: int
    clientType: int

    def __new__(cls, sid: str, /):
        try:
            decoded: bytes = base64.urlsafe_b64decode(
                sid + "=" * (4 - len(sid) % 4)
            )
            data: dict = ujson.loads(decoded[1:-20].decode("utf-8"))
        except (TypeError, UnicodeDecodeError, ujson.JSONDecodeError) as exc:
            raise ValueError('invalid sid.') from exc
        else:
            self = str.__new__(cls, sid)
        self.json = data
        self.key = decoded[-20:].hex()
        self.prefix = decoded[:2].hex()
        self.version = self.json['0']
        self.null = self.json['1']
        self.objectId = self.json['2']
        self.objectType = self.json['3']
        self.ip_address = self.json['4']
        self.timestamp = self.json['5']
        self.clientType = self.json['6']
        return self


class Device(str):
    """Represents an Amino Device.

    Parameters
    ----------
    device : :class:`str`
        The Amino device string.

    Attributes
    ----------
    id : `bytes`
        The device ID in bytes.

    """

    def __new__(cls, device: typing.Union[str, typing_extensions.Self], /) -> typing_extensions.Self:
        if isinstance(device, Device):
            return device
        elif not isinstance(device, str):
            raise TypeError('device must be a integer not %r' % type(device).__name__)
        elif len(device) != 82:
            raise ValueError('Invalid device.')
        try:
            bytes.fromhex(device) # type ignore
        except Exception:
            raise ValueError('invalid device.')
        return str.__new__(cls, device.upper())

    @functools.cached_property
    def id(self) -> bytes:
        """device identifier."""
        return bytes.fromhex(self)[1:21]


@typing.overload
def device_gen(id: None) -> Device:
    ...

@typing.overload
def device_gen(id: bytes) -> Device:
    ...

@typing.overload
def device_gen(id: typing.Optional[bytes]) -> Device:
    ...

def device_gen(id: typing.Optional[bytes] = None) -> Device:
    """Generate an Amino device.

    Parameters
    ----------
    id : `bytes` | `None`
        The device ID in bytes.

    """
    info: bytes = bytes.fromhex(PREFIX) + (id or os.urandom(20))
    device: bytes = info + hmac.new(
        bytes.fromhex(DEVKEY),
        info, hashlib.sha1
    ).digest()
    return Device(device.hex())


def update_device(device: typing.Union[str, Device], /) -> Device:
    return device_gen(bytes.fromhex(device)[1:21])


def signature(data: str) -> str:
    """Amino signature generator.

    Parameters
    ----------
    data : :class:`str`
        The data to encode.

    """
    info: bytes = data.encode("utf-8")
    return base64.b64encode(
        bytes.fromhex(PREFIX) + hmac.new(
            bytes.fromhex(SIGKEY),
            info, hashlib.sha1
        ).digest()
    ).decode("utf-8")


def build_url(path: str, *, fragment: typing.Optional[str] = None, **params: typing.Any) -> str:
    base = urllib.parse.urlparse(path)
    query = urllib.parse.urlencode(dict(urllib.parse.parse_qsl(base.query), **params), quote_via=urllib.parse.quote_plus)
    return urllib.parse.urlunparse([
        base.scheme, base.netloc, base.path,
        base.params, query, base.fragment
    ])


def parse_annotations(func) -> typing.Dict[str, type]:
    function = inspect.signature(func)
    annotations: typing.Dict[str, type] = {}
    for name, parameter in function.parameters.items():
        annotations[name] = parameter.annotation if parameter.annotation is not parameter.empty else MISSING
    return annotations


def match_arguments(func, *args, **kwargs) -> typing.OrderedDict[str, typing.Any]:
    arguments = inspect.signature(func).bind(*args, **kwargs)
    arguments.apply_defaults()
    return arguments.arguments


def typechecker(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        annotations = parse_annotations(func)
        arguments = match_arguments(func, *args, **kwargs)
        for name, value in arguments.items():
            if annotations[name] is MISSING:
                continue
            if not isinstance(value, annotations[name]):
                raise TypeError('%r argument must be %r type not %r.' % (name, annotations[name].__qualname__, type(value).__name__))
        return func(*args, **kwargs)
    inner.__doc__ = func.__doc__
    inner.__signature__ = inspect.signature(func)
    return inner


def deprecated(instead: typing.Optional[str] = None) -> typing.Callable[[typing.Callable], typing.Callable]:
    """Set deprecated functions without altering operation by decoration."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)  # turn off filter
            if instead:
                fmt = "{0.__name__} is deprecated, use {1} instead."
            else:
                fmt = '{0.__name__} is deprecated.'
            warnings.warn(fmt.format(func, instead), stacklevel=3, category=DeprecationWarning)
            warnings.simplefilter('default', DeprecationWarning)  # reset filter
            return func(*args, **kwargs)
        return wrapper
    return decorator



def copy_doc(original):
    """Copy docstring. (decorator)

    Parameters
    ----------
    original : :class:`Callable`
        Any object with docstring.
    
    Returns
    -------
    obj: Callable
        The object that changed the docstring.

    """
    def decorator(overridden):
        overridden.__doc__: str = original.__doc__
        overridden.__signature__ = inspect.signature(overridden)  # type ignore
        return overridden
    return decorator


def copy_all_docs(cls):
    """Decorator that copies docstrings from an abstract base class to a concrete class.

    This decorator copies the docstrings of all methods and properties from the
    abstract base class to the corresponding methods and properties in the concrete
    class. If a method or cached_property in the concrete class already has a docstring,
    it is not overwritten.

    Parameters
    ----------
    cls : :class:`type`
        The concrete class to be decorated.

    Returns
    -------
    type
        The decorated concrete class with copied docstrings.

    """
    for name, member in cls.__dict__.items():
        if not member.__doc__:
            for base in cls.__bases__:
                base_member = getattr(base, name, None)
                if base_member and base_member.__doc__:
                    member.__doc__ = base_member.__doc__
                    break
    return cls


def find_urls(text: str) -> typing.List[str]:
    url_pattern = re.compile(r'((http[s]?|ndc):\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    return [url[0] for url in re.findall(url_pattern, text)]


def active_time(seconds=0, minutes=0, hours=0) -> typing.List[typing.Dict[str, int]]:
    total = seconds + minutes*60 + hours*60*60
    return [
        {
            'start': int(time.time()),
            'end': int(time.time() + 300)
        } for _ in range(total // 300)
    ] + [
        {
            'start': int(time.time()),
            'end': int(time.time() + total % 300)
        }
    ]


@dataclasses.dataclass(unsafe_hash=True, frozen=True, slots=True)
class Link:
    """Represents a link for the content of posts, chat messages, etc.

    Examples
    --------
    ```
    >>> content = "Hello!, see your {}.".format(Link('ndc://user-me', 'profile'))
    >>> content
    'Hello!, see your [ndc://user-me|profile].'
    >>> blog = await amino.post_blog(communityId, input('Blog Title:'), content)
    ```

    Parameters
    ----------
    url : :class:`str`
        The link. (amino, ndc, external)
    alias : :class:`str` | `None`
        The alias link.

    """
    url: str = dataclasses.field(hash=True)
    alias: typing.Optional[str] = dataclasses.field(default=None, hash=True)

    def __str__(self) -> str:
        return f'[{self.url}|{self.alias}]' if self.alias else self.url

    def __post_init__(self) -> None:
        if not isinstance(self.url, str):
            raise TypeError('url argument must be a string, not %r.' % type(self.url).__name__)
        elif not isinstance(self.alias, typing.Optional[str]):
            raise TypeError('alias argument must be a string, not %r.' % type(self.alias).__name__)


@dataclasses.dataclass(unsafe_hash=True, frozen=True, slots=True)
class Media:
    """Represents a media upload for user bio, content of posts, etc.

    Examples
    --------
    ```
    >>> my_frame: Media = Media(MediaType.IMAGE, icon)
    >>> medias: MediaList = amino.user.medias
    >>> await amino.edit_profile(medias=MediaList(*medias, my_frame))
    ```

    """
    type: enums.MediaType = dataclasses.field(hash=False)
    url: str = dataclasses.field(hash=True)
    caption: typing.Optional[str] = dataclasses.field(default=None, hash=True)
    id: typing.Optional[str] = dataclasses.field(default=None, hash=True)

    def __str__(self) -> str:
        return f"[IMG={self.id}]" if self.id else self.url

    def __post_init__(self) -> None:
        if not isinstance(self.url, str):
            raise TypeError('url argument must be a string, not %r.' % type(self.url).__name__)
        elif not isinstance(self.caption, typing.Optional[str]):
            raise TypeError('caption argument must be a string, not %r.' % type(self.alias).__name__)
        elif not isinstance(self.type, enums.MediaType):
            raise TypeError('type argument must be a MediaType object not %r.' % type(self.type).__name__)
        elif self.type not in (enums.MediaType.IMAGE, enums.MediaType.YOUTUBE):
            raise ValueError('type argument must be IMAGE or YOUTUBE, not %r.' % self.type.name)
        elif not isinstance(self.id, typing.Optional[str]):
            raise TypeError('id argument must be a string not %r.' % type(self.id).__name__)
        elif isinstance(self.id, str):
            if len(self.id) != 3:
                raise ValueError('id argument must contain 3 characters, not %d.' % len(self.id))
            elif any(filter(lambda c: not (c.isalpha() and c.isupper()), self.id)):
                raise ValueError('id argument must have only uppercase ascii alphabetic characters.')

    @property
    def json(self) -> typing.Tuple[int, str, typing.Optional[str], typing.Optional[str]]:
        return [
            self.type.value,
            self.url,
            self.caption,
            self.id
        ]


@dataclasses.dataclass(init=False, unsafe_hash=True)
class MediaList:
    args: typing.Tuple[Media, ...] = dataclasses.field(hash=True)

    def __init__(self, *args: Media) -> None:
        unmatch = tuple(filter(lambda m: not isinstance(m, Media), args))
        if unmatch:
            raise ValueError('expected Media object, not %r.' % type(unmatch[0]).__name__)
        self.args = args

    def __iter__(self) -> typing.Iterator[Media]:
        return iter(self.args)

    def __len__(self) -> int:
        return len(self.args)

    @property
    def json(self) -> typing.List[typing.Tuple[int, str, typing.Optional[str], typing.Optional[str]]]:
        return [m.json for m in self.args]

    @property
    def types(self) -> typing.List[enums.MediaType]:
        return [m.type for m in self.args]

    @property
    def urls(self) -> typing.List[str]:
        return [m.url for m in self.args]

    @property
    def captions(self) -> typing.List[str]:
        return [m.caption for m in self.args]

    @property
    def ids(self) -> typing.List[str]:
        return [m.id for m in self.args]
