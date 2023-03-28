from..object import Object
from .appearance import *
from .general import *
from .module import *
from .pagemodule import PageModule

__all__ = 'Configuration',


class Configuration(Object):
    json: dict

    @property
    def appearance(self) -> Appearance:
        return Appearance(self.json.get("appearance") or {})

    @property
    def general(self) -> General:
        return General(self.json.get("general") or {})

    @property
    def module(self) -> Module:
        return Module(self.json.get("module") or {})

    @property
    def page(self) -> PageModule:
        return PageModule(self.json.get("page") or {})
