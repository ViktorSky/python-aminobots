from typing import Optional
from ..object import Object
from .welcomemessage import *

__all__ = 'General',


class General(Object):
    json: dict

    @property
    def accountMembershipEnabled(self) -> bool:
        return self.json.get("accountMembershipEnabled")

    @property
    def disableLiveLayerActive(self) -> bool:
        return self.json.get("disableLiveLayerActive")

    @property
    def disableLiveLayerVisible(self) -> bool:
        return self.json.get("disableLiveLayerVisible")

    @property
    def facebookAppIdList(self) -> list:
        return self.json.get("facebookAppIdList") or []

    @property
    def hasPendingReviewRequest(self) -> bool:
        return self.json.get("hasPendingReviewRequest")

    @property
    def invitePermission(self) -> int:
        return self.json.get("invitePermission")

    @property
    def joinedBaselineCollectionIdList(self) -> list:
        return self.json.get("joinedBaselineCollectionIdList") or []

    @property
    def joinedTopicIdList(self):
        return self.json.get("joinedTopicIdList") or []

    @property
    def onlyAllowOfficialTag(self) -> bool:
        return self.json.get("onlyAllowOfficialTag")

    @property
    def premiumFeatureEnabled(self) -> bool:
        return self.json.get("premiumFeatureEnabled")

    @property
    def videoUploadPolicy(self) -> int:
        return self.json.get("videoUploadPolicy")

    @property
    def welcomeMessage(self) -> WelcomeMessage:
        return WelcomeMessage(self.json.get("welcomeMessage") or {})

    @property
    def welcomeMessageEnabled(self) -> Optional[bool]:
        return self.welcomeMessage.enabled

    @property
    def welcomeMessageText(self) -> Optional[str]:
        return self.welcomeMessage.text
