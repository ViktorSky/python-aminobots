# Library to get images from nekobot api
# Structure made by V¡ktor
# Made on 2022-10-16

from contextlib import suppress
from functools import wraps
from requests import get
from typing import Callable, NoReturn, Union

Text = Url = str
Image = Gif = Video = bytes
Response = Union[bytes, str, NoReturn]

__all__ = ["NekoBot"]


def request(func: Callable) -> Response:
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Union[bytes, str]:
        raw: int = 1 if self.toBytes is True else 0
        params: dict = func(self, *args, **kwargs)
        response = get(
            url="https://nekobot.xyz/api/imagegen",
            params=dict(**params, raw=raw)
        )

        if self.toBytes is False:
            return response.json().get("message")

        with suppress(Exception):
            response = get(response.json().get("message"))

        return response.content

    return wrapper


class NekoBot:
    """ class to get images from NekoBot api :
         documentation: https://docs.nekobot.xyz

         ** Example:
             >>> api = NekoBot(toBytes = False)

         ** Parameters:
             - toBytes : True / False :
                 if toBytes is True:
                     return bytes from all Api methods
                 if toBytes is False:
                     return image url from all Api methods

         ** Methods :
             - gen
             - help
             - image

        ** Help :
            Can u use `help` built-in function
                >>> help(NekoBot)
            Or use `__all__` for get a list of methods
                >>> api.__all__
                >>> api.image.__all__
                >>> api.gen.__all__
    """

    __all__: list = [
        "toBytes",
        "Gen",
        "Help",
        "gen",
        "help",
        "Image",
        "image"
    ]

    toBytes: bool = False

    @property
    def image(self) -> object:
        return self.Image(self.toBytes)

    @property
    def gen(self) -> object:
        return self.Gen(self.toBytes)

    @property
    def help(self) -> object:
        return self.Help()

    def __init__(self, toBytes: bool = False) -> None:
        self.toBytes = bool(toBytes)

    class Image:
        __all__: list = [
            "hass",
            "hmidriff",
            "pgif",
            "uhd",
            "hentai",
            "holo",
            "hneko",
            "neko",
            "hkitsune",
            "kemonomimi",
            "anal",
            "hanal",
            "gonewild",
            "kanna",
            "ass",
            "pussy",
            "thigh",
            "hthigh",
            "gah",
            "coffee",
            "food",
            "paizuri",
            "tentacle",
            "boobs",
            "hboobs",
            "yaoi"
        ]

        def __init__(self, toBytes: bool = False) -> None:
            self.toBytes = bool(toBytes)

        def request(self, url: Text) -> Response:
            response = get(
                url="https://nekobot.xyz/api/image",
                params=dict(type=url)
            ).json().get("message")

            if self.toBytes is True and response:
                response = get(response).content

            return response

        @property
        def hass(self) -> Union[Url, Image]:
            return self.request("hass")

        @property
        def hmidriff(self) -> Union[Url, Image]:
            return self.request("hmidriff")

        @property
        def pgif(self) -> Union[Url, Gif]:
            return self.request("pgif")

        @property
        def uhd(self) -> Union[Url, Image]:
            return self.request("4k")

        @property
        def hentai(self) -> Union[Url, Image]:
            return self.request("hentai")

        @property
        def holo(self) -> Union[Url, Image]:
            return self.request("holo")

        @property
        def hneko(self) -> Union[Url, Image]:
            return self.request("hneko")

        @property
        def neko(self) -> Union[Url, Image]:
            return self.request("neko")

        @property
        def hkitsune(self) -> Union[Url, Image]:
            return self.request("hkitsune")

        @property
        def kemonomimi(self) -> Union[Url, Image]:
            return self.request("kemonomimi")

        @property
        def anal(self) -> Union[Url, Gif]:
            return self.request("anal")

        @property
        def hanal(self) -> Union[Image, Gif]:
            return self.request("hanal")

        @property
        def gonewild(self) -> Union[Url, Image]:
            return self.request("gonewild")

        @property
        def kanna(self) -> Union[Url, Image]:
            return self.request("kanna")

        @property
        def ass(self) -> Union[Url, Image]:
            return self.request("ass")

        @property
        def pussy(self) -> Union[Url, Image]:
            return self.request("pussy")

        @property
        def thigh(self) -> Union[Url, Image]:
            return self.request("thigh")

        @property
        def hthigh(self) -> Union[Url, Image]:
            return self.request("hthigh")

        @property
        def gah(self) -> Union[Url, Gif]:
            return self.request("gah")

        @property
        def coffee(self) -> Union[Url, Image]:
            return self.request("coffee")

        @property
        def food(self) -> Union[Url, Image]:
            return self.request("food")

        @property
        def paizuri(self) -> Union[Url, Image]:
            return self.request("paizuri")

        @property
        def tentacle(self) -> Union[Url, Image]:
            return self.request("tentacle")

        @property
        def boobs(self) -> Union[Url, Image]:
            return self.request("boobs")

        @property
        def hboobs(self) -> Union[Url, Image]:
            return self.request("hboobs")

        @property
        def yaoi(self) -> Union[Url, Image]:
            return self.request("yaoi")

    class Gen:
        toBytes: bool

        __all__: list = [
            "animeface",
            "awooify",
            "baguette",
            "blurpify",
            "captcha",
            "changemymind",
            "clickforhentai",  # deprecated
            "clyde",
            "ddlc",
            "deepfry",
            "fact",
            "iphonex",
            "jpegify",
            "kannagen",
            "kidnap",  # deprecated
            "kms",  # deprecated
            "lolice",
            "magik",
            "nichijou",  # deprecated
            "osu",  # deprecated
            "phcomment",
            "ship",
            "threats",
            "trapcard",
            "trash",
            "truptweet",
            "tweet",
            "whowouldwin"
        ]

        def __init__(self, toBytes: bool = False) -> None:
            self.toBytes = bool(toBytes)

        @request
        def animeface(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="animeface",
                image=image
            )

        @request
        def awooify(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="awooify",
                url=image
            )

        @request
        def baguette(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="baguette",
                url=image
            )

        @request
        def blurpify(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="blurpify",
                image=image
            )

        @request
        def captcha(self,
                    image: Url,
                    username: Text) -> Union[Url, Image, dict]:
            return dict(
                type="captcha",
                url=image,
                username=username
            )

        @request
        def changemymind(self, text: Text) -> Union[Url, Image, dict]:
            return dict(
                type="changemymind",
                text=text
            )

        @request
        def clickforhentai(self,
                           image: Url,
                           fontsize: int = 20) -> Union[Url, Image, dict]:
            """deprecated"""
            return dict(
                type="clickforhentai",
                image=image,
                fontsize=fontsize
            )

        @request
        def clyde(self, text: Text) -> Union[Url, Image, dict]:
            return dict(
                type="clyde",
                text=text
            )

        @request
        def ddlc(self,
                 text: Text,
                 character: Text = "monika",
                 background: Text = "bedroom",
                 body: Text = "1",
                 face: Text = "a") -> Union[Url, Image, dict]:
            """Parameters avalible in NekoBot.Help"""
            return dict(
                type="ddlc",
                character=str(character),
                background=str(background),
                body=str(body),
                face=str(face),
                text=text[: 140]
            )

        @request
        def deepfry(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="deepfry",
                image=image
            )

        @request
        def fact(self, text: Text) -> Union[Url, Image, dict]:
            return dict(
                type="fact",
                text=text
            )

        @request
        def iphonex(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="iphonex",
                url=image
            )

        @request
        def jpegify(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="jpeg",
                url=image
            )

        @request
        def kannagen(self, text: Text) -> Union[Url, Image, dict]:
            return dict(
                type="kannagen",
                text=text
            )

        @request
        def kidnap(self, image: Url) -> Union[Url, Image, dict]:
            """deprecated"""
            return dict(
                type="kidnap",
                image=image
            )

        @request
        def kms(self, image: Url) -> Union[Url, Image, dict]:
            """deprecated"""
            return dict(
                type="kms",
                url=image
            )

        @request
        def lolice(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="lolice",
                url=image
            )

        @request
        def magik(self,
                  image: Url,
                  intensity: int = 5) -> Union[Url, Image, dict]:
            return dict(
                type="magik",
                image=image,
                intensity=intensity
            )

        @request
        def nichijou(self, text: Text) -> Union[Url, Image, dict]:
            """deprecated"""
            return dict(
                type="nichijou",
                text=text
            )

        @request
        def osu(self,
                apiKey: Text,
                username: Text) -> Union[Url, Image, dict]:
            """deprecated"""
            return dict(
                type="osu",
                key=apiKey,
                username=username
            )

        @request
        def phcomment(self,
                      text: Text,
                      username: Text,
                      image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="phcomment",
                username=username,
                image=image,
                text=text
            )

        @request
        def ship(self,
                 image1: Url,
                 image2: Url) -> Union[Url, Image, dict]:
            return dict(
                type="ship",
                user1=image1,
                user2=image2
            )

        @request
        def stickbug(self, image: Url) -> Union[Url, Video, dict]:
            return dict(
                type="stickbug",
                url=image
            )

        @request
        def threats(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="threats",
                url=image
            )

        @request
        def trapcard(self,
                     name: Text,
                     author: Text,
                     image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="trap",
                name=name,
                author=author,
                image=image
            )

        @request
        def trash(self, image: Url) -> Union[Url, Image, dict]:
            return dict(
                type="trash",
                url=image
            )

        @request
        def trumptweet(self, text: Url) -> Union[Url, Image, dict]:
            return dict(
                type="trumptweet",
                text=text
            )

        @request
        def tweet(self,
                  username: Text,
                  text: Text) -> Union[Url, Image, dict]:
            return dict(
                type="tweet",
                username=username,
                text=text
            )

        @request
        def whowouldwin(self,
                        image1: Url,
                        image2: Url) -> Union[Url, Image, dict]:
            return dict(
                type="whowouldwin",
                user1=image1,
                user2=image2
            )

    class Help(object):
        __all__: list = [
            "background",
            "body",
            "character",
            "face",
            "monika",
            "natsuri",
            "sayori",
            "yuri"
        ]

        def __str__(self) -> str:
            return "help(" + ", ".join([
                attr for attr in sorted(dir(self))
                if str(attr).startswith("__") is False
                   and str(attr).istitle() is False
            ]) + ")"

        @property
        def background(self) -> object:
            return self.Background()

        @property
        def body(self) -> object:
            return self.Body()

        @property
        def character(self) -> object:
            return self.Character()

        @property
        def face(self) -> object:
            return self.Face()

        @property
        def monika(self) -> object:
            return self.Monika()

        @property
        def natsuki(self) -> object:
            return self.Natsuki()

        @property
        def sayori(self) -> object:
            return self.Sayori()

        @property
        def yuri(self) -> object:
            return self.Yuri()

        class Background(object):
            __all__: list = "ALL".split()

            def __str__(self) -> str:
                return self.ALL[0]

            ALL: list = [
                "bedroom",
                "class",
                "closet,"
                "club",
                "corridor",
                "house",
                "kitchen",
                "residential",
                "sayori_bedroom"
            ]

        class Body(object):
            __all__: list = "ALL".split()

            def __str__(self) -> str:
                return self.ALL[0]

            ALL: list = [
                "1",
                "1b",
                "2",
                "2b"
            ]

        class Character(object):
            __all__: list = "ALL".split()

            def __str__(self) -> str:
                return self.ALL[0]

            ALL: list = [
                "m", "monika",
                "n", "natsuki",
                "s", "sayori",
                "y", "yuri"
            ]

        class Face(object):
            __all__: list = "ALL".split()

            def __str__(self) -> object:
                return self.ALL[0]

            ALL: list = [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z"
            ]

        class Monika(object):
            __all__: list = [
                "ALL",
                "default",
                "character",
                "background",
                "body",
                "face"
            ]

            def __str__(self) -> str:
                return self.character[0]

            @property
            def default(self) -> list:
                return [
                    self.character[0],
                    self.background[0],
                    self.body[0],
                    self.face[0]
                ]

            @property
            def character(self) -> list:
                return ["m", "monika"]

            @property
            def background(self) -> list:
                return [
                    "bedroom",
                    "class", "closet", "club", "corridor",
                    "house",
                    "kitchen",
                    "residential",
                    "sayori_bedroom"
                ]

            @property
            def body(self) -> object:
                return ["1", "2"]

            @property
            def face(self) -> object:
                return [
                    "a", "b", "c",
                    "d", "e", "f",
                    "g", "h", "i",
                    "j", "k", "l",
                    "m", "n", "o",
                    "p", "q", "r"
                ]

            @property
            def ALL(self) -> list:
                return [
                    self.character,
                    self.background,
                    self.body,
                    self.face
                ]

        class Natsuki(object):
            __all__: list = [
                "ALL",
                "body",
                "background",
                "character",
                "default",
                "face"
            ]

            def __str__(self) -> str:
                return self.character[0]

            @property
            def default(self) -> list:
                return [
                    self.character[0],
                    self.background[0],
                    self.body[0],
                    self.face[0]
                ]

            @property
            def character(self) -> list:
                return ["n", "natsuki"]

            @property
            def background(self) -> list:
                return [
                    "bedroom",
                    "class", "closet", "club", "corridor",
                    "house",
                    "kitchen",
                    "residential",
                    "sayori_bedroom"
                ]

            @property
            def body(self) -> object:
                return ["1", "1b", "2", "2b"]

            @property
            def face(self) -> object:
                return [
                    "a", "b", "c",
                    "d", "e", "f",
                    "g", "h", "i",
                    "j", "k", "l",
                    "m", "n", "o",
                    "p", "q", "r",
                    "s", "t", "u",
                    "v", "w", "x",
                    "y", "z"
                ]

            @property
            def ALL(self) -> list:
                return [
                    self.character,
                    self.background,
                    self.body,
                    self.face
                ]

        class Sayori(object):
            __all__: list = [
                "ALL",
                "default",
                "character",
                "background",
                "body",
                "face"
            ]

            def __str__(self) -> str:
                return self.character[0]

            @property
            def default(self) -> list:
                return [
                    self.character[0],
                    self.background[0],
                    self.body[0],
                    self.face[0]
                ]

            @property
            def character(self) -> list:
                return ["s", "sayori"]

            @property
            def background(self) -> list:
                return [
                    "bedroom",
                    "class", "closet", "club", "corridor",
                    "house",
                    "kitchen",
                    "residential",
                    "sayori_bedroom"
                ]

            @property
            def body(self) -> object:
                return ["1", "1b", "2", "2b"]

            @property
            def face(self) -> object:
                return [
                    "a", "b", "c",
                    "d", "e", "f",
                    "g", "h", "i",
                    "j", "k", "l",
                    "m", "n", "o",
                    "p", "q", "r",
                    "s", "t", "u",
                    "v", "w", "x",
                    "y"
                ]

            @property
            def ALL(self) -> list:
                return [
                    self.character,
                    self.background,
                    self.body,
                    self.face
                ]

        class Yuri(object):
            __all__: list = [
                "ALL",
                "default",
                "character",
                "background",
                "body",
                "face"
            ]

            def __str__(self) -> str:
                return self.character[0]

            @property
            def default(self) -> list:
                return [
                    self.character[0],
                    self.background[0],
                    self.body[0],
                    self.face[0]
                ]

            @property
            def character(self) -> list:
                return "y, yuri".split(", ")

            @property
            def background(self) -> list:
                return [
                    "bedroom",
                    "class", "closet", "club", "corridor",
                    "house",
                    "kitchen",
                    "residential",
                    "sayori_bedroom"
                ]

            @property
            def body(self) -> object:
                return ["1", "1b", "2", "2b"]

            @property
            def face(self) -> object:
                return [
                    "a", "b", "c",
                    "d", "e", "f",
                    "g", "h", "i",
                    "j", "k", "l",
                    "m", "n", "o",
                    "p", "q", "r",
                    "s", "t", "u",
                    "v", "w"
                ]

            @property
            def ALL(self) -> list:
                return [
                    self.character,
                    self.background,
                    self.body,
                    self.face
                ]
