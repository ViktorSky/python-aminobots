from requests import get, Response
from typing import Any, Callable, Union

__all__: list = ["AnimeImages"]

Url = str
Gif = bytes


def request(function: Callable) -> Any:
    @property
    def wrapper(self, *args, **kwargs) -> Union[bytes, str]:
        url: str = function(self, *args, **kwargs)
        response: Response = get(f"https://anime-api.hisoka17.repl.co{url}")
        response: str = response.json().get("url")

        if self.bytes:
            response: bytes = get(response).content

        return response

    return wrapper


class AnimeImages:
    __all__: list = [
        "Nsfw",
        "Sfw",
        "nsfw",
        "sfw",
        "toBytes"
    ]

    toBytes: bool

    @property
    def sfw(self) -> object:
        return self.Sfw(self.toBytes)

    @property
    def nsfw(self) -> object:
        return self.Nsfw(self.toBytes)

    def __init__(self, toBytes: bool = False) -> None:
        self.toBytes = bool(toBytes)

    class Sfw:
        __all__: list = [
            "cuddle",
            "hug",
            "kill",
            "kiss",
            "pat",
            "punch",
            "slap",
            "waifu",
            "wink"
        ]

        toBytes: bool

        def __init__(self, toBytes: bool = False) -> None:
            self.toBytes = bool(toBytes)

        @request
        def cuddle(self) -> Union[Url, Gif]:
            return "img/cuddle"

        @request
        def hug(self) -> Union[Url, Gif]:
            return "img/hug"

        @request
        def kill(self) -> Union[Url, Gif]:
            return "img/kill"

        @request
        def kiss(self) -> Union[Url, Gif]:
            return "img/kiss"

        @request
        def pat(self) -> Union[Url, Gif]:
            return "img/pat"

        @request
        def punch(self) -> Union[Url, Gif]:
            return "img/punch"

        @request
        def slap(self) -> Union[Url, Gif]:
            return "img/slap"

        @request
        def waifu(self) -> Union[Url, Gif]:
            return "img/waifu"

        @request
        def wink(self) -> Union[Url, Gif]:
            return "img/wink"

    class Nsfw:
        __all__: list = [
            "boobs",
            "hentai",
            "lesbian"
        ]

        toBytes: bool

        def __init__(self, toBytes: bool = False) -> None:
            self.toBytes = bool(toBytes)

        @request
        def boobs(self) -> Union[Url, Gif]:
            return "img/nsfw/boobs"

        @request
        def hentai(self) -> Union[Url, Gif]:
            return "img/nsfw/hentai"

        @request
        def lesbian(self) -> Union[Url, Gif]:
            return "img/nsfw/lesbian"
