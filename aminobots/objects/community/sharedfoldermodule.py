from ..object import Object
from .privilege import Privilege

__all__ = 'SharedFolderModule',


class SharedFolderModule(Object):
    json: dict

    @property
    def albumManage(self) -> Privilege:
        return Privilege(self.json.get("albumManagePrivilege") or {})

    @property
    def albumManageMinLevel(self) -> int:
        return self.albumManage.minLevel

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def upload(self) -> Privilege:
        return Privilege(self.json.get("uploadPrivilege") or {})

    @property
    def uploadMinLevel(self) -> int:
        return self.upload.minLevel
