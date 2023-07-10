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
from typing import Optional, TYPE_CHECKING, Union
from datetime import datetime
from re import search
from pydantic import BaseModel, Field, validator
from ..utils import parse_time

__all__ = ('Api',)


def fetch_duration(duration: str) -> float:
    result = search(r'(\d+\.\d+)s', duration)
    return float(result.group().removesuffix('s')) if result is not None else 0.0


class Api(BaseModel):
    timestamp: datetime = Field(alias='api:timestamp')
    message: str = Field(alias='api:message')
    statuscode: int = Field(alias='api:statuscode')
    duration: float = Field(alias='api:duration')

    _timestamp_validator = validator('timestamp')(parse_time)
    _duration_validator = validator('duration')(fetch_duration)

    if not TYPE_CHECKING:
        timestamp: Optional[datetime]
        message: Optional[str]
        statuscode: Optional[int]
        duration: Optional[Union[str, float]]
