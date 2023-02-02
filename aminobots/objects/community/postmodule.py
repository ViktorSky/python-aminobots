from ..object import Object
from .privilege import PrivilegeManager
from .posttype import *

__all__ = 'PostModule',


class PostModule(Object):
    json: dict

    @property
    def blog(self) -> PrivilegeManager:
        return self.postType.blog

    @property
    def catalogEntry(self) -> PrivilegeManager:
        return self.postType.catalogEntry

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def image(self) -> PrivilegeManager:
        return self.postType.image

    @property
    def liveMode(self) -> PrivilegeManager:
        return self.postType.liveMode

    @property
    def poll(self) -> PrivilegeManager:
        return self.postType.poll

    @property
    def publicChat(self) -> PrivilegeManager:
        return self.postType.publicChat

    @property
    def question(self) -> PrivilegeManager:
        return self.postType.question

    @property
    def postType(self) -> PostType:
        return PostType(self.json.get("postType") or {})

    @property
    def quiz(self) -> PrivilegeManager:
        return self.postType.quiz

    @property
    def screeningRoom(self) -> PrivilegeManager:
        return self.postType.screeningRoom

    @property
    def story(self) -> PrivilegeManager:
        return self.postType.story

    @property
    def webLink(self) -> PrivilegeManager:
        return self.postType.webLink
