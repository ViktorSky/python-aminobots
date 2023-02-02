from functools import wraps
from inspect import iscoroutinefunction
from typing import Awaitable, Callable,  Union
import asyncio


__all__ = ("duo",)


def duo(*conditions: Union[Awaitable, Callable], allTrue: bool = False):
    """Join condition functions and routines to create a condition function or coroutine.

    Args:
        allTrue (bool, optional): Returns True if all condition functions do not return false. Defaults to False.

    Returns:
        types.FunctionType: function or coroutine
    """

    assert len(conditions), "conditions are empty."
    assert all(iscoroutinefunction(cn) for cn in conditions) or all(not iscoroutinefunction(cn) for cn in conditions), \
        "conditions must be all coroutine or all non-coroutine."

    verify = all if allTrue else any

    def decorator(callback: Union[Awaitable, Callable]) -> Union[Awaitable, Callable]:
        if iscoroutinefunction(callback):
            @wraps(callback)
            async def asyncwrapper(*args, **kwargs):
                gen = ((condition(*args, **kwargs)) for condition in conditions)
                if verify(await asyncio.gather(*gen)):
                    return await callback(*args, **kwargs)

            return asyncwrapper

        @wraps(callback)
        def wrapper(*args: tuple, **kwargs: dict):
            gen = ((condition(*args, **kwargs)) for condition in conditions)
            if verify(gen):
                return callback(*args, **kwargs)

        return wrapper

    return decorator
