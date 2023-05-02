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
from . import userprofile
import dataclasses
import functools
import typing

__all__ = ('ChatMessage',)


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def id(self) -> str:
        return self.json.get('frameId')

    @functools.cached_property
    def icon(self) -> str:
        return self.json.get('icon')

    @functools.cached_property
    def name(self) -> str:
        return self.json.get('name')

    @functools.cached_property
    def status(self) -> int:
        return self.json.get('status')

    @functools.cached_property
    def type(self) -> int:
        return self.json.get('frameType')

    @functools.cached_property
    def url(self) -> str:
        return self.json.get('resourceUrl')

    @functools.cached_property
    def version(self) -> int:
        return self.json.get('version')


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def accountMembershipStatus(self) -> int:
        return self.json.get('accountMembershipStatus', 0)

    @functools.cached_property
    def avatarFrame(self) -> AvatarFrame:
        return AvatarFrame(self.json.get('avatarFrame') or dict())

    @functools.cached_property
    def icon(self) -> str:
        return self.json.get('icon')

    @functools.cached_property
    def id(self) -> str:
        return self.json.get('uid')

    @functools.cached_property
    def level(self) -> int:
        return self.json.get('level')

    @functools.cached_property
    def nickname(self) -> str:
        return self.json.get('nickname', 0)

    @functools.cached_property
    def reputation(self) -> int:
        return self.json.get('reputation', 0)

    @functools.cached_property
    def role(self) -> int:
        return self.json.get('role')

    @functools.cached_property
    def status(self) -> int:
        return self.json.get('status')


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def authorId(self) -> str:
        """User id."""
        return self.json.get('uid')

    @functools.cached_property
    def banner(self) -> str:
        """Banner url."""
        return self.json.get('bannerUrl')

    @functools.cached_property
    def createdTime(self) -> str:
        """Created date."""
        return self.json.get('createdTime')

    @functools.cached_property
    def icon(self) -> str:
        """Collection icon url."""
        return self.json.get('icon')

    @functools.cached_property
    def id(self) -> str:
        """Collection id."""
        return self.json.get('collectionId')

    @functools.cached_property
    def modifiedTime(self) -> str:
        """Modified date."""
        return self.json.get('modifiedTime')

    @functools.cached_property
    def name(self) -> str:
        """Collection name."""
        return self.json.get('name')

    @functools.cached_property
    def smallIcon(self) -> str:
        """Small collection icon url."""
        return self.json.get('smallIcon')

    @functools.cached_property
    def status(self) -> int:
        """Collection status."""
        return self.json.get('status')

    @functools.cached_property
    def stickersCount(self) -> int:
        """Stickers count."""
        return self.json.get('stickersCount')

    @functools.cached_property
    def type(self) -> int:
        """Collection type."""
        return self.json.get('collectionType')

    @functools.cached_property
    def usedCount(self) -> int:
        """Used count."""
        return self.json.get('usedCount')


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def collection(self) -> StickerCollection:
        return StickerCollection(self.json.get('stickerCollectionSummary' or dict()))

    @functools.cached_property
    def collectionId(self) -> str:
        return self.json.get('stickerCollectionId')

    @functools.cached_property
    def createdTime(self) -> str:
        return self.json.get('createdTime')

    @functools.cached_property
    def icon(self) -> str:
        return self.json.get('icon')

    @functools.cached_property
    def iconV2(self) -> str:
        return self.json.get('iconV2')

    @functools.cached_property
    def id(self) -> str:
        return self.json.get('stickerId')

    @functools.cached_property
    def mediumIcon(self) -> str:
        return self.json.get('mediumIcon')

    @functools.cached_property
    def mediumIconV2(self) -> str:
        return self.json.get('mediumIconV2')

    @functools.cached_property
    def name(self) -> str:
        return self.json.ge('name')

    @functools.cached_property
    def smallIcon(self) -> str:
        return self.json.get('smallIcon')

    @functools.cached_property
    def smallIconV2(self) -> str:
        return self.json.get('smallIconV2')

    @functools.cached_property
    def status(self) -> int:
        return self.json.get('status')

    @functools.cached_property
    def usedCount(self) -> int:
        return self.json.get('usedCount')


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def duration(self) -> typing.Optional[float]:
        return self.json.get('duration')

    @functools.cached_property
    def originalStickerId(self) -> typing.Optional[str]:
        return self.json.get('originalStickerId')

    @functools.cached_property
    def sticker(self) -> Sticker:
        return Sticker(self.json.get('sticker') or dict())


@dataclasses.dataclass(repr=False)
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

    @functools.cached_property
    def author(self) -> userprofile.UserProfile:
        """User profile."""
        return userprofile.UserProfile(self.json.get('author') or dict())

    @functools.cached_property
    def authorId(self) -> str:
        """User id."""
        return self.json.get('uid')

    @functools.cached_property
    def chatId(self) -> str:
        """Chat id."""
        return self.json.get('threadId')

    @functools.cached_property
    def clientRefId(self) -> int:
        """Ref id."""
        return self.json.get('clientRefId')

    @functools.cached_property
    def content(self) -> typing.Optional[str]:
        """Text message."""
        return self.json.get('content')

    @functools.cached_property
    def createdTime(self) -> str:
        """Create date."""
        return self.json.get('createdTime')

    @functools.cached_property
    def extensions(self) -> Extensions:
        """Message extensions."""
        return Extensions(self.json.get('extensions') or dict())

    @functools.cached_property
    def id(self) -> str:
        """Message id."""
        return self.json.get('messageId')

    @functools.cached_property
    def includedInSummary(self) -> bool:
        """Included in summary."""
        return self.json.get('includedInSummary')

    @functools.cached_property
    def isHidden(self) -> bool:
        """Is hidden message"""
        return self.json.get('isHidden')

    @functools.cached_property
    def media(self) -> typing.Optional[str]:
        """Media url."""
        return self.json.get('mediaValue')

    @functools.cached_property
    def mediaDuration(self) -> typing.Optional[float]:
        """Audio duration."""
        return self.extensions.duration

    @functools.cached_property
    def mediaType(self) -> int:
        """Media type."""
        return self.json.get('mediaType') or 0

    @functools.cached_property
    def sticker(self) -> Sticker:
        """Sticker object."""
        return self.extensions.sticker

    @functools.cached_property
    def type(self) -> int:
        """Message type."""
        return self.json.get('type')
