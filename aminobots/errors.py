from .utils import Date


class AminoException(Exception):
    '''Base Exception class for python-aminobots.'''
    ...


class WebSocketClosed(AminoException):
    '''Exception that's raised when the websocket close the connection.'''
    ...


class HTTPException(AminoException):
    """Base Exception class for HTTP requests"""
    ...


class InternalServerError(HTTPException):
    """Exception that's raise when the HTTP response status > 500."""
    ...


class RequestError(HTTPException): # valid name ?
    """Exception that's raise when the HTTP response status > 400."""
    ...


class Forbidden(RequestError):
    """Exception that's raise when an HTTP request throw 403 error.

    Usually it's an ip ban, you've made too many requests.
    """
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
