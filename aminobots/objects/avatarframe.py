from typing import Optional, TYPE_CHECKING
from pydantic import BaseModel, HttpUrl, Field
from ..enums import FrameType

__all__ = ('AvatarFrame',)


class AvatarFrame(BaseModel):
    id: str = Field(alias='frameId', default=None)
    icon: HttpUrl = Field(default=None)
    name: str = Field(default=None)
    ownershipStatus: int = Field(default=None)
    status: int = Field(default=0)
    type: FrameType = Field(alias='frameType', default=None)
    version: int = Field(default=0)
    url: HttpUrl = Field(alias='resourceUrl', default=None)

    if not TYPE_CHECKING:
        id: Optional[str]
        icon: Optional[HttpUrl]
        name: Optional[str]
        ownershipStatus: Optional[int]
        type: Optional[int]
        version: Optional[int]
        url: Optional[HttpUrl]
