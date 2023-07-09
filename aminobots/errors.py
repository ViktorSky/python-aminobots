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
from typing import Any, Dict, Optional, Union, cast
from datetime import datetime
from re import search
from . import utils

__all__ = (
    'AminoException',
    'APIError',
    'ConnectionError',
    'ClientError',
    'RedirectionError',
    'ServerError'
)


class AminoException(Exception):
    """Base Exception class for python-aminobots."""


class ConnectionError(AminoException):
    """Exception that's raised when there is no connection."""


class WebSocketClosed(AminoException):
    """Exception that's raised when the websocket close the connection."""


class ServerError(AminoException):
    """Base Exception class for HTTP requests. Raised when the HTTP response status >= 500."""
    def __init__(self, status: int, reason: str) -> None:
        super().__init__(status, reason)
        self.status: int = status
        self.reason: str = reason

    def __str__(self) -> str:
        return repr(f'{self.status} - {self.reason}')


class InternalServerError(ServerError):
    """Exception that's raised when an HTTP request throws `500` error.

    Indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.
    Usually this means there's an issue or temporary glitch with the website's programming.

    """


class NotImplemented(ServerError):
    """Exception that's raised when an HTTP request throws `501` error.

    Indicates that the server recognizes the command present but is unable to take the requested action
    due to a syntax error in the parameter(s) present with the command.

    """


class BadGateway(ServerError):
    """Exception that's raised when an HTTP request throws `502` error.

    Indicates that the server, while acting as a gateway or proxy, receivedan invalid response from the upstream server.
    Usually the server receives an error from another server. 

    """


class ServiceUnavailable(ServerError):
    """Exception that's raised when an HTTP request throws `503` error.

    Indicates that the server is not ready to handle the request.
    Common causes are a server that is down for maintenance or that is overloaded.

    """


def check_server_error(status: int, reason: str) -> ServerError:
    error = {
        500: InternalServerError,
        501: NotImplementedError,
        502: BadGateway,
        503: ServiceUnavailable
    }.get(status, ServerError)
    return error(status, reason)


class ClientError(AminoException):
    """Base Exception class for HTTP requests. Raised when the HTTP response status >= 400."""
    def __init__(self, status: int, reason: str) -> None:
        super().__init__(status, reason)
        self.status: int = status
        self.reason: str = reason

    def __str__(self) -> str:
        return repr(f'{self.status} - {self.reason}')


class BadRequest(ClientError):
    """Exception that's raised when and HTTP request throws `400` error.

    Usually the server cannot or will not process the request due to something that
    is perceived to be a client error (for example, malformed request syntax,
    invalid request message framing, or deceptive request routing)

    """


class Forbidden(ClientError):
    """Exception that's raised when an HTTP request throws `403` error.

    Indicates that the server understands the request but refuses to authorize it.
    Usually it's an IP ban, you've made too many requests.

    """


class TooManyClientRequests(ClientError):
    """Exception that's raised when an HTTP request throws `429` error.

    Indicates the user has sent too many requests in a given amount of time ("rate limiting").

    """


def check_client_error(status: int, reason: str) -> ClientError:
    error = {
        400: BadRequest,
        403: Forbidden,
        429: TooManyClientRequests
    }.get(status, ClientError)
    return error(status, reason)


class RedirectionError(AminoException):
    """Base Exception class for HTTP requests. Raised when the HTTP response status >= 300."""
    status: int
    reason: str
    def __init__(self, status: int, reason: str) -> None:
        super().__init__(status, reason)
        self.status = status
        self.reason = reason

    def __str__(self) -> str:
        return repr(f'{self.status} - {self.reason}')


def check_redirect_error(status: int, reason: str) -> RedirectionError:
    error = {
    }.get(status, RedirectionError)
    return error(status, reason)


class APIError(AminoException):
    """Exception that's raised when an HTTP API request operation fails.

    Attributes
    ------------
    json : :class:`dict`
        Raw exception data.
    message : :class:`str`
        The api message of the error. Could be an empty string.
    statuscode : :class:`int`
        The Amino specific error code for the failure.
    duration : :class:`float`
        The duration of the API processing.
    timestamp : :class:`datetime`
        The timestamp of the request.

    """

    __slots__ = (
        'duration',
        'json',
        'message',
        'status',
        'timestamp'
    )

    def __init__(self, json: Dict[str, Union[str, int]]) -> None:
        Exception.__init__(self, json)
        duration = cast(str, json.get('api:duration', '0.0s'))
        result = search(r'(\d+\.\d+)s', duration)
        self.duration: float = 0.0 if result is None else float(result.group().removesuffix('s'))
        self.message: str = cast(str, json.get('api:message'))
        self.statuscode: int = cast(int, json.get('api:statuscode'))
        timestamp = cast(str, json.get('api:timestamp'))
        self.timestamp: Optional[datetime] = utils.parse_time(timestamp)
        self.json: Dict[str, Union[str, int]] = json


# frequent api errors
class UnsupportedService(APIError):
    """statuscode : `100`"""

class InvalidRequest(APIError):
    """statuscode : `104`"""

class ActionNotAllowed(APIError):
    """statuscode : `110`"""

class IncorrectPassword(APIError):
    """statuscode : `200`"""

class InvalidEmailAddress(APIError):
    """statuscode : `213`"""

class InvalidPassword(APIError):
    """statuscode : `214`"""

class AccountNotExists(APIError):
    """statuscode : `216`"""

class TooManyRequests(APIError):
    """statuscode : `219`"""

class UserUnavailable(APIError):
    """statuscode : `225`"""

class CommunityDisabled(APIError):
    """statuscode : `814`"""

class MembershipRequired(APIError):
    """statuscode : `4200`"""

class NoEnoughCoins(APIError):
    """statuscode : `4300`"""

class LotteryPlayed(APIError):
    """statuscode : `4400`"""

class TopicNotExists(APIError):
    """statuscode : `5101`"""


def check_api_error(api: Dict[str, Any]) -> APIError:
    statuscode: int = api.get('api:statuscode', -1)
    error = {
        100: UnsupportedService,
        104: InvalidRequest,
        110: ActionNotAllowed,
        200: IncorrectPassword,
        213: InvalidEmailAddress,
        214: InvalidPassword,
        216: AccountNotExists,
        219: TooManyRequests,
        225: UserUnavailable,
        814: CommunityDisabled,
        4200: MembershipRequired,
        4400: LotteryPlayed,
        5101: TopicNotExists
    }.get(statuscode, APIError)
    return error(api)
