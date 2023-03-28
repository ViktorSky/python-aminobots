from typing import Literal, Optional


__all__ = ("Request",)


class Request:
    @property
    def comId(self) -> Optional[int]:
        return self.settings.setdefault("comId", 0)

    @property
    def method(self) -> Literal["DELETE", "GET", "POST"]:
        return self.settings.setdefault("method", "GET")

    @property
    def settings(self) -> dict:
        return self.__dict__.setdefault("settings", dict())

    @property
    def url(self):
        return self.settings.setdefault("url", "")

    def setcommunity(self, comId: int):
        self.settings.update(comId=comId)

    def setmethod(self, method: str):
        assert method in ("GET", "POST", "DELETE", "PUT")
        self.settings.update(method=method)


