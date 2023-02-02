from functools import wraps
from inspect import iscoroutinefunction
from typing import Callable

__all__ = ("show_exception",)


def showexception(func: Callable) -> Callable:
    if iscoroutinefunction(func):
        @wraps(func)
        async def asyncwrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as Error:
                print(f"{func.__name__} : {repr(Error)}")

        return asyncwrapper

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as Error:
            print(f"{func.__name__} : {repr(Error)}")

    return wrapper
