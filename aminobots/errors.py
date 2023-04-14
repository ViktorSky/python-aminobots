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

from .utils import Date

__all__ = (
    'AminoException',
    'APIError',
    'ConnectionError',
    'ClientError',
    'RedirectionError',
    'ServerError'
)


class AminoException(Exception):
    '''Base Exception class for python-aminobots.'''
    ...

# base classes
class RediretionError(AminoException):
    '''Base Exception class for HTTP requests. Raised when the HTTP response status >= 300.'''
    ...


class ClientError(AminoException):
    '''Base Exception class for HTTP requests. Raised when the HTTP response status >= 400.'''
    ...


class ServerError(ClientError):
    '''Base Exception class for HTTP requests. Raised when the HTTP response status >= 500.'''
    ...


class APIError(AminoException):
    '''Exception that's raised when an HTTP API request operation fails.

    Attributes
    ------------
    json: :class:`dict`
        Raw exception data.
    message: :class:`str`
        The api message of the error. Could be an empty string.
    statuscode: :class:`int`
        The Amino specific error code for the failure.
    duration: :class:`float`
        The duration of the API processing.
    timestamp: :class:`Date`
        The timestamp of the request.
    '''

    __slots__ = (
        'duration',
        'json',
        'message',
        'status',
        'timestamp'
    )

    def __init__(self, json: dict):
        self.json: dict = json
        self.duration: float = float(json.get('api:duration', '0.0s').removesuffix('s'))
        self.message: str = json.get('api:message', '')
        self.statuscode: int = json.get('api:statuscode')
        self.timestamp: Date = Date(json['api:timestamp'])
        Exception.__init__(self, json)


# connection
class ConnectionError(AminoException):
    '''Exception that's raised when there is no connection.'''
    ...


class WebSocketClosed(AminoException):
    # unused
    '''Exception that's raised when the websocket close the connection.'''
    ...


# frequent client errors
class Forbidden(ClientError):
    """Exception that's raise when an HTTP request throw 403 error.

    Usually it's an ip ban, you've made too many requests.
    """
    ...


# frequent api errors
class CommunityDisabled(APIError):
    # unused
    """code: 814"""
