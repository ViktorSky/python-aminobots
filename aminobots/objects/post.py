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
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from ujson import loads
from pydantic import BaseModel, HttpUrl, Json, Field, validator
from pydantic.color import Color
from .media import Media
from .style import Style
from .tipinfo import TipInfo
from ..objects import Author
from ..enums import ObjectType

__all__ = ('Post',)


class HeadlineStyle(BaseModel):
    displayTimeIndicator: bool = Field(default=False)
    layout: int = Field(default=0)

    if not TYPE_CHECKING:
        layout: Optional[int]


class Style(BaseModel):
    backgroundColor: Optional[Color] = Field(default=None)
    coverMediaIndexList: List[int] = Field(default_factory=list)
    backgroundMediaList: List[Media] = Field(default_factory=list)


class PageSnippet(BaseModel):
    body: str = Field(default=None)
    deepLink: Optional[HttpUrl] = Field(default=None)
    link: HttpUrl = Field(default=None)
    mediaList: List[Media] = Field(default_factory=list)
    source: str = Field(default=None)
    title: str = Field(default=None)

    if not TYPE_CHECKING:
        body: Optional[str]
        link: Optional[HttpUrl]
        source: Optional[str]
        title: Optional[str]


class Extensions(BaseModel):
    fansOnly: bool = Field(default=False)
    featuredType: Optional[int] = Field(default=None)
    headlineStyle: HeadlineStyle = Field(default_factory=HeadlineStyle)
    page: PageSnippet = Field(alias='pageSnippet', default_factory=PageSnippet)
    privilegeOfCommentOnPost: int = Field(default=0)
    style: Style = Field(default_factory=Style)

    if not TYPE_CHECKING:
        privilegeOfCommentOnPost: Optional[int]


class RefObject(BaseModel):
    author: Author = Field(default_factory=Author)
    commentsCount: int = Field(default=0)
    comId: int = Field(alias='ndcId', default=0)
    content: str = Field(default=None)
    contentRating: int = Field(default=0)
    createdTime: datetime = Field(default=None)
    endTime: Optional[datetime] = Field(default=None)
    globalCommentsCount: int = Field(default=0)
    globalVotesCount: int = Field(default=0)
    globalVotedValue: int = Field(default=None)
    guestVotesCount: int = Field(default=0)
    id: str = Field(alias='blogId', default=None)
    mediaList: List[Media] = Field(default_factory=list)
    modifiedTime: Optional[datetime] = Field(default=None)
    needHidden: bool = Field(default=False)
    status: int = Field(default=0)
    style: Optional[Style] = Field(default=None)
    type: ObjectType = Field(default=ObjectType.BLOG)
    votedValue: int = Field(default=None)
    tip: TipInfo = Field(alias='tipInfo', default_factory=TipInfo)
    title: str = Field(default=None)
    totalPollVoteCount: Optional[int] = Field(default=None)
    totalQuizPlayCount: Optional[int] = Field(default=None)
    keywords: str = Field(default=None)
    viewCount: int = Field(default=None)
    votesCount: int = Field(default=None)
    widgetDisplayInterval: Optional[float] = Field(default=None)

    if not TYPE_CHECKING:
        comId: Optional[int]
        content: Optional[str]
        contentRating: Optional[int]
        createdTime: Optional[datetime]
        globalCommentsCount: Optional[int]
        globalVotesCount: Optional[int]
        globalVotedValue: Optional[int]
        guestVotesCount: Optional[int]
        id: Optional[str]
        votedValue: Optional[int]
        title: Optional[str]
        keywords: Optional[str]
        viewCount: Optional[int]
        votesCount: Optional[int]


class Post(BaseModel):
    author: Author = Field(default_factory=Author)
    commentsCount: int = Field(default=0)
    comId: int = Field(alias='ndcId', default=0)
    content: str = Field(default=None)
    createdTime: datetime = Field(default=None)
    globalCommentsCount: int = Field(default=0)
    globalVotedValue: int = Field(default=None)
    globalVotesCount: int = Field(default=0)
    mediaList: List[Media] = Field(default_factory=list)
    refObject: Optional[RefObject] = Field(default_factory=RefObject)
    refObjectId: str = Field(default=None)
    refObjectSubtype: Optional[ObjectType] = Field(default=None)
    refObjectType: Optional[ObjectType] = Field(default=None)
    score: Optional[float] = Field(default=None)
    status: int = Field(default=0)
    strategyInfo: Json[dict] = Field(default=None)
    title: str = Field(default=None)
    votesCount: int = Field(default=None)
    votedValue: int = Field(default=None)

    @validator('strategyInfo')
    def _strategyInfo_validator(value: Optional[Json]):
        return loads(value) if isinstance(value, str) else {}

    if not TYPE_CHECKING:
        comId: Optional[int]
        content: Optional[str]
        createdTime: Optional[datetime]
        globalVotedValue: Optional[int]
        refObjectId: Optional[str]
        strategyInfo: Optional[Json]
        title: Optional[str]
        votesCount: Optional[int]
        votedValue: Optional[int]
