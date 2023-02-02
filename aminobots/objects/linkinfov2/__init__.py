from ..object import Object
from ..community import Community
from ..invitation import Invitation
from .extensions import *
from .linkinfo import *

__all__ = 'LinkInfoV2',


class LinkInfoV2(Object):
    json: dict

    @property
    def community(self) -> Community:
        return self.extensions.community

    @property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @property
    def invitation(self) -> Invitation:
        return self.extensions.invitation

    @property
    def linkInfo(self) -> LinkInfo:
        return self.extensions.linkInfo

    @property
    def ndc(self) -> str:
        return self.json.get("path")
