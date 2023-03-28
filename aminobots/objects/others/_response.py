from ._api import Api
from ._object import Object

__all__ = ("Response", "jsonExample")


class Response(Object):
    json: dict

    @property
    def api(self) -> Api:
        return Api(self.json)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} object at {hex(id(self))}>"


jsonExample = {
    "api:duration": "",
    "api:message": "",
    "api:statuscode": 0,
    "api:timestamp": "",
    "allItemCount": 0,
    "auid": "",
    "newAccount": False,
    "secret": "",
    "sid": "",
    "userProfileCount": 0,
    "account": {},
    "communityList": [],
    "linkInfoV2": {},
    "paging": {},
    "resultList": [],
    "userProfile": {},
    "userProfileList": []
}
