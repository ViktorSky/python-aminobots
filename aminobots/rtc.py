from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .abc import ABCRTCClient

if TYPE_CHECKING:
    from .amino import Amino

__all__ = ('RTCClient',)


class RTCClient(ABCRTCClient):
    amino: Amino

    def __init__(self, amino: Amino) -> None:
        self.amino = amino
