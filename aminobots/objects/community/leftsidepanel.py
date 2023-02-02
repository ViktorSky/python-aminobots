from typing import Optional
from ..object import Object
from .navigation import Navigation

__all__ = 'LeftSidePanel', 'LeftSidePanelStyle'


class LeftSidePanelStyle(Object):
    json: dict

    @property
    def iconColor(self) -> Optional[str]:
        return self.json.get("iconColor")


class LeftSidePanel(Object):
    json: dict

    @property
    def iconColor(self) -> Optional[str]:
        return self.style.iconColor

    @property
    def navigation(self) -> Navigation:
        return Navigation(self.json.get("navigation") or {})

    @property
    def style(self) -> LeftSidePanelStyle:
        return LeftSidePanelStyle(self.json.get("style") or {})
