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
from __future__ import annotations
from types import MappingProxyType
from typing_extensions import Self
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    TypeVar,
    Tuple,
    Union,
    Iterable,
    TYPE_CHECKING,
    cast,
    overload
)
from inspect import isclass, isfunction, iscoroutinefunction
from uuid import uuid1
import asyncio
from .abc import ABCAnswer, ABCCommand
from .context import Context
from ..enums import ChatType, Role
from ..errors import AminoException
from ..objects import Author, Thread, Sticker
from ..utils import copy_all_docs, parse_annotations, match_arguments, MISSING

__all__ = (
    'ANSWER_ANNOTATIONS',
    'COMMAND_ANNOTATIONS',
    'CONDITION_ANNOTATIONS',
    'Answer',
    'Command'
)
E = TypeVar('E', AminoException, Exception, covariant=True)


def validate_callback(value: Callable) -> None:
    if value is not None and not iscoroutinefunction(value):
        raise TypeError('callback must be a coroutine-funtion, not %r.'
            % value.__name__ if isclass(value) else type(value).__name__)


def validate_condition(value: Callable) -> None:
    if not iscoroutinefunction(value):
        raise TypeError('condition must be a coroutine-function, not %r' % type(value).__name__)
    annotations = parse_annotations(value, MISSING)
    if not annotations:
        raise ValueError('condition can not has empty parameters')
    for idx, (name, value) in enumerate(annotations.items()):
        if idx == 0 and value is not Context:
            raise ValueError('the first parameter must be a Context annotation, not %r' % value)
        if value is MISSING:
            continue
        if value not in CONDITION_ANNOTATIONS:
            correct = ', '.join(map(lambda x: x.__name__, CONDITION_ANNOTATIONS))
            raise ValueError('condition %r parameter has invalid annotation: %r, use (%s)' % (name, value.__name__, correct))


def validate_answer(value: Answer) -> None:
    if not isinstance(value, Answer):
        raise TypeError('answer must be an Answer object not, %r' % type(value).__name__)


def validate_alias(value: str) -> None:
    if not isinstance(value, str):
        raise TypeError('alias must be a string, not %r' % type(value).__name__)
    if not value.isalnum():
        raise ValueError('alias only can contain letters and numbers (alphanumeric)')


def validate_timeout(value: Optional[Union[int, float]]) -> None:
    if not isinstance(value, Optional[Union[int, float]]):
        raise TypeError('timeout must be a number, not %r' % type(value).__name__)


def validate_error(error: Union[AminoException, Exception], callback: Callable) -> None:
    if not issubclass(cast(type, error), AminoException):
        raise TypeError('error must be an Exception subclass, not %r'
            % error.__name__ if isclass(error) else type(error).__name__)
    elif not iscoroutinefunction(callback):
        raise ValueError('error callback must be a coroutine-function, not %r'
            % error.__name__ if isclass(error) else type(error).__name__)


