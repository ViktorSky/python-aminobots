from ..object import Object

__all__ = 'InfluencerModule',


class InfluencerModule(Object):
    json: dict

    @property
    def enabled(self) -> bool:
        return self.json.get("enabled")

    @property
    def lock(self) -> bool:
        return self.json.get("lock")

    @property
    def maxMonthlyFee(self) -> int:
        return self.json.get("maxVipMonthlyFee")

    @property
    def maxVipNumbers(self) -> int:
        return self.json.get("maxVipNumbers")

    @property
    def minMonthlyFee(self) -> int:
        return self.json.get("minVipMonthlyFee")
