from typing import Any, Optional,  Union, Protocol
from ..amino import Amino
from ..acm import ACM
from .abc import (
    ABCAminoBot,
    ABCBot,
    ABCManagerBot
)

from .context import *
from .handler import *
import asyncio

__all__ = (
    'AminoBot',
    'Bot',
    'ManagerBot',
    'InternBot'
)


DEFAULT_NAME = 'amino-bot'
DEFAULT_DESCRIPTION = 'Community Bot'
DEFAULT_PREFIX = '!'


class Base(Protocol):
    def __init__(self) -> None:
        ...

    async def event(self):
        ...


class ManagerBot(ABCManagerBot, ACM):
    """
    + ACM Support
    - Master Support
    
    Require basic privileges of client.
    """


class AminoBot(ABCAminoBot, Amino):
    """
    - ACM Support
    + Master Support

    Require staff privileges of client
    """


class Bot(ABCBot, AminoBot, ManagerBot):
    """
    + ACM Support
    + Master Support
    """

    def __init__(
        self,
        name: str = DEFAULT_NAME,
        description: str = DEFAULT_DESCRIPTION,
        prefix: str = DEFAULT_DESCRIPTION,
        **options: Any
    ):
        super(Amino, self).__init__(**options)
        self.info = dict()
        self.name = name
        self.description = description
        self.prefix = prefix

    def command(self, *aliases: str, expire_time: Optional[Union[float, int]] = None):
        def inner(callback, condition=None, error=None):
            return Command(*aliases, expire_time=expire_time, callback=callback, condition=condition, error=error)
        return inner

    def event(self, code: str):
        ...

    async def start(self, email=None, password=None, sid=None):
        print('starting...')
        print('closing...')
        

    def run(self, *args, **kwargs):
        asyncio.run(self.start(*args, **kwargs))


class InternBot:
    """
    + ACM Support
    + Master Support
    + Intern Support
    """

    def __init__(self) -> None:
        raise NotImplementedError
