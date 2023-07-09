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
from types import MappingProxyType
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    Iterable,
    TypeVar,
    Optional,
    Union,
    TYPE_CHECKING
)
import asyncio

from .abc import ABCBot
from .command import Answer, Command
from ..amino import Amino

__all__ = ('Bot',)

C = TypeVar('C', bound=Command)
A = TypeVar('A', bound=Answer)

DEFAULT_NAME = 'bot'
DEFAULT_DESCRIPTION = 'Community Bot'
DEFAULT_PREFIX = '/'


class Bot(ABCBot):
    """Class to create a basic bot in amino, require basic privileges of client.

    Privileges
    ----------
    - ACM Support: `false`
    - Master Support: `true`

    Parameters
    ----------
    name : `str` | `None`
        The name of the bot
    description: `str` | `None`
        The bot info, what it is, reason, contact, creator, etc.
    prefix : `str`
        The command prefix must contain between 1 and 3 characters, the valid characters are `A-Z`, `a-z`, `!$-/?.` (default is `/`)

    """

    def __init__(
        self,
        name: str = DEFAULT_NAME,
        description: str = DEFAULT_DESCRIPTION,
        prefix: str = DEFAULT_DESCRIPTION,
        **options
    ):
        if not isinstance(name, str):
            raise TypeError('name argument must be a string, not %r.' % type(name).__qualname__)
        if not isinstance(description, str):
            raise TypeError('description argument must be a string, not %r.' % type(description).__qualname__)
        if not isinstance(prefix, str):
            raise TypeError('prefix argument argument must be a string, not %r.' % type(prefix).__qualname__)
        self.name = name
        self.description = description
        self.prefix = prefix

    def __getstate__(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'prefix': self.prefix
            #**super(Amino, self).__getstate__()
        }

    def __setstate__(self, state: dict) -> None:
        self.name = state.pop('name', DEFAULT_NAME)
        self.description = state.pop('description', DEFAULT_DESCRIPTION)
        self.prefix = state.pop('prefix', DEFAULT_PREFIX)
        #super(Amino, self).__setstate__(state)

    @property
    def commands(self) -> MappingProxyType[str, Command]:
        if not TYPE_CHECKING and not hasattr(self, '_commands'):
            self._commands = {}
        return MappingProxyType(getattr(self, '_commands'))

    def add_command(self, command: Command) -> None:
        if not isinstance(command, Command):
            raise TypeError('command must be a Command object, not %r' % type(command).__name__)
        if command.id in self.commands:
            raise ValueError('The %r command is already exists.' % command.name)
        if not TYPE_CHECKING:
            self._commands[command.id] = command
        return command

    def command(
        self,
        name: str,
        *aliases: str,
        answers: Iterable[Answer] = [],
        conditions: Iterable[Callable[..., Coroutine[Any, Any, bool]]] = [],
        errors: Dict[Exception, Callable[..., Coroutine]] = {}
    ) -> Callable[[Callable[..., Coroutine]], Command]:
        def inner(callback: Callable[..., Coroutine]) -> Command:
            command = Command(
                name=name,
                callback=callback,
                aliases=aliases,
                answers=answers,
                conditions=conditions,
                errors=errors
            )
            self.add_command(command)
            return command
        return inner

    def event(self, code: str): pass

    async def start(self, email=None, password=None, sid=None):
        print('starting...')
        print('closing...')

    def run(self, *args, **kwargs):
        asyncio.run(self.start(*args, **kwargs))
