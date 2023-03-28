from ..object import Object
from .homepage import HomePage
from .leftsidepanel import LeftSidePanel

__all__ = 'Appearance',


class Appearance(Object):
    json: dict

    @property
    def homePage(self) -> HomePage:
        return HomePage(self.json.get("homePage") or {})

    @property
    def leftSidePanel(self) -> LeftSidePanel:
        return LeftSidePanel(self.json.get("leftSidePanel") or {})