@copy_all_docs
class Command(ABCCommand):
    def __init__(
        self,
        name: str,
        callback: Callable[..., Coroutine],
        aliases: Iterable[str] = [],
        answers: Union[Iterable[Answer], Dict[str, Answer]] = [],
        conditions: Iterable[Callable[..., Coroutine]] = [],
        errors: Dict[Union[AminoException, Exception], Callable[..., Coroutine]] = {}
    ) -> None:
        if not isinstance(name, str):
            raise TypeError('name argument must be a string, not %r' % type(name).__name__)
        if not isinstance(aliases, Iterable):
            raise TypeError('aliases argument must be a iterable of string, not %r' % type(aliases).__name__)
        if not isinstance(answers, (Iterable, dict)):
            raise TypeError('ansers argument must be a iterable of Answer objects, not %r' % type(answers).__name__)
        if not isinstance(conditions, Iterable):
            raise TypeError('conditions argument must be a iterable of coroutine-functions, not %r' % type(conditions).__name__)
        if not isinstance(errors, dict):
            raise TypeError('errors argument must be a dictionary, not %r' % type(errors).__name__)

        for key, value in errors.items():
            if not issubclass(cast(type, key), Exception):
                raise ValueError('errors key arguments must be a subclass of Exception, not %r' % (key.__name__ if isclass(key) else type(key).__name__))
            if not iscoroutinefunction(value):
                raise ValueError('errors value arguments must be a coroutine-function, not %r' % (key.__name__ if isclass(key) else type(key).__name__))
        for alias in aliases:
            self.add_alias(alias)
        for answer in answers.values() if isinstance(answers, dict) else answers:
            self.add_answer(answer)
        for condition in conditions:
            self.add_condition(condition)
        for error, value in errors.items():
            self.add_error(error, value)
        self.name = name
        self.callback = callback

    def __getstate__(self) -> dict:
        return {
            'name': self.name,
            'aliases': self.aliases,
            'answers': self.answers,
            'conditions': self.conditions,
            'callback': self.callback,
            'error': self.errors
        }

    def __setstate__(self, state: dict) -> None:
        self.__init__(**state)

    def __iter__(self) -> Iterable[str]:
        return self.keys()

    @property
    def id(self) -> str:
        """Command ID"""
        return str(uuid1(None, hash(self.name)))

    @property
    def name(self) -> str:
        return getattr(self, '_name')

    @name.setter
    def name(self, value) -> None:
        validate_alias(value)
        setattr(self, '_name', value)

    @property
    def aliases(self) -> Tuple[str, ...]:
        return tuple(getattr(self, '_aliases', ()))

    @property
    def answers(self) -> MappingProxyType[str, Answer]:
        return MappingProxyType(getattr(self, '_answers', {}))

    @property
    def callback(self) -> Optional[Callable[..., Coroutine]]:
        return getattr(self, '_callback', None)

    @callback.setter
    def callback(self, value: Callable[..., Coroutine], /) -> None:
        validate_callback(value)
        setattr(self, '_callback', value)

    @property
    def conditions(self) -> Tuple[Callable[..., Coroutine[Any, Any, bool]]]:
        return tuple(getattr(self, '_conditions', ()))

    @property
    def errors(self) -> MappingProxyType[Exception, Callable[..., Coroutine[Any, Any, Union[AminoException, Exception]]]]:
        return MappingProxyType(getattr(self, '_errors', {}))

    def keys(self) -> Tuple[str]:
        return (self.name, *self.aliases)

    def answer_keys(self) -> Tuple[str, ...]:
        return tuple(key for answer in self.answers.values() for key in answer.keys())

    def answer(
        self,
        name: str,
        *aliases: str,
        answers: Union[Iterable[Answer], Dict[str, Answer]] = [],
        conditions: List[Callable[..., Coroutine]] = [],
        errors: Dict[Exception, Callable[..., Coroutine]] = {}
    ) -> Callable[[Callable[..., Coroutine]], Answer]:
        def inner(callback: Callable[..., Coroutine]) -> Answer:
            answer = Answer(
                name=name,
                root=self,
                callback=callback,
                aliases=aliases,
                answers=answers,
                conditions=conditions,
                errors=errors
            )
            self.add_answer(answer)
            return answer
        return inner

    @overload
    def error(self, error: Union[AminoException, Exception]) -> Callable[[Callable[..., Coroutine]], Self]:
        ...

    @overload
    def error(self, error: Callable[..., Coroutine]) -> Self:
        ...

    def error(self, error: Union[AminoException, Exception, Callable[..., Coroutine]]) -> Union[Self, Callable[[Callable[..., Coroutine]], Self]]:
        if not isinstance(error, (AminoException, Exception, Callable)):
            raise TypeError('error must be a subclass of Exception, not %r' % (error.__name__ if isclass(error) else type(error).__name__))
        def inner(callback: Callable[..., Coroutine]) -> Self:
            if not iscoroutinefunction(callback):
                raise ValueError('error function must be a coroutine-function, not %r' % callback.__name__)
            self.add_error(cast(Union[AminoException, Exception], error), callback)
            return self
        if isfunction(error):
            error, func = Exception, error # type: ignore
            return inner(func)
        return inner

    def add_alias(self, alias: str) -> None:
        validate_alias(alias)
        if not hasattr(self, '_aliases'):
            setattr(self, '_aliases', set())
        cast(set, getattr(self, '_aliases')).add(alias)

    def add_answer(self, answer: Answer) -> None:
        validate_answer(answer)
        if answer.id in self.answers:
            raise ValueError('The %r answer command is already exists.' % answer.name)
        if not hasattr(self, '_answers'):
            setattr(self, '_answers', {})
        cast(dict, getattr(self, '_answers'))[answer.id] = answer

    def add_condition(self, condition: Callable[..., Coroutine[Any, Any, bool]]) -> None:
        validate_condition(condition)
        if not hasattr(self, '_conditions'):
            setattr(self, '_conditions', set())
        cast(set, getattr(self, '_conditions')).add(condition)

    def add_error(self, error: Union[AminoException, Exception], callback: Callable[..., Coroutine]) -> None:
        validate_error(error, callback)
        if not hasattr(self, '_errors'):
            setattr(self, '_errors', {})
        cast(dict, getattr(self, '_errors'))[error] = callback

    async def invoke(self, ctx: Context) -> None:
        if not callable(self.callback):
            raise RuntimeError('The command not has a callback function.')
        if self.conditions:
            if not all(await asyncio.gather(*[ctn(ctx) for ctn in self.conditions])):
                return
        try:
            await self.callback(ctx)
        except Exception as e:
            if type(e) in self.errors:
                await self.errors[cast(Exception, type(e))](ctx, e)

