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
from .tipinfo import TipInfo
from ..objects import Author
from ..enums import ObjectType

__all__ = ('Post',)


class HeadlineStyle(BaseModel):
    displayTimeIndicator: bool = Field(default=False)
    layout: int

    if not TYPE_CHECKING:
        layout: Optional[int]


class Style(BaseModel):
    backgroundColor: Optional[Color]
    coverMediaIndexList: List[int] = Field(default_factory=list)
    backgroundMediaList: List[Media] = Field(default_factory=list)


class PageSnippet(BaseModel):
    body: str
    deepLink: Optional[HttpUrl]
    link: HttpUrl
    mediaList: List[Media] = Field(default_factory=list)
    source: str
    title: str

    if not TYPE_CHECKING:
        body: Optional[str]
        link: Optional[HttpUrl]
        source: Optional[str]
        title: Optional[str]


class Extensions(BaseModel):
    fansOnly: bool = Field(default=False)
    featuredType: Optional[int]
    headlineStyle: HeadlineStyle = Field(default_factory=HeadlineStyle)
    page: PageSnippet = Field(alias='pageSnippet', default_factory=PageSnippet)
    privilegeOfCommentOnPost: int
    style: Style = Field(default_factory=Style)

    if not TYPE_CHECKING:
        privilegeOfCommentOnPost: Optional[int]


class RefObject(BaseModel):
    author: Author = Field(default_factory=Author)
    commentsCount: int = Field(default=0)
    comId: int = Field(alias='ndcId')
    content: str
    contentRating: int
    createdTime: datetime
    endTime: Optional[datetime]
    globalCommentsCount: int
    globalVotesCount: int
    globalVotedValue: int
    guestVotesCount: int
    id: str = Field(alias='blogId')
    mediaList: List[Media] = Field(default_factory=list)
    modifiedTime: Optional[datetime]
    needHidden: bool = Field(default=False)
    status: int = Field(default=0)
    style: int
    type: ObjectType = Field(default=ObjectType.BLOG)
    votedValue: int
    tip: TipInfo = Field(alias='tipInfo', default_factory=TipInfo)
    title: str
    totalPollVoteCount: Optional[int]
    totalQuizPlayCount: Optional[int]
    keywords: str
    viewCount: int
    votesCount: int
    widgetDisplayInterval: Optional[float]

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
        style: Optional[int]
        votedValue: Optional[int]
        title: Optional[str]
        keywords: Optional[str]
        viewCount: Optional[int]
        votesCount: Optional[int]


class Post(BaseModel):
    author: Author = Field(default_factory=Author)
    commentsCount: int = Field(default=0)
    comId: int = Field(alias='ndcId')
    content: str
    createdTime: datetime
    globalCommentsCount: int = Field(default=0)
    globalVotedValue: int
    globalVotesCount: int = Field(default=0)
    mediaList: List[Media] = Field(default_factory=list)
    refObject: Optional[RefObject] = Field(default_factory=RefObject)
    refObjectId: str
    refObjectSubtype: Optional[ObjectType]
    refObjectType: Optional[ObjectType]
    score: Optional[float]
    status: int = Field(default=0)
    strategyInfo: Json
    title: str
    votesCount: int
    votedValue: int

    @validator('strategyInfo')
    def _strategyInfo_validator(value):
        return loads(value) if value else {}

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
