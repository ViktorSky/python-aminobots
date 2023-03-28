"""
"""

from typing import Any, Union
from dataclasses import dataclass
from .api import Api
import collections.abc

import aiohttp

__all__ = ('Object',)


@dataclass(repr=False)
class Object:
    json: dict

    def __bool__(self) -> bool:
        return bool(self.json)
