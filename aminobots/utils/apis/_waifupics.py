from requests import get, post
from typing import Any, Callable, Dict, Tuple, Union

__all__: list = [
    "WaifuPics"
]

Image = Gif = bytes
Url = str


def request(function: Callable) -> property:
    @property
    def wrapper(self,
                *args: Any,
                **kwargs: Any) -> Union[bytes, str]:
        url: str = function(self, *args, **kwargs)
        response: str = get(f"https://api.waifu.pics/{url!s}").json().get("url")
        if self.toBytes and response:
            response: bytes = get(response).content

        return response

    return wrapper


class WaifuPics:
    toBytes: bool

    __all__: list = [
        "Nsfw",
        "Sfw",
        "nsfw",
        "sfw"
    ]

    @property
    def many(self) -> object:
        return self.Many(self.toBytes)

    @property
    def nsfw(self) -> object:
        return self.Nsfw(self.toBytes)

    @property
    def sfw(self) -> object:
        return self.Sfw(self.toBytes)

    def __init__(self, toByes: bool = False) -> None:
        self.toBytes = bool(toByes)

    class Sfw:

        toBytes: bool

        __all__: list = [
            "awoo",
            "bite",
            "blush",
            "bonk",
            "bully",
            "cringe",
            "cry",
            "cuddle",
            "dance",
            "glomp",
            "handhold",
            "happy",
            "highfive"
            "hug",
            "kick",
            "kill",
            "kiss",
            "lick",
            "megumin",
            "neko",
            "nom",
            "pat",
            "poke",
            "shinobu",
            "slap",
            "smile",
            "smug",
            "yeet",
            "waifu",
            "wave",
            "wink"
        ]

        def __init__(self, toBytes: bool = False) -> None:
            self.toBytes = bool(toBytes)

        @request
        def awoo(self) -> Union[Image, Url]:
            return "sfw/awoo"

        @request
        def bite(self) -> Union[Gif, Url]:
            return "sfw/bite"

        @request
        def blush(self) -> Union[Gif, Url]:
            return "sfw/blush"

        @request
        def bonk(self) -> Union[Gif, Url]:
            return "sfw/bonk"

        @request
        def bully(self) -> Union[Gif, Url]:
            return "sfw/bully"

        @request
        def cringe(self) -> Union[Gif, Url]:
            return "sfw/cringe"

        @request
        def cry(self) -> Union[Gif, Url]:
            return "sfw/cry"

        @request
        def cuddle(self) -> Union[Gif, Url]:
            return "sfw/cuddle"

        @request
        def dance(self) -> Union[Gif, Url]:
            return "sfw/dance"

        @request
        def glomp(self) -> Union[Gif, Url]:
            return "sfw/glomp"

        @request
        def handhold(self) -> Union[Gif, Url]:
            return "sfw/handhold"

        @request
        def happy(self) -> Union[Gif, Url]:
            return "sfw/happy"

        @request
        def highfive(self) -> Union[Gif, Url]:
            return "sfw/highfive"

        @request
        def hug(self) -> Union[Gif, Url]:
            return "sfw/hug"

        @request
        def kick(self) -> Union[Gif, Url]:
            return "sfw/kick"

        @request
        def kill(self) -> Union[Gif, Url]:
            return "sfw/kill"

        @request
        def kiss(self) -> Union[Gif, Url]:
            return "sfw/kiss"

        @request
        def lick(self) -> Union[Gif, Url]:
            return "sfw/lick"

        @request
        def megumin(self) -> Union[Image, Url]:
            return "sfw/megumin"

        @request
        def neko(self) -> Union[Image, Url]:
            return "sfw/neko"

        @request
        def nom(self) -> Union[Gif, Url]:
            return "sfw/nom"

        @request
        def pat(self) -> Union[Gif, Url]:
            return "sfw/pat"

        @request
        def poke(self) -> Union[Gif, Url]:
            return "sfw/poke"

        @request
        def shinobu(self) -> Union[Image, Url]:
            return "sfw/shinobu"

        @request
        def slap(self) -> Union[Gif, Url]:
            return "sfw/slap"

        @request
        def smile(self) -> Union[Gif, Url]:
            return "sfw/smile"

        @request
        def smug(self) -> Union[Gif, Url]:
            return "sfw/smug"

        @request
        def yeet(self) -> Union[Gif, Url]:
            return "sfw/yeet"

        @request
        def waifu(self) -> Union[Image, Url]:
            return "sfw/waifu"

        @request
        def wave(self) -> Union[Gif, Url]:
            return "sfw/wave"

        @request
        def wink(self) -> Union[Gif, Url]:
            return "sfw/wink"

    class Nsfw:

        toBytes: bool

        __all__: list = [
            "blowjob",
            "neko",
            "trap",
            "waifu"
        ]

        def __init__(self, toBytes: bool = False) -> None:
            self.toBytes = bool(toBytes)

        @request
        def blowjob(self) -> Union[Gif, Url]:
            return "nsfw/blowjob"

        @request
        def neko(self) -> Union[Image, Url]:
            return "nsfw/neko"

        @request
        def trap(self) -> Union[Image, Url]:
            return "nsfw/trap"

        @request
        def waifu(self) -> Union[Image, Url]:
            return "nsfw/waifu"

    class Many:

        toBytes: bool

        __all__: list = [
            "Nsfw",
            "Sfw",
            "nsfw",
            "sfw"
        ]

        @property
        def nsfw(self) -> object:
            return self.Nsfw(self.toBytes)

        @property
        def sfw(self) -> object:
            return self.Sfw(self.toBytes)

        def __init__(self, toBytes: bool = False) -> None:
            self.toBytes = bool(toBytes)

        class Sfw:

            toBytes: bool

            __all__: list = [
                "awoo",
                "bite",
                "blush",
                "bonk",
                "bully",
                "cringe",
                "cry",
                "cuddle",
                "dance",
                "glomp",
                "handhold",
                "happy",
                "highfive"
                "hug",
                "kick",
                "kill",
                "kiss",
                "lick",
                "megumin",
                "neko",
                "nom",
                "pat",
                "poke",
                "shinobu",
                "slap",
                "smile",
                "smug",
                "yeet",
                "waifu",
                "wave",
                "wink"
            ]

            def __init__(self, toBytes: bool = False) -> None:
                self.toBytes = bool(toBytes)

            def request(self, url: str, exclude: tuple) -> Tuple[Union[bytes, str]]:
                response: tuple = post(
                    url=f"https://api.waifu.pics/many/{url!s}",
                    data=dict(exclude=exclude or ["..."])
                ).json().get("files", ())

                if self.toBytes and response:
                    response = tuple(get(url).content for url in response)

                return response

            def awoo(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("sfw/awoo", excludeUrls)

            def bite(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/bite", excludeUrls)

            def blush(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/blush", excludeUrls)

            def bonk(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/bonk", excludeUrls)

            def bully(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/bully", excludeUrls)

            def cringe(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/cringe", excludeUrls)

            def cry(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/cry", excludeUrls)

            def cuddle(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/cuddle", excludeUrls)

            def dance(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/dance", excludeUrls)

            def glomp(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/glomp", excludeUrls)

            def handhold(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/handhold", excludeUrls)

            def happy(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/happy", excludeUrls)

            def highfive(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/highfive", excludeUrls)

            def hug(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/hug", excludeUrls)

            def kick(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/kick", excludeUrls)

            def kill(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/kill", excludeUrls)

            def kiss(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/kiss", excludeUrls)

            def lick(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/lick", excludeUrls)

            def megumin(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("sfw/megumin", excludeUrls)

            def neko(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("sfw/neko", excludeUrls)

            def nom(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/nom", excludeUrls)

            def pat(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/pat", excludeUrls)

            def poke(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/poke", excludeUrls)

            def shinobu(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("sfw/shinobu", excludeUrls)

            def slap(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/slap", excludeUrls)

            def smile(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/smile", excludeUrls)

            def smug(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/smug", excludeUrls)

            def yeet(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/yeet", excludeUrls)

            def waifu(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("sfw/waifu", excludeUrls)

            def wave(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/wave", excludeUrls)

            def wink(self, *excludeUrls) -> Tuple[Union[Gif, Url]]:
                return self.request("sfw/wink", excludeUrls)

        class Nsfw:

            toBytes: bool

            __all__: list = [
                "blowjob",
                "neko",
                "trap",
                "waifu"
            ]

            def __init__(self, toBytes: bool = False) -> None:
                self.toBytes = bool(toBytes)

            def request(self, url: str, exclude: tuple) -> Tuple[Union[bytes, str]]:
                response: tuple = post(
                    url=f"https://api.waifu.pics/many/{url!s}",
                    data=dict(exclude=exclude or ["..."])
                ).json().get("files", ())

                if self.toBytes and response:
                    response = tuple(get(url).content for url in response)

                return response

            def blowjob(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("nsfw/blowjob", excludeUrls)

            def neko(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("nsfw/neko", excludeUrls)

            def trap(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("nsfw/trap", excludeUrls)

            def waifu(self, *excludeUrls) -> Tuple[Union[Image, Url]]:
                return self.request("nsfw/waifu", excludeUrls)
