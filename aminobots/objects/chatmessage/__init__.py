from typing import Optional
from ..object import Object

from .author import *
from .extensions import *
from .sticker import *

__all__ = ('ChatMessage',)


class ChatMessage(Object):

    @property
    def author(self) -> Author:
        return Author(self.json.get('author') or dict())

    @property
    def authorId(self) -> str:
        return self.json.get('uid')

    @property
    def chatId(self) -> str:
        return self.json.get('threadId')

    @property
    def clientRefId(self) -> int:
        return self.json.get('clientRefId')

    @property
    def content(self) -> Optional[str]:
        return self.json.get('content')

    @property
    def createdTime(self) -> str:
        return self.json.get('createdTime')

    @property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get('extensions') or dict())

    @property
    def id(self) -> str:
        return self.json.get('messageId')

    @property
    def includedInSummary(self) -> bool:
        return self.json.get('includedInSummary')

    @property
    def isHidden(self) -> bool:
        return self.json.get('isHidden')

    @property
    def media(self) -> Optional[str]:
        return self.json.get('mediaValue')

    @property
    def mediaDuration(self) -> Optional[float]:
        return self.extensions.duration

    @property
    def mediaType(self) -> int:
        return self.json.get('mediaType') or 0

    @property
    def sticker(self) -> Sticker:
        return self.extensions.sticker

    @property
    def type(self) -> int:
        return self.json.get('type')
