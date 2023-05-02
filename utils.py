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
from dataclasses import dataclass, field
from typing_extensions import Self
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Final,
    Sequence,
    Tuple,
    Union
)
from collections.abc import Sequence
from hashlib import sha1
from base64 import b64encode, urlsafe_b64decode
from functools import cached_property
import datetime
import ujson
import hmac
import time
import re
import os

from . import enums


__all__ = (
    'active_time',
    'copy_doc',
    'copy_all_docs',
    'Date',
    'Device',
    'device_gen',
    'Media',
    'MediaList',
    'MISSING',
    'SID',
    'signature',
    'suppress',
    'find_urls',
)

PREFIX: Final[str] = '19'
DEVKEY: Final[str] = 'E7309ECC0953C6FA60005B2765F99DBBC965C8E9'
SIGKEY: Final[str] = 'DFA5ED192DDA6E88A12FE12130DC6206B1251E44'


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


MISSING: Any = _Missing()

def itersplit(array: Sequence[Any], count: int) -> List[Sequence[Any]]:
    """Split iterables

    Examples
    --------
    ```
    >>> my_list = tuple(range(17))
    >>> itersplit(my_list, count=5)
    [(0, 5, 10, 15), (1, 6, 11, 16), (2, 7, 12), (3, 8, 13), (4, 9, 14)]
    ```
    """
    return [array[i::count] for i in range(count)]


class Date(str):
    """Represent a Amino API date format.

    Parameters
    ----------
    timestamp : Optional[:class:`str`]
        The timestamp format string.

    Attributes
    ----------
    year : int
    month : int
    day : int
    hour : int
    minute : int
    second : int
    time
    date

    """
    fmt = '%Y-%m-%dT%H:%M:%SZ'

    def __init__(self, timestamp: Optional[str] = None) -> None:
        if timestamp:
            self.dt = datetime.datetime.strptime(timestamp, self.fmt)
        else:
            self.dt = datetime.datetime.now()

    def __new__(cls, timestamp: Optional[str] = None):
        return str.__new__(cls, timestamp)

    @cached_property
    def year(self) -> int:
        return self.dt.year

    @cached_property
    def month(self) -> int:
        return self.dt.month

    @cached_property
    def day(self) -> int:
        return self.dt.day

    @cached_property
    def hour(self) -> int:
        return self.dt.hour

    @cached_property
    def minute(self) -> int:
        return self.dt.minute

    @cached_property
    def second(self) -> int:
        return self.dt.second

    @cached_property
    def time(self) -> datetime.time:
        """To datetime.time"""
        return self.dt.time()

    @cached_property
    def date(self) -> datetime.date:
        """To datetime.date"""
        return self.dt.date()

    def __str__(self) -> str:
        return self.dt.strftime(self.fmt)

    def __repr__(self) -> str:
        return '{!s}({!r})'.format(self.__class__.__name__, str(self))


class Device(str):
    """Represents an Amino Device

    Parameters
    ----------
    device : :class:`str` | `None`
        Amino device.

    """
    def __new__(cls, device: Optional[str] = None) -> Self:
        if device is None:
            device = device_gen()
        elif isinstance(device, str):
            device = update_device(device)
        return str.__new__(cls, device.upper())

    @cached_property
    def id(self) -> bytes:
        """device identifier."""
        return bytes.fromhex(self)[1:21]


def device_gen(id: bytes = None) -> str:
    info: bytes = bytes.fromhex(PREFIX) + (id or os.urandom(20))
    device: bytes = info + hmac.new(
        bytes.fromhex(DEVKEY),
        info, sha1
    ).digest()
    return device.hex()


def update_device(device: Union[str, Device]) -> str:
    return device_gen(bytes.fromhex(device)[1:21])


