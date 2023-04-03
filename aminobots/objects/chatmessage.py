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

from dataclasses import dataclass
from typing import Optional
from .userprofile import UserProfile

__all__ = ('ChatMessage',)


@dataclass(repr=False)
class AvatarFrame:
    """Represent the author avatar frame.

    Attributes
    ----------
    id: :class:`str`
        Avatar frame id.
    icon: :class:`str`
        Avatar icon url.
    name: :class:`str`
        Avatar name.
    status: :class:`int`
        Avatar status.
    type: :class:`int`
        Frame type.
    url: :class:`str`
        Resource url. (zip)
    version: :class:`int`
        Avatar version.

    """
    json: dict

    @property
    def id(self) -> str:
        return self.json.get('frameId')

    @property
    def icon(self) -> str:
        return self.json.get('icon')

    @property
    def name(self) -> str:
        return self.json.get('name')

    @property
    def status(self) -> int:
        return self.json.get('status')

    @property
    def type(self) -> int:
        return self.json.get('frameType')

    @property
    def url(self) -> str:
        return self.json.get('resourceUrl')

    @property
    def version(self) -> int:
        return self.json.get('version')


@dataclass(repr=False)
class Author:
    """Represent the message author.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    accountMembershipStatus: :class:`int`
        ...
    avatarFrame: :class:`AvatarFrame`
        ...
    icon: :class:`str`
        Profile icon url.
    id: :class:`str`
        User id.
    level: :class:`int`
        ...
    nickname: :class:`str`
        ...
    reputation: :class:`int`
        ...
    role: :class:`int`
        ...
    status: :class:`int`
        ...

    """
    json: dict

    @property
    def accountMembershipStatus(self) -> int:
        return self.json.get('accountMembershipStatus', 0)

    @property
    def avatarFrame(self) -> AvatarFrame:
        return AvatarFrame(self.json.get('avatarFrame') or dict())

    @property
    def icon(self) -> str:
        return self.json.get('icon')

    @property
    def id(self) -> str:
        return self.json.get('uid')

    @property
    def level(self) -> int:
        return self.json.get('level')

    @property
    def nickname(self) -> str:
        return self.json.get('nickname', 0)

    @property
    def reputation(self) -> int:
        return self.json.get('reputation', 0)

    @property
    def role(self) -> int:
        return self.json.get('role')

    @property
    def status(self) -> int:
        return self.json.get('status')


@dataclass(repr=False)
class StickerCollection:
    """Represent a Sticker Collection of Amino.
    
    Attributes
    ----------
    authorId: :class:`str`
        Collection author id.
    banner: :class:`str`
        Banner url.
    createdTime: :class:`str`
        Created date.
    icon: :class:`str`
        Collection icon url.
    id: :class:`str`
        Collection id.
    modifiedTime: :class:`str`
        modified date.
    name: :class:`str`
        Collection name.
    smallIcon: :class:`str`
        Small collection icon url.
    status: :class:`int`
        Collection status.
    stickersCount: :class:`int`
        Collection stickers count.
    type: :class:`int`
        Collection type.
    usedCount: :class:`int`
        Collection used count.

    """
    json: dict

    @property
    def authorId(self) -> str:
        """User id."""
        return self.json.get('uid')

    @property
    def banner(self) -> str:
        """Banner url."""
        return self.json.get('bannerUrl')

    @property
    def createdTime(self) -> str:
        """Created date."""
        return self.json.get('createdTime')

    @property
    def icon(self) -> str:
        """Collection icon url."""
        return self.json.get('icon')

    @property
    def id(self) -> str:
        """Collection id."""
        return self.json.get('collectionId')

    @property
    def modifiedTime(self) -> str:
        """Modified date."""
        return self.json.get('modifiedTime')

    @property
    def name(self) -> str:
        """Collection name."""
        return self.json.get('name')

    @property
    def smallIcon(self) -> str:
        """Small collection icon url."""
        return self.json.get('smallIcon')

    @property
    def status(self) -> int:
        """Collection status."""
        return self.json.get('status')

    @property
    def stickersCount(self) -> int:
        """Stickers count."""
        return self.json.get('stickersCount')

    @property
    def type(self) -> int:
        """Collection type."""
        return self.json.get('collectionType')

    @property
    def usedCount(self) -> int:
        """Used count."""
        return self.json.get('usedCount')


