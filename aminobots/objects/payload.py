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
from functools import cached_property

__all__ = ('Payload',)


@dataclass(repr=False)
class Aps:
    """Represent an Notification aps.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    alert: :class:`str`
        Alert text.
    badge: :class:`str`
        ...
    sound: :class:`str`
        Original App sound identifier (java)

    """
    json: dict

    @cached_property
    def alert(self) -> str:
        """Alert text."""
        return self.json.get('alert')

    @cached_property
    def badge(self) -> int:
        return self.json.get('badge')

    @cached_property
    def sound(self) -> str:
        """Original App sound identifier. (java)"""
        return self.json.get('sound')


@dataclass(repr=False)
class Payload:
    """Represent the Payload of the web-socket message.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    aps: :class:`Aps`
        Alert Aps.
    chatId: :class:`str`
        Chat id.
    comId: :class:`int`
        Community id.
    createdTime: :class:`str`
        Created date.
    id: :class:`str`
        Message id.
    isHidden: :class:`bool`
        Is hidden message.
    msgType: :class:`int`
        Message type.
    type: :class:`int`
        Notification type.

    """
    json: dict

    @cached_property
    def aps(self) -> Aps:
        """Alert aps."""
        return Aps(self.json.get('aps', dict()))

    @cached_property
    def chatId(self) -> str:
        """Chat id."""
        return self.json.get('tid')

    @cached_property
    def comId(self) -> str:
        """Community id."""
        return self.json.get('ndcId')

    @cached_property
    def createdTime(self) -> str:
        """Created date."""
        return self.json.get('ts')

    @cached_property
    def id(self) -> str:
        """Message id."""
        return self.json.get('id')

    @cached_property
    def isHidden(self) -> bool:
        """Is hidden message."""
        return self.json.get('isHidden')

    @cached_property
    def msgType(self) -> int:
        """Message type."""
        return self.json.get('msgType', 0)

    @cached_property
    def type(self) -> int:
        """Notification type."""
        return self.json.get('notifType', 0)
