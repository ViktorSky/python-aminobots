from ..object import Object
from .leaderboard import *
from .rankingtable import *

__all__ = 'RankingModule',


class RankingModule(Object):
    json: dict

    @property
    def defaultLeaderboardType(self) -> int:
        return self.json.get("defaultLeaderboardType")

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def leaderboard(self) -> Leaderboard:
        return Leaderboard(self.json.get("leaderboardList") or [])

    @property
    def leaderboardEnabled(self) -> bool:
        return self.json.get("leaderboardEnabled")

    @property
    def rankingTable(self) -> RankingTable:
        return RankingTable(self.json.get("rankingTable") or [])
