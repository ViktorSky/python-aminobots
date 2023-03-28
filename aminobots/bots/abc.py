from typing import (
    Any,
    Optional,
    Protocol
)
import logging

__all__ = (
    'ABCAminoBot',
    'ABCBot',
    'ABCManagerBot'
)

DEFAULT_LOGGER = logging.getLogger('__name__')
DEFAULT_LOGGER.setLevel(logging.DEBUG)
DEFAULT_STREM = logging.StreamHandler()
DEFAULT_STREM.setFormatter(logging.Formatter(
    fmt='%(levelname)s: %(message)s'
))
DEFAULT_LOGGER.addHandler(DEFAULT_STREM)


class ABCBotBase(Protocol):
    __slots__ = ()

    info: dict
    logger: logging.Logger

    @property
    def name(self) -> str:
        """bot name."""
        return self.info.get('name')

    @name.setter
    def name(self, value: Any) -> None:
        if not isinstance(value, Optional[str]):
            raise TypeError('expected str not %r.' % value.__class__.__name__)
        self.info.update(name=value)

    @property
    def description(self) -> str:
        return self.info.get('description')

    @description.setter
    def description(self, value: Any) -> None:
        if not isinstance(value, Optional[str]):
            raise TypeError('expected str not %r.' % value.__class__.__name__)
        self.info.update(description=value)

    @property
    def prefix(self) -> str:
        return self.info.get('prefix')

    @prefix.setter
    def prefix(self, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError('expected str not %r.' % value.__class__.__name__)
        self.info.update(prefix=value)

    async def on_ready(self):
        self.logger.warning('on_ready event was ignored.')

    def command(self):
        raise NotImplementedError

    def event(self):
        raise NotImplementedError

    async def start(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


class ABCManagerBot(ABCBotBase):
    ...


class ABCAminoBot(ABCBotBase):
    ...


class ABCBot(ABCBotBase):
    ...


class ABCCommand(Protocol):
    ...