@dataclass(repr=False)
class Sticker:
    """Represent a Sticker of Amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    collection: :class:`StickerCollection`
        Sticker Collection.
    createdTime: :class:`str`
        Sticker created time.
    icon: :class:`str`
        Sticker icon url.
    iconV2: :class:`str`
        Sticker icon url.
    mediumIcon: :class:`str`
        Medium sticker icon url.
    mediumIconV2: :class:`str`
        Medium sticker icon url.
    name: :class:`str`
        Sticker name.
    smallIcon: :class:`str`
        Small sticker icon url.
    smallIconV2: :class:`str`
        Small sticker icon url.
    status: :class:`int`
        Sticker status.
    usedCount: :class:`int`
        Sticker used count.

    """
    json: dict

    @property
    def collection(self) -> StickerCollection:
        return StickerCollection(self.json.get('stickerCollectionSummary' or dict()))

    @property
    def collectionId(self) -> str:
        return self.json.get('stickerCollectionId')

    @property
    def createdTime(self) -> str:
        return self.json.get('createdTime')

    @property
    def icon(self) -> str:
        return self.json.get('icon')

    @property
    def iconV2(self) -> str:
        return self.json.get('iconV2')

    @property
    def id(self) -> str:
        return self.json.get('stickerId')

    @property
    def mediumIcon(self) -> str:
        return self.json.get('mediumIcon')

    @property
    def mediumIconV2(self) -> str:
        return self.json.get('mediumIconV2')

    @property
    def name(self) -> str:
        return self.json.ge('name')

    @property
    def smallIcon(self) -> str:
        return self.json.get('smallIcon')

    @property
    def smallIconV2(self) -> str:
        return self.json.get('smallIconV2')

    @property
    def status(self) -> int:
        return self.json.get('status')

    @property
    def usedCount(self) -> int:
        return self.json.get('usedCount')


@dataclass(repr=False)
class Extensions:
    """Represent message extensions.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    duration: Optional[:class:`float`]
        Audio/Video duration.
    originalStickerId: :class:`str`
        Original id.
    sticker: :class:`Sticker`
        Sticker object.

    """
    json: dict

    @property
    def duration(self) -> Optional[float]:
        return self.json.get('duration')

    @property
    def originalStickerId(self) -> Optional[str]:
        return self.json.get('originalStickerId')

    @property
    def sticker(self) -> Sticker:
        return Sticker(self.json.get('sticker') or dict())


@dataclass(repr=False)
class ChatMessage:
    """Represent a chat message of Amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    author: :class:`UserProfile`
        The message author.
    chatId: :class:`str`
        Chat id.
    clientRefId: :class:`int`
        ...
    content: Optional[:class:`str`]
        Text message.
    createdTime: :class:`str`
        Create date.
    extensions: :class:`Extensions`
        Message extensions.
    id: :class:`str`
        Message id.
    includedInSummary: :class:`bool`
        ...
    isHidden: :class:`bool`
        ...
    media: :class:`str`
        Media url. (image, audio, video)
    mediaDuration: :class:`float`
        Audio duration.
    mediaType: :class:`int`
        Media type.
    sticker: :class:`Sticker`
        Sticker.
    type: :class:`int`
        Message type.

    """
    json: dict

    @property
    def author(self) -> UserProfile:
        """User profile."""
        return UserProfile(self.json.get('author') or dict())

    @property
    def authorId(self) -> str:
        """User id."""
        return self.json.get('uid')

    @property
    def chatId(self) -> str:
        """Chat id."""
        return self.json.get('threadId')

    @property
    def clientRefId(self) -> int:
        """Ref id."""
        return self.json.get('clientRefId')

    @property
    def content(self) -> Optional[str]:
        """Text message."""
        return self.json.get('content')

    @property
    def createdTime(self) -> str:
        """Create date."""
        return self.json.get('createdTime')

    @property
    def extensions(self) -> Extensions:
        """Message extensions."""
        return Extensions(self.json.get('extensions') or dict())

    @property
    def id(self) -> str:
        """Message id."""
        return self.json.get('messageId')

    @property
    def includedInSummary(self) -> bool:
        """Included in summary."""
        return self.json.get('includedInSummary')

    @property
    def isHidden(self) -> bool:
        """Is hidden message"""
        return self.json.get('isHidden')

    @property
    def media(self) -> Optional[str]:
        """Media url."""
        return self.json.get('mediaValue')

    @property
    def mediaDuration(self) -> Optional[float]:
        """Audio duration."""
        return self.extensions.duration

    @property
    def mediaType(self) -> int:
        """Media type."""
        return self.json.get('mediaType') or 0

    @property
    def sticker(self) -> Sticker:
        """Sticker object."""
        return self.extensions.sticker

    @property
    def type(self) -> int:
        """Message type."""
        return self.json.get('type')
