from typing import Callable

__all__ = ("copydoc",)

def copydoc(funcWithDoc: Callable) -> Callable:
    def wrapper(func: Callable) -> Callable:
        func.__doc__ = funcWithDoc.__doc__
        return func
    return wrapper
