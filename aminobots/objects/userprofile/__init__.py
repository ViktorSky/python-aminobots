from typing import Literal, Optional
from ..object import Object
from .avatarframe import *
from ..account import DeviceInfo
from ..communitylist import CommunityList
from .extensions import *
from .media import *
# FanClubList

__all__ = 'UserProfile',


class UserProfile(Object):
    json: dict

    @property
    def accountMembershipStatus(self) -> Literal[0, 1]:
        return self.json.get("accountMembershipStatus")

    @property
    def acpDeeplink(self) -> Optional[str]:
        return self.extensions.acpDeeplink

    @property
    def adminLogCountIn7Days(self):
        return self.json.get("adminLogCountIn7Days")

    @property
    def aminoId(self) -> str:
        return self.json.get("aminoId")

    # @property  # not found
    # def aminoIdEditable(self) -> bool:
        # return self.json.get("aminoIdEditable")

    @property
    def avatarFrame(self) -> AvatarFrame:
        return AvatarFrame(self.json.get("avatarFrame") or {})

    @property
    def avatarFrameId(self):
        return self.json.get("avatarFrameId") or self.avatarFrame.id

    @property
    def backgroundColor(self):
        return self.extensions.style.backgroundColor

    @property
    def bio(self) -> Optional[str]:
        return self.json.get("content")

    @property
    def blogsCount(self) -> int:
        return self.json.get("blogsCount")

    @property
    def comId(self) -> Optional[int]:
        return self.json.get("ndcId") or None

    @property
    def commentsCount(self) -> int:
        return self.json.get("commentsCount") or 0

    @property
    def consecutiveCheckInDays(self) -> Optional[int]:
        return self.json.get("consecutiveCheckInDays")

    @property
    def createdTime(self) -> str:
        return self.json.get("createdTime")

    @property
    def creatorDeeplink(self) -> Optional[str]:
        return self.extensions.creatorDeeplink

    @property
    def defaultBubbleId(self) -> Optional[str]:
        return self.extensions.defaultBubbleId

    @property
    def deviceInfo(self) -> DeviceInfo:
        return self.extensions.deviceInfo

    @property
    def extensions(self) -> Extensions:
        return Extensions(self.json.get("extensions") or {})

    @property
    def followersCount(self) -> int:
        return self.json.get("membersCount") or 0

    @property
    def followingCount(self) -> int:
        return self.json.get("joinedCount") or 0

    @property
    def followingStatus(self) -> Literal[0, 1]:
        return self.json.get("followingStatus")

    @property
    def icon(self) -> str:
        return self.json.get("icon")

    @property
    def isGlobalProfile(self) -> bool:
        return self.json.get("isGlobal")

    @property
    def isnicknameVerified(self) -> bool:
        return self.json.get("isNicknameVerified")

    @property
    def level(self) -> int:
        return self.json.get("level")

    @property
    def linkedCommunities(self) -> CommunityList:
        return CommunityList(self.json.get("linkedCommunityList") or {})

    @property
    def media(self) -> Media:
        return Media(self.json.get("mediaList") or [])

    @property
    def membershipStatus(self) -> Literal[0, 1]:
        return self.json.get("membershipStatus")

    @property
    def modifiedTime(self) -> str:
        return self.json.get("modifiedTime")

    # @property
    # def mood(self):
        # return self.json.get("mood")

    # @property
    # def moodSticker(self):  # ...
        # return self.json.get("moodSticker")

    @property
    def nickname(self) -> str:
        return self.json.get("nickname")

    @property
    def notifSubStatus(self) -> Literal[0, 1]:
        return self.json.get("notificationSubscriptionStatus")

    @property
    def onlineStatus(self) -> int: # [2]
        return self.json.get("onlineStatus")

    @property
    def postsCount(self) -> int:
        return self.json.get("postsCount")

    @property
    def privilegeOfChatInviteRequest(self) -> Optional[int]:
        return self.extensions.privilegeOfChatInviteRequest

    @property
    def privilegeOfChatRequest(self) -> int:
        return self.extensions.privilegeOfChatRequest

    @property
    def privilegeOfCommentOnUserProfile(self) -> Optional[int]:
        return self.extensions.privilegeOfCommentOnUserProfile

    @property
    def privilegeOfPublicChat(self) -> Optional[int]:
        return self.extensions.privilegeOfPublicChat

    @property
    def privilegeOfVideoChat(self) -> Optional[int]:
        return self.extensions.privilegeOfVideoChat

    @property
    def pushEnabled(self) -> bool:
        return self.json.get("pushEnabled")

    @property
    def reputation(self) -> int:
        return self.json.get("reputation")

    @property
    def role(self) -> int:
        return self.json.get("role")

    @property
    def status(self) -> Literal[0, 1]:
        return self.json.get("status")

    @property
    def storiesCount(self) -> int:
        return self.json.get("storiesCount")

    @property
    def style(self):
        return self.extensions.style

    @property
    def tippingPermStatus(self) -> Optional[int]:
        return self.extensions.tippingPermStatus

    @property
    def userId(self) -> str:
        return self.json.get("uid")

    @property
    def visitPrivacy(self) -> Optional[int]:  # [1]
        return self.json.get("visitPrivacy")

    @property
    def wikisCount(self) -> int:
        return self.json.get("itemsCount")




