import contextlib

__all__ = (
    'suppress',
)

class suppress(contextlib.suppress):
    async def __aenter__(self):
        return self.__enter__()

    async def __aexit__(self, *args, **kwargs):
        return self.__exit__(*args, **kwargs)
