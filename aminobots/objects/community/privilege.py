from ..object import Object

__all__ = 'Privilege', 'PrivilegeManager'


class Privilege(Object):
    json: dict

    @property
    def minLevel(self) -> int:
        return self.json.get("minLevel") or 0

    @property
    def type(self) -> int:
        return self.json.get("type")


class PrivilegeManager(Object):
    json: dict

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def minLevel(self) -> int:
        return self.privilege.minLevel

    @property
    def privilege(self) -> Privilege:
        return Privilege(self.json.get("privilege") or {})
