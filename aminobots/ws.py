from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)
from .abc import ABCWSClient

if TYPE_CHECKING:
    from .amino import Amino


__all__ = ('WSClient',)


class WSClient(ABCWSClient):
    amino: Amino

    def __init__(self, amino: Amino) -> None:
        self.amino: Amino = amino
