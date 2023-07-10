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
from typing import Optional, Union
from pydantic import Field
from .model import Model
from ..enums import ObjectType
from ..objects.linkinfov2 import LinkInfoV2, Extensions

__all__ = ('LinkResolution',)


class LinkResolution(Model):
    comId: int = property(lambda self: self.linkInfoV2.linkInfo.comId or self.linkInfoV2.community.id) # type: ignore
    extensions: Extensions = property(lambda self: self.linkInfoV2.extensions) # type: ignore
    invitationId: Optional[str] = property(lambda self: self.linkInfoV2.extensions.invitationId) # type: ignore
    linkInfoV2: LinkInfoV2 = Field(default_factory=LinkInfoV2)
    objectId: Union[str, int] = property(lambda self: self.linkInfoV2.extensions.linkInfo.objectId) # type: ignore
    objectType: ObjectType = property(lambda self: self.linkInfoV2.linkInfo.objectType) # type: ignore
    path: str = property(lambda self: self.linkInfoV2.path, doc='NDC path') # type: ignore
    fullPath: Optional[str] = property(lambda self: self.linkInfoV2.linkInfo.fullPath) # type: ignore
    shareURLFullPath: Optional[str] = property(lambda self: self.linkInfoV2.linkInfo.shareURLFullPath) # type: ignore
    shareURLShortCode: Optional[str] = property(lambda self: self.linkInfoV2.linkInfo.shareURLShortCode) # type: ignore
    shortCode: Optional[str] = property(lambda self: self.linkInfoV2.linkInfo.shortCode) # type: ignore
    targetCode: Optional[int] = property(lambda self: self.linkInfoV2.linkInfo.targetCode) # type: ignore