class OldUserProfile(UserProfile):
    # backgroundImage: None
    # staffInfo: None
    @property
    def activation(self):
        return self.json.get('activation')

    @property
    def activePublicLiveChatId(self) -> str:
        return self.json.get('activePublicLiveThreadId')

    @property
    def adminInfo(self) -> dict:
        return self.json.get('adminInfo', dict())

    @property
    def age(self):
        return self.json.get('age')

    @property
    def appleId(self):
        return self.json.get('appleID')

    @property
    def applicant(self):
        return self.json.get('applicant')

    @property
    def avgDailySpendTimeIn7Days(self):
        return self.json.get('avgDailySpendTimeIn7Days')

    @property
    def coverAnimation(self):
        return self.extensions.json.get('coverAnimation')

    @property
    def dateOfBirth(self):
        return self.json.get('dateOfBirth')

    @property
    def disabledLevel(self):
        return self.extensions.json.get('__disabledLevel__')

    @property
    def disabledStatus(self):
        return self.extensions.json.get('__disabledStatus__')

    @property
    def disabledTime(self):
        return self.extensions.json.get('__disabledTime__')

    @property
    def email(self):
        return self.json.get('email')

    def facebookId(self):
        return self.json.get('facebookID')

    @property
    def fanClub(self) -> dict:
        # FanClubList
        return (self.json.get("fanClubList", {}))
    
    @property
    def fansCount(self):
        return self.influencerInfo.get("fansCount")

    @property
    def gender(self):
        return self.json.get('gender')

    @property
    def globalStrikeCount(self):
        return self.adminInfo.get('globalStrikeCount')

    @property
    def googleId(self):
        return self.json.get('googleID')

    @property
    def influencerCreatedTime(self):
        return self.influencerInfo.get('createdTime')

    @property
    def influencerInfo(self) -> dict:
        return self.json.get('influencerInfo') or {}

    @property
    def influencerMonthlyFee(self):
        return self.influencerInfo.get('monthlyFee')

    @property
    def influencerPinned(self):
        return self.influencerInfo.get('pinned')

    @property
    def isMemberOfTeamAmino(self) -> bool:
        return self.extensions.get('isMemberOfTeamAmino')

    @property
    def lastStrikeTime(self):
        return self.adminInfo.get('lastStrikeTime')

    @property
    def lastWarningTime(self):
        return self.adminInfo.get('lastWarningTime')

    @property
    def message(self):
        return self.json.get("message")

    @property
    def mood(self):
        return self.json.get('mood')

    @property
    def moodSticker(self):
        return self.json.get('moodSticker')

    @property
    def onlineStatus2(self):
        return self.settings.get('onlineStatus')

    @property
    def phoneNumber(self):
        return self.json.get('phoneNumber')

    @property
    def race(self):
        return self.json.get('race')

    @property
    def requestId(self):
        return self.json.get('requestId')

    @property
    def securityLevel(self):
        return self.json.get('securityLevel')

    @property
    def settings(self) -> dict:
        return self.json.get('settings')

    @property
    def strikeCount(self):
        return self.adminInfo.get('strikeCount')

    @property
    def tagList(self):
        return self.json.get('tagList')

    @property
    def totalQuizHighestScore(self):
        return self.json.get("totalQuizHighestScore")

    @property
    def totalQuizPlayedTimes(self):
        return self.json.get("totalQuizPlayedTimes")

    @property
    def twitterId(self):
        return self.json.get("twitterID")

    @property
    def verified(self):
        return self.json.get("verified")

    @property
    def visitorsCount(self):
        return self.json.get("visitorsCount")

    @property
    def warningCount(self):
        return self.adminInfo.get("warningCount")
