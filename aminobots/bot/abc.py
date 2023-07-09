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
from abc import ABC, abstractproperty, abstractmethod
from typing import Any, Iterable, TYPE_CHECKING

__all__ = ('ABCAnswer', 'ABCBot', 'ABCCommand')


class ABCBot(ABC):
    __slots__ = ()

    @abstractmethod
    def __getstate__(self) -> dict:
        ...

    @abstractmethod
    def __setstate__(self, state: dict) -> None:
        ...

    def __dir__(self) -> Iterable[str]:
        return [attr for attr in object.__dir__(self) if attr.startswith('__') or not attr.startswith('_')]

    @property
    def name(self) -> Any:
        """The bot name"""
        return getattr(self, '_name', None)

    @name.setter
    def name(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError('Bot name must be a string, not %r' % type(value).__name__)
        if not TYPE_CHECKING:
            self._name = value

    @property
    def description(self) -> Any:
        """The bot description"""
        return getattr(self, '_description', None)

    @description.setter
    def description(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError('Bot description must be a string, not %r' % type(value).__name__)
        if not TYPE_CHECKING:
            self._description = value

    @property
    def prefix(self) -> Any:
        """Bot command prefix"""
        return getattr(self, '_prefix', None)

    @prefix.setter
    def prefix(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError('Command prefix must be a string, not %r' % type(value).__name__)
        if not TYPE_CHECKING:
            self._prefix = value

    @abstractproperty
    def commands(self) -> Any:
        """Bot commands"""


class ABCCommand(ABC):
    def __dir__(self) -> Iterable[str]:
        return [attr for attr in object.__dir__(self) if attr.startswith('__') or not attr.startswith('_')]

    @abstractproperty
    def id(self) -> Any:
        """Command ID"""

    @abstractproperty
    def name(self) -> Any:
        """Command name"""

    @name.setter
    @abstractmethod
    def name(self, value) -> None:
        ...

    @abstractproperty
    def aliases(self) -> Any:
        """Command aliases."""

    @abstractproperty
    def answers(self) -> Any:
        """Command answers"""

    @abstractproperty
    def callback(self) -> Any:
        """Command function"""

    @callback.setter
    @abstractmethod
    def callback(self, value) -> None:
        ...

    @abstractproperty
    def conditions(self) -> Any:
        """Command conditions"""

    @abstractproperty
    def errors(self) -> Any:
        """Command error callbacks"""

    @abstractmethod
    def keys(self) -> Any:
        """Command call keys"""

    @abstractmethod
    def answer_keys(self) -> Any:
        """Command answer keys"""

    @abstractmethod
    def answer(
        self,
        name: Any,
        *aliases: Any,
        answers: Any,
        conditions: Any,
        errors: Any
    ) -> Any:
        """Create an answer command

        Parameters
        ----------
        name : `str`
            The answer call key.
        *aliases : `str`
            Others call keys (Packing argument)
        answers : `Iterable[str]`
            Iterable object of Answer objects
        conditions : `Iterable[Callable]`
            Iterable object of coroutine-functions
        errors : `dict[Exception, Callable]`

        """

    @abstractmethod
    def error(self, error: Any) -> Any:
        """Set the error event

        Parameters
        ----------
        error : `AminoException` | `Exception` | `Callable`
            The exception class or cororutine-function

        """

    @abstractmethod
    def add_alias(self, alias: Any) -> None:
        """Add new alias"""

    @abstractmethod
    def add_answer(self, answer: Any) -> None:
        """Add a new answer command"""

    @abstractmethod
    def add_condition(self, condition: Any) -> None:
        """Add a command condition"""

    @abstractmethod
    def add_error(self, error: Any, callback: Any) -> None:
        """Add an exception event

        Parameters
        ----------
        error : `AminoException` | `Exception`
            The specific exception
        callback : `Callable`
            The coroutine-function

        """

    @abstractmethod
    async def invoke(self, ctx: Any) -> None:
        """Call the event"""


class ABCAnswer(ABCCommand):
    @abstractproperty
    def root(self) -> Any:
        """Answer root"""

    @abstractproperty
    def timeout(self):
        """Answer command timeout"""
