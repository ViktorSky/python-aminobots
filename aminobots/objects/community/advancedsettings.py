from typing import Optional

from ..object import Object
from .feedpagelist import *
from .rankingtable import *

__all__ = 'AdvancedSettings',


class AdvancedSettings(Object):
    json: dict

    @property
    def catalogEnabled(self) -> Optional[bool]:
        return self.json.get("catalogEnabled")

    @property
    def defaultRankingTypeInLeaderboard(self) -> int:
        return self.json.get("defaultRankingTypeInLeaderboard")

    @property
    def facebookAppIdList(self) -> list:
        return self.json.get("facebookAppIdList") or []

    @property
    def feedPages(self) -> FeedPageList:
        return FeedPageList(self.json.get("newsfeedPages") or [])

    @property
    def frontPageLayout(self) -> int:
        return self.json.get("frontPageLayout")

    @property
    def hasPendingReviewRequest(self) -> Optional[bool]:
        return self.json.get("hasPendingReviewRequest")

    @property
    def joinedBaselineCollectionIdList(self) -> list:
        return self.json.get("joinedBaselineCollectionIdList") or []

    @property
    def leaderboardStyle(self) -> dict:  # ...
        return self.json.get("leaderboardStyle") or {}

    @property
    def pollMinFullBarVoteCount(self) -> int:
        return self.json.get("pollMinFullBarVoteCount")

    @property
    def rankingTable(self) -> RankingTable:
        return RankingTable(self.json.get("rankingTable") or [])

    @property
    def welcomeMessageEnabled(self) -> Optional[bool]:
        return self.json.get("welcomeMessageEnabled")

    @property
    def welcomeMessageText(self) -> Optional[str]:
        return self.json.get("welcomeMessageText")