@copy_all_docs
class Answer(Command, ABCAnswer):
    def __init__(
        self,
        name: str,
        root: Union[Command, Answer],
        callback: Callable[..., Coroutine],
        aliases: Iterable[str] = [],
        answers: Union[Iterable[Answer], Dict[str, Answer]] = [],
        conditions: Iterable[Callable[..., Coroutine]] = [],
        errors: Dict[Exception, Callable[..., Coroutine]] = {},
        timeout: Optional[Union[int, float]] = None
    ) -> None:
        self.timeout = timeout
        self.root = root
        super().__init__(
            name=name,
            callback=callback,
            aliases=aliases,
            answers=answers,
            conditions=conditions,
            errors=errors
        )

    def __getstate__(self) -> dict:
        state = super().__getstate__()
        state['timeout'] = self.timeout
        state['root'] = self.root
        return state

    def __setstate__(self, state: dict) -> None:
        return self.__init__(**state)

    @property
    def root(self) -> Union[Command, Answer]:
        return getattr(self, '_root')

    @root.setter
    def root(self, value: Union[Command, Answer]) -> None:
        if not isinstance(value, (Command, Answer)):
            raise TypeError('alias root must be a Command or Answer object, not %r' % type(value).__name__)
        elif hasattr(self, '_root'):
            raise AttributeError('root attribute is read-only.')
        elif not TYPE_CHECKING:
            self._root = value

    @property
    def timeout(self) -> Union[int, float, None]:
        return getattr(self, '_timeout')

    @timeout.setter
    def timeout(self, value: Optional[Union[int, float]]) -> None:
        validate_timeout(value)
        if not TYPE_CHECKING:
            self._timeout = value
    
    def add_alias(self, alias: str) -> None:
        if alias in self.root.answer_keys():
            raise ValueError('%r alias is already exists.' % alias)
        super().add_alias(alias)


CONDITION_ANNOTATIONS = {
    Author, ChatType,
    Command, Context,
    Role, Sticker,
    Thread
}

COMMAND_ANNOTATIONS = ANSWER_ANNOTATIONS = CONDITION_ANNOTATIONS.union({
    bool, float, int, str
})

ANSWER_ANNOTATIONS.add(Answer)
CONDITION_ANNOTATIONS.add(Sticker)