class SID(str):
    """Represent the user sid.

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

    def __init__(self, sid: str) -> None:
        try:
            decoded: bytes = urlsafe_b64decode(
                sid + "=" * (4 - len(sid) % 4)
            )
            data: dict = ujson.loads(decoded[1:-20].decode("utf-8"))
        except (TypeError, UnicodeDecodeError, ujson.JSONDecodeError) as exc:
            raise ValueError('invalid sid.') from exc
        else:
            self.json: dict = data
            self.key = decoded[-20:].hex()
            self.prefix = decoded[:2].hex()

    def __new__(cls, sid: str):
        return str.__new__(cls, sid)

    @cached_property
    def version(self) -> int:
        return self.json['0']

    @cached_property
    def null(self):
        return self.json['1']

    @cached_property
    def objectId(self) -> str:
        return self.json['2']

    @cached_property
    def objectType(self) -> int:
        return self.json['3']

    @cached_property
    def ip_address(self) -> str:
        return self.json['4']

    @cached_property
    def timestamp(self) -> int:
        return self.json['5']

    @cached_property
    def clientType(self) -> int:
        return self.json['6']


class suppress:
    """Basic contextlib.suppress compatible with async/await"""

    __slots__ = ('exc_type',)

    def __init__(self, exc_type) -> None:
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


def signature(data: str) -> str:
    """Signature Generator.

    Parameters
    ----------
    data: str
        The data to encode.

    """
    return b64encode(
        bytes.fromhex(PREFIX) + hmac.new(
            bytes.fromhex(SIGKEY),
            data.encode("utf-8"),
            sha1
        ).digest()
    ).decode("utf-8")


def copy_doc(doc: Union[Callable, str]) -> Callable:
    """Copy docstring. (decorator)

    Parameters
    ----------
    doc: Union[str, Callable]
        the docstring or any object with docstring.
    
    Returns
    -------
    obj: Callable
        The object that changed the docstring.

    """
    def decorator(obj: Callable) -> Any:
        if not isinstance(doc, str):
            obj.__doc__: str = doc.__doc__
        else:
            obj.__doc__: str = str(doc)
        return obj
    return decorator

def copy_all_docs(cls):
    """Decorator that copies docstrings from an abstract base class to a concrete class.

    This decorator copies the docstrings of all methods and properties from the
    abstract base class to the corresponding methods and properties in the concrete
    class. If a method or cached_property in the concrete class already has a docstring,
    it is not overwritten.

    Parameters
    ----------
    cls : type
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

def find_urls(text: str) -> List[str]:
    url_pattern = re.compile(r'((http[s]?|ndc):\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    return [url[0] for url in re.findall(url_pattern, text)]


def active_time(seconds=0, minutes=0, hours=0) -> List[Dict[str, int]]:
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




@dataclass(unsafe_hash=True, frozen=True, slots=True)
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
    url: str = field(hash=True)
    alias: Optional[str] = field(default=None, hash=True)

    def __str__(self) -> str:
        return f'[{self.url}|{self.alias}]' if self.alias else self.url

    def __post_init__(self) -> None:
        if not isinstance(self.url, str):
            raise TypeError('url argument must be a string, not %r.' % type(self.url).__name__)
        elif not isinstance(self.alias, Optional[str]):
            raise TypeError('alias argument must be a string, not %r.' % type(self.alias).__name__)


@dataclass(unsafe_hash=True, frozen=True, slots=True)
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
    type: enums.MediaType = field(hash=False)
    url: str = field(hash=True)
    caption: Optional[str] = field(default=None, hash=True)
    id: Optional[str] = field(default=None, hash=True)

    def __str__(self) -> str:
        return f"[IMG={self.id}]" if self.id else self.url

    def __post_init__(self) -> None:
        if not isinstance(self.url, str):
            raise TypeError('url argument must be a string, not %r.' % type(self.url).__name__)
        elif not isinstance(self.caption, Optional[str]):
            raise TypeError('caption argument must be a string, not %r.' % type(self.alias).__name__)
        elif not isinstance(self.type, enums.MediaType):
            raise TypeError('type argument must be a MediaType object not %r.' % type(self.type).__name__)
        elif self.type not in (enums.MediaType.IMAGE, enums.MediaType.YOUTUBE):
            raise ValueError('type argument must be IMAGE or YOUTUBE, not %r.' % self.type.name)
        elif not isinstance(self.id, Optional[str]):
            raise TypeError('id argument must be a string not %r.' % type(self.id).__name__)
        elif isinstance(self.id, str):
            if len(self.id) != 3:
                raise ValueError('id argument must contain 3 characters, not %d.' % len(self.id))
            elif any(filter(lambda c: not (c.isalpha() and c.isupper()), self.id)):
                raise ValueError('id argument must have only uppercase ascii alphabetic characters.')

    @property
    def json(self) -> Tuple[int, str, Optional[str], Optional[str]]:
        return [
            self.type.value,
            self.url,
            self.caption,
            self.id
        ]


@dataclass(init=False, unsafe_hash=True)
class MediaList:
    args: Tuple[Media, ...] = field(hash=True)

    def __init__(self, *args: Media) -> None:
        unmatch = tuple(filter(lambda m: not isinstance(m, Media), args))
        if unmatch:
            raise ValueError('expected Media object, not %r.' % type(unmatch[0]).__name__)
        self.args = args

    def __iter__(self) -> Iterator[Media]:
        return iter(self.args)

    def __len__(self) -> int:
        return len(self.args)

    @property
    def json(self) -> List[Tuple[int, str, Optional[str], Optional[str]]]:
        return [m.json for m in self.args]

    @property
    def types(self) -> List[enums.MediaType]:
        return [m.type for m in self.args]

    @property
    def urls(self) -> List[str]:
        return [m.url for m in self.args]

    @property
    def captions(self) -> List[str]:
        return [m.caption for m in self.args]

    @property
    def ids(self) -> List[str]:
        return [m.id for m in self.args]
