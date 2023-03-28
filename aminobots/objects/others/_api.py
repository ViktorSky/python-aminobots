from ._object import Object

__all__: tuple = ("Api", "jsonExample")


class Api(Object):
    __json: dict

    @property
    def json(self) -> dict:
        return {
            "api:duration": self.duration,
            "api:message": self.message,
            "api:statuscode": self.statuscode,
            "api:timestamp": self.timestamp
        }

    @property
    def duration(self) -> str:
        return self.__json.get("api:duration")

    @property
    def message(self) -> str:
        return self.__json.get("api:message")

    @property
    def statuscode(self) -> int:
        return self.__json.get("api:statuscode")

    @property
    def timestamp(self) -> str:
        return self.__json.get("api:timestamp")


jsonExample = {
    "api:duration": "0.012s",
    "api:message": "OK.",
    "api:statuscode": 0,
    "api:timestamp": "2022-11-11T07:16:35Z"
}
