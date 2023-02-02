from functools import wraps
from inspect import iscoroutinefunction
from typing import Any, Callable, Union

__all__ = ("catch_exception",)


def catchexception(callback: Callable):
    if iscoroutinefunction(callback):
        @wraps(callback)
        async def asyncwrapper(*args, **kwargs) -> Union[Any, Exception]:
            try:
                await callback(*args, **kwargs)
            except Exception as exc:
                return exc

        return asyncwrapper

    @wraps(callback)
    def wrapper(*args, **kwargs) -> Union[Any, Exception]:
        try:
            callback(*args, **kwargs)
        except Exception as exc:
            return exc

    return wrapper
