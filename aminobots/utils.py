from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Union
)
from collections.abc import Sequence
from hashlib import sha1
from base64 import b64encode, urlsafe_b64decode
from datetime import datetime
import ujson
import hmac
import re
import os

__all__ = (
    'copy_doc',
    'Date',
    'Device',
    'MISSING',
    'SID',
    'signature',
    'suppress',
    'find_url',
)

PREFIX: str = '19'
DEV_KEY = 'E7309ECC0953C6FA60005B2765F99DBBC965C8E9'
SIG_KEY = 'DFA5ED192DDA6E88A12FE12130DC6206B1251E44'


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


class Date:
    fmt = '%Y-%m-%dT%H:%M:%SZ'

    def __init__(self, timestamp: Optional[str] = None) -> None:
        if timestamp:
            self.dt = datetime.strptime(timestamp, self.fmt)
        else:
            self.dt = datetime.now()

    @property
    def year(self) -> int:
        return self.dt.year

    @property
    def month(self) -> int:
        return self.dt.month

    @property
    def day(self) -> int:
        return self.dt.day

    @property
    def hour(self) -> int:
        return self.dt.hour

    @property
    def minute(self) -> int:
        return self.dt.minute

    @property
    def second(self) -> int:
        return self.dt.second

    @property
    def time(self):
        return self.dt.time()

    @property
    def date(self):
        return self.dt.date()

    def __str__(self) -> str:
        return self.dt.strftime(self.fmt)

    def __repr__(self) -> str:
        return '{!s}({!r})'.format(self.__class__.__name__, str(self))


class Device(str):
    """Represent Amino Device

    Parameters
    ----------
    device: :class:`Optional[str]`
        Amino device.

    """
    def __new__(cls, device: Optional[str] = None):
        if device is None:
            device = cls.from_id(os.urandom(20))
        elif isinstance(device, str):
            device = cls.from_id(bytes.fromhex(device)[1:21])
        return str.__new__(cls, device.upper())

    @classmethod
    def from_id(cls, id: bytes) -> str:
        info: bytes = bytes.fromhex(PREFIX) + id
        device: bytes = info + hmac.new(
            bytes.fromhex(DEV_KEY),
            info, sha1
        ).digest()
        return device.hex()

    @property
    def id(self) -> bytes:
        """device identifier"""
        return bytes.fromhex(self)[1:21]


class SID(str):
    __slots__ = (
        'clientType',
        'ip_address',
        'key',
        'null',
        'objectId',
        'objectType',
        'prefix',
        'timestamp',
        'userId',
        'version'
    )
    
    def __new__(cls, sid: str):
        try:
            decoded: bytes = urlsafe_b64decode(
                sid + "=" * (4 - len(sid) % 4)
            )
            data: dict = ujson.loads(decoded[1:-20].decode("utf-8"))
        except (TypeError, UnicodeDecodeError, ujson.JSONDecodeError) as exc:
            raise ValueError('invalid sid.') from exc
        cls.version = data['0']
        cls.null = data['1'] # ? ndcId
        cls.objectId = data['2']
        cls.objectType = data['3']
        cls.ip_address = data['4']
        cls.timestamp = data['5']
        cls.clientType = data['6']
        cls.key = decoded[-20:].hex()
        cls.prefix = decoded[:2].hex()

        """cls.json = dict(
            version=data["0"],
            null=data["1"],  # ?
            userId=data["2"],
            objectType=data["3"],
            ip_address=data["4"],
            timestamp=data["5"],
            clientType=data["6"],
            sidKey=decoded[-20:].hex(),
            sidType=decoded[:2].hex(),
        )"""
        return str.__new__(cls, sid)

    """
    @classmethod
    def new(cls):
        ...

    @property
    def version(self) -> int:
        ...

    @property
    def objectId(self) -> str:
        ...

    @property
    def objectType(self) -> int:
        ...

    @property
    def ip_address(self) -> str:
        ...

    @property
    def timestamp(self):
        ...

    @property
    def clientType(self) -> int:
        ...

    @property
    def key(self) -> bytes:
        ...

    @property
    def prefix(self) -> bytes:
        ...
    """


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
            bytes.fromhex(SIG_KEY),
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


def find_url(text: str) -> set:
    patern = r"((https?|ndc):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)"
    urls = re.compile(patern, re.MULTILINE|re.UNICODE).findall(text)
    return set(url[0] for url in urls)
