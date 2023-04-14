from typing import (
    Any,
    TYPE_CHECKING
)
import logging
from .abc import (
    ABCBotBase as Bot,
    ABCCommand as Command
)
if TYPE_CHECKING:
    from .bot import Bot
    from .handler import Command


__all__ = (
    'Context',
    'ContextInfo'
)

class ContextInfo:
    ...


class Context:
    logger: logging.Logger
    bot: Bot
    cmd: Command

