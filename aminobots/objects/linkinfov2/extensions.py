from typing import Optional
from ..object import Object
from ..community import Community
from ..invitation import Invitation
from .linkinfo import *

__all__ = 'Extensions',


class Extensions(Object):
    json: dict

    @property
    def comId(self) -> int:
        return self.linkInfo.comId or self.community.id

    @property
    def community(self) -> Community:
        return Community(self.json.get("community") or {})

    @property
    def invitation(self) -> Invitation:
        return Invitation(self.json.get("invitation") or {})

    @property
    def invitationId(self) -> Optional[str]:
        return self.json.get("invitationId") or self.invitation.id

    @property
    def linkInfo(self) -> LinkInfo:
        return LinkInfo(self.json.get("linkInfo") or {})
