from ..object import Object
from .privilege import Privilege

__all__ = 'CatalogModule',


class CatalogModule(Object):
    json: dict

    @property
    def curationEnabled(self) -> bool:
        return self.json.get("curationEnabled")

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def privilege(self):
        return Privilege(self.json.get("privilege") or {})

    @property
    def privilegeType(self) -> int:
        return self.privilege.type
