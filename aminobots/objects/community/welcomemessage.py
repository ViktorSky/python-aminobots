from typing import Optional
from ..object import Object

__all__ = 'WelcomeMessage',


class WelcomeMessage(Object):
    json: dict

    @property
    def enabled(self) -> Optional[bool]:
        return self.json.get("enabled")

    @property
    def text(self) -> Optional[str]:
        return self.json.get("text")
