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
from functools import cached_property
from .community import Community
from .currentuserinfo import CurrentUserInfo
from .invitation import Invitation

__all__ = ('LinkInfoV2',)


@dataclass(repr=False)
class LinkInfo:
    """Represent the link info.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    comId: :class:`int`
        Community id.
    fullPath: :class:`str`
        NDC full path.
    fullUrl: :class:`str`
        Full path url.
    objectId: :class:`str`
        Object id.
    shartCode: :class:`str`
        Short code.
    shortUrl: :class:`str`
        Short path url.
    targetCode: :class:`int`
        Target code.

    """
    json: dict

    @cached_property
    def comId(self) -> int:
        """Community id."""
        return self.json.get("ndcId")

    @cached_property
    def fullPath(self) -> Optional[str]:
        return self.json.get("fullPath")

    @cached_property
    def fullUrl(self) -> Optional[str]:
        """Full path url."""
        return self.json.get("shareURLFullPath")

    @cached_property
    def objectId(self) -> str:
        """Object id."""
        return self.json.get("objectId")

    @cached_property
    def objectType(self) -> int:
        """Object type."""
        return self.json.get("objectType")

    @cached_property
    def shortCode(self) -> Optional[str]:
        """Short code."""
        return self.json.get("shortCode")

    @cached_property
    def shortUrl(self) -> Optional[str]:
        """Short path url."""
        return self.json.get("shareURLShortCode")

    @cached_property
    def targetCode(self) -> int:
        """Target code."""
        return self.json.get("targetCode")


@dataclass(repr=False)
class Extensions:
    """Represent the Link info extensions.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    comId: :class:`int`
        Community id.
    community: :class:`Community`
        Community info object.
    currentUser: :class:`CurrentUserInfo`
        Current user profile in the community.
    invitation: :class:`Invitation`
        Community Invitation info object.
    invitationId: :class:`str`
        Community invitation id.
    linkInfo: :class:`LinkInfo`
        Link info object.
    isCurrentUserJoined: :class:`bool`
        Logged account is joined in the community.

    """
    json: dict

    @cached_property
    def comId(self) -> int:
        """Community id."""
        return self.linkInfo.comId or self.community.id

    @cached_property
    def community(self) -> Community:
        """Community object."""
        return Community(self.json.get("community") or {})

    @cached_property
    def currentUser(self) -> CurrentUserInfo:
        """Current user profile in the community."""
        return CurrentUserInfo(self.json.get('currentUserInfo') or {})

    @cached_property
    def invitation(self) -> Invitation:
        """Community invitation object."""
        return Invitation(self.json.get("invitation") or {})

    @cached_property
    def invitationId(self) -> Optional[str]:
        """Community invitation id."""
        return self.json.get("invitationId") or self.invitation.id

    @cached_property
    def linkInfo(self) -> LinkInfo:
        """Link info object."""
        return LinkInfo(self.json.get("linkInfo") or {})

    @cached_property
    def isCurrentUserJoined(self) -> bool:
        """Logged account is joined in the community."""
        return self.json.get('isCurrentUserJoined', False)


@dataclass(repr=False)
class LinkInfoV2:
    """Represent the link information of Amino.

    Attributes
    ----------
    json: :class:`dict`
        The raw API data.
    extensions: :class:`Extensions`
        Link extensions.
    invitation: :class:`Invitation`
        Community Invitation object.
    linkInfo: :class:`LinkInfo`
        Link info.
    path: :class:`str`
        NDC path.

    """
    json: dict

    @cached_property
    def community(self) -> Community:
        return self.extensions.community

    @cached_property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @cached_property
    def invitation(self) -> Invitation:
        return self.extensions.invitation

    @cached_property
    def linkInfo(self) -> LinkInfo:
        return self.extensions.linkInfo

    @cached_property
    def path(self) -> str:
        return self.json.get("path")
