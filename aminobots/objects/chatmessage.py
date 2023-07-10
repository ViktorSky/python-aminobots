"""MIT License

Copyright (c) 2022 ViktorSky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field
from .author import Author
from ..enums import MediaType, MessageType

__all__ = ('ChatMessage', 'Sticker')


class StickerCollection(BaseModel):
    authorId: Optional[str] = Field(alias='uid', default=None)
    bannerUrl: HttpUrl = Field(default=None)
    createdTime: datetime = Field(default=None)
    icon: HttpUrl = Field(default=None)
    id: str = Field(alias='collectionId', default=None)
    modifiedTime: Optional[datetime] = Field(default=None)
    name: str = Field(default=None)
    smallIcon: HttpUrl = Field(default=None)
    status: int = Field(default=0)
    stickersCount: int = Field(default=0)
    type: int = Field(alias='collectionType', default=0)
    usedCount: int = Field(default=0)

    if not TYPE_CHECKING:
        bannerUrl: Optional[HttpUrl]
        createdTime: Optional[datetime]
        icon: Optional[HttpUrl]
        id: Optional[str]
        name: Optional[str]
        smallIcon: Optional[HttpUrl]
        type: Optional[int]


class Sticker(BaseModel):
    collection: StickerCollection = Field(alias='stickerCollectionSummary', default_factory=StickerCollection)
    collectionId: str = Field(alias='stickerCollectionId')
    createdTime: datetime
    icon: HttpUrl
    iconV2: HttpUrl
    id: str = Field(alias='stickerId')
    mediumIcon: HttpUrl
    mediumIconV2: HttpUrl
    name: str
    smallIcon: HttpUrl
    smallIconV2: HttpUrl
    status: int = Field(default=0)
    usedCount: int = Field(default=0)

    if not TYPE_CHECKING:
        collectionId: Optional[str]
        createdTime: Optional[datetime]
        icon: Optional[HttpUrl]
        iconV2: Optional[HttpUrl]
        id: Optional[str]
        mediumIcon: Optional[HttpUrl]
        mediumIconV2: Optional[HttpUrl]
        name: Optional[str]
        smallIcon: Optional[HttpUrl]
        smallIconV2: Optional[HttpUrl]


class Extensions(BaseModel):
    duration: Optional[float] = Field(default=None)
    originalStickerId: Optional[str] = Field(default=None)
    sticker: Optional[Sticker] = Field(default=None)


class ChatMessage(BaseModel):
    author: Author = Field(default_factory=Author)
    authorId: str = Field(alias='uid', default=None)
    chatId: str = Field(alias='threadId', default=None)
    clientRefId: str = Field(default=0)
    content: Optional[str] = Field(default=None)
    createdTime: datetime = Field(default=None)
    extensions: Extensions = Field(default_factory=Extensions)
    id: str = Field(alias='messageId', default=None)
    includedInSummary: bool = Field(default=False)
    isHidden: bool = Field(default=False)
    media: Optional[HttpUrl] = Field(alias='mediaValue', default=None)
    mediaDuration: Optional[float] = property(lambda self: self.extensions.duration) # type: ignore
    mediaType: MediaType = Field(default=MediaType.TEXT)
    sticker: Optional[Sticker] = property(lambda self: self.extensions.sticker) # type: ignore
    type: MessageType = Field(default=MessageType.TEXT)

    if not TYPE_CHECKING:
        authorId: Optional[str]
        chatId: Optional[str]
        clientRefId: Optional[str]
        createdTime: Optional[datetime]
        id: Optional[str]
