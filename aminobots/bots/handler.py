from typing import Any, Optional, Union
from ..types import Callback, Condition
from inspect import iscoroutinefunction
from collections.abc import Iterable

__all__ = (
    'Command', 'Event'
)

class Event:
    code: str
    callback: None
    condition: None

    def __init__(self, **kwargs):
        self.info = dict(**kwargs)

    def callback(self, obj: Callback, /):
        """Set the command callback."""
        if not iscoroutinefunction(obj) or obj is None:
            raise TypeError('expected coroutine-funtion not %r.' % obj.__class__.__name__)
        self.__dict__.update(callback=obj)
        return self

    def condition(self, obj: Condition, /):
        """Set the command condition."""
        if not iscoroutinefunction(obj) or obj is None:
            raise TypeError('expected coroutine-funtion not %r.' % obj.__class__.__name__)
        self.__dict__.update(condition=obj)
        return self

    def error(self, obj: Callback, /):
        if not iscoroutinefunction(obj) or obj is None:
            raise TypeError('expected coroutine-funtion not %r.' % obj.__class__.__name__)
        self.__dict__.update(error=obj)
        return self


class Command:
    __slots__ = ('info',)

    def __init__(
        self,
        *aliases: str,
        expire_time: int,
        callback: int,
        anwers: dict = dict(),
        condition: Callback = None,
        error: Callback = None
    ):
        self.info = dict(
            aliases=set(), answers=dict(),
            callback=None, condition=None,
            error=None, expire=None,
            expire_time=None
        )
        self.expire_time = expire_time
        self.aliases = aliases
        self.answers = anwers
        self.callback(callback)
        self.condition(condition)
        self.error(error)

    @property
    def expire_time(self) -> Optional[Union[float, int]]:
        return self.info.setdefault('expire_time')

    @expire_time.setter
    def expire_time(self, value: Any) -> None:
        if not isinstance(value, Optional[Union[float, int]]):
            raise TypeError('expected float or int not %r.' % value.__class__.__name__)
        self.info.update(expire_time=value)

    @property
    def aliases(self) -> set:
        return self.info.setdefault('aliases', set())

    @aliases.setter
    def aliases(self, value: Any) -> None:
        if not isinstance(value, Iterable):
            raise TypeError('expected iterable.')
        elif not value:
            raise ValueError('aliases is empty.')
        self.info.update(aliases=set(value))

    @property
    def answers(self) -> dict:
        return self.info.setdefault('answers', dict())

    @answers.setter
    def answers(self, value: Any) -> None:
        if not isinstance(value, dict):
            raise TypeError('expected dict not %r.' % value.__class__.__name__)
        for k in value.values():
            if not iscoroutinefunction(k):
                raise TypeError('expected coroutine-function.')
        self.info.update(answers=value)

    def answer(self, key: str):
        def inner(obj: Callback):
            self.info.setdefault('answers', dict()).update({key: obj})
            return self
        if not isinstance(key, str):
            raise TypeError('expected str not %r.' % key.__class__.__name__)
        return inner

    def callback(self, obj: Callback, /):
        """Set the command callback."""
        if not iscoroutinefunction(obj) and obj is not None:
            raise TypeError('expected coroutine-funtion not %r.' % obj.__class__.__name__)
        self.info.update(callback=obj)
        return self

    def condition(self, obj: Condition, /):
        """Set the command condition."""
        if not iscoroutinefunction(obj) and obj is not None:
            raise TypeError('expected coroutine-funtion not %r.' % obj.__class__.__name__)
        self.info.update(condition=obj)
        return self

    def expire(self, obj: Callback, /):
        """Set the command expire callback."""
        if not iscoroutinefunction(obj) and obj is not None:
            raise TypeError('expected coroutine-funtion not %r.' % obj.__class__.__name__)
        self.info.update(expire=obj)

    def error(self, obj: Callback, /):
        """Set the command error catcher callback."""
        if not iscoroutinefunction(obj) and obj is not None:
            raise TypeError('expected coroutine-funtion not %r.' % obj.__class__.__name__)
        self.info.update(error=obj)
        return self

    def getargs(self, ctx):
        ...

    async def invoke(self, ctx):
        if self.info.get('condition'):
            args, kwargs = self.getargs(ctx)
            enabled = await self.info['condition'](*args, **kwargs)
            if not enabled:
                ctx.logger.debug('')
